exi = 1   
while exi != 0:    
    i = 0          
    plus = 0   
    minus = 0   
    for i in range(15):  
        print("Введите число: ")  
        number = int(input())   
        if number == 0: 
            print("ERROR")  
        if number > 0:   
            plus = plus + number  
        else:
            minus = minus + number 
    print("Сумма положительных чисел:" + str(plus))  
    print("Сумма отрицательных чисел:" + str(minus)) 
    print("Для закрытия программы введите 0, для продолжения любую цифру отличную от нуля")  
    exi = int(input())