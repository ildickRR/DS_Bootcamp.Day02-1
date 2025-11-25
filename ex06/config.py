

TG_TOKEN = "8578154119:AAFtq05hHndBHlKaM9Goe2zYbNF8hHjUZiQ"

TG_CHAT_ID = 628528740

num_of_steps = 3

report_template = """
Отчёт:

Мы сделали {total} наблюдений: {tails} раз выпал орёл и {heads} раз выпала решка.
Вероятности составляют: орёл — {tails_perc:.2f}%, решка — {heads_perc:.2f}%.
Наш прогноз: в следующих {num_steps} подбрасываниях будет {pred_tails} орлов и {pred_heads} решек.
"""
