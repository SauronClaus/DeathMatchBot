import wikipedia
import urllib
import requests
import json
from embeds import checkLinks


def get_wiki_main_image(title):
    url = 'https://en.wikipedia.org/w/api.php'
    data = {
        'action' :'query',
        'format' : 'json',
        'formatversion' : 2,
        'prop' : 'pageimages|pageterms',
        'piprop' : 'original',
        'titles' : title
    }
    response = requests.get(url, data)
    json_data = json.loads(response.text)
    return json_data['query']['pages'][0]['original']['source'] if len(json_data['query']['pages']) >0 else 'Not found'

suggestionsFile = open("sanitizedSuggestions.txt", "r", encoding='utf-8')
suggestionsFull = suggestionsFile.read()
suggestions = suggestionsFull.split("\n")

#suggestions = ["Taylor Swift"]
            
for suggestion in suggestions:
    print("Beginning " + suggestion)
    counter = 1
    suggestion = checkLinks(suggestion)
    article = wikipedia.page(suggestion, auto_suggest=False)   
    
    mainPhoto = get_wiki_main_image(suggestion)
    urllib.request.urlretrieve(mainPhoto, "Pictures\\AutoDownload\\" + suggestion + ".png") 
    print("Completed " + suggestion)
#img = Image.open("George Washington Photos\\" + suggestion + str("NEW") + ".png") 
#img.show()
print("Completed images!\n")
