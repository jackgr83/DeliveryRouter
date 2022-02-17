import csv
from utils.Hashmap import Hashmap
from model.Package import Package


# Time Complexity: O(n)
# Space Complexity: O(n)
class ImportPackages:
    def __init__(self):
        self.package_table = Hashmap()
        self.import_package_data('./data/package_data.csv')

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def import_package_data(self, csvfile):
        with open(csvfile) as packagedata:
            packages = csv.reader(packagedata)
            for p in packages:
                package = Package(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'at the hub')
                self.package_table.insert(package.id, package)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_package_table(self):
        return self.package_table












