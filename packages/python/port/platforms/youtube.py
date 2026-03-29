"""
YouTube

This module provides an example flow of a YouTube data donation study

Assumptions:
It handles DDPs in the Dutch and English language with filetype JSON.
"""

import logging
from collections import Counter

import pandas as pd
import port.api.d3i_props as d3i_props
import port.api.props as props
import port.helpers.validate as validate
from port.api.d3i_props import ExtractionResult
from port.helpers.flow_builder import FlowBuilder
from port.helpers.parsers import create_csv_table, create_table
from port.helpers.Structure_extractor_libraries.YT_get_json_structure import (
    structure_from_zip,
)
from port.helpers.validate import DDPCategory, DDPFiletype, Language

logger = logging.getLogger(__name__)

DDP_CATEGORIES = [
    DDPCategory(
        id="json_en",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.EN,
        known_files=[
            "search-history.json",
            "watch-history.json",
            "subscriptions.csv",
            "comments.csv",
        ],
    ),
    DDPCategory(
        id="json_nl",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.NL,
        known_files=[
            "abonnementen.csv",
            "kijkgeschiedenis.json",
            "zoekgeschiedenis.json",
            "reacties.csv",
        ],
    ),
    DDPCategory(
        id="json_es",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.ES,
        known_files=[
            "historial-de-reproducciones.json",
            "historial-de-búsqueda.json",
            "suscripciones.csv",
        ],
    ),
    DDPCategory(
        id="json_ro",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.RO,
        known_files=[
            "istoricul-vizionărilor.json",
            "istoricul căutărilor.json",
            "abonamente.csv",
        ],
    ),
    DDPCategory(
        id="json_lt",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.LT,
        known_files=[
            "žiūrėjimo istorija.json",
            "paieškos istorija.json",
            "prenumeratos.csv",
        ],
    ),
]


def extract_tables(file: str, validation, errors: Counter[str]):
    from port.helpers.entries_data_youtube import YT_CSV_ENTRIES, YT_ENTRIES
    from port.helpers.extraction_helpers import ZipArchiveReader

    reader = ZipArchiveReader(file, validation.archive_members, errors)

    for key, entries in YT_ENTRIES.items():
        try:
            df = create_table([file], entries, reader=reader)
            if not df.empty:
                yield d3i_props.PropsUIPromptConsentFormTableViz(
                    id=key,
                    data_frame=df,
                    title=props.Translatable({"en": key, "nl": key, "es": key}),
                )
        except Exception as e:
            logger.exception("Error in %s: %s", key, e)
            errors[key] += 1

    for key, entries in YT_CSV_ENTRIES.items():
        try:
            df = create_csv_table([file], entries, reader=reader)
            if not df.empty:
                yield d3i_props.PropsUIPromptConsentFormTableViz(
                    id=key,
                    data_frame=df,
                    title=props.Translatable({"en": key, "nl": key, "es": key}),
                )
        except Exception as e:
            logger.exception("Error in CSV table %s: %s", key, e)
            errors[key] += 1

    placeholder_json = structure_from_zip(file)
    df_placeholder = pd.DataFrame([{"Anonymized data structure": placeholder_json}])
    yield d3i_props.PropsUIPromptConsentFormTableViz(
        id="placeholder",
        data_frame=df_placeholder,
        title=props.Translatable({"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur", "lt": "Duomenų struktūra", "ro": "Structura datelor"}),
    )


class YouTubeFlow(FlowBuilder):
    def __init__(self, session_id: str):
        super().__init__(session_id, "YouTube")

    def validate_file(self, file):
        return validate.validate_zip(DDP_CATEGORIES, file)

    def extract_data(self, file: str, validation) -> ExtractionResult:
        errors: Counter[str] = Counter()
        tables = list(extract_tables(file, validation, errors))
        return ExtractionResult(tables=tables, errors=errors)


def process(session_id):
    flow = YouTubeFlow(session_id)
    return flow.start_flow()
