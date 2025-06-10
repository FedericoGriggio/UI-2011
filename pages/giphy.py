import streamlit as st
import numpy as np
import pandas as pd
import requests
import json

st.write("### __*[API docs](https://developers.giphy.com/docs/api/endpoint#search)*__")

with st.form(key='Form for gif search'):

    search_text = st.text_input('Text to search 🔍', value='Cheeseburger')

    st.form_submit_button('Search!')

def get_gif(search_text,  limit=50):
    base_url = "https://api.giphy.com/v1/gifs/search"
    params = {
        "q": search_text,
        "api_key": st.secrets.section.api_key,
        "limit": limit
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    easy_to_read_data = json.dumps(data, indent=4)
    # uncomment to inspect json response:
    # print('🔎 '*5)
    # print(easy_to_read_data)
    # print('🔎 '*5)

    if data["data"]:
        gif_url = data["data"][np.random.randint(0,49)]["images"]["original"]["url"]
        return gif_url
    else:
        return None

if search_text:
    gif_url = get_gif(search_text)

    if gif_url:
        # st.success(f"Here's a GIF for '{search_text}':")
        st.image(gif_url, caption=search_text)
    else:
        st.warning("No GIF found for the given search text.")
