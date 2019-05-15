'Simple program to calculate the Cash you invest after a defined timespan'

#The money you invest
investedMoney = float(input("How much muney would you like to invest? "))

#The interest rate by your bank
interestRate = float(input("Enter your Interest Rate in % "))

#The timespan you want to invest
runtime = int(input("How many years would you like to invest? "))

#Calculates the money earned by the interest rate and adds it to the balance
for i in range(runtime):
    investedMoney = investedMoney*(1 + interestRate / 100)

#Prints the calculated balance after the investment is finisdhed
print("After %s years, you'll have %s$" % (runtime, investedMoney))
