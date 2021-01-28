# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:36:46 2021

@author: tommywha
"""


class shopping_cart():

    def __init__(self, shopping_list=[]):
        self.shopping_list = shopping_list 
        
    def add_to_cart(self, item):
        menu = ['egg', 'bread', 'french toast','avocado','sweet potato']
        if item in menu:
            self.shopping_list.append(item.lower())
            print(f'\n{item.title()} has been added to your shopping cart.\n')
        else:
            print('\nThat is not on the menu for today.\n')
            print('\nHere are the items that are currently being served today:\n')
            for idx, food in enumerate(menu):
                print(f'{idx+1}. {food}')
            
    def remove_from_cart(self, item):
        menu = ['egg', 'bread', 'french toast','avocado','sweet potato']
        if item.lower() in self.shopping_list:
            self.shopping_list.remove(item)
            print(f'\n{item.title()} has been removed from your shopping cart.\n')
        else:
            print('\nThat item is not in your cart.\n')
            print('\nBelow is the list of items in your shopping cart:\n')
            for i in set(self.shopping_list):
                print(str(self.shopping_list.count(i)) + " " + i.title() + '(s)')           
            
            
    def items_in_cart(self):
        if self.shopping_list == []:
            print('\nYour shopping cart is currently empty.\n')
        else:
            print('\nBelow is the list of items in your shopping cart:\n')
            for i in set(self.shopping_list):
                print(str(self.shopping_list.count(i)) + " " + i.title() + '(s)')
        
