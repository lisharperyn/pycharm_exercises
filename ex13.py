# Lembre-se que a linguagem Python compreende os valores lógicos escritos sempre com a primeira letra da palavra em maiúscula. Portanto, true e false não irão funcionar.
# Operador not
# x = True
# y = False
# print(not x)
# print(not y)

x = True
y = False
print(x and y)

x = 10
y = 1
res = not x > y
print(res)

x = 10
y = 1
z = 5.5
res = x > y or x == y
print(res)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x
 # != símbolo de diferente
 
