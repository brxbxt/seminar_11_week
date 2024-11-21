import os
import json
import datetime
import csv

def main_menu():
    while True:
        print('\nДобро пожаловать в Персональный помощник!')
        print('Выберите действие:')
        print('1. Управление заметками')
        print('2. Управление задачами')
        print('3. Управление контактами')
        print('4. Управление финансовыми записями')
        print('5. Калькулятор')
        print('6. Выход')
        choice = input('Введите номер действия: ')

if __name__ == '__main__':
    main_menu()