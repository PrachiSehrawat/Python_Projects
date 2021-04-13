try:
    Marks = float(input("Enter The Marks :"))
    if 95<=Marks<=100:
        print("A+")
    elif 90<=Marks<95:
        print("A")
    elif 80<=Marks<90:
        print("B+")
    elif 60<=Marks<80:
        print("B")
    elif 40<=Marks<60:
        print("C")
    elif 34<=Marks<40:
        print("D")
    elif 33<=Marks<34:
        print("Just Pass")
    else:
        print("Sorry! You Are Fail")
except Exception:
    print('Invalid')


