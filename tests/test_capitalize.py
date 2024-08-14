from capitalize import capitalize

assert capitalize('hello') == 'Hello'
assert capitalize('') == ''
assert capitalize('hello') == 'hello'

print('Все тесты пройдены!')

# run = PYTHONPATH=package_name python3 tests/test_capitalize.py
