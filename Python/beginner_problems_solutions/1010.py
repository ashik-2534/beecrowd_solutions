product1 = input().split()
code1, quantity1, price1 = product1
product2 = input().split()
code2, quantity2, price2 = product2
total_price1 = int(quantity1) * float(price1)
total_price2 = int(quantity2) * float(price2)
final_price = total_price1 + total_price2
print(f"VALOR A PAGAR: R$ {final_price:.2f}")