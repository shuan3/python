def display(r1,r2,r3):
    print(r1,r2,r3)


result=input("Enter value")
print(int(result))




def user_choice():
    choice='WRONG'
    acceptance_range=range(0,10)
    within_range=False
    while choice.isdigit()==False:
        choice=input("Please enter a number")
        if choice.isdigit()==False:
            print("Sorry that is not a digit!")
        if choice.isdigit()==True and int(choice) in acceptance_range:
            within_range=True
        else:
            print('Sorry you are out of range! ')
            within_range=False

    return int(choice)



