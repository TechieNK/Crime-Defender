from newspaper import Article
import nltk
from geotext import GeoText
from googlesearch import search
nltk.download('punkt')
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import pycountry_convert as pc
import pandas as pd
from urllib import request
from geotext import GeoText
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from shapely.geometry import Point, Polygon
import descartes
import plotly
import chart_studio.plotly as py
import plotly.graph_objects as go
from newspaper import Config
from plotly.io import to_html
from collections import Counter
from wordcloud import WordCloud 
import io
import urllib, base64

def country_to_continent(place):
  country_code = pc.country_name_to_country_alpha2(place)

  country_continent_code = pc.country_alpha2_to_continent_code(country_code)

  continent = pc.convert_continent_code_to_continent_name(country_continent_code)

  return (continent.lower(),country_code)

def extracting_cities(summary,country_code):
  places =GeoText(summary,country_code)
  cities = list(set(places.cities))
  print(cities)
  wc = Counter(places.cities)
  print(wc)
  return cities,wc

def extracting_news_content(links):
  summary=" "
  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
  config = Config()
  config.browser_user_agent = user_agent
  for i in links:
    try:
      page = Article(i,config=config)
      #article = Article(i, language="en")
      page.download() 
      page.parse() 
      page.nlp()
      summary+=page.text
    except:
      print("The Website cannot be accessed") 
  
  return summary

def retreving_coordinates(cities):
  geolocator = Nominatim(timeout=2,user_agent="Accidento")
  coordinate=[]
  lat_lon = []
  for city in cities: 
      try:
          location = geolocator.geocode(city)
          if location:
              print(location.latitude, location.longitude)
              coordinate.append([location.latitude, location.longitude])
              lat_lon.append(location)
      except GeocoderTimedOut as e:
          print("Error: geocode failed on input %s with message %s",(city, e))
  

  coordinate_df = pd.DataFrame(coordinate, columns = ['latitude','longitude'])
  coordinate_df['names'] = cities

  return coordinate_df

def map_plot(coordinate_df,continent):
  data = go.Scattergeo(lon = coordinate_df['longitude'], lat = coordinate_df['latitude'],text = coordinate_df['names'],
          marker = dict(symbol = 'star',size=12,colorscale = 'plasma'),
          mode = 'markers')
          
  layout = dict(title = 'Accidents',
                geo_scope = continent.lower()
              )
  choromap = go.Figure(data = [data],layout = layout)
  return to_html(choromap)



def Google_search(place):
  # to search
  query = "Recent accidents in" + place
  links=[]
  for j in search(query, tld='com', num=15, stop=15, lang='en'):
      links.append(j)
  print(links)
  return links

def Word_cloud(ctr):
  wc = WordCloud(background_color="white",width=750,height=750, max_words=10,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(ctr)
  plt.axis('off')
  plt.imshow(wc)
  plt.savefig('static/wc.png')
