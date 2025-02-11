num = int(input("Enter number of Purchased items: "))
sum = 0 #Total of items purchased
for i in range(num):
    price_of_item = float(input(f"Enter price of item {i+1}: "))
    Quantity_of_item = int(input(f"Enter quantity of item {i+1}: "))
    sum += price_of_item*Quantity_of_item
if(sum > 50):
    print("There is discount of on purchase of items having total greater then 50 USD")
    print(f"Total : {sum}")
    print(f"Discounted : {sum/10}")
    print(f"Total payable price is : {sum - sum/10}")
else:
    print(f"Total payable price is : {sum}")