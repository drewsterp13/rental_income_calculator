# The goal is to make a rental income calculator
# first, enter the list of income sources
# next, enter the list of expense sources
# third, enter the list of investment sources (such as down payment, closing cost ect)

# Behind the senes:
# adds up the income, expense, and investment as three seperate variables
# calcualtes the cash flow by subtracting the expenses from the income
# calculates the annual cash flow by multiplying it by 12
# finding out the cash on cash return on investment by dividing the annual cash flow by total investment and dividing by 100 to get percentage
# saves the data into a dictionary

# This class has the calculators
class RentalIncomeCalculator():
    # This creates a list of prices
    def createList(self, alist):
        repeat = True
        while repeat:
            print("Please enter your name")
            name = input("ENTER HERE: ")
            print("Please enter your price")
            num = int(input("ENTER HERE: "))
            alist.append([name, num])
            while True:
                print('Do you want to add more prices? enter "yes" or "no"')
                choice = input("ENTER HERE: ")
                if choice.lower() == "no":
                    repeat = False
                    break
                elif choice.lower() == "yes":
                    break
                else:
                    print("Sorry, invalid input")
                    print()
        return alist
    
    # This shows the list and adds them together
    def showAndCombinePrices(self, alist):
        value = 0
        for i in alist:
            print(f"{i[0]}: ${i[1]}")
            value += i[1]
        print(f"Total: ${value}")
        print()
        return value
    
    # This calculates the cash flow
    def calculateCashFlow(self, inc, exp):
        cash_flow = inc - exp
        print(f"Monthly Cash Flow: ${cash_flow}")
        return cash_flow
    
    # This gets the cash on cash return on investment
    def getCashOnCashROI(self, cash_flow, inve):
        cash_flow *= 12
        result = cash_flow / inve
        result *= 100
        print(f"Cash On Cash Return on Investment: {result}%")
        return result
    
    # This saves the calculations
    # NOTE: cash_flow is the monthly cash flow
    def saveCalcuation(self, mem_dict, ID, inc_list, exp_list, inve_list, inc, exp, inve, cash_flow, cocori):
        mem_dict[ID] = {
            "income_list": inc_list,
            "expense_list": exp_list,
            "investment_list": inve_list,
            "total_income": inc,
            "total_expense": exp,
            "total_investment": inve,
            "monthly_cash_flow": cash_flow,
            "annual_cash_flow": cash_flow * 12,
            "cash_on_cas_roi": cocori
        }
        print("Adding calculation to the archives")
        return mem_dict

# This creates the object to use the calculator
ric = RentalIncomeCalculator()

# This is the class that the user controls
class CalculateControl():
    # This has the variables
    def __init__(self):
        self.memory_id = 0
        self.memory = {}
    
    # This controls when the other methods in the RentalIncomeCalculator() class are used
    def mainControl(self):
        repeat = True

        while repeat:
            income = []
            expense = []
            investment = []
            total_income = 0
            total_expense = 0
            total_investment = 0
            monthly_cash_flow = 0
            cash_on_cash_roi = 0
            choice = " "

            print("Welcome to Bigger Pockets' Rental Income Calculator")
            print()
            print("Now, we will add together the monthtly income")
            ric.createList(income)
            print("Now, we will add together the monthly expenses")
            ric.createList(expense)
            print("Now, we will add together the payments for the property")
            ric.createList(investment)
            print("Here are the results...")
            print()
            print("Income:")
            total_income = ric.showAndCombinePrices(income)
            print("Expenses:")
            total_expense = ric.showAndCombinePrices(expense)
            print("Investments:")
            total_investment = ric.showAndCombinePrices(investment)
            monthly_cash_flow = ric.calculateCashFlow(total_income, total_expense)
            cash_on_cash_roi = ric.getCashOnCashROI(monthly_cash_flow, total_investment)
            self.memory = ric.saveCalcuation(self.memory, self.memory_id, income, expense, investment, total_income, total_expense, total_investment, monthly_cash_flow, cash_on_cash_roi)
            self.memory_id += 1
            while True:
                print()
                print('Do you want to make an another calculation? enter "yes" or "no"')
                choice = input("ENTER HERE: ")
                if choice.lower() == "no":
                    repeat = False
                    break
                elif choice.lower() == "yes":
                    break
                else:
                    print("Sorry, invalid input")
        print("Here are all of your calcualtions:")
        for memkey, memvalue in self.memory.items():
            print(f"Save Number {memkey}:")
            for key, value in memvalue.items():
                print(f"{key}: {value}")
        print()
        print("YOU HAVE A GREAT DAY!")

# This creates the object
control = CalculateControl()

# This activates the method
control.mainControl()


