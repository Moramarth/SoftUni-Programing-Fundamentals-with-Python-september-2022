class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = list()
        self.__capacity_left = __capacity

    def add_item(self, item: str):
        if self.__capacity_left > 0:
            self.items.append(item)
            self.__capacity_left -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity_left}"
