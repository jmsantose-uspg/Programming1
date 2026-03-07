#tabla de multiplicar
num = int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
print(f"\n--- Tabla del {num} ---")
for i in range(1, 13):
    resultado = num * i
    print(f"{num} x {i:2d} = {resultado:3d}")

    #Salida para num = 5
    #--- Tabla del 5 ---
    #5 x  1 =   5
    #5 x  2 =  10
    #...    
    #5 x 12 =  60
    