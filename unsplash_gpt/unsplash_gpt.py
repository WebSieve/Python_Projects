import requests
import bs4
import selenium
import webbrowser


# Step 1: Define a function to get images from Unsplash
def get_images_from_unsplash(query, access_key, per_page=5):
    """
    Fetches image URLs from Unsplash based on a search query.

    Parameters:
        query (str): The search term for the images.
        access_key (str): Your Unsplash API access key.
        per_page (int): Number of images to fetch per request.

    Returns:
        list: A list of image URLs.
    """
    # Unsplash API endpoint
    url = "https://api.unsplash.com/search/photos"

    # Parameters to send with the request
    params = {
        "query": query,  # Search term provided by the user
        "client_id": access_key,  # Unsplash API key
        "per_page": per_page  # Number of images to return
    }

    # Make the GET request to the Unsplash API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract URLs of the images
        image_urls = [image['urls']['regular'] for image in data['results']]
        return image_urls
    else:
        # Print an error message if the request fails
        print(f"Error: Unable to fetch images (Status Code: {response.status_code})")
        return []

# Step 2: Create a chatbot-like interface
def chatbot():
    """
    A chatbot interface to interact with the user and fetch images.
    """
    print("Welcome to the Image Fetcher Chatbot!")
    print("Type 'exit' to quit the chatbot.")
    
    # Unsplash API Access Key (replace 'your_access_key' with your actual key)
    access_key = "GRQ4StMcDTaWZHzIolcFPDIrSYjH3Cfxoe_kbsmIRGw"
    
    while True:
        # Get input from the user
        user_input = input("\nWhat type of images are you looking for? ")

        # Check if the user wants to exit
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Fetch images from Unsplash
        print(f"\nSearching for images related to '{user_input}'...")
        images = get_images_from_unsplash(user_input, access_key)

        # Check if any images were returned
        if images:
            print(f"\nFound {len(images)} images! Opening them in your browser:")
            for i, img_url in enumerate(images):
                print(f"{i + 1}. {img_url}")  # Print image URLs
                webbrowser.open(img_url)  # Open the image URL in the browser
        else:
            print("\nNo images found. Please try a different query.")

# Step 3: Run the chatbot
if __name__ == "__main__":
    chatbot()