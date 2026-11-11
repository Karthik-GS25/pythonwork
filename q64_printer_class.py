"""64. Create three printers and display their identities."""


class Printer:
    def __init__(self, capacity, color_mode, printer_type):
        self.capacity = capacity
        self.color_mode = color_mode
        self.printer_type = printer_type

    def __repr__(self):
        return f"Printer({self.capacity}, {self.color_mode!r}, {self.printer_type!r})"


def create_printers():
    return [
        Printer(20, "color", "inkjet"),
        Printer(30, "mono", "laser"),
        Printer(15, "color", "laser"),
    ]


for printer in create_printers():
    print(id(printer), printer)
