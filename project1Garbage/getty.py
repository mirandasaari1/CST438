import render_template
import flask
import requests

def gettyImage():
      #define header
      headers = {'API_key': 'vvdp68vnrgun32p39z5q8gmg'}
      r = requests.get('https://api.gettyimages.com:443/v3/search/images/editorial?phrase=Disney%20Characters&sort_order=most_popular', headers=headers)
      
      #get json data
      images_url = r.json()
      image_url = images_url["images"][0]["display_sizes"][0]["uri"]


#curl 
#curl -i -H "Api-Key:vvdp68vnrgun32p39z5q8gmg" "https://api.gettyimages.com:443/v3/search/images/editorial?phrase=Disney%20Characters&sort_order=most_popular"