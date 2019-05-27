def es_primo(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True

def primos(num1,num2):
    cont = 0
    for i in range(num1,num2):
        if es_primo(i) == True:
            cont +=1

    print("Hay", cont, "numeros primos")

es_primo(1000)
primos(1,1000) 

        
    
        
    
