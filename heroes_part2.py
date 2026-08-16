# -*- coding: utf-8 -*-
"""Part 2: reviews / business data + e-commerce."""
from heroes_all import add

add(
    "trustpilot-all-in-one-scraper", "#00B67A", "#2D74FF",
    ["TRUSTPILOT", "6 MODES"],
    ["EVERY REVIEW.", "EVERY COMPANY.", "AS JSON."],
    "<b>Reviews (up to 40 fields), company profiles (50+ fields), transparency "
    "analytics, search, categories and reviewer profiles</b> — six modes in one Actor. "
    "<i>More than 200 reviews per company</i>, nested straight inside the company "
    "record. <u>No login, no Trustpilot API key, no proxies to configure.</u>",
    "6 MODES * 40 FIELDS / REVIEW * NO LOGIN",
    [
        '// dataType: "company" · reviews nested in the company record',
        "{",
        '>  "companyName": "Nike", "companyDomain": "www.nike.com",',
        '>  "trustScore": 1.6, "stars": 1.5, "numberOfReviews": 12692,',
        '  "primaryCategory": "Activewear Store", "reviewsCount": 200,',
        '  "transparency": { "ratingOneStar": 9598, "ratingFiveStars": 1797,',
        '    "replyPercentage": 0 },',
        '  "reviews": [{',
        '>    "reviewTitle": "Disgusting customer service", "rating": 1,',
        '>    "reviewText": "On May 25 I bought my customized jersey ...",',
        '    "language": "en", "isVerified": false, "reviewSource": "Organic",',
        '>    "publishedDate": "2026-06-12T18:55:37.000Z", "likes": 0,',
        '    "reviewerName": "...", "reviewerId": "6a2c3953e33cd10be89f2ef1"',
        '  }, ... 199 more]',
        "}",
    ],
)

add(
    "g2-scraper", "#FF492C", "#2D74FF",
    ["G2.COM", "5 MODES"],
    ["EVERY REVIEW.", "EVERY COMPETITOR.", "AS JSON."],
    "G2's official API is enterprise-only — a sales call before you see a single row. "
    "This Actor is an <b>unofficial G2 API</b>: reviews, product profiles, category "
    "listings, alternatives and the category directory. <i>Reviewer job title, "
    "industry, company segment and size on every review.</i> "
    "<u>More than 100 reviews per product.</u>",
    "5 MODES * REVIEWER FIRMOGRAPHICS",
    [
        '// scrapeType: "reviews" · one item per review',
        "{",
        '>  "type": "review", "reviewId": 13183206, "rating": 5.0,',
        '>  "title": "Organized Team Communication with Powerful Search",',
        '  "likeBest": "Honestly, the channel organization is what keeps...",',
        '  "dislike": "The notification system drives me crazy...",',
        '  "problemsSolved": "Before Slack, keeping my team aligned was...",',
        '>  "reviewerName": "Diana C.", "reviewerJobTitle": "Lead Business Architect",',
        '>  "reviewerIndustry": "Information Technology and Services",',
        '>  "companySegment": "Mid-Market", "companySize": "51-1000 emp.",',
        '  "publishedDate": "2026-07-29", "reviewSource": "Organic"',
        "}",
        "// + product_profile, listing, alternatives, categories_directory",
    ],
)

add(
    "google-maps-scraper", "#EA4335", "#34A853",
    ["GOOGLE MAPS", "LOCAL LEADS"],
    ["EVERY PLACE.", "EVERY EMAIL.", "AS JSON."],
    "Build a lead list of any local business in any city — <b>name, category, address, "
    "phone, website, rating, reviews, photos and opening hours</b> — with the "
    "<i>owner's email already extracted from their website</i> plus Facebook, "
    "Instagram and X profiles. <u>No login, no Google API key.</u>",
    "PLACES * EMAILS * REVIEWS * PHOTOS",
    [
        "// one dataset item per place",
        "{",
        '>  "name": "Scissors & Scotch", "category": "Barber shop",',
        '  "address": "331 N St NE, Washington, DC 20002, USA",',
        '  "city": "Washington", "state": "DC", "zip_code": "20002",',
        '>  "phone": "(202) 481-2850", "website": "https://scissorsscotch.com/",',
        '>  "emails": ["info@scissorsscotch.com", "dc@scissorsscotch.com"],',
        '>  "facebook": "https://www.facebook.com/scissorsscotch",',
        '  "instagram": "https://www.instagram.com/scissorsscotch/",',
        '>  "rating": 4.7, "reviews_count": 1422, "price_level": "$$",',
        '  "latitude": 38.9068, "longitude": -77.001, "plus_code": "WX4X+PH",',
        '  "opening_hours": "Monday: 9 AM-8 PM | Tuesday: 9 AM-8 PM | ...",',
        '  "reviews": [{ "rating": 5, "text": "Best haircut in DC..." }, ... ]',
        "}",
    ],
)

add(
    "amazon-scraper", "#FF9900", "#2D74FF",
    ["AMAZON", "6 MODES"],
    ["EVERY PRODUCT.", "EVERY REVIEW.", "AS JSON."],
    "<b>Product details, search, Best-Sellers categories, customer reviews, seller "
    "profiles and buy-box offers</b> — six scrape modes across "
    "<i>19 Amazon marketplaces</i>. Price, list price, stars breakdown, stock, "
    "features and images on every product. <u>Pay per event, no subscription.</u>",
    "6 MODES * 19 MARKETPLACES",
    [
        '// scrapeType: "product" · one item per ASIN',
        "{",
        '>  "asin": "B0BDHWDR12", "brand": "Apple",',
        '>  "title": "Apple AirPods Pro (2nd Gen) Wireless Earbuds...",',
        '>  "price": 258.54, "listPrice": 299.0, "discountPercent": "-14%",',
        '  "currency": "$", "inStock": true, "inStockText": "In Stock",',
        '>  "stars": 4.7, "reviewsCount": 57949,',
        '  "starsBreakdown": { "5 star": "87%", "4 star": "8%", "3 star": "2%",',
        '    "2 star": "0%", "1 star": "3%" },',
        '  "features": ["RICHER AUDIO EXPERIENCE - the Apple H2 chip...", ... ],',
        '  "images": ["https://m.media-amazon.com/images/I/61SUj2..."]',
        "}",
        "// + search, category, reviews, seller, offers",
    ],
)

add(
    "aliexpress-scraper", "#FF4747", "#FF8A00",
    ["ALIEXPRESS", "3 MODES"],
    ["EVERY PRODUCT.", "EVERY VARIANT.", "AS JSON."],
    "<b>One clean row per product</b> — price and discount, orders sold, rating, "
    "<i>every SKU variant with its own price and live stock</i>, shipping cost and "
    "delivery dates. Search, full product details and reviews in one Actor. "
    "<u>No login, no AliExpress API key.</u>",
    "3 MODES * PER-SKU PRICE + STOCK",
    [
        '// scrapeType: "search" · one row per product, no record soup',
        "{",
        '>  "productId": "3256806779925038", "title": "TWS E6S Wireless Earbuds",',
        '>  "price": 0.99, "originalPrice": 6.81, "discountPercent": 85,',
        '  "priceMin": 0.99, "priceMax": 4.87, "currency": "USD",',
        '>  "rating": 4.9, "reviewsCount": 13677, "ordersCount": 100000,',
        '>  "ordersCountExact": 120058, "wishlistCount": 810, "stockTotal": 4049,',
        '  "isChoice": true, "listedAt": "2024-05-13 00:00:00", "skuCount": 5,',
        '  "variantProperties": [{ "name": "Color",',
        '    "values": ["WHITE", "Blue", "green", "black", "Pink"] }],',
        '>  "skus": [{ "price": 0.99, "stock": 812, "attributes": "WHITE" }, ... ],',
        '  "badges": ["Save $5.82", "Delivery: Aug 09 - 14"]',
        "}",
    ],
)

add(
    "alibaba-scraper", "#FF6A00", "#FFB000",
    ["ALIBABA.COM", "5 MODES"],
    ["EVERY PRODUCT.", "EVERY SUPPLIER.", "AS JSON."],
    "<b>Keyword search, full product detail (up to 230 fields), verified supplier "
    "dossiers (52 fields), supplier catalogues and buyer reviews</b>. "
    "<i>Quantity price tiers, MOQ and lead time</i> on every product. "
    "<u>From $1.40 per 1,000 products on paid plans.</u>",
    "5 MODES * UP TO 230 FIELDS / PRODUCT",
    [
        '// scrapeType: "product" · 24 blocks, up to 230 fields',
        "{",
        '>  "productId": "1600169703353", "type": "product",',
        '>  "title": "Neon Led Strip Light Rgb Led Dream Color 60led/m 12v",',
        '  "price": {',
        '>    "min": 9.0, "max": 9.5, "display": "$9-9.50", "unit": "piece",',
        '>    "priceModel": "quantity_tiers", "tiers": [',
        '      { "minQuantity": 100, "maxQuantity": 299, "price": 9.5 },',
        '      { "minQuantity": 300, "maxQuantity": 499, "price": 9.3 },',
        '      { "minQuantity": 500, "price": 9.0 }] },',
        '>  "order": { "minOrderQuantity": 100, "leadTimeDays": 30 },',
        '  "media": { "mainImage": "https://s.alicdn.com/...png", "hasVideo": true },',
        '  "specifications": [{ "name": "Place of Origin", ... }]',
        "}   // + search, supplier, supplierProducts, reviews",
    ],
)

add(
    "tiktok-shop-scraper-usage", "#25F4EE", "#FE2C55",
    ["TIKTOK SHOP", "6 MODES"],
    ["EVERY PRODUCT.", "EVERY SELLER.", "AS JSON."],
    "<b>Search, product details, reviews, category pages, stores and creator "
    "profiles</b> — six modes, each with its own input section. "
    "<i>Price, discount, sales volume, rating and seller data</i> on every product "
    "card, plus <u>store analytics with GMV estimation.</u>",
    "6 MODES * SALES VOLUME * GMV ESTIMATES",
    [
        '// scrapeType: "search" · one item per product card',
        "{",
        '>  "productId": "1729595536444134138", "type": "product_card",',
        '>  "title": "HydroJug Sport 32oz Portable Water Bottle",',
        '>  "currentPrice": "24.99", "originalPrice": "29.99", "discountPercent": "-17%",',
        '>  "salesVolume": 5200, "rating": 4.8, "reviewCount": "342",',
        '  "sellerName": "HydroJug", "tags": ["Best Seller", "Free Shipping"],',
        '  "searchRank": 1, "query": "water bottle",',
        '  "productUrl": "https://shop.tiktok.com/us/pdp/hydrojug-sport-32oz/...",',
        '  "imageUrls": ["https://..."]',
        "}",
        "// + product, reviews, category, store (GMV), creator",
    ],
)

add(
    "rednote-xiaohongshu-scraper", "#FF2442", "#FF8A00",
    ["REDNOTE 小红书", "8 MODES"],
    ["EVERY NOTE.", "EVERY CREATOR.", "AS JSON."],
    "<b>Trending category feeds, full note details, comment threads, creator profiles, "
    "creator notes, keyword research and search</b> — eight modes in one Actor. "
    "<i>Likes, collects, shares, hashtags, topics and IP location</i> on every note. "
    "<u>No login, no cookies.</u>",
    "8 MODES * NOTES + CREATORS + COMMENTS",
    [
        '// scrapeType: "discoverFeed" · one item per note',
        "{",
        '>  "noteId": "6453436d000000000800c87b", "noteType": "image",',
        '>  "title": "芭蕾舞女孩蛋糕 六寸蛋糕 女生蛋糕",',
        '>  "likes": 23, "collects": 15, "commentsCount": 4, "shares": 4,',
        '  "engagementTotal": 46, "publishedAt": "2023-05-04T05:32:29Z",',
        '>  "ipLocation": "河南", "authorName": "宸一烘焙",',
        '  "authorId": "55878481f5a2632c8480b32f",',
        '  "hashtags": ["蛋糕", "最好吃的奶油蛋糕", "生日蛋糕", "定制蛋糕"],',
        '  "topics": [{ "id": "53cb2602b4c4d60d1602cc2a", "name": "蛋糕" }]',
        "}",
        "// + noteDetails, noteComments, userProfiles, userNotes,",
        "//   keywordResearch, searchNotes, searchUsers",
    ],
)
