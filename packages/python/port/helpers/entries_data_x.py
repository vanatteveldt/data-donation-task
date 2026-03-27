"""
Donation file structure data for X (Twitter) takeout flows

Split from entries_data.py. To regenerate, run structure/flow_generation/generate_entries.py
which will use the Merged_structures_*.csv to determine the required entries.
"""

from port.helpers.parsers import Entry, Node

X_ENTRIES: dict[str, list[Entry]] = {
    'Account': [
        Entry(table='Account', filename='data/account.js', tree=Node(columns={'accountId': ('account', 'accountId'), 'createdAt': ('account', 'createdAt')}, children={})),
    ],
    'Account-Suspension': [
        Entry(table='Account-Suspension', filename='data/account-suspension.js', tree=Node(columns={}, children={})),
    ],
    'Ad-Engagements': [
        Entry(table='Ad-Engagements', filename='data/ad-engagements.js', tree=Node(columns={}, children={'ad': Node(columns={}, children={'adsUserData': Node(columns={}, children={'adEngagements': Node(columns={}, children={'engagements': Node(columns={'displayLocation': ('impressionAttributes', 'displayLocation'), 'impressionTime': ('impressionAttributes', 'impressionTime'), 'tweetId': ('impressionAttributes', 'promotedTweetInfo', 'tweetId'), 'tweetText': ('impressionAttributes', 'promotedTweetInfo', 'tweetText'), 'urls': ('impressionAttributes', 'promotedTweetInfo', 'urls'), 'mediaUrls': ('impressionAttributes', 'promotedTweetInfo', 'mediaUrls'), 'advertiserName': ('impressionAttributes', 'advertiserInfo', 'advertiserName'), 'screenName': ('impressionAttributes', 'publisherInfo', 'screenName'), 'trendId': ('impressionAttributes', 'promotedTrendInfo', 'trendId'), 'name': ('impressionAttributes', 'promotedTrendInfo', 'name'), 'description': ('impressionAttributes', 'promotedTrendInfo', 'description'), 'publisherName': ('impressionAttributes', 'publisherInfo', 'publisherName')}, children={'engagementAttributes': Node(columns={'engagementTime': ('engagementTime',), 'engagementType': ('engagementType',)}, children={}), 'impressionAttributes': Node(columns={}, children={'matchedTargetingCriteria': Node(columns={'targetingType': ('targetingType',), 'targetingValue': ('targetingValue',)}, children={})})})})})})})),
    ],
    'Ad-Impressions': [
        Entry(table='Ad-Impressions', filename='data/ad-impressions.js', tree=Node(columns={}, children={})),
    ],
    'Ad-Mobile-Conversions-Attributed': [
        Entry(table='Ad-Mobile-Conversions-Attributed', filename='data/ad-mobile-conversions-attributed.js', tree=Node(columns={}, children={})),
    ],
    'Ad-Mobile-Conversions-Unattributed': [
        Entry(table='Ad-Mobile-Conversions-Unattributed', filename='data/ad-mobile-conversions-unattributed.js', tree=Node(columns={}, children={})),
    ],
    'Ad-Online-Conversions-Attributed': [
        Entry(table='Ad-Online-Conversions-Attributed', filename='data/ad-online-conversions-attributed.js', tree=Node(columns={}, children={})),
    ],
    'Ad-Online-Conversions-Unattributed': [
        Entry(table='Ad-Online-Conversions-Unattributed', filename='data/ad-online-conversions-unattributed.js', tree=Node(columns={}, children={})),
    ],
    'Article': [
        Entry(table='Article', filename='data/article.js', tree=Node(columns={}, children={})),
    ],
    'Article-Metadata': [
        Entry(table='Article-Metadata', filename='data/article-metadata.js', tree=Node(columns={}, children={})),
    ],
    'Block': [
        Entry(table='Block', filename='data/block.js', tree=Node(columns={}, children={})),
    ],
    'Community-Note': [
        Entry(table='Community-Note', filename='data/community-note.js', tree=Node(columns={}, children={})),
    ],
    'Community-Note-Batsignal': [
        Entry(table='Community-Note-Batsignal', filename='data/community-note-batsignal.js', tree=Node(columns={}, children={})),
    ],
    'Community-Note-Rating': [
        Entry(table='Community-Note-Rating', filename='data/community-note-rating.js', tree=Node(columns={'noteId': ('communityNoteRating', 'noteId'), 'helpfulnessLevel': ('communityNoteRating', 'helpfulnessLevel'), 'createdAt': ('communityNoteRating', 'createdAt'), 'userId': ('communityNoteRating', 'userId'), 'helpfulTags': ('communityNoteRating', 'helpfulTags')}, children={})),
    ],
    'Community-Note-Tombstone': [
        Entry(table='Community-Note-Tombstone', filename='data/community-note-tombstone.js', tree=Node(columns={}, children={})),
    ],
    'Community-Tweet': [
        Entry(table='Community-Tweet', filename='data/community-tweet.js', tree=Node(columns={}, children={})),
    ],
    'Follower': [
        Entry(table='Follower', filename='data/follower.js', tree=Node(columns={'accountId': ('follower', 'accountId'), 'userLink': ('follower', 'userLink')}, children={})),
    ],
    'Following': [
        Entry(table='Following', filename='data/following.js', tree=Node(columns={'accountId': ('following', 'accountId'), 'userLink': ('following', 'userLink')}, children={})),
    ],
    'Grok-Chat-Item': [
        Entry(table='Grok-Chat-Item', filename='data/grok-chat-item.js', tree=Node(columns={}, children={})),
    ],
    'Like': [
        Entry(table='Like', filename='data/like.js', tree=Node(columns={'tweetId': ('like', 'tweetId'), 'fullText': ('like', 'fullText'), 'expandedUrl': ('like', 'expandedUrl')}, children={})),
    ],
    'Lists-Created': [
        Entry(table='Lists-Created', filename='data/lists-created.js', tree=Node(columns={'url': ('userListInfo', 'url')}, children={})),
    ],
    'Lists-Member': [
        Entry(table='Lists-Member', filename='data/lists-member.js', tree=Node(columns={'url': ('userListInfo', 'url')}, children={})),
    ],
    'Lists-Subscribed': [
        Entry(table='Lists-Subscribed', filename='data/lists-subscribed.js', tree=Node(columns={'url': ('userListInfo', 'url')}, children={})),
    ],
    'Manifest': [
        Entry(table='Manifest', filename='data/manifest.js', tree=Node(columns={'generationDate': ('archiveInfo', 'generationDate')}, children={})),
    ],
    'Moment': [
        Entry(table='Moment', filename='data/moment.js', tree=Node(columns={}, children={})),
    ],
    'Mute': [
        Entry(table='Mute', filename='data/mute.js', tree=Node(columns={}, children={})),
    ],
    'Note-Tweet': [
        Entry(table='Note-Tweet', filename='data/note-tweet.js', tree=Node(columns={}, children={})),
    ],
    'Personalization': [
        Entry(table='Personalization', filename='data/personalization.js', tree=Node(columns={'shows': ('p13nData', 'interests', 'shows'), 'age': ('p13nData', 'inferredAgeInfo', 'age'), 'birthDate': ('p13nData', 'inferredAgeInfo', 'birthDate'), 'gender': ('p13nData', 'demographics', 'genderInfo', 'gender'), 'lookalikeAdvertisers': ('p13nData', 'interests', 'audienceAndAdvertisers', 'lookalikeAdvertisers'), 'advertisers': ('p13nData', 'interests', 'audienceAndAdvertisers', 'advertisers'), 'numAudiences': ('p13nData', 'interests', 'audienceAndAdvertisers', 'numAudiences')}, children={'p13nData': Node(columns={}, children={'demographics': Node(columns={}, children={'languages': Node(columns={'language': ('language',), 'isDisabled': ('isDisabled',)}, children={})}), 'interests': Node(columns={}, children={'interests': Node(columns={'name': ('name',), 'isDisabled': ('isDisabled',)}, children={})})})})),
    ],
    'Professional-Data': [
        Entry(table='Professional-Data', filename='data/professional-data.js', tree=Node(columns={}, children={})),
    ],
    'Protected-History': [
        Entry(table='Protected-History', filename='data/protected-history.js', tree=Node(columns={}, children={})),
    ],
    'Reply-Prompt': [
        Entry(table='Reply-Prompt', filename='data/reply-prompt.js', tree=Node(columns={}, children={})),
    ],
    'Saved-Search': [
        Entry(table='Saved-Search', filename='data/saved-search.js', tree=Node(columns={'savedSearchId': ('savedSearch', 'savedSearchId'), 'query': ('savedSearch', 'query')}, children={})),
    ],
    'Smartblock': [
        Entry(table='Smartblock', filename='data/smartblock.js', tree=Node(columns={}, children={})),
    ],
    'Spaces-Metadata': [
        Entry(table='Spaces-Metadata', filename='data/spaces-metadata.js', tree=Node(columns={}, children={})),
    ],
    'Tweet-Headers': [
        Entry(table='Tweet-Headers', filename='data/tweet-headers.js', tree=Node(columns={'user_id': ('tweet', 'user_id')}, children={})),
    ],
    'Tweetdeck': [
        Entry(table='Tweetdeck', filename='data/tweetdeck.js', tree=Node(columns={}, children={})),
    ],
    'Tweets': [
        Entry(table='Tweets', filename='data/tweets.js', tree=Node(columns={'retweeted': ('tweet', 'retweeted'), 'source': ('tweet', 'source'), 'display_text_range': ('tweet', 'display_text_range'), 'favorite_count': ('tweet', 'favorite_count'), 'id_str': ('tweet', 'id_str'), 'truncated': ('tweet', 'truncated'), 'retweet_count': ('tweet', 'retweet_count'), 'id': ('tweet', 'id'), 'possibly_sensitive': ('tweet', 'possibly_sensitive'), 'created_at': ('tweet', 'created_at'), 'favorited': ('tweet', 'favorited'), 'full_text': ('tweet', 'full_text'), 'lang': ('tweet', 'lang'), 'in_reply_to_status_id_str': ('tweet', 'in_reply_to_status_id_str'), 'in_reply_to_user_id': ('tweet', 'in_reply_to_user_id'), 'in_reply_to_status_id': ('tweet', 'in_reply_to_status_id'), 'in_reply_to_screen_name': ('tweet', 'in_reply_to_screen_name'), 'in_reply_to_user_id_str': ('tweet', 'in_reply_to_user_id_str'), 'editTweetIds': ('tweet', 'edit_info', 'initial', 'editTweetIds'), 'editableUntil': ('tweet', 'edit_info', 'initial', 'editableUntil'), 'editsRemaining': ('tweet', 'edit_info', 'initial', 'editsRemaining'), 'isEditEligible': ('tweet', 'edit_info', 'initial', 'isEditEligible')}, children={'tweet': Node(columns={}, children={'entities': Node(columns={}, children={'urls': Node(columns={'url': ('url',), 'expanded_url': ('expanded_url',), 'display_url': ('display_url',), 'indices': ('indices',)}, children={}), 'user_mentions': Node(columns={'name': ('name',), 'screen_name': ('screen_name',), 'indices': ('indices',), 'id_str': ('id_str',), 'id': ('id',)}, children={}), 'hashtags': Node(columns={'text': ('text',), 'indices': ('indices',)}, children={}), 'media': Node(columns={'media_url_https': ('media_url_https',), 'source_status_id_str': ('source_status_id_str',)}, children={})})})})),
    ],
    'User-Link-Clicks': [
        Entry(table='User-Link-Clicks', filename='data/user-link-clicks.js', tree=Node(columns={}, children={})),
    ],
    'Verified': [
        Entry(table='Verified', filename='data/verified.js', tree=Node(columns={'verified': ('verified', 'verified')}, children={})),
    ],
}
