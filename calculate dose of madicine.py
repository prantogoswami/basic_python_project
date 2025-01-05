def calculate_dosage(weight, age):
    """Calculate medication dosage based on weight and age."""
    if age < 12:
        # For children under 12, assume a dosage of 10 mg per kg of body weight
        dosage = weight * 10  # mg per dose
    elif 12 <= age <= 60:
        # For adults 12 to 60 years, fixed dosage of 500 mg per dose
        dosage = 500
    else:
        # For seniors over 60, a reduced dosage of 250 mg per dose
        dosage = 250
 
    return dosage
 
 
def main():
    """Main function to get user input and calculate dosage."""
    print("Welcome to the Medication Dosage Calculator!")
 
    # Get patient's age with input validation
    while True:
        try:
            age = int(input("Please enter the patient's age in years: "))
            if age <= 0:
                print("Age must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid age in years.")
 
    # Get patient's weight with input validation
    while True:
        try:
            weight = float(input("Please enter the patient's weight in kg: "))
            if weight <= 0:
                print("Weight must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid weight in kg.")
 
    # Calculate the dosage
    dosage = calculate_dosage(weight, age)
 
    # Display the recommended dosage
    print(
        f"\nThe recommended dosage for a patient aged {age} years with a weight of {weight} kg is: {dosage} mg per dose.\n")
 
 
# Run the program
if __name__ == "__main__":
    main()
 