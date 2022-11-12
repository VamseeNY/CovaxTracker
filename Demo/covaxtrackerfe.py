import folium
import streamlit as st
from streamlit_folium import folium_static
from branca.element import Figure
from geopy.geocoders import Nominatim
import ast

st.set_page_config(layout="wide")

fig=Figure(width=550,height=850)
m=folium.Map(location=[21,80],zoom_start=5,tiles='cartodbpositron')#cartodbdark_matter
fig.add_child(m)

data=ast.literal_eval(st.secrets["fin"])

geolocator = Nominatim(user_agent="MyApp")

latlong={}
n=[]
loc=list(data.keys())
for i in loc:
    location = geolocator.geocode(i)
    try:
        latlong[i]=[location.latitude,location.longitude]
    except AttributeError :
        n.append(i) #use a different engine for these locations


for i in loc:
    folium.Marker(latlong[i],popup=data[i],tooltip=i).add_to(m)

folium_static(m,width=550,height=850)



