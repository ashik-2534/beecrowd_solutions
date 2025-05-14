value = int(input())
print(value)
banknote = [100, 50, 20, 10, 5, 2,1]
for i in banknote:
  needed_notes = value // i
  print(f"{needed_notes} nota(s) de R$ {i},00")
  value %= i
