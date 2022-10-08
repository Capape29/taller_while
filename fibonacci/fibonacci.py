# Fibonacci
a = 0
b = 1
c = a + b

# Processing
while c < 1000:
    print("Secuencia fibonacci impresa desde el tercer número hasta ")
    print(c)
    a = b
    b = c
    c = a + b