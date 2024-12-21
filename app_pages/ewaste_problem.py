import streamlit as st

# Page Title
st.title("Grasping the Global E-Waste Crisis!")

# Introduction Section
st.image("static/assets/e-waste.jpg", use_container_width=True, caption="The Global E-Waste Crisis")

st.write("""
E-waste, or electronic waste, refers to discarded electrical or electronic devices. 
It is one of the **fastest-growing waste streams globally**, posing significant environmental and health risks due to improper disposal and lack of recycling efforts.

With the rise of **consumer electronics** and **technology advancements**, the e-waste problem is becoming increasingly critical to address.
""")

# Visual Representation: Global E-Waste Trend
st.subheader("📈 Global E-Waste Generation Over Time")
st.image("static/assets/global-e-waste-generated.jpg", use_container_width=True, 
         caption="E-Waste Generation and Recycling Trends: 2010-2030 [1]")

st.write("""
The chart above illustrates the **growing scale of e-waste generation** and the gap in recycling rates over the past decade. Without immediate action, global e-waste could reach unsustainable levels, further harming the environment.
""")

# Key Facts Section
st.subheader("📊 Key Facts about E-Waste")
st.markdown("""
- **50+ million tons** of e-waste are generated globally every year.  
- Only **20%** of e-waste is formally recycled; the remaining 80% is either dumped, incinerated, or improperly handled.  
- E-waste contains **hazardous materials** such as:
   - 🧪 **Lead**, which can cause brain damage.  
   - 🧪 **Mercury**, which affects the nervous system.  
   - 🧪 **Cadmium**, which damages kidneys and bones.  
- Informal or manual sorting of e-waste is often performed under unsafe conditions, particularly in developing countries.
""")

# Why is E-Waste Dangerous? Section
st.subheader("⚠️ Why is E-Waste Dangerous?")
st.write("""
E-waste contains a mix of **valuable** and **hazardous** materials. When not disposed of properly, it causes:
1. **Environmental Pollution**:
   - Chemicals leach into the soil, contaminating water and food sources.
2. **Health Risks**:
   - Exposure to toxins causes severe health problems such as brain damage, respiratory issues, and cancer.
3. **Resource Wastage**:
   - Precious metals like **gold**, **silver**, and **copper** in e-waste are lost instead of being recycled.

These issues disproportionately affect developing nations, where e-waste is often processed manually under unsafe conditions [2].
""")

# Visual: Manual Sorting
st.image("static/assets/e-waste-worker-unsafe.png", use_container_width=True, 
         caption="Manual Sorting of E-Waste in Unsafe Environments")

# The Solution Section
st.subheader("🛠️ How Can Technology Solve the E-Waste Problem?")
st.write("""
Advanced technologies such as **Artificial Intelligence (AI)** and **Computer Vision** can play a transformative role in addressing the e-waste problem by:
- Automating the **sorting and classification** of e-waste items.
- Improving recycling efficiency by reducing **manual labor risks**.
- Identifying **reusable** and **recyclable** components more effectively.

AI-driven solutions, like the **E-Waste Detection Application** in this project, are a step toward creating a sustainable future.
""")

# Call to Action
st.info("""
🔍 Explore the **E-Waste Detection Application** to see how AI can automate e-waste classification and contribute to solving this global challenge!
""")

# References
st.write("")
st.subheader("📚 References:")
st.write("[1] [Global E-Waste Monitor 2024](https://ewastemonitor.info/wp-content/uploads/2024/12/GEM_2024_EN_11_NOV-web.pdf)")
st.write("[2] [WHO: E-Waste](https://www.who.int/news-room/fact-sheets/detail/electronic-waste-(e-waste))")
st.write("[3] [The Growing Environmental Risks of E-Waste](https://www.genevaenvironmentnetwork.org/resources/updates/the-growing-environmental-risks-of-e-waste/)")