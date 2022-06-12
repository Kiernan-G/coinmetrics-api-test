import requests
import json

response = requests.get('https://community-api.coinmetrics.io/v4/catalog/assets?pretty=true').json()

##response_file = json.loads(response)
#It's already formatted as a json with the statement on line 4, but a lot of documentation will tell you to do something like this
# .loads() switches from str, bytes, etc. to a dict, .unload() does the reverse.

print(response.keys())

#The only key for the dictionary is 'data' which is pretty annoying. 

#print(response['data'])
#This will just print the whole json again

with open('response.json', 'w') as outfile:
    json.dump(response, outfile)
#This will give you a file of the json in your repo instead of outputting through console. Not v readable tho.

asset_list = []
for asset_name in response['data']:
    asset_list.append(asset_name['asset'])

print(asset_list)

#This is how you create lists for specific data