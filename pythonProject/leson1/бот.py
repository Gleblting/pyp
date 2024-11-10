import random
tag = '@bot'
text = input('vvedite @bot')
facts = [
"Кошки спят в среднем 13-14 часов в день.",
"Слоны могут слышать звуки на расстоянии до 4 километров.",
"Человеческое сердце создает достаточно давления, чтобы выбросить кровь на высоту до 10 метров."
]
if text == tag:
	random_fact = random.choice(facts)
	print(random_fact)
