# Joseph Rhodes #005759960

# imports
from utils.ImportPackages import ImportPackages
from utils.ImportDistances import ImportDistances
from model.Truck import Truck
from model.Clock import Clock

# import data
packages = ImportPackages().get_package_table()
distances = ImportDistances()

# initialize truck package lists
truck_one_packages = []
truck_two_packages = []
truck_three_packages = []

# sort packages onto trucks based on constraints
for k in packages.get_all_keys():
    package = packages.search(k)
    if 'truck 2' in package.notes or 'Delayed' in package.notes:
        truck_two_packages.append(k)
    elif package.deadline != 'EOD' or package.id == 19:
        truck_one_packages.append(k)
    else:
        truck_three_packages.append(k)

# User interface input
rt = input("What time would you like to see package updates? (Enter as HH:MM in 24 hour time format): ")
request_time = Clock(int(rt.split(':')[0]), int(rt.split(':')[1]), 1)

# Initialize instances of Truck class
truck1 = Truck(truck_one_packages, packages, distances, Clock(8, 0, 1), request_time, 1)
truck2 = Truck(truck_two_packages, packages, distances, Clock(9, 5, 1), request_time, 2)
# Truck 3 leaves after truck 1 comes back with driver
truck3 = Truck(truck_three_packages, packages, distances, Clock(10, 0, 1), request_time, 3)

# Start the trucks
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













