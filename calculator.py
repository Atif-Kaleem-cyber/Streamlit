import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Dropdown to select operation
operation = st.selectbox(
    "Select an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Calculate and display the result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")