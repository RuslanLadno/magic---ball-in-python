# магический шар

# базовые значения
from colorist import Color
import random
# answers = ['Бесспорно', 'Абсолютно', 'Не сомневайся', 'Предрешено', '100% да',
#             'Думаю, что да', 'Хорошие перспективы', 'Вероятнее всего', 'Расчёты говорят - да', 'Конечно',
#             'Как тебе сказать, вроде да, а вроде нет', 'Ошибочка, попробуй ещё раз', 'И не говори', 'Сложно сказать', 'Спроси заново',
#             'Просто нет', 'Ни в коем случае', 'Даже не думай', 'Весьма сомнительно', 'Не сегодня']

# доработки
plus_answers = ['Бесспорно', 'Абсолютно', 'Не сомневайся', 'Предрешено', '100% да',
                'Думаю, что да', 'Конечно']
so_so_answers = ['Как тебе сказать, вроде да, а вроде нет', 'Ошибочка, попробуй ещё раз', 'И не говори', 'Сложно сказать', 'Спроси заново', 
                'Затрудняюсь ответить', 'Хммм, пока загадка']
minus_answers = ['Просто нет', 'Ни в коем случае', 'Даже не думай', 'Весьма сомнительно', 'Не сегодня',
                'АХАХАХ, смешно..', 'Не будет такого']

all_question = [plus_answers, so_so_answers, minus_answers]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
user = input('Подскажи, как тебя зовут?\n')
print(f'Привет {user}')

# вопросик
while True:
    question = input('Какой у тебя ко мне вопрос?\n')
    kategory = random.choice(all_question)
    if kategory == plus_answers:
        print(f'{Color.GREEN}{random.choice(kategory)}{Color.OFF}')
    elif kategory == so_so_answers:
        print(f'{Color.YELLOW}{random.choice(kategory)}{Color.OFF}')
    else:
        print(f'{Color.RED}{random.choice(kategory)}{Color.OFF}')
    dop_question = input('Если ещё есть вопрос - напиши "Да"\n')
    if dop_question.lower() == 'да':
        continue
    else:
        print('Возвращайся, если возникнут вопросы!')
        break

