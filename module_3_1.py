calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = (len(string), string.upper(), string.lower())
    count_calls()
    return string

def is_contains(string, _list):
    count_calls()
    _list = [index.lower() for index in _list]
    if string.lower() in _list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)