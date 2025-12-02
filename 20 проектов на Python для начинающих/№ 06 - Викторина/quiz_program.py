quiz = {
    "question1": {
        "question": "Столица Франции?",
        "answer": "Париж"
    },
    "question2": {
        "question": "Столица Германии?",
        "answer": "Берлин"
    },
    "question3": {
        "question": "Столица Италии?",
        "answer": "Рим"
    },
    "question4": {
        "question": "Столица Испании?",
        "answer": "Мадрид"
    },
    "question5": {
        "question": "Столица Португалии?",
        "answer": "Лиссабон"
    },
    "question6": {
        "question": "Столица Швейцарии?",
        "answer": "Берн"
    },
    "question7": {
        "question": "Столица Австрии?",
        "answer": "Вена"
    },
}

score = 0

for key, value in quiz.items():
    print(value["question"])

    answer = input("Ваш ответ? ")

    if answer.lower() == value["answer"].lower():
        print("Правильно!")
        score = score + 1
        print("Ваш счёт: " + str(score))
        print("")
        print("")
    else:
        print("Неправильно!")
        print("Правильный ответ: " + value["answer"])
        print("Ваш счёт: " + str(score))
        print("")
        print("")

print("Вы ответили правильно на " + str(score) + " из 7 вопросов")
print("Ваш процент правильных ответов: " + str(int(score / 7 * 100)) + "%")