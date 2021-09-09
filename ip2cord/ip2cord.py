from time import sleep
import requests
import json



def ip2cord():
    geolocation = requests.get("https://get.geojs.io/v1/ip/geo.json")
    geolocation_output = geolocation.json() 
    geolocation_data_lon = json.dumps(geolocation_output['longitude']) 
    geolocation_data_lat = json.dumps(geolocation_output['latitude'])
    punctuation = '''"''' 
    remove_punct = "" 
    for character in geolocation_data_lat + geolocation_data_lon:
        if character not in punctuation:
            remove_punct = remove_punct + character 
            lat_removed_quotes = remove_punct 
    edit = lat_removed_quotes[:7] + "," + lat_removed_quotes[7:]
    return(edit)

if __name__ == '__ip2cord__.py':
    ip2cord()