"""
Donation file structure data for Instagram takeout flows

Split from entries_data.py. To regenerate, run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

IG_ENTRIES: dict[str, list[Entry]] = {
    'Ads About Meta': [
        Entry(table='Ads About Meta', filename='ads_information/instagram_ads_and_businesses/ads_about_meta.json', tree=Node(columns={'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'value': ('value',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Ads Clicked': [
        Entry(table='Ads Clicked', filename='ads_information/ads_and_topics/ads_clicked.json', tree=Node(columns={}, children={'impressions_history_ads_clicked': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Ads Viewed': [
        Entry(table='Ads Viewed', filename='ads_information/ads_and_topics/ads_viewed.json', tree=Node(columns={}, children={'impressions_history_ads_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Advertisers Using Your Activity Or Information': [
        Entry(table='Advertisers Using Your Activity Or Information', filename='ads_information/instagram_ads_and_businesses/advertisers_using_your_activity_or_information.json', tree=Node(columns={}, children={'ig_custom_audiences_all_types': Node(columns={'advertiser_name': ('advertiser_name',), 'has_data_file_custom_audience': ('has_data_file_custom_audience',), 'has_remarketing_custom_audience': ('has_remarketing_custom_audience',), 'has_in_person_store_visit': ('has_in_person_store_visit',)}, children={})})),
    ],
    'Archived Posts': [
        Entry(table='Archived Posts', filename='your_instagram_activity/media/archived_posts.json', tree=Node(columns={}, children={'ig_archived_post_media': Node(columns={}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={'media_metadata': Node(columns={}, children={'photo_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})})})})})})),
    ],
    'Avatar Story Reactions': [
        Entry(table='Avatar Story Reactions', filename='your_instagram_activity/story_interactions/avatar_story_reactions.json', tree=Node(columns={}, children={'story_activities_avatar_quick_reactions': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Blocked Profiles': [
        Entry(table='Blocked Profiles', filename='connections/followers_and_following/blocked_profiles.json', tree=Node(columns={}, children={'relationships_blocked_users': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Close Friends': [
        Entry(table='Close Friends', filename='connections/followers_and_following/close_friends.json', tree=Node(columns={}, children={'relationships_close_friends': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Comments Allowed From': [
        Entry(table='Comments Allowed From', filename='preferences/media_settings/comments_allowed_from.json', tree=Node(columns={}, children={'settings_allow_comments_from': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}, children={})})),
        Entry(table='Comments Allowed From', filename='preferences/settings/comments_allowed_from.json', tree=Node(columns={}, children={'settings_allow_comments_from': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Comments Allowed From', 'href'), 'value': ('string_map_data', 'Comments Allowed From', 'value'), 'timestamp': ('string_map_data', 'Comments Allowed From', 'timestamp')}, children={})})),
    ],
    'Consents': [
        Entry(table='Consents', filename='preferences/media_settings/consents.json', tree=Node(columns={'timestamp': ('timestamp',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
        Entry(table='Consents', filename='preferences/settings/consents.json', tree=Node(columns={'timestamp': ('timestamp',), 'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Content Interactions': [
        Entry(table='Content Interactions', filename='logged_information/past_instagram_insights/content_interactions.json', tree=Node(columns={}, children={'organic_insights_interactions': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Reels Saves', 'href'), 'value': ('string_map_data', 'Reels Saves', 'value'), 'timestamp': ('string_map_data', 'Reels Saves', 'timestamp')}, children={})})),
    ],
    'Countdowns': [
        Entry(table='Countdowns', filename='your_instagram_activity/story_interactions/countdowns.json', tree=Node(columns={}, children={'story_activities_countdowns': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Custom Lists': [
        Entry(table='Custom Lists', filename='connections/followers_and_following/custom_lists.json', tree=Node(columns={}, children={'relationships_custom_lists': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Group Members', 'href'), 'value': ('string_map_data', 'Group Members', 'value'), 'timestamp': ('string_map_data', 'Group Members', 'timestamp')}, children={})})),
    ],
    'Emoji Sliders': [
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_interactions/emoji_sliders.json', tree=Node(columns={}, children={'story_activities_emoji_sliders': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Emoji Sliders', filename='your_instagram_activity/story_sticker_interactions/emoji_sliders.json', tree=Node(columns={}, children={'story_activities_emoji_sliders': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Emoji Story Reactions': [
        Entry(table='Emoji Story Reactions', filename='your_instagram_activity/story_interactions/emoji_story_reactions.json', tree=Node(columns={}, children={'story_activities_emoji_quick_reactions': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Filtered Keywords For Comments And Messages': [
        Entry(table='Filtered Keywords For Comments And Messages', filename='preferences/settings/filtered_keywords_for_comments_and_messages.json', tree=Node(columns={}, children={'settings_filtered_keywords': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Filtered Keywords For Posts': [
        Entry(table='Filtered Keywords For Posts', filename='preferences/settings/filtered_keywords_for_posts.json', tree=Node(columns={}, children={'settings_filtered_keywords_for_posts': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    "Follow Requests You'Ve Received": [
        Entry(table="Follow Requests You'Ve Received", filename="connections/followers_and_following/follow_requests_you've_received.json", tree=Node(columns={}, children={'relationships_follow_requests_received': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Followers 1': [
        Entry(table='Followers 1', filename='connections/followers_and_following/followers_1.json', tree=Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})),
    ],
    'Following': [
        Entry(table='Following', filename='connections/followers_and_following/following.json', tree=Node(columns={}, children={'relationships_following': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Following Hashtags': [
        Entry(table='Following Hashtags', filename='connections/followers_and_following/following_hashtags.json', tree=Node(columns={}, children={'relationships_following_hashtags': Node(columns={'title': ('title',), 'media_list_data': ('media_list_data',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Hide Story From': [
        Entry(table='Hide Story From', filename='connections/followers_and_following/hide_story_from.json', tree=Node(columns={}, children={'relationships_hide_stories_from': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Hype': [
        Entry(table='Hype', filename='your_instagram_activity/comments/hype.json', tree=Node(columns={}, children={'comments_story_comments': Node(columns={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={'media_list_data': Node(columns={'uri': ('uri',)}, children={})})})),
    ],
    'Igtv Videos': [
        Entry(table='Igtv Videos', filename='your_instagram_activity/media/igtv_videos.json', tree=Node(columns={}, children={'ig_igtv_media': Node(columns={}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})})})})})})),
    ],
    'Instagram Friend Map': [
        Entry(table='Instagram Friend Map', filename='personal_information/personal_information/instagram_friend_map.json', tree=Node(columns={}, children={'profile_friend_map': Node(columns={'href': ('string_map_data', 'Custom list', 'href'), 'value': ('string_map_data', 'Custom list', 'value'), 'timestamp': ('string_map_data', 'Custom list', 'timestamp')}, children={})})),
    ],
    'Instagram Signup Details': [
        Entry(table='Instagram Signup Details', filename='security_and_login_information/login_and_profile_creation/instagram_signup_details.json', tree=Node(columns={}, children={'account_history_registration_info': Node(columns={'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Liked Comments': [
        Entry(table='Liked Comments', filename='your_instagram_activity/likes/liked_comments.json', tree=Node(columns={}, children={'likes_comment_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Liked Posts': [
        Entry(table='Liked Posts', filename='your_instagram_activity/likes/liked_posts.json', tree=Node(columns={}, children={'likes_media_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Link History': [
        Entry(table='Link History', filename='logged_information/link_history/link_history.json', tree=Node(columns={'timestamp': ('timestamp',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Live Videos': [
        Entry(table='Live Videos', filename='logged_information/past_instagram_insights/live_videos.json', tree=Node(columns={}, children={'organic_insights_live': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Shares', 'href'), 'value': ('string_map_data', 'Shares', 'value'), 'timestamp': ('string_map_data', 'Shares', 'timestamp')}, children={})})),
    ],
    'Other Categories Used To Reach You': [
        Entry(table='Other Categories Used To Reach You', filename='ads_information/instagram_ads_and_businesses/other_categories_used_to_reach_you.json', tree=Node(columns={'fbid': ('fbid',), 'ent_name': ('ent_name',)}, children={'label_values': Node(columns={'ent_field_name': ('ent_field_name',), 'label': ('label',)}, children={'vec': Node(columns={'value': ('value',)}, children={})})})),
    ],
    'Other Content': [
        Entry(table='Other Content', filename='your_instagram_activity/media/other_content.json', tree=Node(columns={}, children={'ig_other_media': Node(columns={}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={})})})),
    ],
    'Personal Information': [
        Entry(table='Personal Information', filename='personal_information/personal_information/personal_information.json', tree=Node(columns={}, children={'profile_user': Node(columns={'href': ('string_map_data', 'Private Account', 'href'), 'value': ('string_map_data', 'Private Account', 'value'), 'timestamp': ('string_map_data', 'Private Account', 'timestamp')}, children={})})),
    ],
    'Polls': [
        Entry(table='Polls', filename='your_instagram_activity/story_interactions/polls.json', tree=Node(columns={}, children={'story_activities_polls': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Polls', filename='your_instagram_activity/story_sticker_interactions/polls.json', tree=Node(columns={}, children={'story_activities_polls': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Post Comments 1': [
        Entry(table='Post Comments 1', filename='your_instagram_activity/comments/post_comments_1.json', tree=Node(columns={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={'media_list_data': Node(columns={'uri': ('uri',)}, children={})})),
    ],
    'Posts 1': [
        Entry(table='Posts 1', filename='your_instagram_activity/content/posts_1.json', tree=Node(columns={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={})})),
        Entry(table='Posts 1', filename='your_instagram_activity/media/posts_1.json', tree=Node(columns={'title': ('title',), 'creation_timestamp': ('creation_timestamp',)}, children={'media': Node(columns={'uri': ('uri',), 'creation_timestamp': ('media_metadata', 'video_metadata', 'subtitles', 'creation_timestamp'), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app')}, children={})})),
    ],
    'Posts Viewed': [
        Entry(table='Posts Viewed', filename='ads_information/ads_and_topics/posts_viewed.json', tree=Node(columns={}, children={'impressions_history_posts_seen': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    "Posts You'Re Not Interested In": [
        Entry(table="Posts You'Re Not Interested In", filename="ads_information/ads_and_topics/posts_you're_not_interested_in.json", tree=Node(columns={}, children={'impressions_history_posts_not_interested': Node(columns={}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Professional Information': [
        Entry(table='Professional Information', filename='personal_information/personal_information/professional_information.json', tree=Node(columns={}, children={'profile_business': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Business Connection Methods', 'href'), 'value': ('string_map_data', 'Business Connection Methods', 'value'), 'timestamp': ('string_map_data', 'Business Connection Methods', 'timestamp')}, children={})})),
    ],
    'Profile Privacy Changes': [
        Entry(table='Profile Privacy Changes', filename='security_and_login_information/login_and_profile_creation/profile_privacy_changes.json', tree=Node(columns={}, children={'account_history_account_privacy_history': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Profile Searches': [
        Entry(table='Profile Searches', filename='logged_information/recent_searches/profile_searches.json', tree=Node(columns={}, children={'searches_user': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={'string_list_data': Node(columns={'href': ('href',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    "Profiles You'Re Not Interested In": [
        Entry(table="Profiles You'Re Not Interested In", filename="ads_information/ads_and_topics/profiles_you're_not_interested_in.json", tree=Node(columns={}, children={'impressions_history_recs_hidden_authors': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    "Profiles You'Ve Favorited": [
        Entry(table="Profiles You'Ve Favorited", filename="connections/followers_and_following/profiles_you've_favorited.json", tree=Node(columns={}, children={'relationships_feed_favorites': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Question Media Response': [
        Entry(table='Question Media Response', filename='your_instagram_activity/story_interactions/question_media_response.json', tree=Node(columns={}, children={'story_activities_questions_media': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Questions': [
        Entry(table='Questions', filename='your_instagram_activity/story_interactions/questions.json', tree=Node(columns={}, children={'story_activities_questions': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Quizzes': [
        Entry(table='Quizzes', filename='your_instagram_activity/story_interactions/quizzes.json', tree=Node(columns={}, children={'story_activities_quizzes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Quizzes', filename='your_instagram_activity/story_sticker_interactions/quizzes.json', tree=Node(columns={}, children={'story_activities_quizzes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Recommended Topics': [
        Entry(table='Recommended Topics', filename='preferences/your_topics/recommended_topics.json', tree=Node(columns={}, children={'topics_your_topics': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}, children={})})),
    ],
    'Reels': [
        Entry(table='Reels', filename='your_instagram_activity/media/reels.json', tree=Node(columns={}, children={'ig_reels_media': Node(columns={}, children={'media': Node(columns={'uri': ('media_metadata', 'video_metadata', 'subtitles', 'uri'), 'creation_timestamp': ('media_metadata', 'video_metadata', 'subtitles', 'creation_timestamp'), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'source_type': ('source_type',)}, children={})})})})})})),
        Entry(table='Reels', filename='your_instagram_activity/subscriptions/reels.json', tree=Node(columns={}, children={'subscriptions_reels': Node(columns={'title': ('title',), 'href': ('string_map_data', 'External URL', 'href'), 'value': ('string_map_data', 'External URL', 'value'), 'timestamp': ('string_map_data', 'External URL', 'timestamp')}, children={})})),
    ],
    'Reels Comments': [
        Entry(table='Reels Comments', filename='your_instagram_activity/comments/reels_comments.json', tree=Node(columns={}, children={'comments_reels_comments': Node(columns={'value': ('string_map_data', 'Media Owner', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Removed Suggestions': [
        Entry(table='Removed Suggestions', filename='connections/followers_and_following/removed_suggestions.json', tree=Node(columns={}, children={'relationships_dismissed_suggested_users': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Replies 1': [
        Entry(table='Replies 1', filename='your_instagram_activity/$USERNAME/replies_1.json', tree=Node(columns={'title': ('title',), 'is_still_participant': ('is_still_participant',), 'thread_path': ('thread_path',), 'mode': ('joinable_mode', 'mode'), 'link': ('joinable_mode', 'link')}, children={'participants': Node(columns={'name': ('name',)}, children={}), 'replies': Node(columns={'reply_content': ('reply_content',), 'original_message_sender': ('original_message_sender',), 'timestamp_ms': ('timestamp_ms',)}, children={})})),
    ],
    'Reported Conversations': [
        Entry(table='Reported Conversations', filename='your_instagram_activity/messages/reported_conversations.json', tree=Node(columns={}, children={'ig_reported_conversations': Node(columns={'timestamp': ('timestamp',), 'is_reporter': ('is_reporter',), 'name': ('reportee', 'name')}, children={'messages': Node(columns={'sender_name': ('sender_name',), 'timestamp_ms': ('timestamp_ms',), 'content': ('content',)}, children={})})})),
    ],
    'Reposts': [
        Entry(table='Reposts', filename='personal_information/personal_information/reposts.json', tree=Node(columns={}, children={'profile_media_reposts': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Text', 'href'), 'value': ('string_map_data', 'Text', 'value'), 'timestamp': ('string_map_data', 'Text', 'timestamp')}, children={})})),
    ],
    'Restricted Profiles': [
        Entry(table='Restricted Profiles', filename='connections/followers_and_following/restricted_profiles.json', tree=Node(columns={}, children={'relationships_restricted_users': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Saved Collections': [
        Entry(table='Saved Collections', filename='your_instagram_activity/saved/saved_collections.json', tree=Node(columns={}, children={'saved_saved_collections': Node(columns={'title': ('title',), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Added Time', 'timestamp'), 'href': ('string_map_data', 'Name', 'href')}, children={})})),
    ],
    'Saved Posts': [
        Entry(table='Saved Posts', filename='your_instagram_activity/saved/saved_posts.json', tree=Node(columns={}, children={'saved_saved_media': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Saved on', 'href'), 'timestamp': ('string_map_data', 'Saved on', 'timestamp')}, children={})})),
    ],
    'Signup Details': [
        Entry(table='Signup Details', filename='security_and_login_information/login_and_profile_creation/signup_details.json', tree=Node(columns={}, children={'account_history_registration_info': Node(columns={'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Stories': [
        Entry(table='Stories', filename='your_instagram_activity/content/stories.json', tree=Node(columns={}, children={'ig_stories': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'backup_uri': ('backup_uri',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'video_metadata', 'music_genre')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})}), 'photo_metadata': Node(columns={}, children={'exif_data': Node(columns={'source_type': ('source_type',), 'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',)}, children={})})})})})),
        Entry(table='Stories', filename='your_instagram_activity/media/stories.json', tree=Node(columns={}, children={'ig_stories': Node(columns={'uri': ('uri',), 'creation_timestamp': ('creation_timestamp',), 'title': ('title',), 'source_app': ('cross_post_source', 'source_app'), 'music_genre': ('media_metadata', 'photo_metadata', 'music_genre')}, children={'media_metadata': Node(columns={}, children={'video_metadata': Node(columns={}, children={'exif_data': Node(columns={'date_time_digitized': ('date_time_digitized',), 'date_time_original': ('date_time_original',), 'source_type': ('source_type',)}, children={})}), 'photo_metadata': Node(columns={}, children={'exif_data': Node(columns={'source_type': ('source_type',), 'date_time_original': ('date_time_original',), 'date_time_digitized': ('date_time_digitized',)}, children={})})})})})),
    ],
    'Story Likes': [
        Entry(table='Story Likes', filename='your_instagram_activity/story_interactions/story_likes.json', tree=Node(columns={}, children={'story_activities_story_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
        Entry(table='Story Likes', filename='your_instagram_activity/story_sticker_interactions/story_likes.json', tree=Node(columns={}, children={'story_activities_story_likes': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Story Reaction Sticker Reactions': [
        Entry(table='Story Reaction Sticker Reactions', filename='your_instagram_activity/story_interactions/story_reaction_sticker_reactions.json', tree=Node(columns={}, children={'story_activities_reaction_sticker_reactions': Node(columns={'title': ('title',)}, children={'string_list_data': Node(columns={'href': ('href',), 'value': ('value',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Subscription For No Ads': [
        Entry(table='Subscription For No Ads', filename='ads_information/instagram_ads_and_businesses/subscription_for_no_ads.json', tree=Node(columns={'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'value': ('value',)}, children={})})),
    ],
    'Suggested Profiles Viewed': [
        Entry(table='Suggested Profiles Viewed', filename='ads_information/ads_and_topics/suggested_profiles_viewed.json', tree=Node(columns={}, children={'impressions_history_chaining_seen': Node(columns={'value': ('string_map_data', 'Username', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Time Spent On Instagram': [
        Entry(table='Time Spent On Instagram', filename='your_instagram_activity/other_activity/time_spent_on_instagram.json', tree=Node(columns={'timestamp': ('timestamp',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',)}, children={'vec': Node(columns={}, children={'dict': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})})})),
    ],
    'Videos Watched': [
        Entry(table='Videos Watched', filename='ads_information/ads_and_topics/videos_watched.json', tree=Node(columns={}, children={'impressions_history_videos_watched': Node(columns={'value': ('string_map_data', 'Author', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Word Or Phrase Searches': [
        Entry(table='Word Or Phrase Searches', filename='logged_information/recent_searches/word_or_phrase_searches.json', tree=Node(columns={}, children={'searches_keyword': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Time', 'href'), 'value': ('string_map_data', 'Time', 'value'), 'timestamp': ('string_map_data', 'Time', 'timestamp')}, children={})})),
    ],
    'Your Activity Off Meta Technologies': [
        Entry(table='Your Activity Off Meta Technologies', filename='apps_and_websites_off_of_instagram/apps_and_websites/your_activity_off_meta_technologies.json', tree=Node(columns={}, children={'apps_and_websites_off_meta_activity': Node(columns={'name': ('name',)}, children={'events': Node(columns={'id': ('id',), 'type': ('type',), 'timestamp': ('timestamp',)}, children={})})})),
    ],
    'Your Information Download Requests': [
        Entry(table='Your Information Download Requests', filename='your_instagram_activity/other_activity/your_information_download_requests.json', tree=Node(columns={'timestamp': ('timestamp',)}, children={'label_values': Node(columns={'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Your Link History Settings': [
        Entry(table='Your Link History Settings', filename='logged_information/link_history/your_link_history_settings.json', tree=Node(columns={'timestamp': ('timestamp',), 'fbid': ('fbid',)}, children={'label_values': Node(columns={'label': ('label',), 'timestamp_value': ('timestamp_value',)}, children={})})),
    ],
    'Your Muted Story Teaser Creators': [
        Entry(table='Your Muted Story Teaser Creators', filename='your_instagram_activity/subscriptions/your_muted_story_teaser_creators.json', tree=Node(columns={}, children={'subscriptions_muted_story_teaser_creators': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Muted Creators', 'href'), 'value': ('string_map_data', 'Muted Creators', 'value'), 'timestamp': ('string_map_data', 'Muted Creators', 'timestamp')}, children={})})),
    ],
    'Your Topics': [
        Entry(table='Your Topics', filename='preferences/your_topics/your_topics.json', tree=Node(columns={}, children={'topics_your_topics': Node(columns={'title': ('title',), 'href': ('string_map_data', 'Name', 'href'), 'value': ('string_map_data', 'Name', 'value'), 'timestamp': ('string_map_data', 'Name', 'timestamp')}, children={})})),
    ],
}
