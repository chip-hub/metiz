def make_avto(crafter, model, **param):
    """Строит словарь с информацией о машине."""
    avto = {'mader': crafter, 'model': model}
    for key, val in param.items():
        avto[key] = val
    return avto

avto_like = make_avto('Volga', '2140', color = 'whit', age = 5)

print(avto_like)
