import json,requests,sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
x = response.json()
print(json.dumps(x, indent=2))
print()
for i in x["results"]:
    print(i["trackName"])