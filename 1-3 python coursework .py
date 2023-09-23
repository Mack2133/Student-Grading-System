# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221998 # Date: 19/04/2023
# UoW ID: w1985515

# initializing empty variables.
Progress = 0
Trailer = 0
Retriever = 0
Excluded = 0
Total_Outcomes = 0
Progression = " "
Progression_Data_list = []

# defining a function to check if the user input credits are in range of (0,20,40,60,80,100,120).
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

# difining a function to get the output of ( Progression,Progress (module trailer),Exclude,Do not progress – module retriever )
def Credits_Progression():
    # Converting Local Variables to Global Variables
    global Progress, Trailer, Retriever, Excluded, Progression

    while True:

        pass_credit = input_credit("pass")
        defer_credit = input_credit("defer")
        fail_credit = input_credit("fail")
        total = pass_credit + defer_credit + fail_credit

        if total != 120:
            print("Total is incorrect")

        elif total == 120:

            if pass_credit == 120:
                Progression = "Progress :"
                print('"Progress"\n')
                Progress += 1

            elif pass_credit == 100:
                Progression = "Progress (module trailer) :"
                print('"Progress (module trailer)"\n')
                Trailer += 1

            elif fail_credit >= 80:
                Progression = "Exclude :"
                print('"Exclude"\n')
                Excluded += 1

            else:
                Progression = "module retriever :"
                print('"module retriever"\n')
                Retriever += 1

            # Appending input credits and progression into Progression_Data_List
            Input_Credits = str(pass_credit), str(defer_credit), str(fail_credit)
            SingleVar = Progression, (','.join(Input_Credits))  # adding commas between input credits
            Progression_Data_list.append(SingleVar)             # appending the output to Progression_Data_list

        break


while True:
    # Student Version
    Version = input("please input the Version to continue:\nStudent Version: 1\nStaff Version: 2\nto exit: q\n\n")

    if Version == "1":
        print("=========================Student Version=========================\n")
        Credits_Progression()

    # Staff Version
    elif Version == "2":
        print("==========================Staff Version==========================\n")
        Credits_Progression()

        while True:
            preference = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
            print()

            if preference == "y":
                Credits_Progression()
                Total_Outcomes += 1
                continue

            elif preference == "q":     # if user enters quit
                break

            else:
                print("Please enter a valid input!\n")

        # Histogram

        print("---------------------------------------------------------------")
        print("Histogram\n")
        print(f'Progress {Progress} :', " ".join('*' * Progress))
        print(f'Trailer {Trailer} :', " ".join('*' * Trailer))
        print(f'Retriever {Retriever} :', " ".join('*' * Retriever))
        print(f'Exclude {Excluded} :', " ".join('*' * Excluded))
        print(f'\nTotal outcomes: {Total_Outcomes}')
        print("---------------------------------------------------------------")

        # Part 02
        print("Part 02\n")
        for lines in Progression_Data_list:
            print(*lines)           # removing unwanted brackets and commas
        print("---------------------------------------------------------------")

        # Part 03
        with open("Progression_data.txt", "w") as file:             # Saving the output to a new text file
            file.write("Part 03\n")
            file.write("---------------------------------------------------------------\n")
            for lines in Progression_Data_list:
                x = str(lines) + '\n'           # Writing Progression Data into newlines
                file.write(x.replace("'",'').replace('(','').replace(')','').replace(', ',' '))     # Removing Unwanted brackets and commas
            file.write("---------------------------------------------------------------")

    elif Version == "q":
        print('---------------------------------------------------------------')

    else:
        continue
    break
