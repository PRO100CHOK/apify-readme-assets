# -*- coding: utf-8 -*-
"""Part 3: real estate + travel & hospitality."""
from heroes_all import add

add(
    "zillow-scraper-all-in-one", "#006AFF", "#00C7A9",
    ["ZILLOW", "4 MODES"],
    ["EVERY LISTING.", "EVERY ZESTIMATE.", "AS JSON."],
    "<b>Search (for sale, for rent, sold), full property details with 100+ facts, "
    "Zestimate&reg; home values and real-estate agent profiles</b> — four modes in one "
    "Actor. <i>Price, beds, baths, area, lot size, tax assessment and days on "
    "Zillow.</i> <u>More than 500 results from a single search.</u>",
    "4 MODES * ZESTIMATE * AGENT DATA",
    [
        '// mode: "search" · one item per listing',
        "{",
        '>  "zpid": "113419231", "statusType": "FOR_SALE", "statusText": "House for sale",',
        '>  "price": 2950000, "priceLabel": "$2,950,000",',
        '  "address": "509 Gothic Avenue, Crested Butte, CO 81224",',
        '  "city": "Crested Butte", "state": "CO", "zipcode": "81224",',
        '>  "beds": 3, "baths": 3, "area": 1660, "lotAreaValue": 6098.4,',
        '  "homeType": "SINGLE_FAMILY", "daysOnZillow": 4, "has3DModel": true,',
        '>  "zestimate": 2810200, "rentZestimate": 3572,',
        '>  "taxAssessedValue": 2422570,',
        '  "latitude": 38.8718, "longitude": -106.98193,',
        '  "url": "https://www.zillow.com/homedetails/509-Gothic-Ave/113419231_zpid/"',
        "}   // + propertyDetail, zestimate, agent",
    ],
)

add(
    "realtor-com-scraper", "#D92228", "#2D74FF",
    ["REALTOR.COM", "3 MODES"],
    ["EVERY LISTING.", "EVERY AGENT.", "AS JSON."],
    "<b>Search (~70 fields), full property details (90+ fields) and agent profiles</b> "
    "— plus data no other scraper returns: <i>client reviews and star ratings, "
    "building permit history and neighborhood price medians</i>. "
    "<u>From $1.50 per 1,000 results.</u>",
    "3 MODES * PERMITS * AGENT REVIEWS",
    [
        '// scrapeType: "search" · ~70 fields per listing',
        "{",
        '>  "propertyId": "8742581034", "status": "for_sale",',
        '  "addressLine": "5611 Meadow Crst", "city": "Austin", "stateCode": "TX",',
        '>  "listPrice": 372000, "pricePerSqft": 233, "daysOnMarket": 37,',
        '>  "beds": 3, "baths": 2, "sqft": 1600, "lotSqft": 7187, "yearBuilt": 1988,',
        '  "propertyType": "single_family", "photoCount": 29,',
        '>  "agentName": "Tarek Boulbol", "agentPhone": "5125522198",',
        '  "officeName": "Texas Premier Realty",',
        '>  "estimate": 365138, "estimateSource": "Quantarium",',
        '  "neighborhoodMedianListPrice": 374950,',
        '  "neighborhoodMedianDaysOnMarket": 69',
        "}   // + propertyDetail (90+ fields, permits), agents",
    ],
)

add(
    "apartments-scraper-usage", "#F26522", "#0BA5EC",
    ["APARTMENTS.COM", "3 ACTIONS"],
    ["EVERY RENTAL.", "EVERY CONTACT.", "AS JSON."],
    "<b>Search listings, full property details (120+ fields) and contact emails "
    "scraped straight from property websites</b>. <i>Walk, transit and bike scores, "
    "floor plans, fees, amenities, schools and photos.</i> "
    "<u>Chain the three actions together with a dataset ID.</u>",
    "3 ACTIONS * 120+ FIELDS * EMAILS",
    [
        "// action 1: search listings · one item per property",
        "{",
        '>  "name": "The Max", "listingId": "abc123", "position": 1,',
        '  "address": { "full": "100 W 57th St, New York, NY 10019",',
        '    "city": "New York", "state": "NY", "zip": "10019" },',
        '>  "rentRollup": [{ "beds": "Studio", "price": "$3,917+" },',
        '>    { "beds": "1 Bed", "price": "$5,639" }, { "beds": "2 Beds", "price": "$8,122" }],',
        '>  "priceMin": 3917, "priceMax": 8122, "phone": "(929) 552-4351",',
        '  "amenities": ["Pets Allowed", "Fitness Center", "In Unit Washer & Dryer"],',
        '  "managementCompany": "UDR", "photoCount": 21,',
        '>  "hasVideo": true, "has3DTour": true, "hasSpecials": true, "tier": "diamond"',
        "}",
        "// + action 2: property details (120+ fields) · action 3: emails",
    ],
)

add(
    "idealista-scraper", "#7FBA00", "#FF8A00",
    ["IDEALISTA", "ES · IT · PT"],
    ["EVERY PROPERTY.", "EVERY AGENCY.", "AS JSON."],
    "Listings from <b>Spain, Italy and Portugal</b> — for sale and for rent, homes, "
    "new developments, offices, garages and land. <i>Price, price per m&sup2;, price "
    "drops, size, rooms, condition, year built and energy certificate.</i> "
    "<u>Agency profiles with phone numbers.</u>",
    "3 COUNTRIES * PRICE DROPS * AGENCY PHONES",
    [
        "// one dataset item per property",
        "{",
        '>  "propertyCode": "111901446", "operation": "sale", "propertyType": "homes",',
        '  "title": "Piso en venta en Calle del Príncipe de Vergara",',
        '  "subtitle": "Ciudad Jardín, Madrid",',
        '>  "price": 1250000, "priceByArea": 8117,',
        '>  "priceDrop": { "previousPrice": 1350000, "percentage": 7 },',
        '>  "size": 154, "rooms": 4, "bathrooms": 2, "yearBuilt": 1971,',
        '  "floor": "4ª planta exterior con ascensor", "condition": "good",',
        '>  "energyCertificate": "D", "reference": "DG 220077", "numPhotos": 28,',
        '  "features": ["154 m² construidos", "4 habitaciones", "2 baños", "Terraza"],',
        '  "images": [{ "url": "https://img4.idealista.com/..." }, ... ]',
        "}   // + agency mode: name, phone, listings",
    ],
)

add(
    "booking-all-in-one-scraper", "#0071C2", "#FFB700",
    ["BOOKING.COM", "6 MODES"],
    ["EVERY HOTEL.", "EVERY PRICE.", "AS JSON."],
    "One Actor instead of a stack of single-purpose tools: <b>hotel search, room-level "
    "prices with a calendar up to 365 days ahead, reviews, hotel details and host / "
    "owner data</b>. <i>Rating, review count, star class, coordinates and distance "
    "from the centre.</i> <u>No login, no Booking API key.</u>",
    "6 MODES * 365-DAY PRICE CALENDAR",
    [
        '// scrapeType: "search" · one item per property',
        "{",
        '>  "dataType": "property", "name": "Mercure Amsterdam Sloterdijk Station",',
        '>  "stars": 4, "rating": 8.6, "ratingLabel": "Excellent", "reviewsCount": 4177,',
        '>  "price": 126.21, "priceRounded": "$126", "currency": "USD",',
        '  "city": "Amsterdam", "countryCode": "nl",',
        '  "latitude": 52.387911, "longitude": 4.834296,',
        '>  "distanceFromCenter": "4.3 km from downtown",',
        '  "hostType": "PROFESSIONAL", "isSoldOut": false,',
        '  "image": "https://cf.bstatic.com/xdata/images/hotel/square600/873579185.webp"',
        "}",
        "// + prices (calendar), reviews, hotelDetails, hostInfo, all",
    ],
)

add(
    "tripadvisor-all-in-one", "#34E0A1", "#2D74FF",
    ["TRIPADVISOR", "HOTELS + FOOD"],
    ["EVERY HOTEL.", "EVERY REVIEW.", "AS JSON."],
    "Paste a TripAdvisor URL, type a keyword, or just name a city — the Actor finds "
    "the places and <b>embeds each place's reviews inside its own record</b>. "
    "<i>Prices from every booking provider, deals and special offers.</i> "
    "<u>No login, no TripAdvisor API key, no proxies to configure.</u>",
    "HOTELS * RESTAURANTS * NESTED REVIEWS",
    [
        '// category: "hotels" · reviews embedded in each place',
        "{",
        '>  "__type": "hotel", "locationId": 250927,',
        '>  "name": "Hotel Europe Saint Severin", "accommodationType": "Hotel",',
        '  "description": "Friendly and comfortable property in the Latin quarter...",',
        '>  "priceRangeMin": 149, "priceRangeMax": 320, "finalPrice": "$221",',
        '>  "dealsCount": 11, "specialOffer": "BOOK DIRECT & SAVE 15%",',
        '  "bookingProvider": "all.accor.com",',
        '  "offers": [{ "provider": "Hotels.com", "displayPrice": "$221",',
        '    "basePrice": 221, "currency": "USD", "isSupplierDirect": false }, ... ],',
        '>  "reviews": [{ "rating": 5, "title": "...", "text": "..." }, ... ]',
        "}   // + restaurants, attractions",
    ],
)
