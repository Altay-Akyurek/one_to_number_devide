def one_to_number():
    numbe=int(input("enter a number"))
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list7=[]
    list8=[]
    list9=[]
    list10=[]
    
    a=0
    for i in range(1,numbe+1):
        a+=i
        if (i%2==0):
            list2.append(i)
        if (i%3==0):
            list3.append(i)
        if(i%4==0):
            list4.append(i)
        if(i%5==0):
            list5.append(i)
        if(i%6==0):
            list6.append(i)
        if(i%7==0):
            list7.append(i)
        if(i%8==0):
            list8.append(i)
        if(i%9==0):
            list9.append(i)
        if(i%10==0):
            list10.append(i)
    print("2 devide",list2,end="\n")
    print("3 devide",list3,end="\n")
    print("4 devide",list4,end="\n")
    print("5 devide",list5,end="\n")
    print("6 devide",list6,end="\n")
    print("7 devide",list7,end="\n")
    print("8 devide",list8,end="\n")
    print("9 devide",list9,end="\n")
    print("10 devide",list10,end="\n")
    
one_to_number()





