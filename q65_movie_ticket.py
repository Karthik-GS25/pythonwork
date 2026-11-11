"""65. MovieTicket class with three example ticket objects."""


class MovieTicket:
    def __init__(self, movie_name, theatre, seat_number):
        self.movie_name = movie_name
        self.theatre = theatre
        self.seat_number = seat_number

    def __repr__(self):
        return (
            f"MovieTicket({self.movie_name!r}, {self.theatre!r}, {self.seat_number!r})"
        )


def create_tickets():
    return [
        MovieTicket("Inception", "PVR", "A1"),
        MovieTicket("Interstellar", "INOX", "B4"),
        MovieTicket("Dangal", "Cinepolis", "C7"),
    ]


for ticket in create_tickets():
    print(ticket)
