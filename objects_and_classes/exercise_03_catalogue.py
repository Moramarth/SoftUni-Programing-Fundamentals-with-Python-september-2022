class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = list()


    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        desired_list = list()
        for product in self.products:
            if product.startswith(first_letter):
                desired_list.append(product)
        return desired_list

    def __repr__(self):
        new_list = sorted(self.products)
        string = f"Items in the {self.name} catalogue:\n"
        string += "\n".join(new_list)
        return string

