import streamlit as st


# HERO SECTION
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image("static/assets/profile-pic.png", width=230)

with col2:
    st.title("Chua Jingxuan | (Kanon14)", anchor=False)
    st.write(
        """
        Data Visualization, Computer Vision, AI, and LLM Enthusiast 
        with a passion for solving real-world problems.
        """
    )

# EXPERIENCE & QUALIFICATIONS
st.write("\n")
st.subheader("🔹 Experience & Qualifications", anchor=False)
st.write(
    """
    - ✅ Over 3 years of experience in **Data Science** and **AI Applications**.
    - ✅ Strong foundation in **Computer Vision** and **Large Language Models**.
    - ✅ Built and deployed end-to-end **Machine-Learning** and **Deep-Learning** projects.
    - ✅ Proficient in **data storytelling** and creating interactive visualizations for actionable insights.
    """
)

# HARD SKILLS
st.write("\n")
st.subheader("🔧 Hard Skills", anchor=False)
st.write(
    """
    - **Programming Languages**: Python, SQL
    - **Libraries & Frameworks**: TensorFlow, PyTorch, OpenCV, Ultralytics, Langchain
    - **Data Visualization**: Tableau, Matplotlib, Seaborn, Power BI, Plotly
    - **Tools & Platforms**: Jupyter Notebook, Google Colab, Ollama
    - **Web Development**: Flask, Streamlit
    - **Version Control**: Git, GitHub, GitLab
    """
)

# CONNECT WITH ME
st.write("\n")
st.subheader("🔗 Connect with Me", anchor=False)
st.write("Feel free to connect with me on the following platforms:")

# Create three columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/chua-jingxuan-51a300173")
with col2:
    st.link_button("💻 GitHub", "https://github.com/Kanon14")
with col3:
    st.link_button("📧 Email", "mailto:geochua144@gmail.com")
