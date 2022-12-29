import click
from final_project import Margherita, Pepperoni, Hawaiian, Order


@click.group()
def my_cli():
    pass


@my_cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, delivery: bool, size: str = 'L'):
    """
    Bakes and delivers pizza
    """
    pizza_dict = {
        'pepperoni': Pepperoni,
        'margherita': Margherita,
        'hawaiian': Hawaiian
    }
    if pizza.lower() not in pizza_dict:
        click.echo(
            f'Ordered pizza {pizza} is not in menu. '
            'Please go to menu command')
        return

    ordered_pizza = pizza_dict[pizza.lower()](size=size)
    client_order = Order(ordered_pizza)

    click.echo(client_order.bake())
    if delivery:
        click.echo(client_order.deliver())


@my_cli.command()
def menu():
    """
    Shows the menu
    """
    pizzas = [Pepperoni(), Margherita(), Hawaiian()]
    for p in pizzas:
        pizza_dict = p.dict()
        click.echo('{}: {}'.format(str(p), str(', '.join(pizza_dict[p.name]))))


if __name__ == '__main__':
    my_cli()
