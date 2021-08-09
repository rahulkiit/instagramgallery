import requests
import os
import json

access_token = os.environ.get('INSTAGRAM_ACCESS_TOKEN')
response = requests.get("https://graph.instagram.com/me?access_token="+access_token)
print(response.json())

response = requests.get("https://graph.instagram.com/me/media?fields=id,caption,media_url,permalink,media_type&access_token="+access_token)

out_file = open("_data/instagramdata.json", "w")
#j = json.loads(response.json())
out_file.write(json.dumps(response.json()['data'], ensure_ascii=True, indent=None))
