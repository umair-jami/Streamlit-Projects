import streamlit as st

st.markdown("<h1 style='text-align:center'>Unit Converter</h1>", unsafe_allow_html=True)

# category selection
categories = {
    "📏 Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
    "⚖️ Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "🌡️ Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "⏳ Time": ["Seconds", "Minutes", "Hours", "Days"]
}
selected_category = st.radio("Select a category", list(categories.keys()),horizontal=True)

# Dropdown for units
from_unit=st.selectbox("From",categories[selected_category])
to_unit=st.selectbox("To",categories[selected_category])

# Input field for value
value=st.number_input("Value",min_value=0.0,format="%.2f")

# Conversion
def convert(value,from_unit,to_unit):
    conversion_factors = {
        "Meters": {"Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084, "Inches": 39.3701},
        "Kilometers": {"Meters": 1000, "Miles": 0.621371, "Feet": 3280.84, "Inches": 39370.1},
        "Miles": {"Meters": 1609.34, "Kilometers": 1.60934, "Feet": 5280, "Inches": 63360},
        "Feet": {"Meters": 0.3048, "Kilometers": 0.0003048, "Miles": 0.000189394, "Inches": 12},
        "Inches": {"Meters": 0.0254, "Kilometers": 0.0000254, "Miles": 0.000015783, "Feet": 0.0833333},

        "Kilograms": {"Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Grams": {"Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
        "Pounds": {"Kilograms": 0.453592, "Grams": 453.592, "Ounces": 16},
        "Ounces": {"Kilograms": 0.0283495, "Grams": 28.3495, "Pounds": 0.0625},

        "Celsius": {"Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15},
        "Fahrenheit": {"Celsius": lambda f: (f - 32) * 5/9, "Kelvin": lambda f: (f - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": lambda k: k - 273.15, "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32},

        "Seconds": {"Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400},
        "Minutes": {"Seconds": 60, "Hours": 1/60, "Days": 1/1440},
        "Hours": {"Seconds": 3600, "Minutes": 60, "Days": 1/24},
        "Days": {"Seconds": 86400, "Minutes": 1440, "Hours": 24},
    }
    if from_unit == to_unit:
        return value
    elif callable(conversion_factors.get(from_unit, {}).get(to_unit, None)):
        return conversion_factors[from_unit][to_unit](value)
    else:
        return value * conversion_factors.get(from_unit, {}).get(to_unit, 1)
if st.button("Convert"):
    result=convert(value,from_unit,to_unit)
    st.markdown(f"<div class='result-box'>{result:.6f} {to_unit}</div>", unsafe_allow_html=True)
