import streamlit as st
import math

# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    return x / y

# Define a function for exponentiation
def power(x, y):
    return x ** y

# Define a function for taking square root
def square_root(x):
    return math.sqrt(x)

# Define a function for taking logarithm
def logarithm(x, base):
    return math.log(x, base)

# Define a function for taking trigonometric functions
def trigonometry(x, function):
    if function == "sin":
        return math.sin(x)
    elif function == "cos":
        return math.cos(x)
    elif function == "tan":
        return math.tan(x)
    else:
        return None

# Create a Streamlit app
def app():
    # Print a welcome message and instructions
    st.title("Scientific Calculator")
    st.write("Please enter two numbers to perform arithmetic operations or use the scientific functions below.")

    # Get input from the user
    num1 = st.number_input("Enter the first number:", step=1.0)
    num2 = st.number_input("Enter the second number:", step=1.0)

    # Perform arithmetic operations
    if st.button("Calculate"):
        sum = add(num1, num2)
        difference = subtract(num1, num2)
        product = multiply(num1, num2)
        quotient = divide(num1, num2)
        power_result = power(num1, num2)

        # Print the results of arithmetic operations
        st.write("The sum of the two numbers is:", sum)
        st.write("The difference between the two numbers is:", difference)
        st.write("The product of the two numbers is:", product)
        st.write("The quotient of the two numbers is:", quotient)
        st.write("The result of raising the first number to the power of the second number is:", power_result)

    # Add scientific calculator functions
    st.write("Scientific functions:")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        if st.button("sin"):
            result = trigonometry(num1, "sin")
            st.write(f"The sine of {num1} is:", result)
        if st.button("cos"):
            result = trigonometry(num1, "cos")
            st.write(f"The cosine of {num1} is:", result)
    with col2:
        if st.button("tan"):
            result = trigonometry(num1, "tan")
            st.write(f"The tangent of {num1} is:", result)
        if st.button("sqrt"):
            result = square_root(num1)
            st.write(f"The square root of {num1} is:", result)
    with col3:
        base = st.number_input("Enter the base for logarithm:", step=1.0)
        if st.button("log"):
            result = logarithm(num1, base)
            st.write(f"The logarithm of {num1} with base {base} is:", result)
        st.write("Note: Logarithm function requires a base input.")

# Run the app
if __name__ == '__main__':
    app()
