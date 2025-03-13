import heapq

class MetroGraph:
    def __init__(self):
        self.stations = {}
        self.distances = {}

    def add_station(self, name):
        self.stations[name] = []

    def add_connection(self, station1, station2, distance):
        connection = [station2, distance]
        self.stations[station1].append(connection)

    def display_map(self):
        for station, connections in self.stations.items():
            print(f"\n {station} -> {connections}")

    def dijkstra(self, source, destination=None):
        distances = {node: float('inf') for node in self.stations}
        predecessors = {node: None for node in self.stations}
        distances[source] = 0

        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_station = heapq.heappop(priority_queue)

            if current_distance > distances[current_station]:
                continue

            if current_station == destination:
                break

            for next_station, weight in self.stations[current_station]:
                distance = current_distance + weight

                if distance < distances[next_station]:
                    distances[next_station] = distance
                    predecessors[next_station] = current_station
                    heapq.heappush(priority_queue, (distance, next_station))

        return distances, predecessors

    def shortest_path(self, source, destination):
        distances, predecessors = self.dijkstra(source, destination)

        path = []
        current_station = destination
        while current_station is not None:
            path.insert(0, current_station)
            current_station = predecessors[current_station]

        return path, distances[destination]

bangalore_metro = MetroGraph()

stations_list = ['Majestic', 'Mantri', 'Chickpete', 'Market', 'Mahakavi',
                 'Srirampura', 'Krantiveera', 'Magadi', 'Hosalli','Vishweshwariah','Ambedkar']

for station in stations_list:
    bangalore_metro.add_station(station)

bangalore_metro.add_connection('Mahakavi', 'Srirampura', 5)
bangalore_metro.add_connection('Srirampura','Mahakavi', 5)
bangalore_metro.add_connection('Majestic', 'Mantri', 1)
bangalore_metro.add_connection('Mantri', 'Majestic', 1)
bangalore_metro.add_connection('Mantri', 'Srirampura', 2)
bangalore_metro.add_connection('Srirampura', 'Mantri', 2)
bangalore_metro.add_connection('Chickpete', 'Majestic', 4)
bangalore_metro.add_connection('Majestic', 'Chickpete', 4)
bangalore_metro.add_connection('Chickpete', 'Market', 1)
bangalore_metro.add_connection('Market', 'Chickpete', 4)
bangalore_metro.add_connection('Krantiveera', 'Majestic', 2)
bangalore_metro.add_connection('Majestic', 'Krantiveera', 2)
bangalore_metro.add_connection('Krantiveera', 'Magadi', 3)
bangalore_metro.add_connection('Magadi', 'Krantiveera', 3)
bangalore_metro.add_connection('Hosalli', 'Magadi', 1)
bangalore_metro.add_connection('Magadi', 'Hosalli', 1)
bangalore_metro.add_connection('Majestic', 'Vishweshwariah', 1)
bangalore_metro.add_connection('Vishweshwariah', 'Majestic', 1)
bangalore_metro.add_connection('Ambedkar', 'Vishweshwariah', 3)
bangalore_metro.add_connection('Vishweshwariah', 'Ambedkar', 3)


bangalore_metro.display_map()
source_station = input("\n Enter the source station: ").capitalize()
destination_station = input("\n Enter the destination station: ").capitalize()

if source_station not in bangalore_metro.stations or destination_station not in bangalore_metro.stations:
    print("Invalid station names. Please enter valid station names.")
else:
    shortest_path, shortest_distance = bangalore_metro.shortest_path(source_station, destination_station)

    print(f"\n Shortest Path from {source_station} to {destination_station}: {shortest_path}")
    print(f"\n Total cost: {5 + (shortest_distance)*2 }")