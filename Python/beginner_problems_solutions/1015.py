first_input = input().split()
second_input = input().split()
x1,y1=first_input
x2,y2=second_input
x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)
Distance = ((x2-x1) **2 + (y2-y1) **2) **0.5
print(f"{Distance:.4f}")
