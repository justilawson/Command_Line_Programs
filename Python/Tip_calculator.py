bill = float((input("What is the total cost of the bill? $")))
tip_percent = input("What percent would you like to leave? 10, 12, 15? ")
total_ppl = int(input("How many will you split the bill with?"))

total_tip_percent = float("1." + tip_percent)


total_pay = round((bill/total_ppl) * total_tip_percent,2)

print(f"You should pay ${total_pay} each.")
