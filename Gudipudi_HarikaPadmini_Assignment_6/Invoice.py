"""
HW      # 6
Problem # 2 Invoice
Author  # Gudipudi HarikaPadmini
"""


class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self._part_number = part_number
        self._part_description = part_description
        self.quantity = quantity
        self.price_per_item = price_per_item

    @property
    def part_number(self):
        # getter for part_number
        return self._part_number

    @property
    def part_description(self):
        # getter for part_description
        return self._part_description

    @property
    def quantity(self):
        # getter for quantity
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        # setter for quantity
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value

    @property
    def price_per_item(self):
        # getter for price per item
        return self._price_per_item

    @price_per_item.setter
    # setter for an item, raises an error if the value is negative
    def price_per_item(self, value):
        if value < 0:
            raise ValueError("Price per item cannot be negative.")
        self._price_per_item = float(value)

    def calculate_invoice(self):
        # calculate invoice amount
        return self.quantity * self.price_per_item

    def __str__(self):
        # str method to display the formatted string
        output = f"{'*' * 30}Invoice{'*' * 30}\n"
        output += f"{'part_number':<20}{'part_description':<25}{'quantity':<20}{'price':<10}\n"
        output += f"{self.part_number:<20}{self.part_description:<25}{self.quantity:<20}${self.price_per_item:.2f}\n"
        return output


if __name__ == "__main__":
    # instance of the invoice class
    invoice1 = Invoice(100, 'Light Bulb', 3, 3.6)
    print(f"{invoice1.calculate_invoice():.2f}")
    print(invoice1)

    try:
        # Testing negative quantity to raise an exception
        invoice1.quantity = -3
    except ValueError as e:
        print(f"Error: {e}")
