import streamlit as st

st.title("Machine Learning Project")

from PIL import Image

img = Image.open("art1.jpg")
# st.image(Img)
st.image(img, width=300, caption="Simple image")

#video adding
vid = open("pick.mp4", "rb")
vidbyte = vid.read()
st.video(vidbyte)

#audio adding
audio_file = open("Lorde.mp3", "rb").read()
st.audio(audio_file)

#checkbox
#ML (Gender, M/F)
if st.checkbox("Show / hide"):
    st.text("Showing or hiding widget")

    #Radio button
status = st.radio("What is your status", ("Active", "Inactive"))

# Link with some function
# if status == 'Active':
#     st.success("You are active")

# Else function
if status == 'Active':
    st.success("You are active")
else:
    st.warning("You are inactive, activate it")  

# Selectbox
occupation = st.selectbox("Your occupation", ["Programmer", "Data scientist", "Lawyer", "Entrepreneur"])
st.write("You selected this option", occupation)

#india, china, USA

#Multiselect

location = st.multiselect("Where do you work", ('Delhi', 'Mumbai', 'Karnat', 'Bombay'))

# To get all selected count
st.write("You selected", len(location), "locations")

#Slider
level = st.slider("what is your level", 1,5)

# Buttons
st.button("simple button")
if st.button("About"):
    st.text("Streamlit is cool!")

if st.button("Submit"):
    st.text("Submitted successfully") 

# text input
first_name = st.text_input("Enter your first name", "Type here...")
if st.button("Submit", key="1"):
    result = first_name.title()
    st.success(result)

# Text area
message = st.text_area("Enter your message", "Type here...")
if st.button("Submit", key="2"):
    result = message.title()
    st.success(result)

# Data Input
import datetime
today = st.date_input('Today is', datetime.datetime.now())

# Time
the_time = st.time_input('The time is', datetime.time())

##Display json output
st.text("Display json Data")
st.json({"Name":"Shivan",
        "Gender":"Male"})  

#Import numpy as np
st.text("Display Row Code")
st.code("import numpy as np") 

#Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame

# Progress bar

import time
my_bar = st.progress(0)  
for p in range(10):
    my_bar.progress(p + 10)

#Spinner

with st.spinner("Waiting.."):
    time.sleep(5)
st.success("Finished")          
