import pandas as pd
import folium
from folium.plugins import MarkerCluster


df = pd.read_csv(r"C:\Users\Abdul Raffay\Desktop\Waze\waze_dataset.csv")


m = folium.Map(location=[3.1390, 101.6869], zoom_start=11, tiles="Esri.WorldImagery")


marker_cluster = MarkerCluster().add_to(m)


for _, row in df.iterrows():
    if row["device"] == "android":
        icon = folium.Icon(color="green", icon="android", prefix="fa")
    elif row["device"] == "iphone":
        icon = folium.Icon(color="blue", icon="apple", prefix="fa")
    else:
        icon = folium.Icon(color="gray", icon="question", prefix="fa")
    
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        icon=icon
    ).add_to(marker_cluster)


folium.Marker(
    location=[3.1390, 101.6869],
    popup="Kuala Lumpur",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)


m.save(r"C:\Users\Abdul Raffay\Desktop\Waze\geographic_map.html")
