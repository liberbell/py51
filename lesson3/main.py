import requests

url = "https://use1-prod-th.rbictg.com/graphql"

payload = [
    {
        "operationName": "GetRestaurants",
        "variables": {"input": {
            "filter": "NEARBY",
            "cordinates": {
                "userLat": 43.447788,
                "userLng": -79.3733,
                "searchRadius": 8000
            },
            "first": 20,
            "status": "OPEN",
        }},
        "query": """query GetRestaurants($input: RestaurantsInput) {
    restaurants(input: $input) {
        pageInfo {
        hasNextPage
        endCursor
        __typename
        }
        totalCount
        nodes {
        ...RestaurantNodeFragment
        __typename
        }
        __typename
    }
    }

    fragment RestaurantNodeFragment on RestaurantNode {
    _id
    storeId
    isAvailable
    posVendor
    chaseMerchantId
    cateringHours {
        ...OperatingHoursFragment
        ...OperatingHoursFragment
        __typename
    }
    curbsideHours {
        ...OperatingHoursFragment
        __typename
    }
    cateringHours {
        ...OperatingHoursFragment
        __typename
    }
    timezone
    deliveryHours {
        ...OperatingHoursFragment
        __typename
    }
    diningRoomHours {
        ...OperatingHoursFragment
        __typename
    }
    distanceInMiles
    drinkStationType
    driveThruHours {
        ...OperatingHoursFragment
        __typename
    }
    driveThruLaneType
    email
    environment
    franchiseGroupId
    franchiseGroupName
    frontCounterClosed
    hasBreakfast
    hasBurgersForBreakfast
    hasCatering
    hasCurbside
    hasDelivery
    hasDineIn
    hasDriveThru
    hasTableService
    hasMobileOrdering
    hasLateNightMenu
    hasParking
    hasPlayground
    hasTakeOut
    hasWifi
    hasLoyalty
    id
    isDarkKitchen
    isFavorite
    isHalal
    isRecent
    latitude
    longitude
    mobileOrderingStatus
    name
    number
    parkingType
    phoneNumber
    physicalAddress {
        address1
        address2
        city
        country
        postalCode
        stateProvince
        stateProvinceShort
        __typename
    }
    playgroundType
    pos {
        vendor
        __typename
    }
    posRestaurantId
    restaurantImage {
        asset {
        _id
        metadata {
            lqip
            palette {
            dominant {
                background
                foreground
                __typename
            }
            __typename
            }
            __typename
        }
        __typename
        }
        crop {
        top
        bottom
        left
        right
        __typename
        }
        hotspot {
        height
        width
        x
        y
        __typename
        }
        __typename
    }
    restaurantPosData {
        _id
        __typename
    }
    status
    vatNumber
    timezone
    __typename
    }

    fragment OperatingHoursFragment on OperatingHours {
    friClose
    friOpen
    monClose
    monOpen
    satClose
    satOpen
    sunClose
    sunOpen
    thrClose
    thrOpen
    tueClose
    tueOpen
    wedClose
    wedOpen
    __typename
    }
    """
    }
]

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "accept": "*/*",
    "accept-language": "ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "x-session-id": "d8c8dcb0-df44-41d9-a19a-aa865d8f1462",
    "x-forter-token": "5764664add3e44a1a631d8257379ed63_1750890897453_134522_UDF43-m4_13ck__tt",
    "x-user-datetime": "2025-06-26T07:45:26+09:00",
    "x-ui-language": "en",
    "x-ui-region": "CA",
    "x-ui-platform": "web",
    "origin": "https://www.timhortons.ca",
    "DNT": "1",
    "connection": "keep-alive",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "content-type": "application/json"
}

response = requests.request("POST", url=url, json=payload, headers=headers)