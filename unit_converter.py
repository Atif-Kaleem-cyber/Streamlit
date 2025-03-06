import streamlit as st

# Title of the app
st.title("Unit Converter")

# Sidebar for unit selection
st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose a conversion type",
    ["Length", "Weight", "Temperature"]
)

# Function to convert length
def convert_length(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Main app logic
if conversion_type == "Length":
    st.header("Length Converter")
    col1, col2 = st.columns(2)
    with col1:
        length_value = st.number_input("Enter length value", value=1.0)
        from_length_unit = st.selectbox("From unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    with col2:
        to_length_unit = st.selectbox("To unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    result = convert_length(length_value, from_length_unit, to_length_unit)
    st.success(f"Converted value: {result:.2f} {to_length_unit}")

elif conversion_type == "Weight":
    st.header("Weight Converter")
    col1, col2 = st.columns(2)
    with col1:
        weight_value = st.number_input("Enter weight value", value=1.0)
        from_weight_unit = st.selectbox("From unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    with col2:
        to_weight_unit = st.selectbox("To unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    result = convert_weight(weight_value, from_weight_unit, to_weight_unit)
    st.success(f"Converted value: {result:.2f} {to_weight_unit}")

elif conversion_type == "Temperature":
    st.header("Temperature Converter")
    col1, col2 = st.columns(2)
    with col1:
        temp_value = st.number_input("Enter temperature value", value=0.0)
        from_temp_unit = st.selectbox("From unit", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_temp_unit = st.selectbox("To unit", ["celsius", "fahrenheit", "kelvin"])
    result = convert_temperature(temp_value, from_temp_unit, to_temp_unit)
    st.success(f"Converted value: {result:.2f} {to_temp_unit}")