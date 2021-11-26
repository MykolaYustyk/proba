#
# 2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць
# строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
# ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
# Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
# Функція повинна принтануть і вернуть суму, яка буде на рахунку.
#
def bank(a, years, percents):
    a = a + ( 1 + percents / 100) ** years
    return a
a = float(input("a0 = "))
years = int(input('years = '))
a = bank(a, years, 10)
print(f'a = {a: .2f}')