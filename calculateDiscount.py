def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)
    
    
    if final_price == price:
        print("No discount applied. The original price is:", price)
    else:
        print("The final price after applying the discount is:", final_price)
        
except ValueError:
    print("Please enter a valid number.")
