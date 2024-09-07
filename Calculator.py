




print("Choose One Of The Operator :- + , - , * or /")
operator = input()

if '+' == operator:
    a = int(input("Please Enter The First Number :-  "))
    b = int(input("Please Enter The Second Number :- "))

    print("Your Result is", a+b)

elif '-' == operator:
    
    a = int(input("Please Enter The First Number :-  "))
    b = int(input("Please Enter The Second Number :- "))

    print("Your Result is", a-b)

elif '*' == operator:
    a = int(input("Please Enter The First Number :-  "))
    b = int(input("Please Enter The Second Number :- "))

    print("Your Result is", a*b)


elif '/' == operator:
    a = int(input(" Please Enter The First Number :- "))
    b = int(input("Please Enter The Second Number :- "))

    print("Your Result is", a/b)


else:
    pass
