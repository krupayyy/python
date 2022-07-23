# Take price and display net price after 10% discount

# input
price = int(input("Enter price :"))

#process
discount = price * 10 / 100
tax = price* .08
net_price = price - discount + tax

# output
print(f"Price        {price:8.2f}")
print(f"- Discount   {discount:8.2f}")
print(f"Net Price    {net_price:8.2f}")

