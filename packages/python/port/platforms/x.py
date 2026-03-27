"""
X

This module contains an example flow of a X data donation study

Assumptions:
It handles DDPs in the english language with filetype js.
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
from port.helpers.Structure_extractor_libraries.X_get_json_structure import (
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
            "account-creation-ip.js",
            "app.js",
            "community-tweet.js",
            "expanded-profile.js",
            "ni-devices.js",
            "professional-data.js",
            "tweet-headers.js",
            "account-label.js",
            "article-metadata.js",
            "connected-application.js",
            "follower.js",
            "note-tweet.js",
            "profile.js",
            "tweetdeck.js",
            "account-suspension.js",
            "article.js",
            "contact.js",
            "following.js",
            "periscope-account-information.js",
            "profile_media",
            "tweets.js",
            "account-timezone.js",
            "audio-video-calls-in-dm-recipient-sessions.js",
            "deleted-note-tweet.js",
            "grok-chat-item.js",
            "periscope-ban-information.js",
            "protected-history.js",
            "tweets_media",
            "account.js",
            "audio-video-calls-in-dm.js",
            "deleted-tweet-headers.js",
            "ip-audit.js",
            "periscope-broadcast-metadata.js",
            "README.txt",
            "twitter-shop.js",
            "ad-engagements.js",
            "block.js",
            "deleted-tweets.js",
            "key-registry.js",
            "periscope-comments-made-by-user.js",
            "reply-prompt.js",
            "user-link-clicks.js",
            "ad-impressions.js",
            "branch-links.js",
            "device-token.js",
            "like.js",
            "periscope-expired-broadcasts.js",
            "saved-search.js",
            "verified-organization.js",
            "ad-mobile-conversions-attributed.js",
            "catalog-item.js",
            "direct-message-group-headers.js",
            "lists-created.js",
            "periscope-followers.js",
            "screen-name-change.js",
            "verified.js",
            "ad-mobile-conversions-unattributed.js",
            "commerce-catalog.js",
            "direct-message-headers.js",
            "lists-member.js",
            "periscope-profile-description.js",
            "shop-module.js",
            "ad-online-conversions-attributed.js",
            "community-note-batsignal.js",
            "direct-message-mute.js",
            "lists-subscribed.js",
            "personalization.js",
            "shopify-account.js",
            "ad-online-conversions-unattributed.js",
            "community-note-rating.js",
            "direct-messages-group.js",
            "manifest.js",
            "phone-number.js",
            "smartblock.js",
            "ads-revenue-sharing.js",
            "community-note-tombstone.js",
            "direct-messages.js",
            "moment.js",
            "product-drop.js",
            "spaces-metadata.js",
            "ageinfo.js",
            "community-note.js",
            "email-address-change.js",
            "mute.js",
            "product-set.js",
            "sso.js",
        ],
    ),
]


def extract_tables(file: str, validation, errors: Counter[str]):
    from port.helpers.entries_data_x import X_ENTRIES
    from port.helpers.extraction_helpers import ZipArchiveReader

    reader = ZipArchiveReader(file, validation.archive_members, errors)

    for key, entries in X_ENTRIES.items():
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
        title=props.Translatable({"en": "Data structure", "es": "Estructura de datos", "nl": "Gegevensstructuur"}),
    )


class XFlow(FlowBuilder):
    def __init__(self, session_id: str):
        super().__init__(session_id, "X")

    def validate_file(self, file):
        return validate.validate_zip(DDP_CATEGORIES, file)

    def extract_data(self, file: str, validation) -> ExtractionResult:
        errors: Counter[str] = Counter()
        tables = list(extract_tables(file, validation, errors))
        return ExtractionResult(tables=tables, errors=errors)


def process(session_id):
    flow = XFlow(session_id)
    return flow.start_flow()
