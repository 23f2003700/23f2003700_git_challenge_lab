# Sum Module
# Provides addition functionality

def add(a, b):
    """
    Returns the sum of two numbers.
    
    Parameters:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b

# Test the function
if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10.5 + 2.5 = {add(10.5, 2.5)}")
