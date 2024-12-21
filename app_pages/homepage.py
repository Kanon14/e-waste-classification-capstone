import streamlit as st

# Main Content
st.title("♻️:rainbow[E-Waste Detection Project]♻️")
st.header("An AI-driven solution to address the global e-waste crisis")
st.write("")
st.subheader("📜 About This Project")
st.write(
        """
        The **E-Waste Detection Project** leverages cutting-edge **AI and computer vision models** 
        to automate the sorting and detection of e-waste components. By improving recycling efficiency 
        and reducing human exposure to hazardous materials, this project provides a step toward 
        a **cleaner, healthier, and more sustainable future**.
        """
    )
st.write(
        """
        Use the sidebar to explore the following sections:
        - 👤 **Learn About Me**: Discover the creator behind this project.
        - 🌍 **Understand the E-Waste Problem**: Explore the challenges and impacts of e-waste globally.
        - 🤖 **E-Waste Detection Application**: Test the AI-based detection model in action.
        - 🤖 **Chatbot**: Talk with Wall-E to learn more about e-waste.
        """
    )

st.info("💡 **Start exploring now!** Select a page from the sidebar to get started.")
st.write("**Let's make the world cleaner, smarter, and greener together! 🌱**")
st.image("static/assets/e-waste-recycling.jpg", use_container_width=True)
