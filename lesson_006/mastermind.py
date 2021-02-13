# TODO ты тут импортируешь модуль mastermind_engine, а из него импортируешь этот модуль,
#  тут циклический импорт получается, старайся такого избегать, пусть number_us у тебя хранится в mastermind_engine
from mastermind_engine import process

print(' Ну что же сыграем в игру ')
print(' ------------------------ ')
print(' Введите четырех значное число')

number_us1 = str(input(':'))
process()
