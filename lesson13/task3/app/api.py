def getCatImage(delay):

    # Simulate Delay
    time.sleep(delay)

    url = requests.get(
        "https://api.thecatapi.com/v1/images/search").json()[0]['url']

    # Result
    return url
