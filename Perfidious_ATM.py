# Perfidious ATM

# CS 21 Group Project
# Liam Kelley aka Rhonda aka Gangles (BEWARE: Irrational fear of soft cheese)
# Shayan Amir-Kabirian the Grater

# This is an (totally legitimate) ATM

import random
import time

# read account information

# generates company name using several different company types picked randomly
def bank_name():
  # generate the random integer between 0 and 18 inclusive
  n = random.randint(0,18)

  # tuple of company entities
  title = "GmbH","AG","AG & Co. KG","LLC","ANS","LLLP","K.K.","Inc.","CVBA","Ltd.","有限公司","ApS","T:mi","Oyj","AB","شرکت","ПтК","OOO","GP/ГП"

  # concatenate the title onto the end of the bank's name and return, so that the function can be called in a print statement
  return "Perfidious Banking Group, " + title[n]

# reads previous build number from file, adds one to it, and rewrites the file; returns the new build number
def build():
  # open the build file as build_file
  build_file = open('build.txt','r')

  # read the first line from build_file, which contains the build number
  build_num = build_file.readline()

  # the first line is a string containing a new line, so that must be stripped before the string is converted to an int
  build_num = int(build_num.rstrip("\n"))

  # make the new build as one higher than previous build, read from file
  new_build = build_num + 1

  # reopen the build file as a write-only document, which erases the preexisting file
  build_file = open('build.txt', 'w')

  # write the new build number to the file, adding a new line as an unnecessary precaution
  build_file.write(str(new_build)+"\n")

  # return the new build number so that it can be printed in the intro header
  return new_build

# prints the header
def intro():
  # print ATM name, version number, and build number obtained from build()
  print("Perfidious ATM v1.0 Build", build())

  # print the bank name as determined by bank_name()
  print(bank_name())

  # print a little disclaimer, including the bank name (newly generated)
  print("\nAny damages done to life, limb, or property during the use of this Automated")
  print("Teller Machine shall not be covered by the", bank_name(),"\n")

# Check to see if a lobster has logged in
def lobsters_begone():

  # Ask the user if they are a lobster
  lobster_check = input("\nAre you a lobster? (Y/N): ")

  # If a lobster has logged in, close the program
  if lobster_check == "y" or lobster_check == "Y":
    print("\nLOBSTERS BEGONE!\n")

    # ASCII art of a lobster
    print("                              ,.---.   ")
    print("                    ,,,,     /    _ `.")
    print("                     \\\\\\\\   /      \  )")
    print("                      |||| /\/``-.__\/")
    print("                      ::::/\/_")
    print("      {{`-.__.-'(`(^^(^^^(^ 9 `.========='")
    print("     {{{{{{ { ( ( (  (   (-----:=")
    print("      {{.-'~~'-.(,(,,(,,,(__6_.'=========.")
    print("                      ::::\/\ ")
    print("                     |||| \/\ ,-`/|")
    print("                     ////   \ `` _/  )")
    print("                    ''''     \  `   /")
    print("                              `---''")

    # Lobster is a boolean which carries information as to whether the user is a
    # lobster or not
    return True

  else:
    return False

# Enter PIN with input validation
def validate_pin():
  # admin is a toggle that allows for admin features
  global admin

  #lobster is a toggle that states whether the user is a lobster; if they are, the program exits immediately
  lobster = False

  # Read PINs for admins from admin_pins.txt
  admin_pins = open('pins.txt','r')

  # take information from each line
  SHAYAN_PIN = admin_pins.readline()
  LIAM_PIN = admin_pins.readline()
  RC_PIN = admin_pins.readline()
  JACKIE_PIN = admin_pins.readline()


  # strip newline from end of each string
  SHAYAN_PIN = SHAYAN_PIN.rstrip('\n')
  LIAM_PIN = LIAM_PIN.rstrip('\n')
  RC_PIN = RC_PIN.rstrip('\n')
  JACKIE_PIN = JACKIE_PIN.rstrip('\n')

  # swiping the card simply requires them to press enter
  input("Please swipe your card. Press Enter to swipe\n")

  # input PIN as a string, so that 0001 would be valid as a PIN
  pin = input("Enter your four-digit PIN: ")

  # if the PIN entered is not one of the four valid PINs, ask for another PIN
  while pin != SHAYAN_PIN and pin != LIAM_PIN and pin != RC_PIN and pin != JACKIE_PIN:
    print("Invalid PIN")
    pin = input("Reenter your four-digit PIN: ")

  print()

  # normally the inputted pin will be for a "normal" customer, which we're assuming is Jackie
  if pin == JACKIE_PIN:
    print("Welcome Jackie Horton")
    username = "jhorton"
    admin = False
  # if not, the person must be one of the three admins, and it's easy to figure out who
  else:
    if pin == SHAYAN_PIN:
      print("Welcome Shayan")
    elif pin == LIAM_PIN:
      print("Welcome Liam")
    elif pin == RC_PIN:
      print("Welcome RC or Bloopy")
      # our friend RC has a stuffed animal lobster named bloopy. We need to ensure RC is using the ATM, not Bloopy.
      lobster = lobsters_begone()
      if lobster == False:
        print("\nWelcome RC")

    # lobster is only true if the user enters RC's pin and says they are a lobster
    if lobster == False:
      print("You have administrator privileges")

    # admin status is true in this case and username is "admin"
    admin = True
    username = "admin"

  # the function returns the username, either "jhorton" or "admin", and lobster status
  return username, lobster

# reads checking and savings account values from the appropriate account file
def read_info():
  # utilizes the global USERNAME from main() to open either jhorton.txt or admin.txt
  file = open(USERNAME + ".txt", "r")

  # read checking account and savings account as separate lines
  checking_account = file.readline()
  savings_account = file.readline()

  # strip the newline from each string and convert to float
  checking_account = float(checking_account.rstrip("\n"))
  savings_account = float(savings_account.rstrip("\n"))

  # return these values to main()
  return checking_account, savings_account

# prints Das Main Menu and asks for option
def display_menu(checking_account, savings_account):
  print("\nDAS MAIN MENÜ\n")
  print("Please select an option using your number keys\n")
  # admins have a special menu option (remember, admin is a global boolean)
  if admin:
    print("0: Administrator Options")
  print("1: Deposit")
  print("2: Withdrawal")
  print("3: Fast Cash €100")
  print("4: Check Balance")
  print("5: Transfer Balance")
  print("6: Exit\n")

  option = int(input("Enter your selection: "))

  # input validation depends on whether the user is an admin, as admins have the additional menu option
  if admin:
    # while loop for input validation
    while option < 0 or option > 6:
      print("Invalid selection")
      option = int(input("Enter your selection: "))
  else:
    # while loop for input validation
    while option < 1 or option > 6:
      print("Invalid selection")
      option = int(input("Enter your selection: "))

  # spacer line
  print()

  # pass the account information onto the desired menu option function
  # option 0 only gets this far if they are an admin, so no more validation of that is needed
  if option == 0:
    admin_menu(checking_account, savings_account)
  elif option == 1:
    deposit(checking_account, savings_account)
  elif option == 2:
    withdrawal(checking_account, savings_account)
  elif option == 3:
    fast_cash(checking_account, savings_account)
  elif option == 4:
    check_balance(checking_account, savings_account)
  elif option == 5:
    transfer(checking_account, savings_account)
  # the only other possibility is option == 6
  else:
    exit(checking_account, savings_account)

# prints the admin menu and asks for option
def admin_menu(checking_account, savings_account):
  # no need to validate anything, so the options and header are just printed
  print("\nADMINISTRATOR MENÜ\n")
  print("Please select an option using your number keys\n")
  print("1: Quick Money Laundering")
  print("2: Transfer to Cayman Account")
  print("3: Fast Embezzle €1000")
  print("4: Delete All Evidence")
  print("5: Return to Main Menü\n")

  option = int(input("Enter your selection: "))

  # while loop for validation that option is between 1 and 5
  while option < 1 or option > 5:
    print("Invalid selection")
    option = int(input("Enter your selection: "))

  # depending on the option, a menu option function is called, or the main menu is called
  if option == 1:
    money_laundering(checking_account, savings_account)
  elif option == 2:
    cayman(checking_account, savings_account)
  elif option == 3:
    embezzle(checking_account, savings_account)
  elif option == 4:
    clean_slate(checking_account, savings_account)
  elif option == 5:
    display_menu(checking_account, savings_account)

# a function that, if called, prints an infinite loop that says "meow"
def meow():
  meow = "meow"

  # an infinite loop, as meow is never changed
  while meow == "meow":
    # meow
    print(meow)

# a function that, if called, prints an infinite loop that says "Puppies!"
def conjure_puppies():
  # a universal fact
  puppy_cuteness = True

  # infinite loop, as puppy_cuteness is always True. Not always.
  while puppy_cuteness:
    print("Puppies!")


# Function that takes an amount and gives it to the admins
def give_admins(amount):
  # Open the admin account file
  file = open("admin.txt", "r")

  # read checking account and savings account as separate lines
  admin_checking = file.readline()
  admin_savings = file.readline()

  # strip the newline from each string and convert to float
  admin_checking = float(admin_checking.rstrip("\n"))
  admin_savings = float(admin_savings.rstrip("\n"))

  # Add the amount to the admin savings account
  admin_savings += amount

  # Open the file as a writable and write to it
  accounts = open("admin.txt", "w")
  accounts.write(str(format(admin_checking,'.2f')) + "\n")
  accounts.write(str(format(admin_savings,'.2f')) + "\n")

# Deposit function: Asks the user for which account they would like to
# deposit money into, and then allows the user to enter the money to be
# deposited.
def deposit(checking_account, savings_account):
  # print the selected option
  print("DEPOSIT")

  # Setting up input validation for electing to deposit again after the first
  # deposit. Set to "Y" to allow the loop to begin.
  repeat = "Y"

  # If the user wishes to deposit, the while loop loops.
  while repeat == "Y" or repeat == "y":

    # Print the two available accounts and ask the user to which they would
    # like to deposit
    print("\nPlease pick the account you would like to deposit to:")
    print("1: Checking\n2: Savings")
    option = int(input("Enter your choice: "))

    # While loop for input validation.
    while option != 1 and option != 2:
      print("\nYou entered an invalid option\nDo you even deposit\n")
      option = int(input("Enter your choice: "))

    # toggle for the later function if the user inputs a negative number
    gift = False

    # Depositing to the checking account
    if option == 1:
      phrase = "checking"
    else:
      phrase = "savings"

    # Ask for the amount
    print("\nEnter the amount to be deposited in your", phrase, "account: €",end="")
    amount = float(input(""))

    while amount <= 0:
      # If the amount is negative and the user is not an admin
      if amount < 0 and USERNAME != "admin":
        #Make amount positive
        amount = -amount
        give_admins(amount)
        print("\nYou have entered a negative amount to be deposited in your account.")
        print("\nWe assume that this entry was not a mistake, but rather your way of telling")
        print("us that you wish to deposit the money, but not put it into your account.")
        print("\nThus we have taken the €" + format(amount,',.2f') + " you deposited and added it to our accounts.")
        print("\nWe thank you on behalf of the", bank_name())
        gift = True
      else:
        print("The value deposited must be positive")
        print("\nEnter the amount to be deposited in your", phrase, "account: €",end="")
        amount = float(input(""))
        gift = False

    if gift == False:
      # Add the entered amount to the active account
      if option == 1:
        checking_account += amount
      else:
        savings_account += amount
      # Print a confimation statement that states how much money was deposited
      # into the active account
      print("€" + format(amount,',.2f') + " was deposited into your", phrase, "account")

    # Ask the user if they want to make another deposit
    repeat = input("\nDo you want to make another deposit? (Y/N): ")

    # While loop for input validation
    while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
      print("Invalid option")
      repeat = input("\nDo you want to make another deposit? (Y/N): ")

  # Pause in the program, asking the user to press enter to continue
  input("\nPress Enter to return to Main Menu")
  # Call the display menu and give it checking_account and savings_account
  display_menu(checking_account, savings_account)

# Withdrawal function: Allows the user to withdraw money from either account
def withdrawal(checking_account, savings_account):
  # Print the current menu
  print("FÜND WITHDRAWAL")

  # Setting up input validation for electing to deposit again after the first
  # deposit. Set to "Y" to allow the loop to begin.
  repeat = "Y"

  # While loop for input validation
  while repeat == "Y" or repeat == "y":
    # Ask the user which account they would like to withdraw from
    print("\nPlease pick the account you would like to withdraw from:")
    print("1: Checking \n2: Savings")
    option = int(input("\nEnter your choice: "))

    # While loop for input validation
    while option != 1 and option != 2:
      print("You entered an invalid option\n")
      option = int(input("Enter your choice: "))

    # Give the user pre-determined withdrawal options, or give the option to
    # enter a custom amount.
    print("Please pick the amount of money to be withdrawn:")
    print("1: €20\n2: €40\n3: €60\n4: €240\n5: Custom Amount")
    amount_option = int(input("\nPlease enter your choice: "))

    # While loop for input validation.
    while amount_option != 1 and amount_option != 2 and amount_option != 3 and amount_option != 4 and amount_option != 5:
      print("Nay, thy option doth be invalid")
      amount_option = int(input("\nPlease enter your choice: "))

    # Amount if-elif-else statements
    if amount_option == 1:
      # Set the variable amount to 20, and different amounts for the other options
      amount = 20
    elif amount_option == 2:
      amount = 40
    elif amount_option == 3:
      amount = 60
    elif amount_option == 4:
      amount = 240

    elif amount_option == 5:
      # If the user selects custom withdrawal, ask the user for the custom
      # amount which is a multiple of 20
      custom_withdraw = float(input("\nEnter the custom amount to be withdrawn (must be a multiple of 20): €"))

      # While loop to validate that the custom amount is a multiple of 20
      while (custom_withdraw % 20) != 0 or custom_withdraw <= 0:
        if (custom_withdraw % 20) != 0:
          print("The value withdrawn must be a multiple of €20")
        if custom_withdraw <= 0:
          print("The value withdrawn must be above zero.")
        if custom_withdraw < 0:
          print("If you are looking to withdraw negative money, perhaps try deposit instead")
        custom_withdraw = float(input("\nEnter the custom amount to be withdrawn (must be a multiple of 20): €"))

      # Set the amount to the custom entered amount
      amount = custom_withdraw

    # If-else statement to withdraw from the account selected by the user at
    # the beginning of the function
    # Checking account:
    if option == 1:
      # Check if the user has enough money in their checking account to do
      # the transaction
      if checking_account >= amount:
        # If there is enough money, subtract the amount from the checking
        # account
        checking_account -= amount
        # Print a confirmation statement with the amount withdrawn
        print("€" + format(amount, ',.2f') + " was withdrawn from your checking account.")
      else:
        # Tell the user if they do not have enough money to withdraw the
        # specified amount
        print("You do not have enough money in your checking account to withdraw €" + format(amount,',.2f'))

    # Savings account:
    else:
      # Check if the user has enough money in their savings account to
      # do the transaction
      if savings_account >= amount:
        # If the user has enough money in their savings account, subtract the
        # amount from the savings account
        savings_account -= amount
        # Print a confirmation statement
        print("€" + format(amount, ',.2f') + " was withdrawn from your savings account.")
      else:
        # Tell the user if they do not have enough money in their savings
        # account
        print("You do not have enough money in your savings account to withdraw €" + format(amount,',.2f'))

    # Ask the user if they would like to make another withdrawal
    repeat = input("\nDo you want to make another withdrawal? (Y/N): ")
    # If the user enters "Y" or "y" the while loop at the beginning of the
    # function repeats

    # while loop for input validation
    while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
      print("Invalid option")
      repeat = input("\nDo you want to make another withdrawal? (Y/N): ")

  # Pause in the program, asking the user to press enter to continue
  input("\nPress Enter to return to Main Menu")
  # Call the display menu and give it checking_account and savings_account
  display_menu(checking_account, savings_account)

# Fast Cash function. Gives the user 100 Euros of cash from their checking
# account if they have the fundz
def fast_cash(checking_account, savings_account):
  # Check to see if the user has 100 Euros in the account
  if checking_account >= 100:
    # Subtract 100 Euros from the checking account
    checking_account -= 100
    # Print a confirmation of the withdrawal
    print("€100 withdrawn from your checking account.")
  # If the user does not have enough money in their account
  else:
    # Tell the user that they do not have enough money in the checking account
    print("You do not have enough money in your checking account. You need at least €100 in your account to withdraw €100.")

  # Pause in the program, asking the user to press enter to continue
  input("\nPress Enter to return to Main Menu")
  # Call the display menu and give it checking_account and savings_account
  display_menu(checking_account, savings_account)

# Function to check balances. Is given checking_account and savings_account
# data from the main menu function
def check_balance(checking_account,savings_account):
  # All this function does is print the current account balances in a fancy
  # way. It then returns the user to the main menu
  print("BALANCES")
  print()
  print("CHECKING ACCOÜNT")
  print("Balance: €",format(checking_account,',.2f'),sep="")
  print()
  print("SAVINGS ACCOÜNT")
  print("Balance: €",format(savings_account,',.2f'),sep="")
  print()

  # Pause in the program, asking the user to press enter to continue
  input("\nPress Enter to return to Main Menu")
  # Call the display menu and give it checking_account and savings_account
  display_menu(checking_account, savings_account)

# Transfer function. Allows the user to transfer money between accounts
def transfer(checking_account, savings_account):
  print("INTER-ACCOÜNT FÜND TRANSFERS")

  # Setting up input validation for electing to deposit again after the first
  # deposit. Set to "Y" to allow the loop to begin.
  repeat = "Y"

  # While the user wished to do transfers
  while repeat == "Y" or repeat == "y":
    # Ask the user which one of the the accounts they would like to
    # transfer from.
    print("\nFrom which account would you like to transfer funds?")
    print("1: Checking to Savings \n2: Savings to Checking")
    t_option = int(input("\nEnter your choice: "))

    # While loop for input validation
    while t_option != 1 and t_option != 2:
      print("Invalid option")
      t_option = int(input("\nEnter your choice: "))

    # Checking to savings
    if t_option == 1:
      t_amount = float(input("Enter the amount you want to transfer to Savings: €"))

      # While loop for input validation
      while t_amount <= 0:
        print("The amount must be a positive number greater than zero")
        t_amount = float(input("\nEnter the amount you want to transfer to Savings: €"))

      # The actual transfer, if the user has enough money
      if checking_account >= t_amount:
        checking_account -= t_amount
        savings_account += t_amount
        print("€" + format(t_amount,',.2f') + " was transferred from Checking to Savings")
      # If the user has no money
      else:
        print("You do not have enough money in your Checking Account to transfer €" + format(t_amount,',.2f'))

    # Savings to checkings
    elif t_option == 2:
      t_amount = float(input("Enter the amount you want to transfer to Checking: €"))

      # While loop for input validation
      while t_amount <= 0:
        print("The amount must be a positive number greater than zero")
        t_amount = float(input("\nEnter the amount you want to transfer to Savings: €"))

      # The actual transfer, if the user has enough money
      if savings_account >= t_amount:
        savings_account -= t_amount
        checking_account += t_amount
        print("€" + format(t_amount,',.2f') + " was transferred from Savings to Checking")
      # If the user has no money
      else:
        print("You do not have enough money in your Savings Account to transfer €" + format(t_amount,',.2f'))

    # Ask the user if they want to make another transfer
    repeat = input("\nWould you care to make another transfer? (Y/N): ")

    # While loop for input validation
    while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
      print("Invalid option")
      repeat = input("\nWould you care to make another transfer? (Y/N): ")

  # Pause in the program, asking the user to press enter to continue
  input("\nPress Enter to return to Main Menu")
  # Call the display menu and give it checking_account and savings_account
  display_menu(checking_account, savings_account)

# Exit function. Writes the new checking and savings balances and says
# goodbye
def exit(checking_account, savings_account):
  # Open the user file as a writable file
  accounts = open(USERNAME + '.txt', 'w')
  # Write the new balances to the text file
  accounts.write(str(format(checking_account,'.2f')) + "\n")
  accounts.write(str(format(savings_account,'.2f')) + "\n")
  # Say goodbye
  print("\n\nThank you for using", bank_name())
  print("A division of the Comcast Corporation",sep="\n")

# Money laundering function. Acts as a withdrawal function
def money_laundering(checking_account, savings_account):
  print("\nMONEY LAÜNDERING\n")
  print("Please select an account whence to launder money\n")
  print("1: Checkings Account")
  print("2: Savings Account\n")

  # Ask the admin from which account they would like to launder
  option = int(input("Enter your selection: "))

  # While loop for input validation
  while option != 1 and option != 2:
    print("Invalid option")
    option = int(input("Enter your selection: "))

  # If the admin choses the checking account
  if option == 1:
    print("\nEnter amount to be laundered from checking account")
    # Ask the admin for the amount to be laundered
    amount = float(input("Amount: €"))

    # While loop for input validation
    while amount < 0 or amount > checking_account:
      if amount < 0:
        print("\nAmount must be greater than zero\n")
        amount = float(input("Please reenter amount to be laundered: €"))

      # Check if the admin account has enough money
      if amount > checking_account:
        print("\nYou do not have that much in your checking account")
        print("You may launder up to €" + format(checking_account,',.2f'))
        amount = float(input("Please reenter amount to be laundered: €"))

    # Print a confirmation about how much money the admin has laundered
    print("\n€" + format(amount,',.2f') + " has been laundered from your checking account")
    # Subtract the amount to be laundered from the checking account
    checking_account -= amount

  # If the admin choses to launder from the savings account
  elif option == 2:
    # Ask the user how much to launder
    print("\nEnter amount to be laundered from savings account")
    amount = float(input("Amount: €"))

    # While loop for input validation
    while amount < 0 or amount > savings_account:
      if amount < 0:
        print("\nAmount must be greater than zero\n")
        amount = float(input("Please reenter amount to be laundered: €"))

      # Check if the admin account has enough money
      if amount > checking_account:
        print("\nYou do not have that much in your savings account")
        print("You may launder up to €" + format(savings_account,',.2f'))
        amount = float(input("Please reenter amount to be laundered: €"))

    # Print a confirmation of the money laundered.
    print("\n€" + format(amount,',.2f') + " has been laundered from your checking account")
    savings_account -= amount

  # Repeat
  repeat = input("\nWould you like to launder more money? (Y/N): ")

  # While loop for input validation
  while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
    print("Invalid option")
    repeat = input("Would you like to launder more money? (Y/N): ")

  # If-elif to check which option the user entered
  if repeat == "Y" or repeat == "y":
    money_laundering(checking_account, savings_account)

  elif repeat == "N" or repeat == "n":
    print("\nThank you for using this money laundering service, brought to")
    print("you by our colleagues at Saul Goodman & Associates")

    # Return to the admin menu
    input("\nPress Enter to return to Admin Menu")
    admin_menu(checking_account, savings_account)


# Function to transfer money to an offshore account
def cayman(checking_account, savings_account):
  print("\nTRANSFER TO CAYMAN ISLAND ACCOÜNT\n")

  # Repeat Setup
  repeat = "Y"

  # While loop for repetition
  while repeat == "Y" or repeat == "y":
    # Ask the admin which account they would like to transfer money from
    print("Please select an account whence to transfer money offshore\n")
    print("1: Checkings Account")
    print("2: Savings Account\n")
    option = int(input("Enter your selection: "))

    # While loop for input validation
    while option != 1 and option != 2:
      print("Invalid option")
      option = int(input("Enter your selection: "))

    # From checking
    if option == 1:
      print("E\nnter amount to be transferred from checking account")
      amount = float(input("Amount: €"))

      # While loop for input validation
      while amount < 0 or amount > checking_account:
        if amount < 0:
          print("\nAmount must be greater than zero\n")
          amount = float(input("Please reenter amount to be transferred: €"))

          # Check if the admin has enough money
          if amount > checking_account:
            print("\nYou do not have that much in your checking account")
            print("You may transfer up to €" + format(checking_account,',.2f'))
            amount = float(input("Please reenter amount to be transferred: €"))

      # Print a confirmation
      print("\n€" + format(amount,',.2f') + " has been transferred from your checking account")
      # Do math
      checking_account -= amount

    # Savings
    elif option == 2:
      # Ask the admin how much they would like to transfer
      print("\nEnter amount to be transferred from savings account")
      amount = float(input("Amount: €"))

      # While loop for input validation
      while amount < 0 or amount > savings_account:
        if amount < 0:
          print("\nAmount must be greater than zero\n")
          amount = float(input("Please reenter amount to be laundered: €"))

        # Check if the user has enough money
        if amount > checking_account:
          print("\nYou do not have that much in your savings account")
          print("You may transfer up to €" + format(savings_account,',.2f'))
          amount = float(input("Please reenter amount to be transferred: €"))

      # Print a confirmation and do math
      print("\n€" + format(amount,',.2f') + " has been transferred from your checking account")
      savings_account -= amount

    # Ask the admin if they would like to transfer more money offshore
    repeat = input("\nWould you like to transfer more money? (Y/N): ")

  # While loop in input validation
  while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
    print("Invalid option")
    repeat = input("Would you like to transfer more money? (Y/N): ")

  # To return to the admin menu
  input("\nPress Enter to return to Admin Menu")
  admin_menu(checking_account, savings_account)

# Embezzle function for admins
def embezzle(checking_account, savings_account):
  # Embezzling constant
  EMBEZZLE_AMOUNT = 1000

  repeat = "Y"

  # Menu name, with spacing
  print("\nEMBEZZLE MENÜ")

  # begin the while loop of embezzling awesomness
  while repeat == "Y" or repeat == "y":
    # Ask the user which account they would like to embezzle
    print("\nWhich account would you like to benefit from a nice embezzling?")
    print("1: Checkings Account")
    print("2: Savings Account\n")
    option = int(input("Enter your selection: "))

    # While loop for input selection
    while option != 1 and option != 2:
      print("Invalid option")
      option = int(input("Enter your selection: "))

    # If the admin selects checking
    if option == 1:
      # Add 1000 euros to checking
      checking_account += EMBEZZLE_AMOUNT
      print("€1000 added to your checking account from the bank accounts of")
      print("poor and (probably) starving people")
    # If the admin selects savings
    elif option == 2:
      # Add 1000 Euros to savings
      savings_account += EMBEZZLE_AMOUNT
      print("€1000 added to your savings account from the bank accounts of")
      print("poor and (probably) starving people")

    # Ask the admin whether they would like to embezzle some more
    repeat = input("\nWould you like to embezzle more money? (Y/N): ")

    # While loop for input validation
    while repeat != "Y" and repeat != "y" and repeat != "N" and repeat != "n":
      print("Invalid option")
      repeat = input("Would you like to embezzle again? (Y/N): ")

  # The admin wishes to be returned to the admin menu on a comfortable
  # cushion stuffed with embezzled €500 notes.
  input("\nPress Enter to return to Admin Menu")
  admin_menu(checking_account, savings_account)

# Destroy all evidence of illegal shenanigans
def clean_slate(checking_account, savings_account):
  # Tell the admin about the function, and ask the admin to confirm
  print("\nCLEAN SLATE PROGRAM\n")
  print("This deletes all account information and then initiates a self destruct sequence at this ATM")
  print("To continue, enter the code HOOVER into the box below")
  print("Entering any other code will revert to the Admin Menu")
  code = input("Code: ")

  # the code HOOVER is a reference to a character in Breaking Bad that helps people get a clean slate and disappear
  # If the code is correct
  if code == "HOOVER":
    # Write empty values to the file
    accounts = open(USERNAME + '.txt', 'w')
    accounts.write("0\n")
    accounts.write("0\n")

    #Tell the user that the program will self destruct
    print("Account information wiped")
    print("Self destruct initiated")

    # Count down to self destruct
    for n in range(10,0,-1):
      print(n)
      time.sleep(1)

    # Self destruct
    print("\insert{fiery explosion}")
  else:
    # If the end of the world was not selected, return to admin menu
    print("Reverting to Admin Menu in ",end="")
    for n in range(3,0,-1):
      print(n,"... ",sep="",end="")
      time.sleep(1)
    print()
    admin_menu(checking_account,savings_account)

# Main
def main():
  # Make USERNAME global. Used for admin related things
  global USERNAME
  # print header
  intro()

  # Set username and lobster equal to what validate_pin gives ya
  USERNAME, lobster = validate_pin()

  # the main menu is only displayed if the user is *not* a lobster
  if lobster == False:
    # *read_info() destructures the tuple returned by read_info(), allowing for the function call inside of display_menu()
    display_menu(*read_info())

# run the program
main()
