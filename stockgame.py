# Sim Game of Buy and Sell Stocks

# get json module
import json


# begin the game overall to choose between a new game or continue a saved file
def begin():
        selection = str(input('new or continue? '))
        if selection == 'new':
            return new()
        elif selection == 'continue':
            return load()
        else:
            print('choose "new" or "continue" only')


# new game file
def new():
    # begin by stating how much funds we want to start game with
    money = input('starting funds? ')
    portfolio['funds'] = float(money)


# our save file function; saving it as a json file
def save():
    # create json object from dictionary/serializing json
    json_object = json.dumps(portfolio, indent=4)

    # writing to .json file, 'w'; using 'with' will automatically close file without the need to code in .close()
    with open('portfolio.json', 'w') as outfile:
        outfile.write(json_object)


# our load file function; load json file as dict
def load():
    while True:
        try:
            # opening json file
            with open('portfolio.json', 'r') as openfile:

                # reading from json file
                portfolio = json.load(openfile)
        
        # while true, try, except, and return in load() function is used to catch if there is no saved file exists
        except FileNotFoundError:
            print('No Saved File. Please select new!')

        return begin()
    

# close = saves and close file/game
def close():
    save()


# view portfolio
def view():
    print(portfolio)
    transaction()
        
# our buy function
def buy():
    ticker = input('buying ticker? ')
    quantity = input('buying quantity? ')
    price = input('buying price? ')
    if portfolio.get('funds') - float(float(price)*float(quantity)) < 0: # <-- make sure we have funds to buy the stock
        print('Insufficient funds')
        transaction()
    elif ticker in portfolio:
        portfolio[ticker] = portfolio.get(ticker) + int(quantity) # <-- adds quantity to stock already in portfolio
        portfolio['funds'] = portfolio.get('funds') - float(float(price)*float(quantity)) # <-- subtracts money from our funds
        print('quantity updated')
        save()
        transaction()
    else:
        portfolio[ticker] = int(quantity) # <-- adds new stock to portfolio; append new key:value to dictionary
        portfolio['funds'] = portfolio.get('funds') - float(float(price)*float(quantity)) # <-- subtracts money from our funds
        print('quantity updated')
        save()
        transaction()

# our sell function. still need to fix so we can't sell funds itself.
def sell():
    ticker = input('selling ticker? ')
    if ticker in portfolio: # <-- checks to see if we own the stock in our portfolio
        quantity = input('selling quantity? ')
        if portfolio.get(ticker) - int(quantity) < 0: # <-- checks to see if we own the quantity of stock to sell
            print('insufficient stock quantity')
            transaction()
        elif portfolio.get(ticker) - int(quantity) == 0: # <-- if selling all quantity of said stock
            price = input('selling price? ')
            portfolio['funds'] = portfolio.get('funds') + float(float(price)*float(quantity))# <-- adds money to our funds
            del portfolio[ticker] # <-- removing the stock from portfolio
            print('sale successful')
            save()
            transaction()
        else:
            price = input('selling price? ')
            portfolio[ticker] = portfolio.get(ticker) - int(quantity) # <-- subtracts the quantity of stock from portfolio
            portfolio['funds'] = portfolio.get('funds') + float(float(price)*float(quantity))# <-- adds money to our funds
            print('sale successful')
            save()
            transaction()
    else:
        print("Don't own stock")
        transaction()


# loop function to buy, sell, and save
def transaction():
    choice = str(input('buy, sell, view, or close? '))
    if choice == 'buy':
        return buy()
    elif choice == 'sell':
        return sell()
    elif choice == 'view':
        return view()
    elif choice == 'close':
        return close()
    else:
        print('Please select only one of the following...')
        transaction()

# testing our function


# START GAME
# begin with an empty portfolio in form of a dictionary
portfolio = {}

# beginning the game
begin()

print(portfolio)

transaction()

print(portfolio)
