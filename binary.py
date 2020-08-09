def esbinario(binario):
    conjunto_bits= set(list(binario))
    
    return('0' in conjunto_bits or '1' in conjunto_bits) and len(conjunto_bits) in [1,2] 

def convertirbinario(binario):
    if esbinario(binario):
        bits=list(binario)
        valor=0
        
        for i in range(len(bits)):
            bit=bits.pop()
            
            if bit== '1':
                valor+=pow(2, i)
                
        return valor
    
    else: ValueError('la cadena no representa un numero binario valido')
        

if __name__== "__main__":
    binario=input("Ingrese un numero binario para convertir a entero: ") 
    print(convertirbinario(binario))
