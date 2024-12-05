import time
import requests

def getCatImage(delay):
    """
    Fetches a cat image URL after a specified delay.
    
    Parameters:
    delay (int): The delay in seconds before fetching the image.
    
    Returns:
    str: The URL of the cat image if successful, otherwise an error message.
    """
    # Simulate Delay
    time.sleep(delay)
    
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        # Parse JSON and get the image URL
        data = response.json()
        
        if isinstance(data, list) and len(data) > 0:
            url = data[0].get('url')
            if url:
                return url
            else:
                return "No URL found in the response."
        else:
            return "Unexpected response format."
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"
