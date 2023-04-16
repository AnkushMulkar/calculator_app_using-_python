import math
import streamlit as st

st.set_page_config(page_title="Scientific Calculator")

st.title("Scientific Calculator")

# Sidebar for mode selection
mode = st.sidebar.selectbox(
    "Select mode:",
    ["Basic", "Scientific"],
)

# Function to handle math operations
def math_op(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "^":
        return num1 ** num2

# Function to handle trigonometric operations
def trig_op(num, operation):
    if operation == "sin":
        return math.sin(num)
    elif operation == "cos":
        return math.cos(num)
    elif operation == "tan":
        return math.tan(num)
    elif operation == "asin":
        return math.asin(num)
    elif operation == "acos":
        return math.acos(num)
    elif operation == "atan":
        return math.atan(num)

# Main calculator logic
if mode == "Basic":
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)
    operator = st.selectbox(
        "Select operation:",
        ["+", "-", "*", "/", "^"],
    )

    # Perform math operation
    result = math_op(num1, num2, operator)

    # Display result
    st.write("Result:", result)

else:
    num = st.number_input("Enter number:", value=0.0)
    operation = st.selectbox(
        "Select operation:",
        ["sin", "cos", "tan", "asin", "acos", "atan"],
    )

    # Perform trigonometric operation
    result = trig_op(num, operation)

    # Display result
    st.write("Result:", result)
    st.write("Created by [Ankush Mulkar](https://www.linkedin.com/in/ankush-mulkar-ab539454/)")

