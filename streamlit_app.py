import streamlit as st

# Page Setup
homepage = st.Page(
    page="pages/homepage.py", 
    title="Welcome to the Project",
    icon="👋",
    default=True
)

about_me_page = st.Page(
    page="pages/about_me.py", 
    title="About Me",
    icon="👤",
)

ewaste_problem_page = st.Page(
    page="pages/ewaste_problem.py", 
    title="Global E-Waste Problem", 
    icon="🌍",
)

detection_app_page = st.Page(
    page="pages/detection_app.py", 
    title="E-Waste Detection Application",
    icon="🤖",
)

# Navigation Setup
pg = st.navigation(
    {
        "Home": [homepage],
        "Info": [about_me_page, ewaste_problem_page],
        "Projects": [detection_app_page],
    }
)

# Share on All Pages
st.logo("static/assets/images.ico")
st.sidebar.text("Created by 🎧 Kanon14")

# Run Application
pg.run()