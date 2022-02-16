import csv
from utils.Hashmap import Hashmap
from model.Package import Package


class ImportPackages:
    def __init__(self):
        self.package_table = Hashmap()
        self.import_package_data('./data/package_data.csv')

    def import_package_data(self, csvfile):
        with open(csvfile) as packagedata:
            packages = csv.reader(packagedata)
            for p in packages:
                package = Package(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'at the hub')
                self.package_table.insert(package.id, package)

    def get_package_table(self):
        return self.package_table












