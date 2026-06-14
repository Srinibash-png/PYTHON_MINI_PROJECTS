expenselist=[]

print("\n WELXOME TO  BUDGET EXPENSE TRACKER   \n")
def add():
    date=input("enter the date on which you spend:")
    category=input("enter on which things did you spend:")
    amt=int(input("enter the amount spent on the things:"))
    expense={
        "date":date,
        "amt":amt,
        "category":category
    }
    expenselist.append(expense)

    print("expense data added:")

def show():
    if not expenselist:
        print("no data is found:")
        return
    

    for i in expenselist:
        print(f"{i["category"]} => {i["date"]}  => {i["amt"]} \n")



def total_amount():
    amount=0
    for i in expenselist:
        amount=amount+i["amt"]

    print("total amount you spent:",amount)


    
def main():
    while True:
        print("HELLO WELCOME DO WHATEVER YOU WANT  DO NOW ")
        print("1.add expesnes\n")
        print("2.show expenses\n")
        print("3.total amount\n")
        print("4.exit\n")
        ch=int(input("enter your choice:"))

        if ch==1:
            add()

        elif ch==2:
            show()

        elif ch==3:
            total_amount()

        elif ch==4:
            print("THANK YOU")
            break
        else:
            print("please enter valid choice :\n")

main()