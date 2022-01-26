# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#           Например:
#>>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]
#Документировать код функции.
#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
#(когда каждое слово можно использовать только в одной шутке)?
#можете ли вы сделать аргументы именованными?
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "светит"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "туман", "днем"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(numberofjokes, unique=True):
    """функция возвращающая количество(numberofjokes) шуток по заданным спискам"""
    for i in range(numberofjokes):
        if unique is False:
            jokes = []
            x = random.choice(nouns)
            a = random.choice(adverbs)
            b = random.choice(adjectives)
            jokes.append(x)
            jokes.append(a)
            jokes.append(b)
            print(jokes)
        elif unique is True:
            unique_jokes = []
            x = random.choice(nouns)
            a = random.choice(adverbs)
            b = random.choice(adjectives)
            unique_jokes.append(x)
            unique_jokes.append(a)
            unique_jokes.append(b)
            nouns.remove(x)
            adverbs.remove(a)
            adjectives.remove(b)
            print(unique_jokes)
get_jokes(45, False)


