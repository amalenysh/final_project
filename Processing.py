from random import randint


def log(string=None):
    """
    Decorator for bake and deliver methods
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            action_time = randint(1, 20)
            if string is not None:
                return string.format(action_time)
            return f'{func.__name__} - {action_time}с!'

        return wrapper

    return decorator


@log('👨‍🍳 Приготовили за {}с!')
def bake():
    """
    Bakes pizza
    """
    pass


@log('🛵 Доставили за {}с!')
def delivery():
    """
    Delivers pizza
    """
    pass


@log('🏠 Забрали за {}с!')
def pickup():
    """
    Pick-up of pizza
    """
    pass


if __name__ == '__main__':
    pizza = 'Pizza'  # do not use exemplar due to circular imports
    print(bake(pizza))
    print(delivery(pizza))
    print(pickup(delivery))
