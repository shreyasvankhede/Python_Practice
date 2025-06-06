
def tip_calci():
    bill = float(input("Enter bill amount: "))
    tip_percent = int(input("Enter tip percentage: "))
    people = int(input("How many people? "))

    tip_amount=(tip_percent/100)*bill
    total=bill+tip_amount
    per_person=total/people

    print(f"Total bill (with tip): ₹{total:.2f}")
    print(f"Each person pays: ₹{per_person:.2f}")

tip_calci()


