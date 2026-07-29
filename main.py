import scratchattach as sa
import time

def execute():
    # Get credentials from user
    uname = input("Enter Scratch username: ")
    pswd = input("Enter Scratch password: ")

    # Login to scratch using provided credentials
    session = sa.login(f"{uname}", f"{pswd}") #Returns a sa.Session object


    
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
