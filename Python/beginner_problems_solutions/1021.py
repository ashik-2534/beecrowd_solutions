value = float(input())
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for i in notes :
  needed_note = value // i 
  print(f"{int(needed_note)} nota (s)de R$ {i:.2f}")
  value %= i
print("MOEDAS:")
cent_value = int(value * 100)
for i in coins:
  cent = int(i * 100)
  needed_coins = cent_value // cent
  print(f"{int(needed_coins)} moeda(s) de R$ {i:.2f}")
  cent_value %= cent
