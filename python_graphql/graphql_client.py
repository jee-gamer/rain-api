import requests
import json

url = 'http://localhost:3000/graphql'
json_query = {'query': '''
    basin(basinId:5){
    somebullshit
    }
'''}

r = requests.post(url=url, json=json_query)
obj = json.loads(r.text)

pretty_json = json.dumps(obj, indent=2)
print(pretty_json)