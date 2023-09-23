# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221998 # Date: 19/04/2023
# UoW ID: w1985515

# initializing empty variables.
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
dictionary = {}

# defining a function to check if the user input credits are in range (0,20,40,60,80,100,120)
def input_credit(name):
    while True:
        try:
            input_credit = int(input(f"Please intput credits at {name}: "))
            if input_credit in range(0, 121, 20):
                return input_credit
            else:
                print("Out of range")
        except ValueError:
            print('"Integer is required"')


# difining a function to get the output of Progression,Progress (module trailer),Exclude,Do not progress – module retriever
def credits():
    # Converting Local Variables to Global Variables
    global Progress, Trailer, Retriever, Excluded, Progression, Stu_id

    while True:
        Stu_id = input("Please enter your student id: ")
        if len(Stu_id[1:]) != 7:            # Printing a error message if the length of the student id from [1:] end was not equal to 7.
            print("Enter a valid id")
            continue
        if Stu_id[0] != "w".lower():        # Printing a error message if the fist character wasn't "w".
            print("Invalid format")
            continue
        if not Stu_id[1:].isdigit():        # Printing a error message if the the student id from [1:] to end wasn't digits.
            print("Enter a valid id")
            continue

        else:

            pass_credit = input_credit("pass")
            defer_credit = input_credit("defer")
            fail_credit = input_credit("fail")
            total = pass_credit + defer_credit + fail_credit

            if total != 120:
                print("Total is incorrect")

            elif total == 120:

                if pass_credit == 120:
                    Progression = "Progression - " + str(pass_credit) , str(defer_credit) , str(fail_credit)
                    print('"Progress"\n')
                    Progress += 1

                elif pass_credit == 100:
                    Progression = "Progress (module trailer) - " + str(pass_credit) , str(defer_credit) , str(fail_credit)
                    print('"Progress (module trailer)"\n')
                    Trailer += 1

                elif fail_credit >= 80:
                    Progression = "Exclude - " , str(pass_credit) + str(defer_credit) , str(fail_credit)
                    print('"Exclude"\n')
                    Excluded += 1

                else:
                    Progression = "Module retriever - " + str(pass_credit) , str(defer_credit) , str(fail_credit)
                    print('"Module retriever"\n')
                    Retriever += 1

                Progression = ",".join(Progression)     # adding commas between characters.
                dictionary.update({Stu_id:Progression}) # adding the output data to the dictionary

        break


while True:
    credits()

    while True:
        preference = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
        print()

        if preference == "y":
            credits()
            continue

        elif preference == "q":
            break
        else:
            print("Please enter a valid input!\n")

    break

print("Part 04:\n")

# printing the dictionary.
for key,value in dictionary.items():
    print(key,":",value,end=" ")
