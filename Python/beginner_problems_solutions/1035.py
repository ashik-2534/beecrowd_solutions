num = input().split()
A, B, C, D = num
A =int(A)
B=int(B)
C=int(C)
D=int(D)
if B>C and D>A and C+D > A+B and C>0 and D>0 and A%2 == 0 :
  print("Valores aceitos")
else:
  print("Valores nao aceitos")
