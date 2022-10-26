def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def mul(a, b):
  return a * b
def div(a, b):
  return a / b
def main():
st.title("Simple Calculator")
st.write("This is a simple calculator app")
a = st.number_input("Enter a number")
b = st.number_input("Enter another number")
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])
if operation == "Add":
st.write(add(a, b))
elif operation == "Subtract":
st.write(sub(a, b))
elif operation == "Multiply":
st.write(mul(a, b))
elif operation == "Divide":
st.write(div(a, b))
if __name__ == '__main__':
main()
