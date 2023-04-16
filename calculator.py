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
    num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
    num2 = st.number_input("Enter second number:", value=0.0, step=1.0)
    operation = st.selectbox("Select operation:", ["+", "-", "*", "/", "sin", "cos", "tan"])
    
    # Create digit buttons
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button("1"):
            num1 = num1*10 + 1
        if st.button("4"):
            num1 = num1*10 + 4
        if st.button("7"):
            num1 = num1*10 + 7
    with col2:
        if st.button("2"):
            num1 = num1*10 + 2
        if st.button("5"):
            num1 = num1*10 + 5
        if st.button("8"):
            num1 = num1*10 + 8
        if st.button("0"):
            num1 = num1*10 + 0
    with col3:
        if st.button("3"):
            num1 = num1*10 + 3
        if st.button("6"):
            num1 = num1*10 + 6
        if st.button("9"):
            num1 = num1*10 + 9
    
    # Perform calculation and display result
    if st.button("Calculate"):
        if operation in ["+", "-", "*", "/"]:
            result = calculate(num1, num2, operation)
            st.write("Result:", format_result(result))
        elif operation in ["sin", "cos", "tan"]:
            result = calculate_trig(num1, operation)
            st.write("Result:", format_result(result))

# Run the app
if __name__ == "__main__":
    main()
