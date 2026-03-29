"""
Facebook

This module contains an example flow of a Facebook data donation study

Assumptions:
It handles DDPs in the english language with filetype JSON.
"""

import logging
from collections import Counter

import pandas as pd
import port.api.d3i_props as d3i_props
import port.api.props as props
import port.helpers.validate as validate
from port.api.d3i_props import ExtractionResult
from port.helpers.flow_builder import FlowBuilder
from port.helpers.parsers import create_table
from port.helpers.Structure_extractor_libraries.FB_get_json_structure import (
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
            "subscription_for_no_ads.json",
            "other_categories_used_to_reach_you.json",
            "ads_feedback_activity.json",
            "ads_personalization_consent.json",
            "advertisers_you've_interacted_with.json",
            "advertisers_using_your_activity_or_information.json",
            "story_views_in_past_7_days.json",
            "ad_preferences.json",
            "groups_you've_searched_for.json",
            "your_search_history.json",
            "primary_public_location.json",
            "timezone.json",
            "primary_location.json",
            "your_privacy_jurisdiction.json",
            "people_and_friends.json",
            "ads_interests.json",
            "notifications.json",
            "notification_of_meta_privacy_policy_update.json",
            "recently_viewed.json",
            "recently_visited.json",
            "your_avatar.json",
            "meta_avatars_post_backgrounds.json",
            "contacts_sync_settings.json",
            "timezone.json",
            "autofill_information.json",
            "profile_information.json",
            "profile_update_history.json",
            "your_transaction_survey_information.json",
            "your_recently_followed_history.json",
            "your_recently_used_emojis.json",
            "no-data.txt",
            "navigation_bar_activity.json",
            "pages_and_profiles_you_follow.json",
            "pages_you've_liked.json",
            "your_saved_items.json",
            "fundraiser_posts_you_likely_viewed.json",
            "your_fundraiser_donations_information.json",
            "your_event_responses.json",
            "event_invitations.json",
            "your_event_invitation_links.json",
            "likes_and_reactions_1.json",
            "your_uncategorized_photos.json",
            "payment_history.json",
            "no-data.txt",
            "your_answers_to_membership_questions.json",
            "your_group_membership_activity.json",
            "your_contributions.json",
            "group_posts_and_comments.json",
            "your_comments_in_groups.json",
            "instant_games.json",
            "your_page_or_groups_badges.json",
            "instant_games_usage_data.json",
            "no-data.txt",
            "who_you've_followed.json",
            "people_you_may_know.json",
            "received_friend_requests.json",
            "your_friends.json",
            "likes_and_reactions.json",
            "controls.json",
        ],
    ),
]


def extract_tables(file: str, validation, errors: Counter[str]):
    from port.helpers.entries_data_facebook import FB_ENTRIES
    from port.helpers.extraction_helpers import ZipArchiveReader

    reader = ZipArchiveReader(file, validation.archive_members, errors)

    for key, entries in FB_ENTRIES.items():
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

    placeholder_json = structure_from_zip(file)
    df_placeholder = pd.DataFrame([{"Anonymized data structure": placeholder_json}])
    yield d3i_props.PropsUIPromptConsentFormTableViz(
        id="placeholder",
        data_frame=df_placeholder,
        title=props.Translatable({"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur", "lt": "Duomenų struktūra", "ro": "Structura datelor"}),
    )


class FacebookFlow(FlowBuilder):
    def __init__(self, session_id: str):
        super().__init__(session_id, "Facebook")

    def validate_file(self, file):
        return validate.validate_zip(DDP_CATEGORIES, file)

    def extract_data(self, file: str, validation) -> ExtractionResult:
        errors: Counter[str] = Counter()
        tables = list(extract_tables(file, validation, errors))
        return ExtractionResult(tables=tables, errors=errors)


def process(session_id):
    flow = FacebookFlow(session_id)
    return flow.start_flow()
