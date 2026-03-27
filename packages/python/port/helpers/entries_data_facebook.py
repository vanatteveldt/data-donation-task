"""
Donation file structure data for Facebook takeout flows

Split from entries_data.py. To regenerate, run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

FB_ENTRIES: dict[str, list[Entry]] = {
    "$Username": [
        Entry(
            table="$Username",
            filename="your_facebook_activity/groups/your_group_messages/$USERNAME.json",
            tree=Node(columns={"thread_name": ("thread_name",)}, children={}),
        ),
    ],
    "Ad Preferences": [
        Entry(
            table="Ad Preferences",
            filename="ads_information/ad_preferences.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",), "label": ("label",), "value": ("value",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "ent_field_name": ("ent_field_name",),
                                            "label": ("label",),
                                            "value": ("value",),
                                            "timestamp_value": ("timestamp_value",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "vec": Node(columns={"value": ("value",)}, children={}),
                        },
                    )
                },
            ),
        ),
    ],
    "Admin Activity": [
        Entry(
            table="Admin Activity",
            filename="your_facebook_activity/pages/admin_activity.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "value": ("value",), "href": ("href",)}, children={})
                },
            ),
        ),
    ],
    "Ads About Meta": [
        Entry(
            table="Ads About Meta",
            filename="ads_information/ads_about_meta.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "timestamp_value": ("timestamp_value",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Ads Feedback Activity": [
        Entry(
            table="Ads Feedback Activity",
            filename="ads_information/ads_feedback_activity.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "timestamp_value": ("timestamp_value",)}, children={})
                },
            ),
        ),
    ],
    "Ads Interests": [
        Entry(
            table="Ads Interests",
            filename="logged_information/other_logged_information/ads_interests.json",
            tree=Node(columns={}, children={"topics_v2": Node(columns={"topics_v2": ()}, children={})}),
        ),
    ],
    "Ads Personalization Consent": [
        Entry(
            table="Ads Personalization Consent",
            filename="ads_information/ads_personalization_consent.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "timestamp_value": ("timestamp_value",),
                            "ent_field_name": ("ent_field_name",),
                            "value": ("value",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Ads Viewed": [
        Entry(
            table="Ads Viewed",
            filename="ads_information/ads_and_topics/ads_viewed.json",
            tree=Node(
                columns={},
                children={
                    "impressions_history_ads_seen": Node(
                        columns={
                            "value": ("string_map_data", "Author", "value"),
                            "timestamp": ("string_map_data", "Time", "timestamp"),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Advertisers Using Your Activity Or Information": [
        Entry(
            table="Advertisers Using Your Activity Or Information",
            filename="ads_information/advertisers_using_your_activity_or_information.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "ent_field_name": ("ent_field_name",)},
                        children={"vec": Node(columns={"value": ("value",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Advertisers You Ve Interacted With": [
        Entry(
            table="Advertisers You Ve Interacted With",
            filename="ads_information/advertisers_you_ve_interacted_with.json",
            tree=Node(
                columns={},
                children={
                    "history_v2": Node(
                        columns={"title": ("title",), "action": ("action",), "timestamp": ("timestamp",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Advertisers You'Ve Interacted With": [
        Entry(
            table="Advertisers You'Ve Interacted With",
            filename="ads_information/advertisers_you've_interacted_with.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "history_v2": Node(
                        columns={"title": ("title",), "action": ("action",), "timestamp": ("timestamp",)}, children={}
                    ),
                    "label_values": Node(columns={"label": ("label",)}, children={}),
                },
            ),
        ),
    ],
    "Ai Conversations": [
        Entry(
            table="Ai Conversations",
            filename="your_facebook_activity/messages/ai_conversations.json",
            tree=Node(
                columns={"title": ("title",), "timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "title": ("title",)},
                        children={
                            "dict": Node(
                                columns={"label": ("label",), "value": ("value",), "href": ("href",), "title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "label": ("label",),
                                            "value": ("value",),
                                            "title": ("title",),
                                            "timestamp_value": ("timestamp_value",),
                                        },
                                        children={"vec": Node(columns={"vec": ()}, children={})},
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Archived Stories": [
        Entry(
            table="Archived Stories",
            filename="your_facebook_activity/stories/archived_stories.json",
            tree=Node(
                columns={},
                children={
                    "archived_stories_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={
                                            "uri": ("media", "uri"),
                                            "creation_timestamp": ("media", "creation_timestamp"),
                                            "title": ("media", "title"),
                                            "description": ("media", "description"),
                                        },
                                        children={},
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Close Friends": [
        Entry(
            table="Close Friends",
            filename="connections/followers_and_following/close_friends.json",
            tree=Node(
                columns={},
                children={
                    "relationships_close_friends": Node(
                        columns={"title": ("title",)},
                        children={
                            "string_list_data": Node(
                                columns={"href": ("href",), "value": ("value",), "timestamp": ("timestamp",)}, children={}
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Collections": [
        Entry(
            table="Collections",
            filename="your_facebook_activity/saved_items_and_collections/collections.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={}),
                    "collections_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "attachments": Node(columns={}, children={"data": Node(columns={"name": ("name",)}, children={})})
                        },
                    ),
                },
            ),
        ),
    ],
    "Comments": [
        Entry(
            table="Comments",
            filename="personal_information/profile_information/your_facebook_activity/comments_and_reactions/comments.json",
            tree=Node(
                columns={},
                children={
                    "comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={"timestamp": ("comment", "timestamp"), "comment": ("comment", "comment")}, children={}
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Comments",
            filename="your_activity_across_facebook/comments_and_reactions/comments.json",
            tree=Node(
                columns={},
                children={
                    "comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={"timestamp": ("comment", "timestamp"), "comment": ("comment", "comment")}, children={}
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Comments",
            filename="your_facebook_activity/comments_and_reactions/comments.json",
            tree=Node(
                columns={},
                children={
                    "comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={"timestamp": ("comment", "timestamp"), "comment": ("comment", "comment")}, children={}
                            ),
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={
                                            "uri": ("media", "uri"),
                                            "creation_timestamp": ("media", "creation_timestamp"),
                                            "url": ("external_context", "url"),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Comments Allowed From": [
        Entry(
            table="Comments Allowed From",
            filename="preferences/settings/comments_allowed_from.json",
            tree=Node(
                columns={},
                children={
                    "settings_allow_comments_from": Node(
                        columns={
                            "title": ("title",),
                            "href": ("string_map_data", "Comments Allowed From", "href"),
                            "value": ("string_map_data", "Comments Allowed From", "value"),
                            "timestamp": ("string_map_data", "Comments Allowed From", "timestamp"),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Consents": [
        Entry(
            table="Consents",
            filename="logged_information/other_logged_information/consents.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "ent_field_name": ("ent_field_name",),
                            "timestamp_value": ("timestamp_value",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Content Sharing Links You Have Created": [
        Entry(
            table="Content Sharing Links You Have Created",
            filename="personal_information/profile_information/your_facebook_activity/posts/content_sharing_links_you_have_created.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "value": ("value",), "href": ("href",)}, children={})
                },
            ),
        ),
        Entry(
            table="Content Sharing Links You Have Created",
            filename="your_facebook_activity/posts/content_sharing_links_you_have_created.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "href": ("href",),
                            "ent_field_name": ("ent_field_name",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Controls": [
        Entry(
            table="Controls",
            filename="personal_information/profile_information/preferences/feed/controls.json",
            tree=Node(
                columns={},
                children={
                    "controls": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={"timestamp": ("timestamp",), "name": ("data", "name"), "uri": ("data", "uri")},
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Controls",
            filename="preferences/feed/controls.json",
            tree=Node(
                columns={},
                children={
                    "controls": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={"timestamp": ("timestamp",), "name": ("data", "name"), "uri": ("data", "uri")},
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Edits You Made To Posts": [
        Entry(
            table="Edits You Made To Posts",
            filename="personal_information/profile_information/your_facebook_activity/posts/edits_you_made_to_posts.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Edits You Made To Posts",
            filename="your_facebook_activity/posts/edits_you_made_to_posts.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Emails We Sent You": [
        Entry(
            table="Emails We Sent You",
            filename="personal_information/other_personal_information/emails_we_sent_you.json",
            tree=Node(columns={"title": ("title",), "timestamp": ("timestamp",)}, children={}),
        ),
    ],
    "Facebook Reels Usage Information": [
        Entry(
            table="Facebook Reels Usage Information",
            filename="logged_information/other_logged_information/facebook_reels_usage_information.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "ent_field_name": ("ent_field_name",)},
                        children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Feed": [
        Entry(
            table="Feed",
            filename="preferences/feed/feed.json",
            tree=Node(
                columns={},
                children={
                    "people_and_friends_v2": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={"timestamp": ("timestamp",), "name": ("data", "name"), "uri": ("data", "uri")},
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Follow Requests You'Ve Received": [
        Entry(
            table="Follow Requests You'Ve Received",
            filename="connections/followers_and_following/follow_requests_you've_received.json",
            tree=Node(
                columns={},
                children={
                    "relationships_follow_requests_received": Node(
                        columns={"title": ("title",)},
                        children={
                            "string_list_data": Node(
                                columns={"href": ("href",), "value": ("value",), "timestamp": ("timestamp",)}, children={}
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Followers 1": [
        Entry(
            table="Followers 1",
            filename="connections/followers_and_following/followers_1.json",
            tree=Node(
                columns={"title": ("title",)},
                children={
                    "string_list_data": Node(
                        columns={"href": ("href",), "value": ("value",), "timestamp": ("timestamp",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Following": [
        Entry(
            table="Following",
            filename="connections/followers_and_following/following.json",
            tree=Node(
                columns={},
                children={
                    "relationships_following": Node(
                        columns={"title": ("title",)},
                        children={
                            "string_list_data": Node(
                                columns={"href": ("href",), "value": ("value",), "timestamp": ("timestamp",)}, children={}
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Group Invites You'Ve Received": [
        Entry(
            table="Group Invites You'Ve Received",
            filename="your_facebook_activity/groups/group_invites_you've_received.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "timestamp_value": ("timestamp_value",),
                            "value": ("value",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Group Invites You'Ve Sent": [
        Entry(
            table="Group Invites You'Ve Sent",
            filename="your_facebook_activity/groups/group_invites_you've_sent.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Group Posts And Comments": [
        Entry(
            table="Group Posts And Comments",
            filename="your_activity_across_facebook/groups/group_posts_and_comments.json",
            tree=Node(
                columns={},
                children={
                    "group_posts_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"post": ("post",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Group Posts And Comments",
            filename="your_facebook_activity/groups/group_posts_and_comments.json",
            tree=Node(
                columns={},
                children={
                    "group_posts_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "data": Node(columns={"post": ("post",)}, children={}),
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={
                                            "uri": ("media", "uri"),
                                            "creation_timestamp": ("media", "creation_timestamp"),
                                            "description": ("media", "description"),
                                            "title": ("media", "title"),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Groups And Pages That You May Find Engaging": [
        Entry(
            table="Groups And Pages That You May Find Engaging",
            filename="your_facebook_activity/groups/groups_and_pages_that_you_may_find_engaging.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"ent_field_name": ("ent_field_name",), "label": ("label",)},
                        children={"vec": Node(columns={"value": ("value",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Groups You Ve Visited": [
        Entry(
            table="Groups You Ve Visited",
            filename="logged_information/your_interactions_on_facebook/groups_you_ve_visited.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"ent_field_name": ("ent_field_name",), "label": ("label",), "value": ("value",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Groups You'Ve Searched For": [
        Entry(
            table="Groups You'Ve Searched For",
            filename="logged_information/search/groups_you've_searched_for.json",
            tree=Node(
                columns={},
                children={
                    "group_search": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "data": Node(columns={"text": ("text",)}, children={}),
                            "attachments": Node(columns={}, children={"data": Node(columns={"text": ("text",)}, children={})}),
                        },
                    )
                },
            ),
        ),
    ],
    "Groups You'Ve Visited": [
        Entry(
            table="Groups You'Ve Visited",
            filename="logged_information/interactions/groups_you've_visited.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Groups You'Ve Visited",
            filename="logged_information/your_interactions_on_facebook/groups_you've_visited.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Information You'Ve Submitted To Advertisers": [
        Entry(
            table="Information You'Ve Submitted To Advertisers",
            filename="ads_information/information_you've_submitted_to_advertisers.json",
            tree=Node(
                columns={}, children={"lead_gen_info_v2": Node(columns={"label": ("label",), "value": ("value",)}, children={})}
            ),
        ),
    ],
    "Join Requests": [
        Entry(
            table="Join Requests",
            filename="your_facebook_activity/groups/join_requests.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"title": ("title",)},
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Likes And Reactions": [
        Entry(
            table="Likes And Reactions",
            filename="personal_information/profile_information/your_facebook_activity/comments_and_reactions/likes_and_reactions.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Likes And Reactions",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "href": ("href",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "ent_field_name": ("ent_field_name",),
                                            "label": ("label",),
                                            "value": ("value",),
                                        },
                                        children={},
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Likes And Reactions 1": [
        Entry(
            table="Likes And Reactions 1",
            filename="personal_information/profile_information/your_facebook_activity/comments_and_reactions/likes_and_reactions_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
        Entry(
            table="Likes And Reactions 1",
            filename="your_activity_across_facebook/comments_and_reactions/likes_and_reactions_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
        Entry(
            table="Likes And Reactions 1",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Likes And Reactions 2": [
        Entry(
            table="Likes And Reactions 2",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_2.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Likes And Reactions 3": [
        Entry(
            table="Likes And Reactions 3",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_3.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Likes And Reactions 4": [
        Entry(
            table="Likes And Reactions 4",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_4.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Likes And Reactions 5": [
        Entry(
            table="Likes And Reactions 5",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_5.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Likes And Reactions 6": [
        Entry(
            table="Likes And Reactions 6",
            filename="your_facebook_activity/comments_and_reactions/likes_and_reactions_6.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"data": Node(columns={"reaction": ("reaction", "reaction")}, children={})},
            ),
        ),
    ],
    "Link History": [
        Entry(
            table="Link History",
            filename="your_facebook_activity/other_activity/link_history.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "value": ("value",), "href": ("href",)}, children={})
                },
            ),
        ),
    ],
    "Other Categories Used To Reach You": [
        Entry(
            table="Other Categories Used To Reach You",
            filename="ads_information/other_categories_used_to_reach_you.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "ent_field_name": ("ent_field_name",)},
                        children={"vec": Node(columns={"value": ("value",)}, children={})},
                    ),
                    "bcts": Node(columns={"bcts": ()}, children={}),
                },
            ),
        ),
    ],
    "Pages And Profiles You Follow": [
        Entry(
            table="Pages And Profiles You Follow",
            filename="personal_information/profile_information/your_facebook_activity/pages/pages_and_profiles_you_follow.json",
            tree=Node(
                columns={},
                children={
                    "pages_followed_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Pages And Profiles You Follow",
            filename="your_activity_across_facebook/pages/pages_and_profiles_you_follow.json",
            tree=Node(
                columns={},
                children={
                    "pages_followed_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Pages And Profiles You Follow",
            filename="your_facebook_activity/pages/pages_and_profiles_you_follow.json",
            tree=Node(
                columns={},
                children={
                    "pages_followed_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Pages And Profiles You'Ve Recommended": [
        Entry(
            table="Pages And Profiles You'Ve Recommended",
            filename="your_facebook_activity/pages/pages_and_profiles_you've_recommended.json",
            tree=Node(
                columns={},
                children={
                    "recommended_pages_v2": Node(
                        columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Pages And Profiles You'Ve Unfollowed": [
        Entry(
            table="Pages And Profiles You'Ve Unfollowed",
            filename="your_facebook_activity/pages/pages_and_profiles_you've_unfollowed.json",
            tree=Node(
                columns={},
                children={
                    "pages_unfollowed_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Pages You Are A Customer Of": [
        Entry(
            table="Pages You Are A Customer Of",
            filename="your_facebook_activity/pages/pages_you_are_a_customer_of.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "timestamp_value": ("timestamp_value",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={"label": ("label",), "value": ("value",), "href": ("href",)}, children={}
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Pages You Ve Liked": [
        Entry(
            table="Pages You Ve Liked",
            filename="your_facebook_activity/pages/pages_you_ve_liked.json",
            tree=Node(
                columns={},
                children={
                    "page_likes_v2": Node(
                        columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Pages You'Ve Liked": [
        Entry(
            table="Pages You'Ve Liked",
            filename="personal_information/profile_information/your_facebook_activity/pages/pages_you've_liked.json",
            tree=Node(
                columns={},
                children={
                    "page_likes_v2": Node(
                        columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={}
                    )
                },
            ),
        ),
        Entry(
            table="Pages You'Ve Liked",
            filename="your_activity_across_facebook/pages/pages_you've_liked.json",
            tree=Node(
                columns={},
                children={
                    "page_likes_v2": Node(
                        columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={}
                    )
                },
            ),
        ),
        Entry(
            table="Pages You'Ve Liked",
            filename="your_facebook_activity/pages/pages_you've_liked.json",
            tree=Node(
                columns={},
                children={
                    "page_likes_v2": Node(
                        columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={}
                    )
                },
            ),
        ),
    ],
    "People And Friends": [
        Entry(
            table="People And Friends",
            filename="logged_information/activity_messages/people_and_friends.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "people_interactions_v2": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={"timestamp": ("timestamp",), "name": ("data", "name"), "uri": ("data", "uri")},
                                children={},
                            )
                        },
                    ),
                    "label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={}),
                },
            ),
        ),
    ],
    "People We Think You Should Follow": [
        Entry(
            table="People We Think You Should Follow",
            filename="logged_information/your_topics/people_we_think_you_should_follow.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={"label_values": Node(columns={"label": ("label",)}, children={})},
            ),
        ),
    ],
    "Polls You Voted On": [
        Entry(
            table="Polls You Voted On",
            filename="your_activity_across_facebook/polls/polls_you_voted_on.json",
            tree=Node(
                columns={},
                children={
                    "poll_votes_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={"question": ("poll", "question")},
                                        children={
                                            "poll": Node(
                                                columns={},
                                                children={
                                                    "options": Node(
                                                        columns={"option": ("option",), "voted": ("voted",)}, children={}
                                                    )
                                                },
                                            )
                                        },
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Polls You Voted On",
            filename="your_facebook_activity/polls/polls_you_voted_on.json",
            tree=Node(
                columns={},
                children={
                    "poll_votes_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={},
                                        children={
                                            "poll": Node(
                                                columns={},
                                                children={
                                                    "options": Node(
                                                        columns={"option": ("option",), "voted": ("voted",)}, children={}
                                                    )
                                                },
                                            )
                                        },
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Posts On Other Pages And Profiles": [
        Entry(
            table="Posts On Other Pages And Profiles",
            filename="personal_information/profile_information/your_facebook_activity/posts/posts_on_other_pages_and_profiles.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Posts On Other Pages And Profiles",
            filename="your_facebook_activity/posts/posts_on_other_pages_and_profiles.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "timestamp_value": ("timestamp_value",),
                            "title": ("title",),
                        },
                        children={
                            "media": Node(
                                columns={
                                    "uri": ("uri",),
                                    "creation_timestamp": ("creation_timestamp",),
                                    "description": ("description",),
                                },
                                children={},
                            ),
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "label": ("label",),
                                            "timestamp_value": ("timestamp_value",),
                                            "value": ("value",),
                                            "title": ("title",),
                                        },
                                        children={
                                            "media": Node(
                                                columns={
                                                    "uri": ("uri",),
                                                    "creation_timestamp": ("creation_timestamp",),
                                                    "description": ("description",),
                                                },
                                                children={},
                                            )
                                        },
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Posts Viewed": [
        Entry(
            table="Posts Viewed",
            filename="ads_information/ads_and_topics/posts_viewed.json",
            tree=Node(
                columns={},
                children={
                    "impressions_history_posts_seen": Node(
                        columns={
                            "value": ("string_map_data", "Author", "value"),
                            "timestamp": ("string_map_data", "Time", "timestamp"),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Privacy Settings": [
        Entry(
            table="Privacy Settings",
            filename="personal_information/profile_information/preferences/preferences/privacy_settings.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Privacy Settings",
            filename="preferences/preferences/privacy_settings.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Professional Information": [
        Entry(
            table="Professional Information",
            filename="personal_information/personal_information/professional_information.json",
            tree=Node(columns={}, children={"profile_business": Node(columns={"title": ("title",)}, children={})}),
        ),
    ],
    "Profile Information": [
        Entry(
            table="Profile Information",
            filename="personal_information/profile_information/profile_information.json",
            tree=Node(
                columns={},
                children={
                    "profile_v2": Node(
                        columns={}, children={"phone_numbers": Node(columns={"verified": ("verified",)}, children={})}
                    )
                },
            ),
        ),
    ],
    "Recently Viewed": [
        Entry(
            table="Recently Viewed",
            filename="logged_information/interactions/recently_viewed.json",
            tree=Node(
                columns={},
                children={
                    "recently_viewed": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "children": Node(
                                columns={"name": ("name",), "description": ("description",)},
                                children={
                                    "entries": Node(
                                        columns={
                                            "timestamp": ("timestamp",),
                                            "name": ("data", "name"),
                                            "uri": ("data", "uri"),
                                            "watch_time": ("data", "watch_time"),
                                            "value": ("data", "value"),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "entries": Node(
                                columns={
                                    "timestamp": ("timestamp",),
                                    "name": ("data", "name"),
                                    "uri": ("data", "uri"),
                                    "share": ("data", "share"),
                                },
                                children={},
                            ),
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Recently Viewed",
            filename="logged_information/your_interactions_on_facebook/recently_viewed.json",
            tree=Node(
                columns={},
                children={
                    "recently_viewed": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={"timestamp": ("timestamp",), "name": ("data", "name"), "uri": ("data", "uri")},
                                children={},
                            ),
                            "children": Node(
                                columns={"name": ("name",), "description": ("description",)},
                                children={
                                    "entries": Node(
                                        columns={
                                            "timestamp": ("timestamp",),
                                            "value": ("data", "value"),
                                            "name": ("data", "name"),
                                            "uri": ("data", "uri"),
                                            "watch_time": ("data", "watch_time"),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Recently Visited": [
        Entry(
            table="Recently Visited",
            filename="logged_information/interactions/recently_visited.json",
            tree=Node(
                columns={},
                children={
                    "visited_things_v2": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={
                                    "timestamp": ("timestamp",),
                                    "name": ("data", "name"),
                                    "uri": ("data", "uri"),
                                    "value": ("data", "value"),
                                },
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Recently Visited",
            filename="logged_information/your_interactions_on_facebook/recently_visited.json",
            tree=Node(
                columns={},
                children={
                    "visited_things_v2": Node(
                        columns={"name": ("name",), "description": ("description",)},
                        children={
                            "entries": Node(
                                columns={
                                    "timestamp": ("timestamp",),
                                    "name": ("data", "name"),
                                    "uri": ("data", "uri"),
                                    "value": ("data", "value"),
                                },
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Recommended Topics": [
        Entry(
            table="Recommended Topics",
            filename="preferences/your_topics/recommended_topics.json",
            tree=Node(
                columns={},
                children={
                    "topics_your_topics": Node(
                        columns={
                            "title": ("title",),
                            "href": ("string_map_data", "Name", "href"),
                            "value": ("string_map_data", "Name", "value"),
                            "timestamp": ("string_map_data", "Name", "timestamp"),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Reduce": [
        Entry(
            table="Reduce",
            filename="preferences/feed/reduce.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "ent_field_name": ("ent_field_name",),
                            "label": ("label",),
                            "value": ("value",),
                            "timestamp_value": ("timestamp_value",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Reels Preferences": [
        Entry(
            table="Reels Preferences",
            filename="personal_information/profile_information/preferences/preferences/reels_preferences.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Reels Preferences",
            filename="preferences/preferences/reels_preferences.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "ent_field_name": ("ent_field_name",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Registration Information": [
        Entry(
            table="Registration Information",
            filename="security_and_login_information/registration_information.json",
            tree=Node(columns={"timestamp": ("timestamp",)}, children={}),
        ),
    ],
    "Shared Memories": [
        Entry(
            table="Shared Memories",
            filename="your_facebook_activity/posts/shared_memories.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={
                            "media": Node(
                                columns={"uri": ("uri",), "creation_timestamp": ("creation_timestamp",), "title": ("title",)},
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Snooze": [
        Entry(
            table="Snooze",
            filename="personal_information/profile_information/preferences/feed/snooze.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Snooze",
            filename="preferences/feed/snooze.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "timestamp_value": ("timestamp_value",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Story Reactions": [
        Entry(
            table="Story Reactions",
            filename="personal_information/profile_information/your_facebook_activity/stories/story_reactions.json",
            tree=Node(columns={}, children={"stories_feedback_v2": Node(columns={"title": ("title",)}, children={})}),
        ),
        Entry(
            table="Story Reactions",
            filename="your_facebook_activity/stories/story_reactions.json",
            tree=Node(
                columns={},
                children={
                    "stories_feedback_v2": Node(
                        columns={"title": ("title",), "timestamp": ("timestamp",)},
                        children={"data": Node(columns={"text": ("text",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Story Views In Past 7 Days": [
        Entry(
            table="Story Views In Past 7 Days",
            filename="ads_information/story_views_in_past_7_days.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Subscription For No Ads": [
        Entry(
            table="Subscription For No Ads",
            filename="ads_information/subscription_for_no_ads.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Support Messages": [
        Entry(
            table="Support Messages",
            filename="personal_information/profile_information/your_facebook_activity/messages/support_messages.json",
            tree=Node(
                columns={
                    "timestamp": ("support_messages", "7156925894430515", "timestamp"),
                    "subject": ("support_messages", "7156925894430515", "subject"),
                },
                children={
                    "support_messages": Node(
                        columns={},
                        children={
                            "8752122044910884": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "7156925894430515": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Support Messages",
            filename="your_facebook_activity/messages/support_messages.json",
            tree=Node(
                columns={
                    "timestamp": ("support_messages", "10236753073510368", "timestamp"),
                    "subject": ("support_messages", "10236753073510368", "subject"),
                },
                children={
                    "support_messages": Node(
                        columns={},
                        children={
                            "10230171959787248": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "10223298304470161": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "10237935489150020": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "10237421081890160": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "10237203958142202": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                            "10236753073510368": Node(
                                columns={},
                                children={
                                    "messages": Node(
                                        columns={
                                            "from": ("from",),
                                            "to": ("to",),
                                            "subject": ("subject",),
                                            "message": ("message",),
                                            "timestamp": ("timestamp",),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Time Spent On Facebook": [
        Entry(
            table="Time Spent On Facebook",
            filename="personal_information/profile_information/your_facebook_activity/other_activity/time_spent_on_facebook.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={
                            "vec": Node(
                                columns={},
                                children={
                                    "dict": Node(
                                        columns={"label": ("label",), "timestamp_value": ("timestamp_value",)}, children={}
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Time Spent On Facebook",
            filename="your_facebook_activity/other_activity/time_spent_on_facebook.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "ent_field_name": ("ent_field_name",),
                            "timestamp_value": ("timestamp_value",),
                        },
                        children={
                            "vec": Node(
                                columns={},
                                children={
                                    "dict": Node(
                                        columns={"label": ("label",), "timestamp_value": ("timestamp_value",)}, children={}
                                    )
                                },
                            ),
                            "dict": Node(columns={"label": ("label",), "value": ("value",)}, children={}),
                        },
                    )
                },
            ),
        ),
    ],
    "Video": [
        Entry(
            table="Video",
            filename="personal_information/profile_information/preferences/preferences/video.json",
            tree=Node(
                columns={},
                children={
                    "watch_videos_v2": Node(
                        columns={
                            "video_title": ("video_title",),
                            "user_action": ("user_action",),
                            "action_time": ("action_time",),
                            "feedback_collection": ("feedback_collection",),
                        },
                        children={},
                    )
                },
            ),
        ),
        Entry(
            table="Video",
            filename="preferences/preferences/video.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "watch_videos_v2": Node(
                        columns={
                            "video_title": ("video_title",),
                            "user_action": ("user_action",),
                            "action_time": ("action_time",),
                            "feedback_collection": ("feedback_collection",),
                        },
                        children={},
                    ),
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "timestamp_value": ("timestamp_value",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "ent_field_name": ("ent_field_name",),
                                            "label": ("label",),
                                            "value": ("value",),
                                            "href": ("href",),
                                            "title": ("title",),
                                        },
                                        children={
                                            "dict": Node(
                                                columns={"title": ("title",)},
                                                children={
                                                    "dict": Node(
                                                        columns={
                                                            "ent_field_name": ("ent_field_name",),
                                                            "label": ("label",),
                                                            "value": ("value",),
                                                        },
                                                        children={},
                                                    )
                                                },
                                            )
                                        },
                                    )
                                },
                            )
                        },
                    ),
                },
            ),
        ),
    ],
    "Videos Watched": [
        Entry(
            table="Videos Watched",
            filename="ads_information/ads_and_topics/videos_watched.json",
            tree=Node(
                columns={},
                children={
                    "impressions_history_videos_watched": Node(
                        columns={
                            "value": ("string_map_data", "Author", "value"),
                            "timestamp": ("string_map_data", "Time", "timestamp"),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Who You Ve Followed": [
        Entry(
            table="Who You Ve Followed",
            filename="connections/followers/who_you_ve_followed.json",
            tree=Node(
                columns={},
                children={"following_v3": Node(columns={"name": ("name",), "timestamp": ("timestamp",)}, children={})},
            ),
        ),
    ],
    "Who You'Ve Followed": [
        Entry(
            table="Who You'Ve Followed",
            filename="connections/followers/who_you've_followed.json",
            tree=Node(
                columns={},
                children={"following_v3": Node(columns={"name": ("name",), "timestamp": ("timestamp",)}, children={})},
            ),
        ),
    ],
    "Your Actions On Violating Content In Your Groups": [
        Entry(
            table="Your Actions On Violating Content In Your Groups",
            filename="your_facebook_activity/groups/your_actions_on_violating_content_in_your_groups.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "timestamp_value": ("timestamp_value",), "title": ("title",)},
                        children={
                            "dict": Node(
                                columns={"label": ("label",), "value": ("value",), "title": ("title",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "label": ("label",),
                                            "value": ("value",),
                                            "href": ("href",),
                                            "title": ("title",),
                                        },
                                        children={
                                            "dict": Node(
                                                columns={"title": ("title",)},
                                                children={
                                                    "dict": Node(
                                                        columns={"label": ("label",), "value": ("value",)}, children={}
                                                    )
                                                },
                                            )
                                        },
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Activity Off Meta Technologies": [
        Entry(
            table="Your Activity Off Meta Technologies",
            filename="apps_and_websites_off_of_facebook/your_activity_off_meta_technologies.json",
            tree=Node(
                columns={"title": ("title",), "fbid": ("fbid",)},
                children={
                    "off_facebook_activity_v2": Node(
                        columns={"name": ("name",)},
                        children={
                            "events": Node(columns={"id": ("id",), "type": ("type",), "timestamp": ("timestamp",)}, children={})
                        },
                    ),
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={
                            "vec": Node(
                                columns={},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    ),
                },
            ),
        ),
    ],
    "Your Comment Active Days": [
        Entry(
            table="Your Comment Active Days",
            filename="personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_active_days.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Your Comment Active Days",
            filename="your_facebook_activity/comments_and_reactions/your_comment_active_days.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Your Comment Edits": [
        Entry(
            table="Your Comment Edits",
            filename="personal_information/profile_information/your_facebook_activity/comments_and_reactions/your_comment_edits.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Your Comment Edits",
            filename="your_facebook_activity/comments_and_reactions/your_comment_edits.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
    ],
    "Your Comments In Groups": [
        Entry(
            table="Your Comments In Groups",
            filename="personal_information/profile_information/your_facebook_activity/groups/your_comments_in_groups.json",
            tree=Node(
                columns={},
                children={
                    "group_comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={
                                    "timestamp": ("comment", "timestamp"),
                                    "comment": ("comment", "comment"),
                                    "group": ("comment", "group"),
                                },
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Comments In Groups",
            filename="your_activity_across_facebook/groups/your_comments_in_groups.json",
            tree=Node(
                columns={},
                children={
                    "group_comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={
                                    "timestamp": ("comment", "timestamp"),
                                    "comment": ("comment", "comment"),
                                    "group": ("comment", "group"),
                                },
                                children={},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Comments In Groups",
            filename="your_facebook_activity/groups/your_comments_in_groups.json",
            tree=Node(
                columns={},
                children={
                    "group_comments_v2": Node(
                        columns={"timestamp": ("timestamp",)},
                        children={
                            "data": Node(
                                columns={
                                    "timestamp": ("comment", "timestamp"),
                                    "comment": ("comment", "comment"),
                                    "group": ("comment", "group"),
                                },
                                children={},
                            ),
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={
                                            "uri": ("media", "uri"),
                                            "creation_timestamp": ("media", "creation_timestamp"),
                                            "url": ("external_context", "url"),
                                        },
                                        children={},
                                    )
                                },
                            ),
                        },
                    )
                },
            ),
        ),
    ],
    "Your Consent Settings": [
        Entry(
            table="Your Consent Settings",
            filename="ads_information/your_consent_settings.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={
                    "label_values": Node(columns={"label": ("label",), "timestamp_value": ("timestamp_value",)}, children={})
                },
            ),
        ),
    ],
    "Your Facebook Watch Activity In The Last 28 Days": [
        Entry(
            table="Your Facebook Watch Activity In The Last 28 Days",
            filename="logged_information/other_logged_information/your_facebook_watch_activity_in_the_last_28_days.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "ent_field_name": ("ent_field_name",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Your Friends": [
        Entry(
            table="Your Friends",
            filename="connections/friends/your_friends.json",
            tree=Node(
                columns={}, children={"friends_v2": Node(columns={"name": ("name",), "timestamp": ("timestamp",)}, children={})}
            ),
        ),
    ],
    "Your Group Membership Activity": [
        Entry(
            table="Your Group Membership Activity",
            filename="personal_information/profile_information/your_facebook_activity/groups/your_group_membership_activity.json",
            tree=Node(
                columns={},
                children={
                    "groups_joined_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Your Group Membership Activity",
            filename="your_activity_across_facebook/groups/your_group_membership_activity.json",
            tree=Node(
                columns={},
                children={
                    "groups_joined_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
        Entry(
            table="Your Group Membership Activity",
            filename="your_facebook_activity/groups/your_group_membership_activity.json",
            tree=Node(
                columns={},
                children={
                    "groups_joined_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"name": ("name",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Your Groups": [
        Entry(
            table="Your Groups",
            filename="your_activity_across_facebook/groups/your_groups.json",
            tree=Node(
                columns={},
                children={"groups_admined_v2": Node(columns={"name": ("name",), "timestamp": ("timestamp",)}, children={})},
            ),
        ),
        Entry(
            table="Your Groups",
            filename="your_facebook_activity/groups/your_groups.json",
            tree=Node(
                columns={},
                children={"groups_admined_v2": Node(columns={"name": ("name",), "timestamp": ("timestamp",)}, children={})},
            ),
        ),
    ],
    "Your Information Download Requests": [
        Entry(
            table="Your Information Download Requests",
            filename="personal_information/profile_information/your_facebook_activity/other_activity/your_information_download_requests.json",
            tree=Node(columns={"timestamp": ("timestamp",)}, children={}),
        ),
        Entry(
            table="Your Information Download Requests",
            filename="your_facebook_activity/other_activity/your_information_download_requests.json",
            tree=Node(columns={"timestamp": ("timestamp",)}, children={}),
        ),
    ],
    "Your Pages": [
        Entry(
            table="Your Pages",
            filename="your_facebook_activity/pages/your_pages.json",
            tree=Node(
                columns={},
                children={
                    "pages_v2": Node(columns={"name": ("name",), "timestamp": ("timestamp",), "url": ("url",)}, children={})
                },
            ),
        ),
    ],
    "Your Pages Mentions": [
        Entry(
            table="Your Pages Mentions",
            filename="ads_information/your_pages_mentions.json",
            tree=Node(
                columns={"timestamp": ("timestamp",), "fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",)}, children={})},
            ),
        ),
    ],
    "Your Pending Posts In Groups": [
        Entry(
            table="Your Pending Posts In Groups",
            filename="your_facebook_activity/groups/your_pending_posts_in_groups.json",
            tree=Node(
                columns={},
                children={
                    "pending_posts_v2": Node(
                        columns={"timestamp": ("timestamp",)}, children={"data": Node(columns={"post": ("post",)}, children={})}
                    )
                },
            ),
        ),
    ],
    "Your Poll Votes": [
        Entry(
            table="Your Poll Votes",
            filename="your_facebook_activity/polls/your_poll_votes.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "title": ("title",)},
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Post Audiences": [
        Entry(
            table="Your Post Audiences",
            filename="connections/friends/your_post_audiences.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "title": ("title",),
                        },
                        children={
                            "dict": Node(
                                columns={"title": ("title",)},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Posts  Check Ins  Photos And Videos 1": [
        Entry(
            table="Your Posts  Check Ins  Photos And Videos 1",
            filename="personal_information/profile_information/your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={
                    "data": Node(columns={"update_timestamp": ("update_timestamp",)}, children={}),
                    "attachments": Node(
                        columns={}, children={"data": Node(columns={"url": ("external_context", "url")}, children={})}
                    ),
                },
            ),
        ),
        Entry(
            table="Your Posts  Check Ins  Photos And Videos 1",
            filename="your_activity_across_facebook/posts/your_posts__check_ins__photos_and_videos_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={
                    "data": Node(columns={"post": ("post",)}, children={}),
                    "attachments": Node(
                        columns={}, children={"data": Node(columns={"url": ("external_context", "url")}, children={})}
                    ),
                },
            ),
        ),
        Entry(
            table="Your Posts  Check Ins  Photos And Videos 1",
            filename="your_facebook_activity/posts/your_posts__check_ins__photos_and_videos_1.json",
            tree=Node(
                columns={"timestamp": ("timestamp",)},
                children={
                    "data": Node(
                        columns={
                            "update_timestamp": ("update_timestamp",),
                            "post": ("post",),
                            "backdated_timestamp": ("backdated_timestamp",),
                        },
                        children={},
                    ),
                    "attachments": Node(
                        columns={},
                        children={
                            "data": Node(
                                columns={
                                    "url": ("external_context", "url"),
                                    "name": ("place", "name"),
                                    "source": ("external_context", "source"),
                                    "uri": ("media", "uri"),
                                    "creation_timestamp": ("media", "creation_timestamp"),
                                    "title": ("media", "title"),
                                    "description": ("media", "description"),
                                },
                                children={
                                    "media": Node(
                                        columns={},
                                        children={
                                            "media_metadata": Node(
                                                columns={},
                                                children={
                                                    "video_metadata": Node(
                                                        columns={},
                                                        children={
                                                            "exif_data": Node(
                                                                columns={"upload_timestamp": ("upload_timestamp",)}, children={}
                                                            )
                                                        },
                                                    )
                                                },
                                            )
                                        },
                                    )
                                },
                            )
                        },
                    ),
                },
            ),
        ),
    ],
    "Your Preferred Categories": [
        Entry(
            table="Your Preferred Categories",
            filename="preferences/preferences/your_preferred_categories.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"ent_field_name": ("ent_field_name",), "label": ("label",)},
                        children={
                            "vec": Node(
                                columns={"ent_field_name": ("ent_field_name",)},
                                children={
                                    "dict": Node(
                                        columns={
                                            "ent_field_name": ("ent_field_name",),
                                            "label": ("label",),
                                            "value": ("value",),
                                        },
                                        children={},
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Recent Reported Conversions": [
        Entry(
            table="Your Recent Reported Conversions",
            filename="ads_information/your_recent_reported_conversions.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "timestamp_value": ("timestamp_value",),
                            "ent_field_name": ("ent_field_name",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
    "Your Recently Followed History": [
        Entry(
            table="Your Recently Followed History",
            filename="personal_information/profile_information/your_facebook_activity/other_activity/your_recently_followed_history.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={
                            "vec": Node(
                                columns={},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Recently Followed History",
            filename="your_activity_across_facebook/other_activity/your_recently_followed_history.json",
            tree=Node(
                columns={},
                children={
                    "label_values": Node(
                        columns={"label": ("label",)},
                        children={
                            "vec": Node(
                                columns={},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Recently Followed History",
            filename="your_facebook_activity/other_activity/your_recently_followed_history.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "ent_field_name": ("ent_field_name",)},
                        children={
                            "vec": Node(
                                columns={},
                                children={"dict": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Reels": [
        Entry(
            table="Your Reels",
            filename="your_facebook_activity/reels/your_reels.json",
            tree=Node(
                columns={},
                children={
                    "lasso_videos_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={"data": Node(columns={"post": ("post",)}, children={})},
                    )
                },
            ),
        ),
    ],
    "Your Saved Items": [
        Entry(
            table="Your Saved Items",
            filename="personal_information/profile_information/your_facebook_activity/saved_items_and_collections/your_saved_items.json",
            tree=Node(
                columns={},
                children={
                    "saves_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "attachments": Node(
                                columns={},
                                children={
                                    "data": Node(
                                        columns={
                                            "name": ("external_context", "name"),
                                            "source": ("external_context", "source"),
                                            "url": ("external_context", "url"),
                                        },
                                        children={},
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Saved Items",
            filename="your_facebook_activity/saved_items_and_collections/your_saved_items.json",
            tree=Node(
                columns={}, children={"saves_v2": Node(columns={"timestamp": ("timestamp",), "title": ("title",)}, children={})}
            ),
        ),
    ],
    "Your Search History": [
        Entry(
            table="Your Search History",
            filename="logged_information/search/your_search_history.json",
            tree=Node(
                columns={},
                children={
                    "searches_v2": Node(
                        columns={"timestamp": ("timestamp",), "title": ("title",)},
                        children={
                            "data": Node(columns={"text": ("text",)}, children={}),
                            "attachments": Node(columns={}, children={"data": Node(columns={"text": ("text",)}, children={})}),
                        },
                    )
                },
            ),
        ),
    ],
    "Your Story Highlights": [
        Entry(
            table="Your Story Highlights",
            filename="personal_information/profile_information/preferences/preferences/your_story_highlights.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Your Story Highlights",
            filename="preferences/preferences/your_story_highlights.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "value": ("value",), "timestamp_value": ("timestamp_value",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Your Video Consumption Summary": [
        Entry(
            table="Your Video Consumption Summary",
            filename="personal_information/profile_information/your_facebook_activity/other_activity/your_video_consumption_summary.json",
            tree=Node(columns={"fbid": ("fbid",)}, children={"label_values": Node(columns={"label": ("label",)}, children={})}),
        ),
        Entry(
            table="Your Video Consumption Summary",
            filename="your_facebook_activity/other_activity/your_video_consumption_summary.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={"label": ("label",), "ent_field_name": ("ent_field_name",), "value": ("value",)}, children={}
                    )
                },
            ),
        ),
    ],
    "Your Videos": [
        Entry(
            table="Your Videos",
            filename="personal_information/profile_information/your_facebook_activity/posts/your_videos.json",
            tree=Node(
                columns={},
                children={
                    "videos_v2": Node(
                        columns={
                            "uri": ("uri",),
                            "creation_timestamp": ("creation_timestamp",),
                            "title": ("title",),
                            "description": ("description",),
                        },
                        children={
                            "media_metadata": Node(
                                columns={},
                                children={
                                    "video_metadata": Node(
                                        columns={},
                                        children={
                                            "exif_data": Node(columns={"upload_timestamp": ("upload_timestamp",)}, children={})
                                        },
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
        Entry(
            table="Your Videos",
            filename="your_facebook_activity/posts/your_videos.json",
            tree=Node(
                columns={},
                children={
                    "videos_v2": Node(
                        columns={
                            "uri": ("uri",),
                            "creation_timestamp": ("creation_timestamp",),
                            "title": ("title",),
                            "description": ("description",),
                        },
                        children={
                            "media_metadata": Node(
                                columns={},
                                children={
                                    "video_metadata": Node(
                                        columns={},
                                        children={
                                            "exif_data": Node(columns={"upload_timestamp": ("upload_timestamp",)}, children={})
                                        },
                                    )
                                },
                            )
                        },
                    )
                },
            ),
        ),
    ],
    "Your Watch Settings": [
        Entry(
            table="Your Watch Settings",
            filename="personal_information/profile_information/preferences/preferences/your_watch_settings.json",
            tree=Node(
                columns={"fbid": ("fbid",)},
                children={"label_values": Node(columns={"label": ("label",), "value": ("value",)}, children={})},
            ),
        ),
        Entry(
            table="Your Watch Settings",
            filename="preferences/preferences/your_watch_settings.json",
            tree=Node(
                columns={"fbid": ("fbid",), "ent_name": ("ent_name",)},
                children={
                    "label_values": Node(
                        columns={
                            "label": ("label",),
                            "value": ("value",),
                            "ent_field_name": ("ent_field_name",),
                            "timestamp_value": ("timestamp_value",),
                        },
                        children={},
                    )
                },
            ),
        ),
    ],
}
