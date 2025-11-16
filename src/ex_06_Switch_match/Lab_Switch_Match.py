print("Enter the which test case you want to run")
test_type = input("Enter the Test Type : API, UI, Security, Performance--> ")

match test_type:
    case "API":
        print("Enter we running a POSTMAN API Testcase")
    case "UI":
        print("Enter we running a Selinium Testcase")
    case "Security":
        print("Enter we running a Security Testcase")
    case "Performance":
        print("Enter we running a Performance Testcase")
    case _:
        print("Invalid Testtype")


### It will try in thw way of if_elif_else
test_type = input("Enter the Test Type : API, UI, Security, Performance--> ")

if test_type == "API":
    print("Enter we running a POSTMAN API Testcase")
elif test_type == "UI":
    print("Enter we running a Selinium Testcase")
elif test_type == "Security":
    print("Enter we running a Security Testcase")
elif test_type == "Performance":
    print("Enter we running a Performance Testcase")
else:
    print("Invalid Testtype")


day = int(input("Enter the Day \n"))
match day :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input")

