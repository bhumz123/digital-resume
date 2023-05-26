from pathlib import Path

import streamlit as st 
from PIL import Image

currect_dir= Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file= currect_dir / "style" / "main.css"
resume_file= currect_dir / "assets" / "bhumi.pdf"
profile_pic= currect_dir / "assets" / "picture.png.jpeg"

PAGE_TITLE = " Digital CV | Bhumika Rana"
PAGE_ICON = ":wave:"
Name = "Bhumika Rana"
DESCRIPTION = """ 
Machine Learning and Data Science enthusiast. 
"""
EMAIL = "bhumikarana983@gmail.com"
SOCIAL_MEDIA = {
    "GITHUB":  " https://github.com/bhumz123",
    "LINKEDIN": "https://www.linkedin.com/in/bhumika-rana-64a50222a/",
    "TWITTER": " https://twitter.com/ranabhumika09"
}

PROJECTS = {
    "  🎗 House Pricing- ML model that predicts house prices.":"https://github.com/bhumz123/Machine-Learning/tree/main/linear%20regression",
    "  🎗 SDE SALARY Prediction- A webiste that predicts the salary of SDE's of different countries":"https://github.com/bhumz123/salary-prediction-website",
    "  🎗 Credit Card Fraud Detetction- Ml model that detects about the false ":"https://github.com/bhumz123/Fraud-detection",
    "  🎗Virtual Mouse- Mouse control through hands": "https://github.com/bhumz123/opencv",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open (css_file)as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic= Image.open(profile_pic)


col1,col2= st.columns(2,gap="small")
with col1:
  st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )   
    st.write("Ⓜ️", EMAIL)



st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


st.write("#")
st.subheader("Experience and Qualifications")
st.write(
    """
    - ✅ 2 years experience extracting actionable insights from data
    - ✅ 1 year experience in Machine Learning 
    - ✅ Strong hands on experience and knowledge in python
    - ✅ Good understanding of Data Structures & Algorithms
    - ✅ Clear understanding of statistical principles and their applications
    - ✅ Excellent team player and displaying strong initiative on tasks
    """
)

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    -  💻 Programming : Python ( Scikit Learn , Pandas , Numpy , Streamlit , Keras , Tensorflow , NLP , Open CV) , Java
    -  📊 Data Visualisation : Seaborn , PowerBI , Excel , Matplotlib , Plotly
    -  📼 Machine Learning & Data Science
    -  📚 Databases : SQL , Mongo DB , Postgres

    """
)

st.write("#")
st.subheader("Work History")
st.write("👩‍💻 Software Developer Intern || Medoc ")
st.write(" Time Period : 1/12/2022 - 31/05/23")
st.write(
    """
    - ➔ Verbally communicated product vision and strategy.
    - ➔ Led team in designing and building features to support business goals. 
    - ➔ Defined, tracked, and reported on key metrics to measure success.
    - ➔ Facilitated team meetings and resolved conflicts.


    """
)


st.write("#")
st.subheader("Projects")
st.write("-----")
for projects, links in PROJECTS.items():
    st.write(f"[{projects}]({links})")