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
loc=list(data.keys())

latlong=ast.literal_eval(st.secrets["coordinates"])


for i in loc:
    folium.Marker(latlong[i],popup=data[i],tooltip=i).add_to(m)

folium_static(m,width=550,height=850)
