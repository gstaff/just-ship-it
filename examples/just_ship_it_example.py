def greet(name):
    """Greets you by name!"""
    return 'Hello {name}!'.format(name=name)


def hello():
    return {'hello': 'world'}


if __name__ == '__main__':
    from just_ship_it import ship_it
    ship_it()
