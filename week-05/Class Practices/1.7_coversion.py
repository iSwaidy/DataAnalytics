original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

discount_amount = original_price * (discount / 100)
final_price = original_price - discount_amount

print(f"Final Price = ${final_price:.2f}")