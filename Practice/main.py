def getEvenOdd(num : int) -> str :
    resObj = {True : 'Even', False : 'Odd' }
    
    ifEven = num % 2 == 0
    print(resObj[ifEven])


getEvenOdd(2)
