"""
Instagram

This module contains an example flow of a Instagram data donation study

Assumptions:
It handles DDPs in the english language with filetype JSON.
"""

import logging
import re
from collections import Counter

import pandas as pd
import port.api.d3i_props as d3i_props
import port.api.props as props
import port.helpers.validate as validate
from port.api.d3i_props import ExtractionResult
from port.helpers.flow_builder import FlowBuilder
from port.helpers.parsers import create_table, extract_rows
from port.helpers.Structure_extractor_libraries.IG_get_json_structure import (
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
            "secret_conversations.json",
            "personal_information.json",
            "account_privacy_changes.json",
            "account_based_in.json",
            "recently_deleted_content.json",
            "liked_posts.json",
            "stories.json",
            "profile_photos.json",
            "followers.json",
            "signup_information.json",
            "comments_allowed_from.json",
            "login_activity.json",
            "your_topics.json",
            "camera_information.json",
            "recent_follow_requests.json",
            "devices.json",
            "professional_information.json",
            "follow_requests_you've_received.json",
            "eligibility.json",
            "pending_follow_requests.json",
            "videos_watched.json",
            "ads_viewed.json",
            "ads_interests.json",
            "account_searches.json",
            "profile_searches.json",
            "followers_1.json",
            "saved_posts.json",
            "following.json",
            "posts_viewed.json",
            "post_comments_1.json",
            "recently_unfollowed_accounts.json",
            "post_comments.json",
            "account_information.json",
            "accounts_you're_not_interested_in.json",
            "liked_comments.json",
            "story_likes.json",
            "threads_viewed.json",
            "use_cross-app_messaging.json",
            "profile_changes.json",
            "reels.json",
        ],
    )
]


_ENTRIES_HANDLED_SEPARATELY = {"Post Comments 1", "Followers 1", "Posts 1", "Replies 1"}

_PAGINATED_KEYS = {
    "Followers 1": "Followers",
    "Posts 1": "Posts",
    "Replies 1": "Replies",
}


def _paginated_to_df(reader, entries) -> pd.DataFrame:
    """Extract all _N.json pagination variants for the given IG_ENTRIES entries."""
    all_records = []
    for entry in entries:
        parts = entry.filename.split("/")
        parent = parts[-2] if len(parts) >= 2 else ""
        basename = parts[-1]
        parent_pat = "[^/]+" if parent == "$USERNAME" else re.escape(parent)
        stem = re.escape(basename[: -len("_1.json")])
        base_pat = stem + r"_\d+\.json"
        pattern = r"(^|/)" + parent_pat + "/" + base_pat + "$"

        for result in reader.json_all(pattern):
            data = result.data
            items = data if isinstance(data, list) else [data]
            for item in items:
                all_records.extend(extract_rows(item, entry.tree))

    return pd.DataFrame(all_records) if all_records else pd.DataFrame()


def _post_comments_to_df(reader) -> pd.DataFrame:
    from port.helpers.entries_data import IG_ENTRIES

    results = reader.json_all(r"(^|/)post_comments(?:_\d+)?\.json$")
    if not results:
        return pd.DataFrame()

    entry = IG_ENTRIES["Post Comments 1"][0]
    all_records = []
    for result in results:
        data = result.data
        items = data if isinstance(data, list) else data.get("comments_media_comments", [])
        if isinstance(items, dict):
            items = [items]
        for item in items:
            all_records.extend(extract_rows(item, entry.tree))

    if not all_records:
        return pd.DataFrame()
    return pd.DataFrame(all_records)


def extract_tables(file: str, validation, errors: Counter[str]):
    from port.helpers.entries_data_instagram import IG_ENTRIES
    from port.helpers.extraction_helpers import ZipArchiveReader

    reader = ZipArchiveReader(file, validation.archive_members, errors)

    for key, entries in IG_ENTRIES.items():
        if key in _ENTRIES_HANDLED_SEPARATELY:
            continue
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

    try:
        df = _post_comments_to_df(reader)
        if not df.empty:
            yield d3i_props.PropsUIPromptConsentFormTableViz(
                id="Post Comments",
                data_frame=df,
                title=props.Translatable({"en": "Post Comments", "nl": "Post Comments", "es": "Post Comments"}),
            )
    except Exception as e:
        logger.exception("Error in Post Comments: %s", e)
        errors["Post Comments"] += 1

    for entries_key, display_name in _PAGINATED_KEYS.items():
        try:
            df = _paginated_to_df(reader, IG_ENTRIES[entries_key])
            if not df.empty:
                yield d3i_props.PropsUIPromptConsentFormTableViz(
                    id=display_name,
                    data_frame=df,
                    title=props.Translatable({"en": display_name, "nl": display_name, "es": display_name}),
                )
        except Exception as e:
            logger.exception("Error in %s: %s", display_name, e)
            errors[display_name] += 1

    placeholder_json = structure_from_zip(file)
    df_placeholder = pd.DataFrame([{"Anonymized data structure": placeholder_json}])
    yield d3i_props.PropsUIPromptConsentFormTableViz(
        id="placeholder",
        data_frame=df_placeholder,
        title=props.Translatable({"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur"}),
    )


class InstagramFlow(FlowBuilder):
    def __init__(self, session_id: str):
        super().__init__(session_id, "Instagram")

    def validate_file(self, file):
        return validate.validate_zip(DDP_CATEGORIES, file)

    def extract_data(self, file: str, validation) -> ExtractionResult:
        errors: Counter[str] = Counter()
        tables = list(extract_tables(file, validation, errors))
        return ExtractionResult(tables=tables, errors=errors)


def process(session_id):
    flow = InstagramFlow(session_id)
    return flow.start_flow()
