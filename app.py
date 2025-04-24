import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Smart Home Dashboard", layout="wide")

# Load external CSS and JS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open("assets/script.js") as f:
    custom_js = f"<script>{f.read()}</script>"
    components.html(custom_js, height=0)

# Title
st.markdown("<h1 class='title'>⚡ Smart Home Dashboard</h1>", unsafe_allow_html=True)

# Wattage Calculator
with st.expander("🔢 Wattage Calculator"):
    watts = st.number_input("Wattage (W)", 0.0)
    hours = st.number_input("Hours Used per Day", 0.0)
    days = st.number_input("Number of Days", 1.0)
    kwh = (watts * hours * days) / 1000
    st.success(f"Estimated Energy Usage: {kwh:.2f} kWh")

# Chatbot
with st.expander("🧠 Chatbot Assistant"):
    query = st.text_input("Ask me anything about your smart home:")
    if query:
        if "usage" in query.lower():
            st.info("Your energy usage this week increased by 7%. Try reducing evening AC usage.")
        elif "save" in query.lower():
            st.info("You can save ~15% energy by scheduling dishwasher and washing machine at non-peak hours.")
        else:
            st.info("I'm still learning. Try asking about 'usage', 'save', or 'efficiency'.")

# Predicted vs Actual Usage Chart
st.markdown("<h3 class='section-title'>📊 Predicted vs Actual Usage</h3>", unsafe_allow_html=True)
st.line_chart({
    "Predicted": [1.2, 1.4, 1.5, 1.3, 1.6],
    "Actual": [1.1, 1.6, 1.4, 1.2, 1.7]
})

# Real-Time Chart
st.markdown("<h3 class='section-title'>📈 Real-Time Energy Usage</h3>", unsafe_allow_html=True)
components.html(open("assets/chart.js", "r").read(), height=400)
