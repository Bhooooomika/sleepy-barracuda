import streamlit as st
import streamlit.components.v1 as components
import random
import time
import json

# -------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Smart Home Dashboard", layout="wide")

# -------------- CUSTOM CSS ------------------
with open("public/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------- HEADER ----------------------
st.markdown("<h1 class='dashboard-title'>Smart Home Energy Dashboard</h1>", unsafe_allow_html=True)

# -------------- CHART AREA ------------------
st.subheader("📈 Real-Time Energy Usage")
components.html(open("public/chart.html").read(), height=400)

# -------------- PREDICTED vs ACTUAL --------------
st.subheader("🔮 Predicted vs Actual Energy Usage")
actual = [random.uniform(1.5, 4) for _ in range(12)]
predicted = [val + random.uniform(-0.3, 0.3) for val in actual]

st.line_chart({"Actual": actual, "Predicted": predicted})

# -------------- CHATBOT ----------------------
st.subheader("🤖 Chat with EnergyBot")

appliances = {
    "Dishwasher": 1.2,
    "Fridge": 0.3,
    "Furnace": 1.5,
    "Home Office": 0.8,
    "Wine Cellar": 0.6
}
cost_per_kwh = 0.12

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "cost" in user_input:
        total_cost = sum(appliances.values()) * cost_per_kwh
        return f"💸 Estimated cost per hour: ${total_cost:.2f}"

    elif "average" in user_input:
        avg = sum(appliances.values()) / len(appliances)
        return f"📊 The average usage across devices is {avg:.2f} kW."

    elif "usage" in user_input:
        usage_lines = [f"{k}: {v} kW" for k, v in appliances.items()]
        return "⚡ Here's the usage of each device:\n" + "\n".join(usage_lines)

    return "🤷‍♂️ Sorry, I didn’t understand. Try asking about 'cost', 'usage', or 'average usage'."

with st.container():
    user_input = st.text_input("Ask EnergyBot something:", key="chat_input")
    if user_input:
        response = chatbot_response(user_input)
        st.success(response)

# -------------- WATTAGE CALCULATOR ----------------------
st.subheader("🧮 Wattage Calculator")

with st.form("calc_form"):
    device_name = st.text_input("Device name:")
    device_watt = st.number_input("Power (Watts):", min_value=1)
    hours = st.number_input("Usage Hours per Day:", min_value=0.0)
    submitted = st.form_submit_button("Calculate")

    if submitted:
        kwh = (device_watt * hours) / 1000
        cost = kwh * cost_per_kwh
        st.write(f"⚡ Daily Usage: {kwh:.2f} kWh")
        st.write(f"💵 Estimated Daily Cost: ${cost:.2f}")

# -------------- FOOTER ----------------------
st.markdown("<footer>Made with ❤️ for Smart Energy</footer>", unsafe_allow_html=True)
