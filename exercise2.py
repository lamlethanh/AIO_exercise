import math

def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1/(1+ math.exp(x)) # math.exp -> e^x

# ReLu: Rectified Linear Unit
def relu(x):
    if (x <= 0):
        return 0
    return x

def elu(x):
    alpha = 0.01
    if (x <= 0):
        return alpha*(math.exp(x) - 1)
    return x

def func_active(func, x):
    if (func == "sigmoid"):
        result = sigmoid(x)
        print(f"sigmoid: f({x}) = {result}")
    elif (func == "relu"):
        result = relu(x)
        print(f"relu: f({x}) = {result}")
    elif (func == "elu"):
        result = elu(x)
        print(f"elu: f({x}) = {result}")
    else:
        print(func + "is not supported")

# Main function
x = input("Input x = ")

if is_float(x):
    func = input("Input activation Function (sigmoid | relu | elu): ")
    func_active(func, float(x))
else:
    print("x must be a number")

