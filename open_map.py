import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("GHG Merkezi CO2 Haritasi")

latitude = 0  
longitude = 0  
zoom_start = 2  

m = folium.Map(location=[latitude, longitude], zoom_start=zoom_start, tiles=None)  

tile_url = "https://earth.gov/ghgcenter/api/raster/searches/66188a19a80c7f68a5bfa71f60026713/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=xco2&colormap_name=magma&rescale=412%2C422"

folium.TileLayer(
    tiles=tile_url,
    attr='GHG Merkezi API',
    name='GHG CO2 Tiles',
    overlay=True,
    control=True,
    max_zoom=3,
    min_zoom=0,
    tile_size=256
).add_to(m)

folium.TileLayer(
    tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',  
    attr='OpenStreetMap',
    name='OpenStreetMap Saydam',
    overlay=True,
    control=True,
    max_zoom=6,
    opacity=0.3
).add_to(m)

st_data = st_folium(m, width=800, height=600)
