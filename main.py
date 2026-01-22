# Arithmetic Operations Project
# Author: Aaryan Choudhary (23f2003700)
# IITM BS in Data Science

def main():
    print("=== Arithmetic Calculator ===")
    print("1. Sum")
    print("2. Difference")
    print("3. Product")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                from sum_module import add
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                from difference_module import subtract
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                from product_module import multiply
                print(f"Result: {multiply(num1, num2)}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
