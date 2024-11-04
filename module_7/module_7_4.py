'''
Комментарии к заданию:

    В русском языке окончания слов меняются (1 участник, 2 участника),
    пока что давайте не обращать на это внимания.
    Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать.

    Например, для challenge_result:

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
result = ‘Победа команды Мастера кода!’
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
result = ‘Победа команды Волшебники Данных!’
else:
result = ‘Ничья!’
'''

team1_num = 5
print("В команде Мастера кода участников: %s!" % team1_num)

team2_num = 6
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

score_2 = 42
print("Команда Волшебники данных решила задач: {}!".format(score_2))

team1_time = 18015.2
print("Волшебники данных решили задачи за {0} с!".format(team1_time))

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = "победа команды Мастера кода"
print(f'Результат битвы: {challenge_result}!')

tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = '%s' % challenge_result            #'Победа команды Волшебники Данных!'
else:
    result = f'Ничья!'

print(result)