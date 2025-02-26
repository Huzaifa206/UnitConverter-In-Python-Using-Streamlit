import streamlit as st # type: ignore

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "metric tons": 0.001,
        "pounds": 2.20462,
        "ounces": 35.274,
        "stones": 0.157473,
        "celsius": lambda c: c,
        "fahrenheit": lambda c: (c * 9/5) + 32,
        "kelvin": lambda c: c + 273.15
    }
    
    temperature_units = {"celsius", "fahrenheit", "kelvin"}
    if from_unit in temperature_units and to_unit in temperature_units:
        temp_converters = {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: (x - 32) * 5/9,
            "kelvin": lambda x: x - 273.15
        }
        value_in_celsius = temp_converters[from_unit](value)
        return conversion_factors[to_unit](value_in_celsius)
    
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

st.markdown("""
    <h1 style='text-align: center; font-size: 36px;'>🔄 Unit Converter</h1>
    <h3 style='text-align: center; font-size: 24px;'>Convert between different units easily!</h3>
""", unsafe_allow_html=True)

all_units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", "kilograms", "grams", "milligrams", "metric tons", "pounds", "ounces", "stones", "celsius", "fahrenheit", "kelvin"]

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", all_units)
with col2:
    to_unit = st.selectbox("To", all_units)

value = st.number_input("Enter value", value=0.0, step=1.0)

if st.button("Convert", use_container_width=True):
    result = convert_units(value, from_unit, to_unit)
    st.markdown(f"""
        <h2 style='text-align: center; font-size: 28px; color: green;'>✅ {value} {from_unit} is equal to {result:.4f} {to_unit}</h2>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; font-size: 16px;'>Built with ❤️ using Streamlit</p>
""", unsafe_allow_html=True)
