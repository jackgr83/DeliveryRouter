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

    # Nearest Neighbor Algorithm
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

        if current_index < len(self.packages):
            self.sort_route(self.package_data.search(pid).address, current_index)

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
                    package.set_status('delivered')
                    self.mileage += dist
                    self.location = package.address
                else:
                    break

    def track_time(self, distance):
        t = distance / self.mph
        m = int(t * 60) % 60
        s = int((t * 60) * 60) % 60
        self.time.add_minute(m)
        self.time.add_second(s)

    def get_mileage(self):
        return self.mileage

    def get_time(self):
        return self.time.get_hour()




