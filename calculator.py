import math
import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Calculator", page_icon=":1234:")

# Define function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2

# Define function to perform trigonometric operations
def calculate_trig(num, operation):
    if operation == "sin":
        return math.sin(num)
    elif operation == "cos":
        return math.cos(num)
    elif operation == "tan":
        return math.tan(num)

# Define function to format large results
def format_result(result):
    if result > 1000000 or result < -1000000:
        return "{:.2e}".format(result)
    else:
        return result

# Define main function
def main():
    st.title("Calculator")
    
    # Create input fields for numbers and operations
    num1 = st.number_input("Enter first number:")
    num2 = st.number_input("Enter second number:")
    operation = st.selectbox("Select operation:", ["+", "-", "*", "/", "sin", "cos", "tan"])
    
    # Perform calculation and display result
    if operation in ["+", "-", "*", "/"]:
        result = calculate(num1, num2, operation)
        st.write("Result:", format_result(result))
    elif operation in ["sin", "cos", "tan"]:
        result = calculate_trig(num1, operation)
        st.write("Result:", format_result(result))

# Run the app
if __name__ == "__main__":
    main()
