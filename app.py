import datetime
import folium
import geopandas as gpd
import geopy
import networkx as nx
import joblib
import osmnx as ox
# import pickle
import shapely.wkt
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import time
import base64
from folium.features import DivIcon
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Nakagawa Dashboard for Safest Path during Earthquakes",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FA8072 ">Nakagawa Dashboard for Safest Path </h1>',
                    unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("Home", "About", "Features", "Safest Path", "Visualizations", "Conclusion", "Team")
)

if add_selectbox == 'Home':
    
    LOGO_IMAGE = "Images/omdena_japan_logo.jpg"
    
    st.markdown(
          """
          <style>
          .container {
          display: flex;
        }
        .logo-text {
             font-weight:700 !important;
             font-size:50px !important;
             color: #f9a01b !important;
             padding-top: 75px !important;
        }
        .logo-img {
             float:right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
          f"""
          <div class="container">
               <img class="logo-img" src="data:image/jpg;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
          </div>
          """,
          unsafe_allow_html=True
    )
    
    st.subheader('PROBLEM STATEMENT')
    
    st.markdown('Natural Disasters are problems in Japan, with risk of earthquakes, floods and tsunamis. Japan has well-developed \
        disaster response systems, but densely populated cities and narrow roads make managing the response difficult. By giving \
            individuals information about the safest ways from their homes and places of work, it will increase their awareness of \
                the surrounding area and improve their preparedness.', unsafe_allow_html=True)

elif add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Project Goals</h4>', unsafe_allow_html=True)
    st.markdown('• collect satellite images and identify road characteristics', unsafe_allow_html=True) 
    st.markdown('• build a model for scoring the roads in terms of their suitability for use in emergency', unsafe_allow_html=True) 
    st.markdown('• build a pathfinding model from A to B, combining it with road characteristics', unsafe_allow_html=True) 
    st.markdown('• suggest safest path from A to B', unsafe_allow_html=True) 
    st.markdown('• publish interactive dashboards to display road characteristics and safest paths', unsafe_allow_html=True) 
    st.markdown('• arrange demonstration and publicise to local audiences', unsafe_allow_html=True) 
    
    st.markdown('<h4>Location Choosen</h4>', unsafe_allow_html=True)
    st.markdown('We had choosen "Nakagawa-Ku as our region of interest, which comes under Aichi prefecture of Nagoya City. It comes under Chubu region and \
        is the 4th densely populated city in Japan with high risk prone to disasters.',
                unsafe_allow_html=True)
    
    st.markdown('<h4>Developments Made</h4>', unsafe_allow_html=True)
    st.markdown('We had designed a model collecting data about the local roads from satellite images, classify them and indicate the safest \
        route to be taken from point A to point B and an interactive dashboard to display the safest route in a map.',
                unsafe_allow_html=True)
    st.markdown('By making individuals aware, it will improve their preparedness and it can be used within families to prepare disaster \
        response plans, depending on their circumstances. To be used by individuals, families and groups, and foreign residents who may \
            not understand local information. Further development will be covering more geographical areas and publicising on a local level.'
                , unsafe_allow_html=True)
    
elif add_selectbox == 'Features':

    st.subheader('PROJECT ENDORSEMENTS')

    st.markdown('• Safest route path to take at occurences of japan disasters', unsafe_allow_html=True)
    st.markdown('• Locates shelters in Nakagawa Ward - Earthquakes, Tsunamis and Floods', unsafe_allow_html=True)
    st.markdown('• Visualizations to Check and Differentiate Parameters across the Nakagawa Ward', unsafe_allow_html=True)
    
elif add_selectbox == 'Visualizations':
    
    st.subheader('PROJECT VISUALIZATIONS')
    st.markdown('<h4>Japan Earthquake Zoning Areas</h4>', unsafe_allow_html=True)
    st.image("Images/Japan_Earthquakes_Zoning.png", width=500)
    st.markdown('<h4>Nakagawa Shelter Maps</h4>', unsafe_allow_html=True)
    st.image("Images/Nakagawa_Shelter_Maps.png", width=500)
    st.markdown('<h4>Nakagawa Building Density Score</h4>', unsafe_allow_html=True)
    st.image("Images/Nakagawa_Building_Density_Score.png", width=500)
    st.markdown('<h4>Nakagawa Distance Risk Score</h4>', unsafe_allow_html=True)
    st.image("Images/Nakagawa_Distance_Risk_Score.png", width=500)
    
elif add_selectbox == 'Conclusion':
    
    st.subheader('PROJECT SUMMARY')

    st.markdown('Write Project Summary here', unsafe_allow_html=True) 
    
    st.subheader('CONCLUSION')
    
    st.markdown('Write Conclusion here', unsafe_allow_html=True)
        
elif add_selectbox == 'Team':
    
    st.subheader('COLLABORATORS')

    st.markdown('<a href="https://www.linkedin.com/in/mkmanolova/">Monika Manolova</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/prathima-kadari/">Prathima Kadari</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/armielyn-obinguar-9229561b0/">Armielyn Obinguar</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/rhey-ann-magcalas-47541490/">Rhey Ann Magcalas</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/avinash-mahech/">Avinash Mahech</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/deepali-bidwai/">Deepali Bidwai</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/shalini-gj-6a006712/">Shalini GJ</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/pawan-roy123">Pawan Roy Choudhury</a>',
                unsafe_allow_html=True)
    st.markdown('<a href="https://www.linkedin.com/in/ahmedgaal/">Ahmed Gaal</a>',
                unsafe_allow_html=True)

    st.subheader('PROJECT MANAGER')

    st.markdown('<a href="https://www.linkedin.com/in/galina-naydenova-msc-fhea-b89856196/">Galina Naydenova</a>', unsafe_allow_html=True)
                
