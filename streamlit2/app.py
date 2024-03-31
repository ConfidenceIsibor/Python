import streamlit as st

#title
st.title("Machine Learning project")

#header/subheader
st.header("This is a header")
st.subheader("This is a subheader")

#text
st.text("Hello streamlit")

#markdown
st.markdown("# This is our first markdown")

st.markdown("## This is our first markdown")

#error/colorful test
st.success("Successful done")

#Information
st.info('Information')

#warning
st.warning("This is a warning")

#error
st.error("This is an error")

#Exception
st.exception("NameError('name tt is not defined')")

import pandas
st.help(pandas)

#range
st.help(range)


#Writing text super function
st.write("Text with write")

st.write(range(10))

from PIL import Image

Img = Image.open("art1.jpg")
st.image(Img)

