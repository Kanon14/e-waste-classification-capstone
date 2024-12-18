import streamlit as st

# Page Setup
homepage = st.Page(
    page="app_pages/homepage.py", 
    title="Welcome to the Project",
    icon="👋",
    default=True
)

about_me_page = st.Page(
    page="app_pages/about_me.py", 
    title="About Me",
    icon="👤",
)

ewaste_problem_page = st.Page(
    page="app_pages/ewaste_problem.py", 
    title="Global E-Waste Problem", 
    icon="🌍",
)

detection_app_page = st.Page(
    page="app_pages/detection_app.py", 
    title="E-Waste Detection Application",
    icon="🤖",
)

chatbot_page = st.Page(
    page="app_pages/chatbot.py", 
    title="E-Waste Chatbot",
    icon="🤖",
)

# Navigation Setup
pg = st.navigation(
    {
        "Home": [homepage],
        "Information": [about_me_page, ewaste_problem_page],
        "Projects": [detection_app_page, chatbot_page],
    }
)

# Share on All Pages
st.logo("static/assets/ewp-logo-dashed.webp", size="large")
st.sidebar.text("Created by 🎧 Kanon14")

# Run Application
pg.run()