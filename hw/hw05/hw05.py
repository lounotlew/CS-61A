def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    attempted_passwords = []

    def withdraw(amount, input_password):
        nonlocal balance, password

        if len(attempted_passwords) == 3:
            return 'Your account is locked. Attempts: ' + str(attempted_passwords)

        if password == input_password:
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance = balance - amount
                return balance

        if input_password != password:
            attempted_passwords.append(input_password)
            return 'Incorrect password'

    return withdraw

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    access_denied = withdraw(0, old_password)

    if type(access_denied) == str:
        return access_denied

    def joint_account(amount, attempted_password):
        if attempted_password == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, attempted_password)

    return joint_account

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, price):
        self.balance = 0
        self.product = product
        self.stock = 0
        self.price = price

    def vend(self):
        message = 'Here is your {0}'.format(self.product)
        change = self.price - self.balance

        if self.stock == 0:
            return 'Machine is out of stock.'

        if self.balance < self.price:
            return 'You must deposit ${0} more.'.format(change)

        if change != 0:
            message = message + ' and ${0} change'.format(-change)

        self.balance = 0
        self.stock = self.stock - 1
        
        return message + '.'

    def deposit(self, deposit):
        if self.stock == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(deposit)

        self.balance = self.balance + deposit
        return 'Current balance: ${0}'.format(self.balance)

    def restock(self, stock):
        self.stock = self.stock + stock
        return 'Current {0} stock: {1}'.format(self.product, self.stock)

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    def __init__(self, goal):
        self.goal = goal

    def ask(self, message, *args):
        magic_word = 'please '

        if not message.startswith(magic_word):
            return 'You must learn to say please first.'

        atr = message[len(magic_word):]

        if not hasattr(self.goal, atr):
            return 'Thanks for asking, but I know not how to ' + atr

        return getattr(self.goal, atr)(*args)
