import streamlit as st
import requests as r

apikey = "6yzaYdk9Ep9IR3OLhPfbSiRvRrvzzXcPbTyuv7F4"
url = "https://api.nasa.gov/planetary/apod?api_key=6yzaYdk9Ep9IR3OLhPfbSiRvRrvzzXcPbTyuv7F4"

re = r.get(url)
content = re.json()

title = content["title"]

st.title("Astronomy Picture Of the Day!")
st.header(title)

imgurl = content["url"]
response = r.get(imgurl)

with open("image.jpg", "wb") as file:
    file.write(response.content)

st.image("image.jpg")

st.write(content["explanation"])