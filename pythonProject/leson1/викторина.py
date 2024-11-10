questions = {
	"Как называется столица Франции?": "Париж",
	"Сколько планет в Солнечной системе?": "Восемь",
	"Как называется жидкость, заполняющая глазное яблоко?": "Слеза"
}

score = 0

for question, answer in questions.items():
	user_answer = input(question)
	if user_answer.lower() == answer.lower():
		print("Правильно!")
		score += 1
	else:
		print("Неправильно. Правильный ответ:", answer)

print("Итоговый счет:", score)