n = int(input())
palabras = []

while n != 0:
    palabra = input()
    palabras.append(palabra)
    n = n - 1
    
palabrasFormateadas = []
for palabra in palabras:
    longitudPalabra = len(palabra)    
    
    if longitudPalabra > 10:    
        caracteresIntermedios = longitudPalabra - 2
        respuesta = palabra[0] + str(caracteresIntermedios) + palabra[-1]
        palabrasFormateadas.append(respuesta)
    else:
        palabrasFormateadas.append(palabra)

for palabra in palabrasFormateadas:
    print(palabra)
    




        
            
