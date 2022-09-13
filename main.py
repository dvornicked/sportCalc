height = 173
weight = 65
steps = 8000
time = 20

length = height / 4 + 0.37
distance = length * steps
speed = length / time
expense = 0.035 * weight + ((speed ** 2) / height) * 0.029 * weight

print(f'Distance: {length} m, Expense: {expense} kcal/min')
print(f'Distance: {length / 1000} km, Expense: {expense} kcal/min')

if length < 2000:
    print('Bad distance')
elif length < 4000:
    print('Good distance')
else:
    print('Are you professional sportsmen?!')
