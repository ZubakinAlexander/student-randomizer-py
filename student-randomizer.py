students = [
    'Быков Тимофей Александрович',
    'Димова Александра Сергеевна',
    'Зубакин Александр Сергеевич',
    'Митрохин Антон',
    'Синицына Лилия Дмитриевна',
    'Шапель Владимир Антонович',
    'Щегольков Никита Сергеевич',
    'Азаренко Андрей Сергеевич',
    'Гребенщиков Богдан Вячеславович',
    'Григорьев Алексей Сергеевич',
    'Ильина Мария Анатольевна',
    'Майборода Вера Андреевна',
    'Нестеров Олег Олегович',
    'Шубина Ольга Сергеевна',
]

questons = []
for q in open('questons.txt').readlines():
    questons.append(q)

import random
print(random.choice(students) + str(':'), random.choice(questons))
