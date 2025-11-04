import math

def Collect_Data():
    a = input("Пожалуйста,введите параметр а: ")
    b = input("Пожалуйста,введите параметр b: ")
    c = input("Пожалуйста,введите параметр c: ")
    if (not (a.isdigit() or (a[0] == "-" and a[1:].isdigit()) ) or not (b.isdigit() or(b[0] == "-" and b[1:].isdigit())) or not (c.isdigit() or (c[0] == "-" and c[1:].isdigit()))):
        print("Неправильные корни, попытайтесь снова")
        exit()
    else:
        return [a,b,c]

Data = Collect_Data()

def Calculate(Data_1):
    a = float(Data_1[0])
    b = float(Data_1[1])
    c = float(Data_1[2])
    D = b**2 - 4*a*c
    if(D < 0):
        print("Корней нет")
    elif(D == 0):
        Ans1 = (-b) / (2 * a)
        print("Дискриминант:", D, " Корень: ",Ans1)
    else:
        Ans1 = (- b - D**0.5)/(2*a)
        Ans2 = (- b + D**0.5)/(2*a)
        print("Дискриминант:", D, " Корни: ",Ans1,Ans2)

Calculate(Data)