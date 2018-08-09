from longbow import models
from django.utils import timezone

TESTS = [
    {
        'description': 'Московская Русь',
        'questions': [
            {
                'question_text': 'В каком году в Москве деревянный кремль сменяется белокаменным?',
                'answers': [
                    {
                        'answer_text': 'В 1267',
                    },
                    {
                       'answer_text': 'В 1312',
                    },
                    {
                       'answer_text': 'В 1355',
                    },
                    {
                       'answer_text': 'В 1367',
                       'is_answer_correct': True,
                    },
                ],
            },
            {
                'question_text': 'Какая битва произошла в 1380 году?',
                'answers': [
                    {
                        'answer_text': 'На реке Шелонь',
                    },
                    {
                        'answer_text': 'На реке Пьяна',
                    },
                    {
                        'answer_text': 'На Куликовом поле',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'Под Тверью',
                    },
                ],
            },
            {
                'question_text': 'При каком князе в состав Московского княжества был включен город Нижний Новгород?',
                'answers': [
                    {
                        'answer_text': 'При Иване Калите',
                    },
                    {
                        'answer_text': 'При Дмитрии Донском',
                    },
                    {
                        'answer_text': 'При Василии I',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'При Иване III',
                    },
                ],
            },
            {
                'question_text': 'В каком году Иван Грозный был провозглашен царем?',
                'answers': [
                    {
                        'answer_text': 'В 1533',
                    },
                    {
                        'answer_text': 'В 1547',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'В 1548',
                    },
                    {
                        'answer_text': 'В 1552',
                    },
                ],
            },
            {
                'question_text': 'Чем на Руси прославился итальянец Аристотель Фиорованти?',
                'answers': [
                    {
                        'answer_text': 'Написал много икон',
                    },
                    {
                        'answer_text': 'Писал хвалебные баллады русским князьям',
                    },
                    {
                        'answer_text': 'Командовал русскими войсками',
                    },
                    {
                        'answer_text': 'Был архитектором Успенского Собора',
                        'is_answer_correct': True,
                    },
                ],
            },
            {
                'question_text': 'Назовите дату междоусобной войны в Московском княжестве.',
                'answers': [
                    {
                        'answer_text': '1325-1329',
                    },
                    {
                        'answer_text': '1425-1453',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': '1433-1491',
                    },
                    {
                        'answer_text': '1448-1480',
                    },
                ],
            },
            {
                'question_text': 'В каком году произошло стояние на Угре, освободившее Русь от татарского ига?',
                'answers': [
                    {
                        'answer_text': 'В 1381 году',
                    },
                    {
                        'answer_text': 'В 1400 году',
                    },
                    {
                        'answer_text': 'В 1480 году',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'В 1547 году',
                    },
                ],
            },
            {
                'question_text': 'Потребность в каких товарах испытывала Московская Русь?',
                'answers': [
                    {
                        'answer_text': 'В кожевенных',
                    },
                    {
                        'answer_text': 'В металлах',
                    },
                    {
                        'answer_text': 'В оружии',
                    },
                    {
                        'answer_text': 'В предметах роскоши',
                        'is_answer_correct': True,
                    },
                ],
            },
            {
                'question_text': 'В каком году был построен Благовещенский Собор Московского Кремля?',
                'answers': [
                    {
                        'answer_text': 'В 1485',
                    },
                    {
                        'answer_text': 'В 1489',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'В 1495',
                    },
                    {
                        'answer_text': 'В 1533',
                    },
                ],
            },
            {
                'question_text': 'Какое архитектурное сооружение было воздвигнуто в 1485-1495 годах?',
                'answers': [
                    {
                        'answer_text': 'Краснокирпичный Кремль',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'Грановитая палата',
                    },
                    {
                        'answer_text': 'Благовещенский Собор',
                    },
                    {
                        'answer_text': 'Успенский Собор',
                    },
                ],
            },
        ]
    },
    {
        'description': 'Причины перехода к НЭПу',
        'questions': [
            {
                'question_text': 'В каком году была введена продовольственная диктатура?',
                'answers': [
                    {
                        'answer_text': '1917 г.',
                    },
                    {
                        'answer_text': '1918 г.',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': '1919 г.',
                    },
                    {
                        'answer_text': '1920',
                    },
                ],
            },
            {
                'question_text': 'Как называлось крупное крестьянское восстание на юге Украины в мае-июле 1919 г.?',
                'answers': [
                    {
                        'answer_text': '"Григорьевщина"',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': '"Антоновщина"',
                    },
                    {
                        'answer_text': '"Махновщина"',
                    },
                    {
                        'answer_text': '"Пугачевщина"',
                    },
                ],
            },
            {
                'question_text': 'В какое время произошло ижевско-воткинское восстание в Поволжье?',
                'answers': [
                    {
                        'answer_text': 'август-октябрь 1918 г.',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': 'май-июль 1919 г.',
                    },
                    {
                        'answer_text': '1920-1921 гг.',
                    },
                    {
                        'answer_text': '1922 г.',
                    },
                ],
            },
            {
                'question_text': 'Какое образное название получило восстание Антонова в Тамбовской губернии?',
                'answers': [
                    {
                        'answer_text': '"Советская разинщина"',
                    },
                    {
                        'answer_text': '"Советская пугачевщина"',
                    },
                    {
                        'answer_text': '"Русская Вандея"',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': '"Русская Жакерия"',
                    },
                ],
            },
            {
                'question_text': 'В каком году продразверстка была заменена продналогом?',
                'answers': [
                    {
                        'answer_text': '1919 г.',
                    },
                    {
                        'answer_text': '1920 г.',
                    },
                    {
                        'answer_text': '1921 г.',
                        'is_answer_correct': True,
                    },
                    {
                        'answer_text': '1922 г.',
                    },
                ],
            },
        ]
    }
]

question_order = answer_order = 0
for test_item in TESTS:
    test = models.Test()
    test.description, test.pub_date = (test_item['description'], timezone.now())
    test.save()

    for question_item in test_item['questions']:
        question = test.question_set.create()
        question.question_text, question.order = (question_item['question_text'], question_order)
        question.save()
        question_order += 1

        for answer_item in question_item['answers']:
            answer = question.answer_set.create()
            answer.answer_text, answer.is_answer_correct, answer.order = (answer_item['answer_text'], answer_item.get('is_answer_correct', False), answer_order)
            answer.save()
            answer_order += 1
