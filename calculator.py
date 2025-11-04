# deepak code
while (True):
    print('1.Addition\n 2. Substraction 3.Multiplication 4. Division 5. Exit')
    n=int(input('enter any of the options\n'))
    if n in(1,2,3,4,5):
        if n in(1,2,3,4):
            if n ==1:
                sum,l=0,[]
                n=int(input('how many number you want to add'))
                for i in range(1,n+1):
                    value=int(input(f'enter {i} value'))
                    l.append(value)
                    sum=sum+value
                print(f'sum of given {l} is {sum}')
            elif n ==2:
                sub,l=0,[]
                n=int(input('how many number you want to substract'))
                for i in range(1,n+1):
                    value=int(input(f'enter {i} value'))
                    if value==1:
                        sub=value
                        l.append(value)
                    else:    
                     l.append(value)
                     sub=sub-value
                print(f'sub of given {l} is {sub}')
            elif n ==3:
                mul,l=1,[]
                n=int(input('how many number you want to multiply'))
                for i in range(1,n+1):
                    value=int(input(f'enter {i} value'))
                    l.append(value)
                    mul=mul*value
                print(f'sub of given {l} is {mul}')
            elif n ==4:
                div,l=1,[]
                n=int(input('how many number you want to divide'))
                for i in range(1,n+1):
                    value=int(input(f'enter {i} value'))
                    if i==1:
                        div=value
                        l.append(value)
                    else:    
                        l.append(value)
                        div=div//value
                print(f'sub of given {l} is {div}')    
                
        else:
            break
    else:
        print(' please enter valid options')