import streamlit as st
import streamlit.components.v1 as components
import random

# Set page config
st.set_page_config(layout="wide", page_title="Smart Home Dashboard")

# Load CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">Smart Home Energy Dashboard ⚡</div>', unsafe_allow_html=True)

# ---------- SECTIONS ----------
col1, col2 = st.columns(2)

# Simulated appliance data
appliances = {
    "Dishwasher": 1.5,
    "Furnace 1": 2.0,
    "Furnace 2": 2.2,
    "Home Office": 0.5,
    "Fridge": 0.8,
    "Wine Cellar": 0.4
}

average_cost_per_kw = 5.5  # ₹ per kWh

# ---------- COLUMN 1: Realtime Chart + Predicted vs Actual ----------
with col1:
    st.markdown('<div class="section-title">🔁 Real-Time Energy Usage</div>', unsafe_allow_html=True)
    components.html(open("assets/chart.html").read(), height=400)

    st.markdown('<div class="section-title">📉 Predicted vs Actual</div>', unsafe_allow_html=True)
    st.line_chart({
        "Predicted": [random.uniform(1.0, 3.5) for _ in range(20)],
        "Actual": [random.uniform(1.0, 3.0) for _ in range(20)],
    })

# ---------- COLUMN 2: Calculator + Chatbot ----------
with col2:
    st.markdown('<div class="section-title">🔢 Wattage Calculator</div>', unsafe_allow_html=True)

    selected_appliance = st.selectbox("Select Appliance", list(appliances.keys()))
    hours_used = st.slider("Usage Hours Per Day", 1, 24, 4)

    wattage = appliances[selected_appliance]
    energy_used = wattage * hours_used
    cost = energy_used * average_cost_per_kw

    st.success(f"🔌 {selected_appliance} uses {energy_used:.2f} kWh/day costing ₹{cost:.2f}/day.")

    # Chatbot section
    st.markdown('<div class="section-title">🤖 Smart Home Chatbot</div>', unsafe_allow_html=True)

    user_input = st.text_input("Ask me anything about energy usage or appliance costs:", key="chatbox", placeholder="E.g., What's the average usage of the fridge?")
    
    def chatbot_response(user_input):
        user_input = user_input.lower()
        for appliance in appliances:
            if appliance.lower() in user_input:
                avg = appliances[appliance]
                cost = avg * hours_used * average_cost_per_kw
                return f"{appliance} consumes about {avg:.2f} kWh/hour. That’s ₹{cost:.2f}/day if used {hours_used} hrs/day."
        if "average usage" in user_input or "cost" in user_input:
            total = sum(appliances.values())
            return f"Average usage per appliance is around {total/len(appliances):.2f} kWh/hr. Daily cost (avg): ₹{(total*hours_used*average_cost_per_kw)/len(appliances):.2f}."
        return "I'm not sure about that, but I can help with appliance usage and cost!"

    if user_input:
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**Bot:** {chatbot_response(user_input)}")
