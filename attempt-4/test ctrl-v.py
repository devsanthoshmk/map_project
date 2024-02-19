from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_DZfxrBVXhsdYkm1L71NHa4KUkDPrnY2mVkHW")

# Prepare the Actor input
run_input = {
    "searchStringsArray": ["restaurant"],
    "locationQuery": "New York, USA",
    "maxCrawledPlacesPerSearch": 50,
    "language": "en",
    "maxImages": 10,
    "onlyDataFromSearchPage": False,
    "includeWebResults": False,
    "scrapeDirectories": False,
    "deeperCityScrape": False,
    "maxReviews": 5,
    "reviewsSort": "newest",
    "reviewsFilterString": "",
    "scrapeReviewerName": True,
    "scrapeReviewerId": True,
    "scrapeReviewerUrl": True,
    "scrapeReviewId": True,
    "scrapeReviewUrl": True,
    "scrapeResponseFromOwnerText": True,
    "countryCode": "us",  # Replace with the desired country code
    "searchMatching": "all",
    "placeMinimumStars": "",
    "skipClosedPlaces": False,
    "allPlacesNoSearchAction": "",
}

# Run the Actor and wait for it to finish
run = client.actor("nwua9Gu5YrADL7ZDj").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
