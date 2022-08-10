import math

#Get the user to input 'investment' or 'bond'.
finance_choice = str(input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\n"
                           "investment     - to calculate the amount of interest you'll earn on interest\n"
                           "bond           - to calculate the amount you'll have to pay on home loan\n\n"))

# Make input lowercase to elimenate user error.
finance_choice = finance_choice.lower()

#Checks if the corrrect input has been entered if not print statement below.
if (finance_choice != "bond") and (finance_choice != "investment") :
    print("That is not a valid input. Please try again")

#Print(finance_choice) #checking if the finance_choice veriable has been allocated properly.

#If finance_choice veriable is the same as the string 'investment' follow the steps below.
if (finance_choice == "investment") :
    #Getting inputs from user and storing them in the appropriate  veriables.
    deposit = float(input("Enter the deposit amount:\n£"))
    interest_rate = float(input("Enter the interest rate:\n%"))
    years = int(input("Enter the number of years you wish to invest:\n"))
    #Getting the user to choose betweem simple or compound interest.
    interest_type = str(input("Choose either 'compound' or 'simple' investment plan:\n"
                              "compound\nsimple\n"))

    #Calculating actual interest rate for calculation later.
    interest_rate_actual = interest_rate / 100
    #Set interest_type to lower case to eliminate user error.
    interest_type = interest_type.lower()

    #If the user inputed simple follow steps below.
    if (interest_type == "simple") :
        #calculate and store value for simple interest plan in variable 'total'.
        total = deposit * (1 + interest_rate_actual * years)
    #If statement above is false and the user input is 'compound' follow steps below.
    elif (interest_type == "compound") :
        #calculate and store value for compound interest plan in variable 'total'.
        total = deposit*math.pow((1 + interest_rate_actual),years)
    #If all statements above are false execute print commad below.
    else :
        print("invalid input. Please try again")

    #Print the total amount after the interest amount is applied to the deposit for the allocated years.
    print("With £{:0,.2f} deposit at %{} interest rate for {} years your total amount will be £{:0,.2f}".format(deposit,interest_rate,years,total))

#If the statement above for (finance_choice == "investment") is not met and the finance_choice variable is qual to "bond" execude the steps below.    
elif (finance_choice == "bond") :
    #Get the appropriate values for calculating the bond and store them in appropriate veriables.
    house_value  = float(input("Enter the present value of the house:\n£"))
    interest_rate = float(input("Enter the interest rate:\n%"))
    months = int(input("Enter the number of months it will take to repay the bond:\n"))

    #Annual interest is converted to monthly interest rate for calculation later.
    interest_rate_monthly = (interest_rate / 12) / 100
    #Calculate the monthly payment for the bond by using the formula provided. 
    monthly_payment = (interest_rate_monthly * house_value) / (1 - math.pow((1 + interest_rate_monthly),(months * -1)))

    #Print the monthly payment for the house. 
    print("With a house valued £{:0,.2f} at %{} interest rate for {} months will be £{:0,.2f} per month".format(house_value,interest_rate,months,monthly_payment))
