# -*- coding: utf-8 -*-
"""Hero banner configs for every pro100chok Apify actor.

Every claim here is taken from the actor's own README / input schema; the JSON in
each terminal is trimmed from that README's real output example.
"""

CONFIGS = {}


def add(actor, accent, accent2, eyebrow, headline, lede, pill, code, **kw):
    CONFIGS[actor] = dict(
        actor=actor, accent=accent, accent2=accent2, eyebrow=eyebrow,
        headline=headline, lede=lede, pill=pill, code=code, **kw
    )


# ---------------------------------------------------------- SEO & web intelligence

add(
    "semrush-scraper", "#FF642D", "#2D74FF",
    ["SEMRUSH", "4 MODES"],
    ["EVERY DOMAIN.", "EVERY KEYWORD.", "AS JSON."],
    "Turn Semrush into a plug-in SEO data API: <b>domain overview, keyword research, "
    "site audit and top-websites ranking</b>. <i>Volume, CPC, keyword difficulty, "
    "intents, clusters, related keywords and questions</i> — flat KPI fields plus "
    "the raw nested detail. <u>No Semrush subscription.</u>",
    "4 MODES * KEYWORD + DOMAIN DATA * NO LOGIN",
    [
        "// mode: \"keyword\" · one dataset item per keyword",
        "{",
        ">  \"keyword\": \"best running shoes\", \"database\": \"us\", \"volume\": 60500,",
        ">  \"cpc_usd\": 1.1, \"competition\": 1, \"keyword_difficulty\": 49,",
        "  \"intents\": [\"commercial\"], \"referring_domains_median\": 11,",
        "  \"organic_results_count\": 753000000, \"keyword_ideas_total\": 31402,",
        "  \"volume_trend_12mo\": [44, 44, 44, 36, 44, 44, 44, 36, 44, 44, 44, 100],",
        ">  \"volume_by_country\": [{ \"country\": \"us\", \"volume\": 60500 },",
        ">    { \"country\": \"in\", \"volume\": 40500 }, { \"country\": \"uk\", \"volume\": 12100 }],",
        "  \"related_keywords\": [{ \"keyword\": \"best running shoes for men\",",
        "    \"volume\": 33100, \"keyword_difficulty\": 45 }, ... ],",
        ">  \"questions\": [{ \"keyword\": \"what are the best running shoes\",",
        ">    \"volume\": 2400, \"keyword_difficulty\": 42 }, ... ],",
        "  \"clusters\": [...]   // + domain, seo_audit and top_websites modes",
        "}",
    ],
)

add(
    "similarweb-scraper", "#00C7A9", "#2D74FF",
    ["SIMILARWEB", "3 SOURCES"],
    ["EVERY VISIT.", "EVERY RANK.", "AS JSON."],
    "<b>Traffic estimates, global and country rank, engagement, traffic sources and "
    "top countries</b> for any domain — plus <i>similar-sites discovery and AITDK "
    "domain intelligence</i> with WHOIS and keyword density. "
    "<u>Up to 50 domains per run.</u>",
    "3 SOURCES * 50 DOMAINS / RUN * NO LOGIN",
    [
        "// searchType: \"similarweb\" · one item per domain",
        "{",
        ">  \"SiteName\": \"google.com\", \"Title\": \"Google\",",
        "  \"Category\": \"computers_electronics_and_technology/search_engines\",",
        ">  \"GlobalRank\": { \"Rank\": 1 }, \"CountryRank\": { \"CountryCode\": \"US\", \"Rank\": 1 },",
        "  \"Engagments\": {",
        ">    \"Visits\": 85756574615, \"VisitsFormatted\": \"85.76B\",",
        ">    \"BounceRate\": 28.36, \"PagePerVisit\": 8.52, \"TimeOnSite\": 610 },",
        "  \"EstimatedMonthlyVisits\": { \"2025-12-01\": 84172772881, ... },",
        ">  \"TrafficSources\": { \"Direct\": 85.83, \"Search\": 8.35,",
        ">    \"Referrals\": 4.46, \"Social\": 0.76, \"Paid Referrals\": 0.33 },",
        "  \"TopCountryShares\": [{ \"CountryCode\": \"US\", \"Value\": 24.59 }, ... ]",
        "}   // + similar_sites and aitdk search types",
    ],
)

add(
    "extract-emails", "#10B981", "#2D74FF",
    ["WEBSITE CONTACTS", "BULK CRAWL"],
    ["EVERY EMAIL.", "EVERY PHONE.", "AS JSON."],
    "Bulk <b>email extractor, phone-number scraper and social-profile finder</b> in one: "
    "crawl <i>up to 100 domains per run in parallel</i>, decode obfuscated addresses and "
    "validate real phone numbers. <u>$1 per 1,000 domains — domains that return "
    "nothing are not charged.</u>",
    "100 DOMAINS / RUN * EMAILS + PHONES + SOCIALS",
    [
        "// one dataset item per domain crawled",
        "{",
        ">  \"domain\": \"example.com\", \"url\": \"https://example.com\",",
        ">  \"emails\": [\"info@example.com\", \"sales@example.com\"],",
        "  \"externalEmails\": [\"studio@design-partner.com\"],",
        ">  \"phones\": [\"+41441234567\"],",
        "  \"socialLinks\": {",
        "    \"facebook\": \"https://facebook.com/example\",",
        "    \"twitter\": \"https://x.com/example\",",
        ">    \"linkedin\": \"https://linkedin.com/company/example\",",
        "    \"instagram\": null, \"youtube\": null, \"tiktok\": null, \"github\": null },",
        ">  \"pagesScanned\": 12, \"scrapedAt\": \"2026-07-05T12:00:00.000Z\"",
        "}",
    ],
)

# --------------------------------------------------------------- Social media & ads

add(
    "instagram-scraper-all-in-one", "#E1306C", "#F77737",
    ["INSTAGRAM", "15 MODES"],
    ["EVERY POST.", "EVERY FOLLOWER.", "AS JSON."],
    "<b>Profiles, posts, reels, comments, likes, followers, following, tagged, stories, "
    "highlights, hashtags, locations and search</b> — 15 modes in one Actor. "
    "<i>Emails and phones pulled out of bios</i> for lead-gen. "
    "<u>Most modes need no login at all.</u>",
    "15 MODES * BIO CONTACTS * NO API KEY",
    [
        "// scrapeType: \"profile\" · one item per profile",
        "{",
        ">  \"username\": \"nasa\", \"fullName\": \"NASA\", \"id\": \"528817151\",",
        "  \"biography\": \"Exploring the universe and our home planet.\",",
        ">  \"followersCount\": 104409417, \"followsCount\": 78, \"postsCount\": 4828,",
        "  \"externalUrl\": \"https://www.nasa.gov\", \"bioLinks\": [\"https://www.nasa.gov\"],",
        ">  \"isVerified\": true, \"isPrivate\": false, \"isBusinessAccount\": true,",
        "  \"category\": \"Government organization\",",
        "  \"profilePicUrl\": \"https://instagram.f...jpg\"",
        "}",
        "// + posts, reels, comments, likes, followers, following, tagged,",
        "//   stories, highlights, hashtag, location, search, contacts",
    ],
)

add(
    "tiktok-profile-pro", "#FE2C55", "#25F4EE",
    ["TIKTOK", "PROFILE API"],
    ["EVERY PROFILE.", "EVERY VIDEO.", "AS JSON."],
    "TikTok has no open official API. This Actor is an <b>unofficial TikTok profile "
    "API</b>: follower, heart and video counts, the profile's <i>videos, reposts and "
    "liked videos</i> with full play/like/comment/share stats, plus "
    "<u>emails and links pulled from the bio</u> and engagement analytics.",
    "BIO CONTACTS * VIDEOS * ANALYTICS",
    [
        "// one dataset item per profile",
        "{",
        ">  \"username\": \"psiho.kisa\", \"nickname\": \"Кисы\", \"verified\": false,",
        ">  \"followerCount\": 326901, \"heartCount\": 16800000, \"videoCount\": 121,",
        "  \"signature\": \"ДРУГ КИСА · 4-5\", \"region\": \"RU\", \"bioLink\": null,",
        "  \"avatar\": { \"thumb\": \"https://...\", \"large\": \"https://...\" },",
        "  \"videos\": [{",
        ">    \"id\": \"7625229188693232918\", \"duration\": 76, \"createTime\": 1775387026,",
        ">    \"playCount\": 2000000, \"diggCount\": 156500, \"commentCount\": 612,",
        ">    \"shareCount\": 10700, \"collectCount\": 13818",
        "  }, ... ],",
        "  \"contacts\": { ... },   // extractContacts: true",
        "  \"analytics\": { ... }   // computeAnalytics: true",
        "}",
    ],
)

add(
    "youtube-scraper-all-in-one", "#FF0033", "#FF8A00",
    ["YOUTUBE", "7 MODES"],
    ["EVERY VIDEO.", "EVERY TRANSCRIPT.", "AS JSON."],
    "<b>Videos, channels, search, Shorts, comments, transcripts and playlists</b> — "
    "seven modes, <i>no API key and no quota</i>. 30+ fields per video, captions in "
    "every available language, channel emails and socials. "
    "<u>From $2 per 1,000 videos on paid plans.</u>",
    "7 MODES * TRANSCRIPTS * NO API KEY",
    [
        "// searchType: \"video\" · 30+ fields per video",
        "{",
        ">  \"id\": \"dQw4w9WgXcQ\", \"title\": \"Rick Astley - Never Gonna Give You Up\",",
        ">  \"viewCount\": 1780016266, \"likes\": 19140845, \"commentsCount\": 2400000,",
        "  \"durationSeconds\": 213, \"publishDate\": \"2009-10-25\",",
        ">  \"channelName\": \"Rick Astley\", \"numberOfSubscribers\": 4500000,",
        "  \"channelId\": \"UCuAXFkgsw1L7xaCfnd5JJOw\",",
        "  \"hashtags\": [\"#RickAstley\", \"#NeverGonnaGiveYouUp\"],",
        ">  \"availableCaptions\": [\"en\", \"de-DE\", \"ja\", \"pt-BR\", \"es-419\"],",
        "  \"thumbnailUrl\": \"https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg\"",
        "}",
        "// + channel, search, shorts, comments, transcript, playlist",
    ],
)

add(
    "reddit-scraper-all-in-one", "#FF4500", "#FFB000",
    ["REDDIT", "5 MODES"],
    ["EVERY POST.", "EVERY COMMENT.", "AS JSON."],
    "Reddit's official API wants app registration, OAuth and — above small volumes "
    "— money. This Actor is an <b>unofficial Reddit API alternative</b>: search, "
    "subreddits, single posts, users and any Reddit URL. <i>Comment trees, scores, "
    "flairs and awards</i>, plus <u>emails found in posts and profiles.</u>",
    "5 MODES * COMMENT TREES * NO OAUTH",
    [
        "// scrapeType: \"search\" · one item per post",
        "{",
        ">  \"type\": \"post\", \"id\": \"1kx9q2z\", \"community\": \"r/Entrepreneur\",",
        ">  \"title\": \"How I got my first 100 customers\", \"author\": \"startup_founder\",",
        "  \"body\": \"Long story short: I stopped building and started talking...\",",
        ">  \"score\": 1543, \"upvoteRatio\": 0.97, \"numberOfComments\": 218,",
        "  \"createdAt\": \"2026-05-20T14:08:11+00:00\", \"flair\": \"Case Study\",",
        "  \"isNsfw\": false, \"isSelf\": true, \"totalAwards\": 3,",
        "  \"url\": \"https://www.reddit.com/r/Entrepreneur/comments/1kx9q2z/...\"",
        "}",
        "// + subreddit, post (with comment tree), user, url modes",
    ],
)

add(
    "threads-scraper-usage", "#8B5CF6", "#E1306C",
    ["THREADS.NET", "POSTS + PROFILES"],
    ["EVERY POST.", "EVERY PROFILE.", "AS JSON."],
    "<b>Posts, user profiles, follower and following lists and search results</b> from "
    "Threads.net at scale. <i>Likes, replies, reposts, quotes and shares</i> on every "
    "post, linked Instagram account on every profile, and "
    "<u>emails and URLs extracted straight out of post text.</u>",
    "POSTS * PROFILES * FOLLOWERS * SEARCH",
    [
        "// action: \"user_posts\" · one item per post",
        "{",
        ">  \"post_id\": \"3578921456789012345\", \"code\": \"DVp9LrHAjHq\",",
        "  \"text\": \"Just launched our new Python library for data processing...\",",
        ">  \"username\": \"techdev\", \"full_name\": \"Tech Developer\", \"is_verified\": true,",
        ">  \"like_count\": 245, \"reply_count\": 32, \"repost_count\": 18,",
        "  \"quote_count\": 5, \"reshare_count\": 12, \"is_reply\": false,",
        "  \"taken_at\": 1710000000, \"media_type\": 19, \"images\": [],",
        ">  \"emails_in_text\": [\"hello@techdev.com\"],",
        "  \"urls_in_text\": [\"https://github.com/techdev/library\"]",
        "}",
    ],
)

add(
    "pinterest-scraper-all-in-one", "#E60023", "#FF8A00",
    ["PINTEREST", "7 MODES"],
    ["EVERY PIN.", "EVERY BOARD.", "AS JSON."],
    "<b>Search, pin details, profiles, user pins, boards, board sections and related "
    "pins</b> — seven modes, <i>no login and no Pinterest API key</i>. Image, GIF "
    "and video pins detected automatically with every resolution URL. "
    "<u>From $1 per 1,000 pins on paid plans.</u>",
    "7 MODES * NO LOGIN * ALL PIN MEDIA",
    [
        "// scrapeType: \"search\" · one item per pin",
        "{",
        ">  \"dataType\": \"pin\", \"id\": \"1234567890\", \"title\": \"Minimal home office\",",
        "  \"description\": \"A clean desk setup with warm wood tones...\",",
        ">  \"images\": { \"170x\": \"...\", \"236x\": \"...\", \"474x\": \"...\", \"736x\": \"...\", \"orig\": \"...\" },",
        "  \"media_type\": \"image\", \"is_video\": false, \"dominant_color\": \"#d9c7b8\",",
        ">  \"repin_count\": 4210, \"comment_count\": 18, \"reaction_count\": 312,",
        "  \"link\": \"https://example.com/article\", \"domain\": \"example.com\",",
        ">  \"pinner_username\": \"studio.nord\", \"pinner_followers\": 58200,",
        "  \"board_name\": \"Workspaces\", \"board_url\": \"https://www.pinterest.com/...\"",
        "}",
    ],
)

add(
    "meta-ads-library-scraper", "#0866FF", "#E1306C",
    ["META AD LIBRARY", "AD SPY"],
    ["EVERY AD.", "EVERY CREATIVE.", "AS JSON."],
    "Scrape the Meta Ad Library by <b>keyword, Facebook page or ad archive ID</b> — "
    "up to <i>39 flat fields per ad</i>: creatives, ad copy, video URLs, CTA type, "
    "platforms, run dates and page data. "
    "<u>Facebook, Instagram, Messenger, Audience Network and Threads.</u>",
    "39 FIELDS / AD * VIDEO + IMAGE URLS",
    [
        "// scrapeType: \"search\" · one flat item per ad",
        "{",
        ">  \"adArchiveId\": \"1677230640306960\", \"pageName\": \"Amazon Fashion\",",
        ">  \"pageId\": \"151871258163795\", \"pageLikeCount\": 4214242,",
        "  \"pageCategories\": [\"Clothing (Brand)\"], \"pageIsDeleted\": false,",
        ">  \"adContent\": \"Fits that go the distance and level up your A-game.\",",
        "  \"adTitle\": \"Amazon Fashion\", \"adLinkCaption\": \"amazon.com\",",
        ">  \"adCallToActionType\": \"SHOP_NOW\", \"adFormat\": \"dpa\",",
        "  \"adLinkUrl\": \"https://www.amazon.com/b?node=210992350011&...\",",
        "  \"imageUrls\": [\"https://scontent-phx1-1.xx.fbcdn.net/...\"],",
        "  \"adLibraryUrl\": \"https://www.facebook.com/ads/library/?id=1677230640306960\"",
        "}",
    ],
)
