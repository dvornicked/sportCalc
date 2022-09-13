HEIGHT = 173
WEIGHT = 65
STEPS = 8000
TIME = 20

length = HEIGHT / 4 + 0.37
distance = length * STEPS
speed = length / TIME
expense = 0.035 * WEIGHT + ((speed ** 2) / HEIGHT) * 0.029 * WEIGHT

print(f'Distance: {length} m, Expense: {expense} kcal/min')
print(f'Distance: {length / 1000} km, Expense: {expense} kcal/min')

if length < 2000:
    print('Bad distance')
elif length < 4000:
    print('Good distance')
else:
    print('Are you professional sportsmen?!')
