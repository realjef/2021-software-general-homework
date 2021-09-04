import math
budget = int(input("Input Your Budget: "))
yoda_plushie = 20
beyblades = 7.2
sticky_hands = 0.5
total_toys = "Total Amount of Toys: "
if budget >= 20:
   number_of_yoda = str(math.floor(budget / 20))
   print(number_of_yoda + str(" Yoda Plushies"))
   budget = budget % 20
if budget >= 10:
   number_of_beyblades = str(math.floor(budget / 7.2))
   print(number_of_beyblades + " Beyblades")
   budget = budget % 7.2
if budget >= 3.2:
   number_of_sticky_hands = str(math.floor(budget / 0.5))
   print(number_of_sticky_hands + " Sticky Hands")
   budget = budget % 0.5
print("Remaining Money: " + str(budget))