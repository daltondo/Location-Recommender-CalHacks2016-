from instagram.client import InstagramAPI
import sys, webbrowser, time
from bottle import Bottle, request
from threading import Thread

# predefined variables
client_id = "0efe33ef2a4f4d6da9f0ad6ef59c66e0"
client_secret = "019491546c624a10ac4d011fc686800c"
redirect_uri = "http://localhost:8000"

#start web server
server = Bottle()
token  = list()
@server.route('/')
def root():
 	token.append(request.url)
def begin():
    server.run(host='0.0.0.0', port=8000)
f = Thread(target=begin)
f.daemon = True
f.start()

#predefined scope
raw_scope = ""
scope = raw_scope.split(' ')
if not scope or scope == [""]:
    scope = ["basic"]

#creating api
api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

#getting access token and user_id
redirect_uri = api.get_authorize_login_url(scope = scope)
webbrowser.open(redirect_uri)
#time.sleep(10)
while not token:
	time.sleep(1)
code = token[0][28:]
access = api.exchange_code_for_access_token(code)

access_token = access[0]
user_id = access[1]['id']

#recreating api and running code
api = InstagramAPI(access_token = access_token, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
recent_media, next_ = api.user_recent_media(user_id=user_id, count=10)
for media in recent_media:
   print (media.caption.text)