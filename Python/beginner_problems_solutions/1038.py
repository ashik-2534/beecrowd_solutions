X, Y = map(int, input().split())
product_price = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

if X in product_price:
  total_product_price = product_price[X] * Y
  print(f"Total: R$ {total_product_price:.2f}")
else:
  print("please enter a valid code")
