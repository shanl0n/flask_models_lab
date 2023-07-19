class Order():

    def __init__(self, date, name, quantity, game_title, done):
        self.order_date = date
        self.customer_name = name
        self.quantity = quantity
        self.game_title = game_title
        self.done = done