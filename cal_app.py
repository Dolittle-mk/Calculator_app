import streamlit as st

# App title
st.title("🧮 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate and display result
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"

    st.success(f"Result: {result}")
