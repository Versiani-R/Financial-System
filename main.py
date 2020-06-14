from modules.database import Database
from modules.utils import *
# TODO: Make it error and idiot proof
# TODO: Format this code, and refactor it 1000 times
# TODO: After done formatting this shithole, add a bunch of comments


class System():

    def __init__(self):

        self.main_database = Database('profit_and_debt.txt')
        self.secondary_database = Database('product_sales_info.txt')

        while True:

            user_input = input('> ')
            if (user_input.lower() == 'exit'):
                return

            self.handle_input(user_input)

    def handle_input(self, user_input):

        user_input = user_input.split(' ')

        # if the user wants to read the database, and didn't specify any parameters
        # it will print out the entire database
        if (user_input[0] == 'read' and len(user_input) == 1):
            return self.main_database.read()

        # if the user wants to read the database, but specified a parameter
        elif (user_input[0] == 'read'):
            return self.main_database.read_(user_input[1])

        # TODO: Error proof: cannot type float value ( it shouldn't )
        if (user_input[0] == 'month' and user_input[1] == 'balance' and len(user_input) == 3):

            return self.main_database.get_month_balance(int(user_input[2]))

        # TODO: Check for Option 2 ( readme.txt )
        # TODO: Add an inspection first, to see if the user_input is right

        # if the user input doesn't has any of the above data
        # it wants to add a key-value to the database
        # it does some checking before and then add's it to the database
        if (len(user_input) == 4):
            profit_or_debt = user_input[0]
            value = ' '.join(user_input[1:3])
            product_code = user_input[-1]

            if (profit_or_debt == '+' or profit_or_debt == '-'):
                if ('R$' in value):
                    query = f'{profit_or_debt} {value} {product_code} {get_formated_date()}'
                    self.main_database.write(query)


if __name__ == '__main__':

    System()
