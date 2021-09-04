test1 = float(input("Test 1 Score: "))
test2 = float(input("Test 2 Score: "))
test3 = float(input("Test 3 Score: "))
Average = (test1 + test2 + test3)/3
print(f"Your test average is: {Average}")
if Average >= 90: 
    print("Your letter grade is A.")
elif Average < 90 and Average >= 80:
    print("Your letter grade is B.")
elif Average < 80 and Average >= 70:
    print("Your letter grade is C.")
elif Average < 70 and Average >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade is F, you have failed.")