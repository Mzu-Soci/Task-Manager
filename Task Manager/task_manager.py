# print to screen formating function for reviewing tasks
def print_to_screen(line_split):
    print("_______________________________________________________________")
    print(f"Task:\t \t \t {line_split[1].strip()}")
    print(f"Assigned to:\t \t {line_split[0].strip(',')}")
    print(f"Date assigned:\t \t {line_split[4].strip()}")
    print(f"Due date:\t \t {line_split[3].strip()}")
    print(f"Task Complete?\t \t {line_split[5].strip()}")
    print(f"Task Description:\t {line_split[2].strip()}")
    print("_______________________________________________________________")

# User name an password verification check
def login(login_user_name):
    login_user_password = input("Enter User Password: ").lower()

    # usr password and user account variable status
    user_in_list = False
    password_in_list = False

    # open file user.txt and read 
    with open("user.txt", "r") as file:
        for line in file:
            # Get user login name an password
            login_account = line.split()
            user_name = login_account[0].strip(",")
            user_password = login_account[1]

            # check if user_name from file and from user are correct
            if user_name.lower() == login_user_name:
                user_in_list = True
                if user_password.lower() == login_user_password:
                    password_in_list = True

    # If user name and password are correct update update user account variable status
    if user_in_list == True and password_in_list == True:
        print("_______________________________________________________________")
        print("Welcome to the Task Manager App")

    # if user name and password are incorrect display message and exit program
    else:
        print("_______________________________________________________________")
        print("Your user name or password is incorrect")
        print("_______________________________________________________________")
        exit()

# message to display when user is not admin
def admin_check_message():
            print("_______________________________________________________________")
            print("You must login as Administrator to perfom this action")
            print("_______________________________________________________________")
            login_user_name = input("Enter User Name: ").lower()
            login(login_user_name)
    
# Import datetime library for determining completion time
import datetime
from collections import Counter

# create empty username variable
login_user_name = ""

# request user for user name
login_user_name = input("Enter User Name: ").lower()

# password verification check
login(login_user_name)

# display user options
while True:

    # variable for non admin user menu
    menu_list = '''_______________________________________________________________
Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks'''

    # admin user stats view option
    admin_option = "vs - veiw stats"

    # Present the menu to the user (for admin and non admin) and 
    # make sure that the user input is converted to lower case.
    if login_user_name != "admin":
        menu = input(f"{menu_list}\ne - exit\n: ").lower()
    else:
        menu = input(f"{menu_list}\n{admin_option}\ne - exit\n: ").lower()

    if menu == 'r':
        # if user is not admin no user registration is allowed, display message
        if login_user_name != "admin":
            admin_check_message()

        else:          
            # prompt admin for new user and password details
            user_name = input("Enter user name: ")
            password = input("Enter password: ")
            password_check = input("Confirm password: ")
        
            # check if passwords match and add user to user.txt file, if not display message
            if password == password_check:
                with open("user.txt", "a") as file:
                    file.write(f"\n{user_name}, {password}")
            else:
                print("The password you entered did not match.")

    elif menu == 'a':
        # Request user for assignee, title and description of task
        assigned_user = input("Assigned user: ")
        title = input("Task title: ")
        description = input("Task Description: ")

        # Request user number of days till due date and set due date
        days_due = int(input("When is it due (in days): "))
        tdelta = datetime.timedelta(days=days_due)    
        
        # compose format for current days date
        date = datetime.date.today()
        day =  date.strftime("%d")
        month = date.strftime("%B")
        year = date.strftime("%Y")
        today_date_name = str(f"{day} {month} {year}")
        
        # compose format for due date
        date_due = date + tdelta
        due_day =  date_due.strftime("%d")
        due_month = date_due.strftime("%B")
        due_year = date_due.strftime("%Y")
        due_date_name = str(f"{due_day} {due_month} {due_year}")

        # request user for competion status
        is_complete = input("Is the task complete? \"Y\" or \"N\": ").lower()

        # structure a variable for new task
        task_update = f"{assigned_user}, {title}, {description}, {due_date_name}, {today_date_name}"

        # open tasks.txt file and update with task information including completion status
        with open("tasks.txt", "a") as file:
            if is_complete == "n":
                file.write(f"\n{task_update}, No")
            else:
                file.write(f"\n{task_update}, Yes")

    elif menu == 'va':
        # open and read tasks.txt file and display view all tasks
        with open("tasks.txt", "r") as file:
            for line in file:
                line_split = line.split(",")
                # call print_to_screen formating function to display on screen
                print_to_screen(line_split)

    elif menu == 'vm':
        # open and read tasks.txt file and split lines at the commas
        with open("tasks.txt", "r") as file:
            for line in file:
                line_split = line.split(",")
                # get assignee name form task
                assignee = line_split[0].strip(",")
                # print task only for the logged in user
                if login_user_name.lower() == assignee.lower():
                    print_to_screen(line_split)
                    
    elif menu == 'vs':
        # Check if user is admin, display message
        if login_user_name != "admin":
            admin_check_message()

        # open and read tasks.txt file and split lines at the commas
        with open("tasks.txt", "r") as file:

            # variables for tasks and assignees counters
            task_count = 0
            assignee_list = []

            for line in file:
                line_split = line.split(",")
                # add assignee to assignee list
                assignee_list.append(line_split[0].strip(","))
                # add 1 to task counter
                task_count += 1

        # print stats view
        print("_______________________________________________________________")
        print("Stats View")
        print("_______________________________________________________________")
        print(f"Total number of Tasks:\t {task_count}")
        print(f"Number of Assignees:\t {len(Counter(assignee_list))}")
        print("_______________________________________________________________")


    elif menu == 'e':
        # print on screen and exit program
        print('Goodbye!!!')
        exit()

    # display message on wrong menu option
    else:
        print("You have not selected the correct option, please try again")