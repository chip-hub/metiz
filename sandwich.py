def make_sandvich(*komponents):
    print("Для Вас будет сделан сэндвич с ", end="")
    print(', '.join(komponents))

make_sandvich('кукуруза', 'помидоры', 'сыр')