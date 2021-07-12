
gor = 'kojevo'
strana = 'russia'


def city(gor, strana, pop=''):

    if pop:
        x = f'{gor}, {strana} - '
        z = f'{pop}'
        return x.title() + z
    else:
        x = f'{gor}, {strana}'
        return x.title()


city(gor, strana, pop='')