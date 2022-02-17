# Time Complexity: O(n^2)
# Space Complexity: O(n)
class Truck:
    def __init__(self, packages, package_data, distances, start, request_time, number):
        self.packages = packages
        self.package_data = package_data
        self.distances = distances
        self.time = start
        self.number = number
        self.mileage = 0.0
        self.mph = 18.0
        self.requested_time = request_time
        self.location = 'HUB'
        self.sort_route('HUB', 0)
        self.corrected_address = False

    # Greedy Algorithm
    #
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def sort_route(self, location, current_index):
        min_dist = 999
        pid = 0
        pidx = 0

        # Find the next closest address
        for i, p in enumerate(self.packages[current_index:], start=current_index):
            package = self.package_data.search(p)
            dist = self.distances.lookup_distance(location, package.address)
            if dist < min_dist and pid >= 0 and pidx >= 0:
                min_dist = dist
                pid = package.id
                pidx = i

        # move to next in line
        self.packages[pidx], self.packages[current_index] = self.packages[current_index], self.packages[pidx]
        current_index += 1

        # recursive call for next in list
        if current_index < len(self.packages):
            self.sort_route(self.package_data.search(pid).address, current_index)

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def start_route(self):
        print(self.packages)
        if str(self.requested_time) >= "08:00":
            for i, p in enumerate(self.packages):
                # Go back to the hub to get the rest of the packages
                if i == 16:
                    dist_to_hub = self.distances.lookup_distance(self.location, 'HUB')
                    self.track_time(dist_to_hub)
                    self.mileage += dist_to_hub
                    self.location = 'HUB'
                package = self.package_data.search(p)
                package.set_status('en route')
                dist = self.distances.lookup_distance(self.location, package.address)
                self.track_time(dist)
                if str(self.requested_time) >= str(self.time):
                    package.set_status('delivered at ' + str(self.time))
                    self.mileage += dist
                    self.location = package.address
                else:
                    break
            # first driver needs to go back to the hub to get truck 3 when finished
            if self.number == 1:
                dist_to_hub = self.distances.lookup_distance(self.location, 'HUB')
                self.track_time(dist_to_hub)
                self.mileage += dist_to_hub
                self.location = 'HUB'

    def track_time(self, distance):
        t = distance / self.mph
        m = int(t * 60) % 60
        s = int((t * 60) * 60) % 60
        self.time.add_minute(m)
        self.time.add_second(s)
        # correct the wrong address at 10:20
        if self.number == 3 and str(self.time) >= '10:20' and not self.corrected_address:
            self.package_data.search(9).set_address("410 S State St")
            self.corrected_address = True

    def get_mileage(self):
        return self.mileage

    def get_time(self):
        return self.time.get_hour()




