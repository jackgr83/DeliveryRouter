from utils.ImportPackages import ImportPackages
from utils.ImportDistances import ImportDistances
from model.Truck import Truck
from model.Clock import Clock
import json

packages = ImportPackages().get_package_table()
distances = ImportDistances()


truck_one_packages = []
truck_two_packages = []
truck_three_packages = []


for k in packages.get_all_keys():
    package = packages.search(k)
    if 'truck 2' in package.notes or 'Delayed' in package.notes:
        truck_two_packages.append(k)
    elif package.deadline != 'EOD':
        truck_one_packages.append(k)
    else:
        truck_three_packages.append(k)


# User input
rt = input("What time would you like to see package updates? (Enter as HH:MM in 24 hour time format): ")


# Start the trucks
request_time = Clock(int(rt.split(':')[0]), int(rt.split(':')[1]), 1)

truck1 = Truck(truck_one_packages, packages, distances, Clock(8, 0, 1), request_time, 1)
truck2 = Truck(truck_two_packages, packages, distances, Clock(9, 5, 1), request_time, 2)
truck3 = Truck(truck_three_packages, packages, distances, Clock(8, 0, 1), request_time, 3)


truck1.start_route()
truck2.start_route()
truck3.start_route()

# Print the status and Information given the input time
print("")
print("Package Status and Info at " + rt + ": ")
print("")
print(packages.print_table())
print("")
total_mileage = float(str(truck1.get_mileage())) + float(str(truck2.get_mileage())) + float(str(truck3.get_mileage()))
print("Total mileage traveled: " + str(total_mileage))

# Eventually remove this section
print("Truck 1 mileage: " + str(truck1.get_mileage()))
print("Truck 2 mileage: " + str(truck2.get_mileage()))
print("Truck 3 mileage: " + str(truck3.get_mileage()))













