input_data = input().split()
a,b,c = input_data
a = int(a)
b = int(b)
c = int(c)

MaiorAB = (a+b+abs(a-b))/2
MaiorABC = (MaiorAB+c+abs(MaiorAB-c))/2
print(f"{int(MaiorABC)} eh o maior")
