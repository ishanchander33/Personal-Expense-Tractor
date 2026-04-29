expenselist=[]    #list of all expense in form od dictionaries
print("Welcom To Expense Tracker ")

while True:
    print("====menu====")
    print("1.Add Expense")
    print("2.View All Expense")
    print("3.View The Total Spend")
    print("4.Exit")

    choice=int(input("Enter your choice : "))

    #Add expense 
    if(choice==1):
        date=input("Enter in which date you are spend ")
        category=input("Enter where you spend money like:food,clothes,books,travel ")
        description=input("Enter the description (what you buy) ")
        amount=float(input("Enter the amount "))

        expense= {
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenselist.append(expense)
        print("\n Done All The Expense Are Recorded ")

    # View all expense
    elif(choice==2):
        print("here shows your all spening expense  ")
        if(len(expenselist)==0):
            print("No expense, first first buy someting ")
        else:
            print("all your expense here ")
            
            count = 1
            for data in expenselist:
                print(f"{count}-> {data["date"]}, {data["category"]},{data["description"]}, {data["amount"]}")
                count=count+1

    # Total spendng 
    elif (choice==3):
        total = 0  
        for data in expenselist:
            total = total + data["amount"]         
        print("\n total amount is ",total)

    # Exit
    elif(choice==4):
        print("thanking you")
        break

    else:
        print("please enter the vaild choice")