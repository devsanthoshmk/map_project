from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_DZfxrBVXhsdYkm1L71NHa4KUkDPrnY2mVkHW")

# Prepare the Actor input
run_input = {
    "search": "restaurant",
    "location": "New York",
    "maxCrawledPlacesPerSearch": 10,
}

# Run the Actor and wait for it to finish
run = client.actor("tGmy6jMKXM0UbIsjT").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
