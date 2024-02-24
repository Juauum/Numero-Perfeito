n = int(input("Digite um numero: "))
resto = quociente = 0
total_resto = []
total_quociente = []
nums = []
soma = []
for c in range(1,n):
  resto = n % c
  if resto == 0:
    soma.append(c)
total_resto.append(resto)
quociente = n / c
total_quociente.append(quociente)
print("-"*43)
print("Total Restos:")
print(f"{total_resto}")				
print("-"*43)
print("Total Quocientes:")
for c in total_quociente:
   print(f"{c:.2f}",end=" ")
print()
print("-"*43)
print("Divisores Próprios:")
print(f"{soma}")
print("="*43)
if sum(soma) == n:
  print("\033[1;32mEste numero é PERFEITO\033[m")
else:
  print("\033[1;34mEste numero NÃO é perfeito\033[m")  
print("="*43)				