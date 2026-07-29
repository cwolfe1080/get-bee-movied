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

    # Check to see if the account has a verified email. Accounts without verified emails cannot post comments
    user.update()
    print("Checking for account email verification...")
    if not session.has_outstanding_email_confirmation :
        print("Please verify the email address associated with this account, or use another account with a verified email address.")
        exit()
    else:
        pass
    
        


    
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
