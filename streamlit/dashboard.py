import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Sample Superstore!!!", page_icon=":bar_chart:", layout="wide")

st.title(" :bar_chart: Superstore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\confidence\Desktop\streamlit")
    df = pd.read_csv("SuperStoreUS.csv", encoding="ISO-8859-1") 

col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

#getting the min and max date
startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Start date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("End date", endDate)) 

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy() 

st.sidebar.header("Choose your filter: ")

#create for region
region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)] 

# Create for state
state = st.sidebar.multiselect("Pick the State", df2["State or Province"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State or Province"].isin(state)]

# create for city 
city = st.sidebar.multiselect("Pick the City", df2["City"].unique())

# filter the data based on Region, State and City 

if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]    
elif not region and not city:
    filtered_df = df[df["State or Province"].isin(state)]
elif state and city:
    filtered_df = df3[df["State or Province"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]
elif city:
    filtered_df = df3[df3["city"].isin(city)]
else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]

category_df = filtered_df.groupby(by = ["Product Category"], as_index= False)["Sales"].sum()

with col1:
    st.subheader("Product Category wise sales")
    fig = px.bar(category_df, x = "Product Category", y = "Sales", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]],
                template = "seaborn")
    st.plotly_chart(fig,use_container_width=True, height = 200)

with col2:
    st.subheader("Region wise Sales")
    fig = px.pie(filtered_df, values= "Sales", names = "Region", hole = 0.5)
    fig.update_traces(text = filtered_df["Region"], textposition = "outside")
    st.plotly_chart(fig, use_container_width=True)    


# Previous code...

col1, col2 = st.columns(2)
with col1:
    with st.expander("Product Category_ViewData"):
        st.write(category_df.style.background_gradient(cmap="Blues"))
        csv = category_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Product Category.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

with col2:
    with st.expander("Region_ViewData"):
        region = filtered_df.groupby(by="Region", as_index=False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap="Oranges"))
        csv = region.to_csv(index=False).encode('utf-8')
        st.download_button("Download Data", data=csv, file_name="Region.csv", mime="text/csv",
                           help='Click here to download the data as a CSV file')

# Ensure proper indentation for the rest of your code...

filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
st.subheader('Time Series Analysis')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y="Sales", labels={"Sales": "Amount"}, height=500, width=1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data= csv, file_name= "TimeSeries.csv", mime='test/csv')

# create a treemap based on region,product category, sub category
st.subheader("Hierarchical view of Sales using Treemap")
fig3 = px.treemap(filtered_df, path= ["Region", "Product Category", "Product Sub-Category"], values= "Sales", hover_data= ["Sales"],
                  color = "Product Sub-Category")
fig3.update_layout(width = 800, height = 650)
st.plotly_chart(fig3, use_container_width=True)  

chart1, chart2 =  st.columns(2)
with chart1:
    st.subheader('Customer Segment wise Sales')
    fig = px.pie(filtered_df, values= "Sales", names= "Customer Segment", template= "plotly_dark")
    fig.update_traces(text = filtered_df["Customer Segment"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader('Product Category wise Sales')
    fig = px.pie(filtered_df, values= "Sales", names= "Product Category", template= "gridon")
    fig.update_traces(text = filtered_df["Product Category"], textposition = "inside")
    st.plotly_chart(fig, use_container_width=True)

import plotly.figure_factory as ff
st.subheader(":point_right: Month wise Product Sub-Category Sales Summary")  
with st.expander("Summary_Table"):
    df_sample = df[0:5][["Region","State or Province","City","Product Category","Sales","Profit","Quantity ordered new"]] 
    fig = ff.create_table(df_sample, colorscale= "cividis") 
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("Month wise Sub-Category Table")
    filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
    sub_category_Year = pd.pivot_table(data = filtered_df, values= 'Sales', index= ["Product Sub-Category"],columns= "month")
    st.write(sub_category_Year.style.background_gradient(cmap="Blues"))


# Create a scatter plot
data1 = px.scatter(filtered_df, x= "Sales", y="Profit", size="Quantity ordered new")
data1['layout'].update(title="Relationship between Sales and profits using Scatter Plot.",
                       titlefont = dict(size=20), xaxis = dict(title="Sales", titlefont=dict(size=19)),
                       yaxis = dict(title = "Profit", titlefont = dict(size=19))
                       )
st.plotly_chart(data1, use_container_width=True)  

with st.expander("View data"):
    st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

# download original dataset
csv = df.to_csv(index=False).encode('utf-8')
st.download_button('Download Data', data = csv, file_name= "Data.csv", mime = "text/csv")        
  



