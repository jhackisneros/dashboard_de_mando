import geopandas as gpd

url = "https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/madrid-districts.geojson"
gdf = gpd.read_file(url)
gdf.to_file("data/distritos_madrid.geojson", driver="GeoJSON")
