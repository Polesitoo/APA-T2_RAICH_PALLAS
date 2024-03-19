"""
Alumnos: Víctor Pallàs i Pol Raich
"""


import math


def esPrimo(num):
    """
    Devuelve True si su argumento es primo y False si no lo es
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    
    for it in range(2, num):
        if num % it == 0: 
            return False      
    return True


def primos(lim):
    """
    Devuelve una tupla de todos los primos hasta el argumento sin incluirlo
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    
    return tuple(i for i in range(2, lim) if esPrimo(i))


def descompon(num):
    """
    Devuelve una tupla con la descomposición en números primos del argumento ordenada de menor a mayor
    En este caso utilizamos La Propiedad de los número primos donde si un numero compuesto n tiene un divisor d, d <= sqrt(n)
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """   
     
    desc = []
    divisor = 2    
    while divisor * divisor <= num:
        if num % divisor == 0:
            desc.append(divisor)
            num //= divisor
        else:
            divisor += 1    
    if num > 1:
        desc.append(num)    
    return tuple(desc)


def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de los dos argumentos
    >>> mcm(90, 14)
    630
    """
    
    desc1 = descompon(num1)
    desc2 = descompon(num2)
    mCmList = list(desc1)
    for i in range(len(desc2)):
        quantInDesc1 = mCmList.count(desc2[i])
        quantInDesc2 = desc2.count(desc2[i])
        if quantInDesc1 < quantInDesc2:
            n = quantInDesc2 - quantInDesc1
            for j in range(n):
                mCmList.append(desc2[i])       
    return math.prod(mCmList)


def mcd(num1, num2):
    """Devuelve el máximo común divisor de los dos argumentos.
    Utilizando la propiedad: mcd(a, b) = a * b / mcm(a, b)
    >>> mcd(924, 780)
    12
    """
    
    return num1 * num2 // mcm(num1, num2)


def mcmN(*nums):
    """Devuelve el mínimo común múltiplo de todos los argumentos
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    
    MCM = 1
    for i in range(len(nums)):
        MCM = mcm(MCM, nums[i])
    return MCM


def mcdN(*nums):
    """
    Devuelve el máximo común divisor de todos los argumentos
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    
    MCD = nums[0]
    for num in nums[1: ]:
        MCD = mcd(MCD, num)
    return MCD
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)


"""
FUNCIÓN ANTIGUA DE DESCOMPOSICIÓN - ÉS MUY LENTA
def descompon(num):    
    listaPrimos = primos(num)
    desc = []
    if not esPrimo(num):
        while num != 1:
            for i in range(len(listaPrimos)):
                if num % listaPrimos[i] == 0:
                    #print(str(num) + "   |   " + str(listaPrimos[i]))
                    num = num // listaPrimos[i]
                    desc.append(listaPrimos[i])
                    break
    else:
        desc.append(num)
    
    return tuple( desc[i] for i in range(len(desc)) )
"""