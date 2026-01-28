from random import randint

colors = [
    'MediumBlue',
    'ForestGreen',
    'Red',
    'DarkMagenta',
    'LightSteelBlue',
    'Crimson',
    'YellowGreen',
    'HotPink',
    'MediumVioletRed',
    'Navy'
]

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b