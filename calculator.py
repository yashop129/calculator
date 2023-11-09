a=int(input('enetr first number:'))
b=int(input('enetr secound number:'))
print('print two number :')
ch=0
while ch<5:
    print('calculator')
    print('1.addition')
    print('2.subtraction')
    print('3.multiplication')
    print('4.division')
    print('5.exit')
    ch=int(input('enter your choice:'))
    if ch==1:
        c=a+b
        print('sum:',c)
    elif ch==2:
        c=a-b
        print('difference:',c)
    elif ch==3:
        c=a*b
        print('product:',c)
    elif ch==4:
        c=a/b
        print('quotinet:',c)            
    elif ch==5:
        break
    else:
        print('invalid')