#Model class to hold info

class Profile:

    def __init__ (self,linked_mobiles = [],
                  linked_emails = [],
                  total_num_orders = None,
                  total_price_spent = None,
                  random_orders = [],
                  **kwargs
    ):
        self.linked_mobiles = linked_mobiles
        self.linked_emails = linked_emails
        self.total_num_orders = total_num_orders
        self.total_price_spent = total_price_spent
        self.random_orders = random_orders
       
    def get_json(self):
        return self.__dict__




