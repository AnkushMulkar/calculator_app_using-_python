import streamlit as st

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

# Create a Streamlit app
def app():
    # Print a welcome message and instructions
    st.title("Calculator App")
    st.write("Please enter two numbers to perform arithmetic operations.")

    # Get input from the user
    num1 = st.number_input("Enter the first number:", step=1.0)
    num2 = st.number_input("Enter the second number:", step=1.0)

    # Perform arithmetic operations
    if st.button("Calculate"):
        sum = add(num1, num2)
        difference = subtract(num1, num2)
        product = multiply(num1, num2)
        quotient = divide(num1, num2)

        # Print the results
        st.write("The sum of the two numbers is:", sum)
        st.write("The difference between the two numbers is:", difference)
        st.write("The product of the two numbers is:", product)
        st.write("The quotient of the two numbers is:", quotient)

# Run the app
if __name__ == '__main__':
    app()
