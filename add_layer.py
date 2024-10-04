import streamlit as st
import folium
from streamlit_folium import st_folium


st.title("GHG Merkezi CO2 ve CH4 Haritasi")

latitude = 0  
longitude = 0  
zoom_start = 2  

co2 = st.checkbox("CO2 Katmanini Göster", value=True)
ch4 = st.checkbox("CH4 Katmanini Göster", value=False)

m = folium.Map(location=[latitude, longitude], zoom_start=zoom_start, tiles=None)

co2_tile_url = "https://earth.gov/ghgcenter/api/raster/searches/66188a19a80c7f68a5bfa71f60026713/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=xco2&colormap_name=magma&rescale=412%2C422"

ch4_tile_url = "https://earth.gov/ghgcenter/api/raster/searches/ac178c9e3d4f069d1334475c7febad34/tiles/WebMercatorQuad/{z}/{x}/{y}?assets=ensemble-mean-ch4-wetlands-emissions&colormap_name=magma&rescale=0%2C3e-9"

if co2:
    folium.TileLayer(
        tiles=co2_tile_url,
        attr='GHG Merkezi API',
        name='CO2 Tiles',
        overlay=True,
        control=True,
        max_zoom=9,
        min_zoom=0,
        tile_size=256
    ).add_to(m)

if ch4:
    folium.TileLayer(
        tiles=ch4_tile_url,
        attr='GHG Merkezi API',
        name='CH4 Tiles',
        overlay=True,
        control=True,
        max_zoom=9,
        min_zoom=0,
        tile_size=256
    ).add_to(m)

folium.TileLayer(
    tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    attr='OpenStreetMap',
    name='OpenStreetMap Saydam',
    overlay=True,
    control=True,
    opacity=0.5
).add_to(m)

folium.LayerControl().add_to(m)

st_data = st_folium(m, width=800, height=600)
