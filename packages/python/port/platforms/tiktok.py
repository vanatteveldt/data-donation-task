"""
TikTok

This module contains an example flow of a TikTok data donation study.

Assumptions:
It handles DDPs in the English language with filetype JSON (user_data.json).
TikTok changed their export format from .txt to .json. Several section names
also changed; both old and new names are tried when navigating the JSON.
"""

import logging
from collections import Counter

import pandas as pd
import port.api.d3i_props as d3i_props
import port.api.props as props
import port.helpers.port_helpers as ph
import port.helpers.validate as validate
from port.api.d3i_props import ExtractionResult
from port.helpers.flow_builder import FlowBuilder
from port.helpers.parsers import create_table
from port.helpers.Structure_extractor_libraries.TT_get_json_structure import (
    structure_from_json_file,
)
from port.helpers.validate import DDPCategory, DDPFiletype, Language

logger = logging.getLogger(__name__)

DDP_CATEGORIES = [
    DDPCategory(
        id="json_en",
        ddp_filetype=DDPFiletype.JSON,
        language=Language.EN,
        known_files=[
            "user_data.json",
            "user_data_tiktok.json",
        ],
    ),
]


def extract_tables(file: str, validation, errors: Counter[str]):
    from port.helpers.entries_data_tiktok import TIKTOK_ENTRIES

    for key, entries in TIKTOK_ENTRIES.items():
        try:
            df = create_table([file], entries)
            if not df.empty:
                yield d3i_props.PropsUIPromptConsentFormTableViz(
                    id=key,
                    data_frame=df,
                    title=props.Translatable({"en": key, "nl": key, "es": key}),
                )
        except Exception as e:
            logger.exception("Error in %s: %s", key, e)
            errors[key] += 1

    placeholder_json = structure_from_json_file(file)
    df_placeholder = pd.DataFrame([{"Anonymized data structure": placeholder_json}])
    yield d3i_props.PropsUIPromptConsentFormTableViz(
        id="placeholder",
        data_frame=df_placeholder,
        title=props.Translatable({"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur", "lt": "Duomenų struktūra", "ro": "Structura datelor"}),
    )


class TikTokFlow(FlowBuilder):
    def __init__(self, session_id: str):
        super().__init__(session_id, "TikTok")

    def generate_file_prompt(self):
        return ph.generate_file_prompt("application/json, application/zip")

    def validate_file(self, file) -> validate.ValidateInput:
        import json

        # Try zip first (TikTok also offers zip exports)
        v = validate.validate_zip(DDP_CATEGORIES, file)
        if v.get_status_code_id() == 0:
            return v
        # Fall back: plain JSON file
        status_codes = [
            validate.StatusCode(id=0, description="Valid TikTok JSON"),
            validate.StatusCode(id=1, description="Invalid TikTok file"),
        ]
        v2 = validate.ValidateInput(status_codes, DDP_CATEGORIES)
        try:
            with open(file) as f:
                data = json.load(f)
            if isinstance(data, dict):
                v2.set_current_status_code_by_id(0)
                v2.current_ddp_category = DDP_CATEGORIES[0]
            else:
                v2.set_current_status_code_by_id(1)
        except Exception:
            v2.set_current_status_code_by_id(1)
        return v2

    def extract_data(self, file: str, validation) -> ExtractionResult:
        errors: Counter[str] = Counter()
        tables = list(extract_tables(file, validation, errors))
        return ExtractionResult(tables=tables, errors=errors)


def process(session_id):
    flow = TikTokFlow(session_id)
    return flow.start_flow()
