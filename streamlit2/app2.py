import streamlit as st

st.title("Happy birthday")

# ballon
st.balloons()

#Sidebar
st.sidebar.header("About")
st.sidebar.text("This is our demo project")

#select box
algorithms = st.sidebar.selectbox("Your algorithm", ["Linear regression", "Logistic regression", "Decision tree", "Random forest"])