import streamlit as st

# Main Content
st.title("♻️:rainbow[E-Waste Detection Project]♻️")
st.header("An AI-driven solution to address the global e-waste crisis")
st.write("")
st.subheader("📜 About This Project")
st.write(
        """
        The **:green[E-Waste Detection Project]** leverages cutting-edge **:orange[AI]** and **:orange[computer vision]** models 
        to automate the sorting and detection of e-waste components. By improving recycling efficiency 
        and reducing human exposure to hazardous materials, this project provides a step toward 
        a **:green[cleaner, healthier, and more sustainable future]**.
        """
    )
st.write(
        """
        Use the :gray-background[sidebar] to explore the following sections:
        - 👤 **:gray-background[Learn About Me: ]** Discover the creator behind this project.
        - 🌍 **:gray-background[Understand the E-Waste Problem: ]** Explore the challenges and impacts of e-waste globally.
        - 📂 **:gray-background[E-Waste Dataset: ]** Discover the dataset used by this project.
        - 🤖 **:gray-background[E-Waste Detection Application: ]** Test the AI-based detection model in action.
        - 🤖 **:gray-background[Chatbot: ]** Talk with Wall-E to learn more about e-waste.
        """
    )

st.info("💡 **Start exploring now!** Select a page from the sidebar to get started.")
st.write("**Let's make the world cleaner, smarter, and greener together! 🌱**")
st.image("static/assets/e-waste-recycling.jpg", use_container_width=True)
