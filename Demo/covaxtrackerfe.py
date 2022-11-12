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

header=st.container()

with header:
    txt, mp = st.columns([2,1])
    with txt:
        st.header("CovaxTracker")
        st.subheader("Get Telegram alerts on COVID-19 Vaccine availability in your locality")
        st.subheader("Notifications provide you information on:")
        st.text("Address of Vaccination center")
        st.text("Center ID")
        st.text("Age group(18+ or 45+)")
        st.text("Fee Type")
        st.text("Number of doses available")
        st.subheader("To join a channel")
        st.text("Select your location on the map")
        st.text("Open the link on your browser")
        st.text("Click on Join Channel")
        st.subheader("Code")
        st.text("The source code for the bot,automated channel creation and this webpage are available at: ")
        st.write("[https://github.com/VamseeNY/CovaxTracker](https://github.com/VamseeNY/CovaxTracker)")
    with mp:
        folium_static(m,width=550,height=850)
