# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:15:24 2018

@author: hayesmat
"""

class BankAccount(object):
    def __init__(self, institution, acc_num,  balance=0.00):
        self._institution = institution
        self._acc_num = acc_num
        self._balance = balance

    def deposit(self, amount):
        """make a deposit"""
        self._balance += amount

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        """check the balance"""
        return self._balance
    
    @property
    def acc_num(self):
        """check the balance"""
        return self._acc_num

    def __repr__(self):
        return '{0.__class__.__name__}(balance={0.balance})'.format(self)

    def __str__(self):
        return 'Bank account of {}, current balance: {}'.format(self.name, self.balance)
    
class CheckingAccount(BankAccount):
    def __init__(self, institution, acc_num, balance=0.00):
        BankAccount.__init__(self, institution, acc_num, balance=0.00)
        
class SavingAccount(BankAccount):
    def __init__(self, institution, acc_num, balance=0.00):
        if balance < 0.00:
            raise ValueError("Savings accounts cannot be opened with negative balance")
        BankAccount.__init__(self, institution, acc_num, balance=0.00)
        
class CreditCardAccount(BankAccount):
    def __init__(self, institution, acc_num, balance=0.00):
        BankAccount.__init__(self, institution, acc_num, balance=0.00)