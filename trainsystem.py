class Train:
    def __init__(self, train_name, time, passenger_strength, train_number):
        self.train_name = train_name
        self.time = time
        self.passenger_strength = passenger_strength
        self.train_number = train_number


class RailwayStation:
    def __init__(self, station_name):
        self.station_name = station_name
        self.available_trains = []

    def add_train(self, train):
        self.available_trains.append(train)

    def remove_train(self, train):
        self.available_trains.remove(train)


class ReservationSystem:
    def __init__(self):
        self.stations = ["Delhi", "Jaipur", "Prayagraj", "Mumbai"]
        self.railway_stations = {station: RailwayStation(station) for station in self.stations}
        self.booked_tickets = {}

    def get_train_information(self, source, destination, date_of_travel):
        # Implement logic to find and return available trains based on source, destination, and date_of_travel
        pass

    def check_seat_availability(self, train, date_of_travel):
        # Implement logic to check seat availability for a given train and date_of_travel
        pass

    def book_ticket(self, train, date_of_travel, passenger_name, seat_number):
        # Implement logic to book a ticket for a passenger on a specific train and date_of_travel
        pass

    def cancel_ticket(self, ticket_number):
        # Implement logic to cancel a booked ticket
        pass

    def display_ticket_details(self, ticket_number):
        # Implement logic to display ticket details
        pass

    def error_handling(self, error_message):
        # Implement error handling logic
        pass


# Example usage
if __name__ == "__main__":
    system = ReservationSystem()

    # Create some train objects and add them to stations
    train1 = Train("Mumbai - Delhi", "13:05", 50, 1010)
    train2 = Train("Delhi - Jaipur", "7:00", 50, 2013)
    train3 = Train("Prayagraj - Delhi", "10:00", 50, 3045)

    system.railway_stations["Mumbai"].add_train(train1)
    system.railway_stations["Delhi"].add_train(train2)
    system.railway_stations["Prayagraj"].add_train(train3)

    # Now, you can start using the ReservationSystem methods to interact with the system.
