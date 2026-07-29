import scratchattach as sa
import time
import getpass

def execute():
    # Get credentials from user
    uname = input("Enter Scratch username: ")
    pswd = getpass.getpass("Enter Scratch password: ")

    print("Logging in...")
    # Login to scratch using provided credentials
    session = sa.login(f"{uname}", f"{pswd}") #Returns a sa.Session object

    # Refresh account data
    print("Fetching account data...")
    session.update()


    # Check to see if the account has a verified email. Accounts without verified emails cannot post comments
    print("Checking for account email verification...")
    if not session.email:
        print("Please verify the email address associated with this account, or use another account with a verified email address.")
        exit()
    else:
        pass
    # Check to see if account is banned
    print("Checking if account is banned...")
    if session.banned:
        print("The Scratch account that you signed in with is banned.")
    else:
        pass

    # Sign in the user using the session data above
    print("Connecting to user...")
    user = session.connect_linked_user()
    # Fetch new user data
    print("Fetching user data...")
    user.update()

    # NOTE: I'm not sure what the difference between the user and session things are. I'm pretty sure that user is needed for comments and things like that, whereas session is needed for cloud variables. Not sure that I need to login the session, but oh well, maybe we'll need it later in the project, but for now I'm going to leave it there.

    
        


    
# Startup
print("get-bee-movied by cwolfe1080 under the Apache License 2.0")
time.sleep(1)
print("==============================================================")
print("NOTE:")
print("This script DOES NOT store any personal information")
print("Executing this script may result in temporary bans on Scratch.")
print("By executing this script, you assume full responsibility for the actions that it executes.")
print("==========================================================================================")
first = input("Do you wish to continue? (y/n) ")
if first == "yes" or first == "y":
    execute()
else:
    exit()
