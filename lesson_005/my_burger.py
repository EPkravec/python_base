# -*- coding: utf-8 -*-

def cheeseburger():
    print('Рецепт чисбургера:')
    bun()
    cutlet()
    cheese()
    cucumber()
    tomato()
    mayonnaise()
    return

def doublecheeseburger():
    print('Рецепт даблчисбургера:')
    bun()
    cutlet()
    cheese()
    cucumber()
    tomato()
    mayonnaise()
    bun()
    cutlet()
    cheese()
    cucumber()
    bun()
    return

def bun():
    return print("А теперь добавим булочку")

def cutlet():
    return print("А теперь добавим котлету")

def cucumber():
    return print("А теперь добавим огурчик")

def tomato():
    return print("А теперь добавим помидорчики")

def mayonnaise():
    return print("А теперь добавим майонез")

def cheese():
    return print("А теперь добавим сыр")

cheeseburger()
doublecheeseburger()