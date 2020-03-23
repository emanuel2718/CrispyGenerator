#!/bin/bash

from time import sleep
import math
import random

# Created by Emanuel Ramirez on 03/23/2020


def main():
    """Simple cli-password generator script."""

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'\
            + '!@&$%^*-()+'

    pass_amount = int(input('Please enter how many passwords would you like: '))
    pass_length = int(input('Length of the password(s): '))

    password_list = []
    for i in range(pass_amount):
        password = ""
        for i in range(pass_length):
            password += random.choice(chars) # Get a random letter.
        password_list.append(password)

    print('------------------------------')
    for i in range(len(password_list)):
        print('Password:', password_list[i])
    print('------------------------------')


def welcome_screen():
    """Print the welcome screen to the user."""

    print('\n')
    print(' -----------------------------------')
    print('|                                   |')
    print('|    Welcome to Crispy Generator    |')
    print('|        by Emanuel Ramirez         |')
    print('|                                   |')
    print(' -----------------------------------')
    print('\n')


if __name__ == '__main__':
    welcome_screen()
    main()

