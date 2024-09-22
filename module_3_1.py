from pipenv.cli.command import update
from tomlkit import string

calls = 0  # звонки

def count_calls():     #количество_вызовов
    global calls
    calls += 1


def string_info(string): # информация о строке string
    count_calls()
    num = len(string)
    up = string.upper()
    low_ = string.lower()
    name = (num,  up, low_)
    return (name)


def is_contains(string, list_to_search):   #string   list_to_search(список_для_поиска)
    count_calls()
    bool_ = False
    str1 = string.upper()
    for _ in range(len(list_to_search)):
        str = list_to_search[_]
        str = str.upper()
        if str1 == str:
            bool_ = True
            break
    return (bool_)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
