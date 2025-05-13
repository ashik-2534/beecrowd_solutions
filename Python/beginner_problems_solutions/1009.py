# -*- coding: utf-8 -*-

seller_name=str(input())
fixed_salary = float(input())
total_sale = float(input())
bonus = total_sale * 0.15
final_salary = fixed_salary + bonus
print(f"TOTAL = R$ {final_salary:.2f}")