from pyfacebook import GraphAPI

api = GraphAPI(access_token="EAAJjeJnW2qkBO6NG0yfnEVc6FcUCdForKmraLZCVuaJJgICoYyVLN8ZABN5o5Dzo6ZBOGyYR8XnxaS7LRM8Cs01ebVNhtq8ef8qjHig2xDSZBMbRr9nZA4Jd6oDAUwZBsuSO06BgVcZADZAKtjDMRggcwfUD0EhftBD5S7F782hUCiJ334bC1HMlff0TpH0DeHsNBZBzj2K9KClZAo6cVH7MMM4MZClOgZDZD",app_id="672319581641385")

# basic credentials
# test api page
page_id = "288293304366062"


api.post_object(object_id=f"{page_id}",data={"message":"this is api testing",  "published":True})