money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0


def student_life(money_capital, salary, spend, increase, month):
   while True:
      money_capital -= spend
      if money_capital < 0:
         break
      money_capital += salary
      month += 1
      spend *= (1+increase)
   return month
print(student_life(money_capital, salary, spend, increase, month))
