def IMC(peso, altura):
 IMC = peso / (altura**2)
 return IMC

altura = float (input('Ingresa tu altura en metros'))
    
peso = float (input('Ingresa tu peso en kilogramos'))


resultadoIMC = IMC(peso, altura)
print('El resultado de tu índice de masa corporal (IMC) es:', resultadoIMC)
    
if resultadoIMC < 18.5:
    print('Categoría: Bajo peso')
elif 18.5 <= resultadoIMC < 25:
    print('Categoría: Peso normal')
elif 25 <= resultadoIMC < 30:
    print('Categoría: Sobrepeso')
elif resultadoIMC >= 30:
    print('Categoría: Obesidad')