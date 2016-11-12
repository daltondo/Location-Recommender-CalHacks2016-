from instagram.client import InstagramAPI
import sys


# predefined variables
client_id = "0efe33ef2a4f4d6da9f0ad6ef59c66e0"
client_secret = "019491546c624a10ac4d011fc686800c"
redirect_uri = "http://localhost:8000"

#predefined scope
raw_scope = "follower_list public_content".strip()
scope = raw_scope.split(' ')
if not scope or scope == [""]:
    scope = ["basic"]

#creating api
api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

#getting access token and user_id
# redirect_uri = api.get_authorize_login_url(scope = scope)
# print ("Visit this page and authorize access in your browser: "+ redirect_uri)
# code = (str(input("Paste in code in query string after redirect: ").strip()))
# access = api.exchange_code_for_access_token(code)

# access_token = access[0]
# user_id = access[1]['id']

# print (access_token, user_id)

access_token, user_id = "1474609945.0efe33e.e94c8f154d5b405dbd594a16570a3b52", "1474609945"


#recreating api and running code
api = InstagramAPI(access_token = access_token, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
recent_media, next_ = api.user_recent_media(user_id=user_id)

user = api.user(user_id)
data = api.user_liked_media()

# acquire lattitude and longitude based off liked pictures
def locations(media_list): 
	location_list = []
	for media in media_list[0]:
		try: 
			location = media.location 
			location_name = media.location.name
			location_list.append([location, location_name]) 
		except AttributeError: 
			pass 
	return location_list


def get_lon(location): 
	return location.point.longitude

def get_lat(location):
	return location.point.latitude

def get_lat_and_lon(locations):
	lat_lon = []
	for location in locations: 
		lat_lon.append([get_lat(location[0]), get_lon(location[0])])
	return lat_lon

def get_center(lat_lon):
	lats = []
	lons = []

	for val in lat_lon: 
		lats.append(val[0])
		lons.append(val[1])

	return sum(lats)/len(lats), sum(lons)/len(lons)



lat_lon = get_lat_and_lon(locations(data))
center = get_center(lat_lon)






