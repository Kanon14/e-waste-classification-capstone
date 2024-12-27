import streamlit as st
import pandas as pd

st.title("📂 Curated E-Waste Dataset")
st.write("Explore the dataset created for this project, designed to enhance research in e-waste detection and classification.")

# Dataset Overview
st.subheader("🔎 Overview")
st.write("""
The **Capstone Kanon E-Waste Dataset** contains over **10,000 images** across **20 categories**, meticulously curated and annotated for object detection tasks. 
This dataset aims to facilitate advancements in computer vision for automating e-waste detection and classification.
""")

st.write("""
**Key Details:**
- **Total Images:** 10,000+
- **Number of Classes:** 20
- **Image Format:** `.jpg` and `.png` with YOLO annotation format.
- **Sources:** Curated from online repositories, synthetic data generation, and personal collection.
- **Intended Use:** Object detection, image classification, and AI model training.
""")

# Dataset Table
st.subheader("📋 Dataset Distribution Table")
data = {
    "Class Name": [
        "vape", "battery", "tv", "light-source", "remote", "usb", "air-cond",
        "fridge", "mouse", "microwave", "printer", "fan", "telephone", 
        "smartphone", "laptop", "audio-set", "keyboard", "pcb", "kettle", "washing-machine"
    ],
    "Total Count": [
        1088, 1068, 988, 891, 808, 715, 705, 689, 663, 649, 647, 633, 633, 
        631, 618, 606, 603, 592, 556, 542
    ],
    "Training Count": [
        877, 859, 784, 700, 643, 574, 576, 551, 510, 528, 527, 500, 491, 
        508, 497, 478, 478, 472, 446, 444
    ],
    "Validation Count": [
        109, 110, 67, 84, 66, 64, 66, 66, 84, 58, 58, 71, 65, 61, 63, 64, 
        62, 54, 55, 47
    ],
    "Test Count": [
        102, 99, 137, 107, 99, 77, 63, 72, 69, 63, 62, 62, 77, 62, 58, 64, 
        63, 66, 55, 51
    ]
}
df = pd.DataFrame(data)

# Display the table with formatting
st.dataframe(df, width=800, height=400)

# Sample Images Section
st.subheader("🖼️ Sample Images")
st.write("Below are some examples of annotated images from the dataset:")
st.image(["static/assets/air-cond.jpg", "static/assets/battery.jpg", "static/assets/laptop.jpg"], 
         caption=["Air Conditioner", "Battery", "Laptop"], 
         use_container_width="auto")

# Link to Roboflow Dataset
st.subheader("🔗 Access the Full Dataset")
st.link_button("Capston-Kanon-2", "https://universe.roboflow.com/computer-vision-learning-touhj/capstone-kanon-2)")

# Terms of Use
st.subheader("⚖️ Terms of Use")
st.markdown("""
This dataset is released under a **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. Proper attribution is required for any research or projects utilizing this dataset.
""")

st.info("For any queries or additional support, feel free to reach out via the **About Me** page.")