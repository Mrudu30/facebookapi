import requests
import json

# # Replace with your actual page access token
# page_access_token = "EAAJjeJnW2qkBO1O8ZBUB00r8gN4ZAamNBPZB5Y2ruCB4MgCvO2uKZCeJyrHyT0JZAXGBhyZCAZCWaRrAOjtaLTddsIzGhiKE2HmX8ZCsU2ZBG7nkv0ZApg8xWVMNCZBX6trhnxmDhqV7X4Y3KfzkAnOZBZCtRvMfhi33MJCu9ejyZBrx5qiLUSaJVXBZCktiNZBLVUbRCLkNNyYNlcRYMDEVhPxxByce8XCXV5LaWZBvb"

# # Page ID of the "Test Api" page
# page_id = "288293304366062"

# # API endpoint for posting to the page's feed
# url = f"https://graph.facebook.com/{page_id}/feed"

# # Parameters for the post (you can adjust as needed)
# params = {
#     "access_token": page_access_token,
#     "message": "Test 2 from the flask app!"
# }

# # Make the POST request to create the post
# response = requests.post(url, params=params)

# # Parse the response (assuming it's in JSON format)
# data = response.json()

# # Print the response data
# print(data)

def upload_photo_and_post(caption, photo_url, access_token, page_id):
    # Upload the photo
    photo_data = {
        "url": photo_url,
        "access_token": access_token,
        "published":False
    }
    photo_response = requests.post(f"https://graph.facebook.com/{page_id}/photos", data=photo_data)
    photo_data = photo_response.json()
    if "error" in photo_data:
        print('first error')
        print("Error uploading photo:", photo_data["error"]["message"])
        return None

    # Get the photo ID
    photo_id = photo_data["id"]

    # Create the post with the caption and photo ID
    attached_media = [{"media_fbid": str(photo_id)}]
    post_data = {
        "message": caption,
        "attached_media": f"{attached_media}",
        "access_token": access_token
    }
    print(post_data)
    post_response = requests.post(f"https://graph.facebook.com/{page_id}/feed", data=post_data)
    post_result = post_response.json()
    if "error" in post_result:
        print("2nd error")
        print("Error creating post:", post_result["error"]["message"])
        return None

    return post_result["id"]

# photo_url = "https://img.freepik.com/free-photo/cascade-boat-clean-china-natural-rural_1417-1356.jpg?t=st=1713244356~exp=1713247956~hmac=52b45a30268feb87c5c4b90a01cfd3efd4a75d8f91e27404d66c58c8b9e0ba1e&w=740"
photo_path = 'C:\Users\admin\Downloads\wallpapers\mushroom.jpg'
page_id = "288293304366062"
access_token = "EAAJjeJnW2qkBOy8iRGHet2FsN7FIZAujiVigAntpKoIbrsN63c4oRh49wHjtH1oSSUpjmCMpvZBYsaR8hUNcimqpkmj5JGFhnMFds0MMIJloyACQFfwiWmZCPzpMnxIyDNZAWX075ZCTVoR3khAZBbZAVXcYuR2qPZBhqkoYAOtvjlTjOAiM9LczxBOOAIzJkjpHryY4iVIFLH3M6kcEhQKgdOoqt7zLHlrt"
caption = "Butterfly with pink flowers"

post_id = upload_photo_and_post(caption, photo_url, access_token,page_id)
if post_id:
    print("Post created successfully. Post ID:", post_id)
else:
    print("Failed to create post.")