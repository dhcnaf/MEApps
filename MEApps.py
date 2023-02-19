import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image

import numpy as np
import cv2
from st_aggrid import AgGrid
import plotly.express as px
import io
import pandas as pd


# "with" notation
with st.sidebar:    
    choose = option_menu("App Gallery", ["Dashboard", "Machine", "Schedule", "Message"],
                       icons=['speedometer','gear','kanban','envelope'],
                       menu_icon="app-indicator", default_index=0,
                       styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
     }
   )
   #if st.button('Dashboard'):
    #    st.write('DASHBOARD')
     #   st.title("DASHBOARD")

  # if st.button('Machine'):
   #     st.write('MACHINE') 
  # if st.button('Schedule'):
   #     st.write('SCHEDULE')
   #if st.button('Message'):
   #     st.write('MESSAGE')     
   #else:
   #     st.write('Choose View')

#with st.sidebar:
 #   choose = option_menu("App Gallery", ["Dashboard", "Machine", "Project Planning", "Message"],
  #                       icons=['speedometer', 'gear', 'kanban', 'envelope'],
   #                      menu_icon="app-indicator", default_index=0,
    #                     styles={
     #   "container": {"padding": "5!important", "background-color": "#fafafa"},
      #  "icon": {"color": "orange", "font-size": "25px"}, 
       # "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "#02ab21"},
   # }
   # )