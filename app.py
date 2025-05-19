def add(a, b):
   
    return a + b

def multiply(a, b):
   
    return a * b

if __name__ == "__main__":
    # Simple CLI interaction
    print("Simple Calculator")
    x = 5
    y = 6
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")

