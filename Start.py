import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Dana Schnekenburger (schned06@students.zhaw.ch)
- Katarina Djuric (djurikat@students.zhaw.ch)   

Unsere App unterstützt Menschen mit AD(H)S dabei, ihren Alltag strukturierter zu gestalten. Sie bietet einen Wochenplaner, To-Do-Listen und hilfreiche Tipps für eine bessere Organisation. Gleichzeitig hilft sie auch Angehörigen und Freunden, AD(H)S besser zu verstehen, iindem sie praktische Ratschläge und Einblicke vermittelt.
"""

from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_ADHS")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_app_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )