import csv


# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class ImportDistances:
    def __init__(self):
        self.distance_table = {}
        self.import_distance_data('./data/distance_data.csv')

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def import_distance_data(self, csvfile):
        with open(csvfile) as csv_read:
            distance_file = csv.reader(csv_read)
            header = next(distance_file)
            for i, address in enumerate(header):
                nested = {}
                for row in distance_file:
                    destination = row[0]
                    if i < 27:
                        distance = float(row[i+1])
                    nested[destination] = distance
                self.distance_table[address] = nested
                csv_read.seek(0)
                next(distance_file)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def lookup_distance(self, start, end):
        return self.distance_table[start][end]


