import random

print("Hello valued guest, Welcome to the worlds fairest Casino"
      "Where anyone can become rich over night!")

print("Our first game is called the 50-50. As the name suggests the"
      "game is simple, the computer will randomly generate a fact")

print("So lets get started then!")

true = ["There was a dog mayor", "You can't breathe and swallow at the same time",
        "Alaska is the most western and eastern state in the US",
        "A bolt of lightning contains enough energy to toast 100,000 slices of bread"]
false = ["France didn't stopped using the guillotine until 1900",
         "The average person will spend 8 months of their life waiting for red lights to turn green",
         ]
explanation = ["France stopped using the guillotine in 1977 not 1900", "The average person spends 6 months, not 8"
               ]
bank = 0
total = 0
while True:
    money = int(input("Enter Bet:"))
    if money == 0:
        break
    picker1 = random.randint(0, 1)
    picker2 = 0
    if picker1 == 0:
        picker2 = random.randint(0, (len(true)-1))
        print("and your fact is: %s" % true[picker2])
    if picker1 == 1:
        picker2 = random.randint(0, (len(false)-1))
        print("and your fact is: %s" % false[picker2])
    yourChoice = input("Now is the fact true, or false?")
    if yourChoice == "true" and picker1 == 0 or yourChoice == "false" and picker1 == 1:
        total += money * 1.5
        bank -= money
        print("Congratulations that was the right choice "
              "Your money has now been increased by 1.5 and is: %s"
              " and the bank is now at: %s" % (total, bank))
    else:
        total -= money
        bank += money
        print("Sorry valued guest, that was the wrong answer and we have had to, "
              "unfortunately, take your money. You are now at:%s and the bank is now"
              " at:%s" % (total, bank))
    if picker1 == 1:
        print("As you know know the answer was false the real fact was as follows:")
        print(explanation[picker2])







