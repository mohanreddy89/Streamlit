from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="My webpage", page_icon=":fountain_pen:", layout="wide")
st.sidebar.title("PORTFOLIO")
## check box 
checkbox = st.sidebar.checkbox("ARE YOU INTERESTED TO KNOW ABOUT ME")
if checkbox:
    selectbox = st.sidebar.selectbox("selectbox",["ABOUT ME","PROJECTS"])
    button = st.sidebar.button("SUBMIT")
else:
    st.sidebar.warning("Checkbox not selected")
##slider = st.sidebar.slider("slider",0,50,100)##
## selection box 
##selectbox = st.sidebar.selectbox("selectbox",["ABOUT ME","PROJECTS"])
##button = st.sidebar.button("SUBMIT")
## checking whether the checkbox is activated 
##if checkbox:
    ##st.write("checkbox is selected")
##else:
   ## st.write("checkbpx is not selected")
##st.write("selectbox:",selectbox)
## -------- #####
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ----- load assess ----- #
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_XMTduDVODZ.json")
image_contact_form = Image.open("images/images.png")
image_content_form = Image.open("images/png-clipart-cloud-analytics-big-data-data-analysis-cloud-computing-cloud-computing-business-data.png")
## ----Header section---- ## 
st.subheader("Hi, I am Sai Mohan")
st.title("An Aspiring Business Analyst")
st.write("As an aspiring business analyst, I am eager to leverage my analytical skills and business acumen to uncover insights, drive informed decision-making, and contribute to the success of organizations by translating data into actionable strategies.")
st.write("[Know More>](https://github.com/mohanreddy89)")
## ---- What I do ----##
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write("""   
        
        1]Data Collection and Preparation: Gathering and ensuring the quality of data from various sources.

        2]Exploratory Data Analysis: Understanding data patterns and characteristics through descriptive statistics and visualizations.

        3]Model Development: Building machine learning or statistical models for analysis and prediction.

        4]Feature Engineering: Creating or transforming features to improve model performance.

        5]Model Evaluation and Validation: Assessing model performance using evaluation metrics and validation techniques.

        6]Visualization and Reporting: Presenting insights and findings through visualizations and reports.
 """)
        st.write("[Know More>](https://www.linkedin.com/in/amukantisaimohan)")
with right_column:
    st_lottie(lottie_coding,height=400,key="coder")
# ----- Projects ----- #
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    ## ---- image cloumn ----- ##
    with image_column:
        st.image(image_contact_form)
    with text_column:
        st.subheader("Exploratory Data Analysis")
        st.write("""
        1] EDA involves analyzing and summarizing data to understand its key characteristics and gain insights.

        2]It helps in identifying data quality issues, missing values, outliers, and inconsistencies.

        3]EDA includes calculating descriptive statistics such as mean, median, mode, standard deviation, and quartiles.
        
        4]Visualizations such as histograms, box plots, scatter plots, and bar charts are used to understand data distributions and relationships.
        
        5]EDA explores patterns, trends, and correlations in the data to generate hypotheses or guide further analysis.
        
        6]It involves examining categorical variables, including frequency tables and bar plots, to understand the distribution of categories.""")

        st.markdown('[watch video>](https://www.youtube.com/watch?v=xi0vhXFPegw)')

# ----- 2nd project ------ #
with st.container():
    st.write("----")
    image_column,text_column = st.columns((1,2))
    ## ---- image cloumn ----- ##
    with image_column:
        st.image(image_content_form)
        st.write("##")
        st.image(image_content_form)
        st.write("##")
        st.image(image_content_form)
    with text_column:
        st.subheader("Visualisations")
        st.write("""
        1]Bar Charts: Used to compare categorical data by representing categories as bars with lengths proportional to the values they represent.
        
        2]Line Charts: Depict trends and patterns by connecting data points with lines, commonly used for time series or continuous data.
        
        3]Scatter Plots: Display the relationship between two variables by plotting individual data points on a two-dimensional plane.
        
        4]Pie Charts: Show the proportion or percentage distribution of categorical data by dividing a circle into sectors.
        
        5]Histograms: Represent the distribution of continuous or numerical data by dividing it into bins and displaying the frequency or count within each bin.
        
        6]Heatmaps: Visualize data in a matrix form using colors to represent values, often used for displaying correlation or clustering.
        
        7]Box Plots: Display the summary statistics (median, quartiles, outliers) of a dataset, providing insights into its distribution and identifying potential anomalies.
        
        8]Area Charts: Similar to line charts, but the area below the line is filled, making it useful for comparing cumulative or stacked data.
        
        9]Bubble Charts: Show relationships between three variables by representing data points as bubbles with different sizes or colors.
        
        10]Treemaps: Display hierarchical data using nested rectangles, where the size of each rectangle represents a specific value.
        
        11]Geospatial Maps: Present data on maps, allowing for visualizing patterns and relationships based on geographic locations.
         """)

        st.markdown('[watch video>](https://www.youtube.com/watch?v=a9UrKTVEeZA)')
st.write("----")
st.write("##")
st.header("Get in contact with me...")

email = st.text_input("Enter your email")
form_action = f"https://formsubmit.co/{email}"

contact_form = f""" 
<form action="{form_action}" method="POST">
     <input type="text" name="name" placeholder="your name" required>
     <br></br>
     <input type= "text" message="message" placeholder="Your meassage here" required>
     <br></br>
     <button type="submit">Send</button>
</form>

"""
st.markdown(contact_form,unsafe_allow_html=True)