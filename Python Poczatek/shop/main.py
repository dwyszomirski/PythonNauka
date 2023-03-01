import data_generator
from express_order import ExpressOrder


def run_homework():
    order_elements = data_generator.generate_order_elements()
    express_order = ExpressOrder(
        delivery_date="10-05-2020",
        client_first_name="D",
        client_last_name="W",
        order_elements=order_elements
    )
    print(express_order)


if __name__ == '__main__':
    run_homework()
