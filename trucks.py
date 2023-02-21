import copy
import datetime
import graph
from packages import Packages
import algorithm


# Creates a class for the trucks to carry the packages that need to be delivered
class Truck:
    # Each truck class has two lists storing information.
    # The complete package information
    # The route information for each package
    def __init__(self):
        self.truck_packages = []
        self.route = []

    # Adds two items to the truck class based on the inputted package_id.
    # The first is all the package information
    # The second is the package destination
    # Time Complexity O(1)
    # Space Complexity O(1)
    def insert(self, package_id):
        self.truck_packages.append(package_id)
        self.route.append(package_id[1])

    # Removes all the information from the truck class based on the inputted package_id
    # Time Complexity O(N)
    # Space Complexity O(1)
    def remove(self, package_id):
        self.truck_packages.remove(package_id)
        self.route.remove(package_id[1])


total_distance_travelled = []  # list to store the distance travelled by each truck
delivered_packages = []  # list of which packages have been delivered

truck1_start_time = datetime.datetime(2022, 6, 8, 8, 0, 0)  # starts the day off at 8am and the time that truck 1 leaves

truck2_start_time = datetime.datetime(2022, 6, 8, 9, 10, 0)  # truck 2 leaves the hub at 9:10 AM

truck3_start_time = datetime.datetime(2022, 6, 8, 10, 0, 0)  # truck 3 leaves the hub at 10AM, after truck 1 returns

# Creates an instance of each truck
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#  list of packages for each truck by the package ID number

truck1_list = [2, 13, 14, 15, 16, 19, 20, 21, 27, 29, 33, 34, 35, 39, 40]
truck2_list = [1, 3, 4, 6, 8, 10, 11, 18, 23, 24, 30, 31, 36, 37, 38]
truck3_list = [5, 7, 9, 12, 17, 22, 25, 26, 28, 32]

# Inserts the packages associated with the ID into the proper truck
# Time Complexity O(N)
# Space Complexity O(1)
for i in truck1_list:
    truck1.insert(Packages.package_hash.get(i))

for i in truck2_list:
    truck2.insert(Packages.package_hash.get(i))

for i in truck3_list:
    truck3.insert(Packages.package_hash.get(i))

# Runs the nearest_neighbor algorith on each truck to determine the shortest route for each package
# Time Complexity O(N^2)
# Space Complexity O(N)
truck1_route = algorithm.nearest_neighbor(truck1)
truck2_route = algorithm.nearest_neighbor(truck2)
truck3_route = algorithm.nearest_neighbor(truck3)


# Delivers the packages and updates the current status of each package given a given time of the day
# Time Complexity O(N^2)
# Space Complexity O(N)
def check_packages(hour, minute, second):
    # Converts the user entered time into a datetime.datetime object that packages will be checked against
    checking_time = datetime.datetime(2022, 6, 8, hour, minute, second)
    distance_travelled = graph.graph.edge_weight  # Edge weight between every Vertex
    speed = 0.3  # Trucks travel at a rate of 0.3 miles every minute

    #
    # The first truck is delivering the packages
    #

    truck1_current_time = truck1_start_time  # Current time of the day is the start time of truck1

    # Sets the status' of the packages on truck1 to "En Route'
    for i in range(len(truck1.truck_packages)):
        truck1.truck_packages[i][8] = "En Route"

    truck1_delivered_packages = []
    truck1_distance_travelled = []

    # Runs through the locations in truck1_route and determines the distance between each Vertex
    # Updates each package with the time it was delivered
    for i in range(len(truck1_route) - 1):
        distance = distance_travelled[truck1_route[i], truck1_route[i + 1]]
        time_taken_between_cities = datetime.timedelta(minutes=(distance / speed))
        truck1_current_time = truck1_current_time + time_taken_between_cities
        # Compares the current time to the checking time
        # If the checking time is greater than the current time then it stops further packages from being delivered
        if checking_time < truck1_current_time:
            break
        for j in range(len(truck1_route) - 2):
            if truck1.truck_packages[j][1] == truck1_route[i + 1]:
                # ensures unique package ID for each location
                if truck1.truck_packages[j] not in truck1_delivered_packages:
                    truck1.truck_packages[j][8] = "Delivered"  # updates status of each package
                    # timestamp of when each package is delivered
                    truck1.truck_packages[j][9] = datetime.datetime.strftime(
                        truck1_current_time, "%H:%M:%S")
                    #  updates current time
                    truck1_delivered_packages.append(truck1.truck_packages[j])
    delivered_packages.append(truck1_delivered_packages)

    # Adds the distance between each Vertex to the distanced_travelled list for truck1
    for i in range(len(truck1_route) - 1):
        miles_between_cities = distance_travelled[truck1_route[i], truck1_route[i + 1]]
        truck1_distance_travelled.append(miles_between_cities)
    total_distance_travelled.append(truck1_distance_travelled)

    #
    # The second truck is delivering the packages
    #

    truck2_current_time = truck2_start_time  # Current time of the day is the start time of truck2

    # Sets the status' of the packages on truck2 to "En Route'
    if checking_time > truck2_current_time:
        for i in range(len(truck2.truck_packages)):
            truck2.truck_packages[i][8] = "En Route"

    truck2_delivered_packages = []
    truck2_distance_travelled = []

    # Runs through the locations in truck2_route and determines the distance between each Vertex
    # Updates each package with the time it was delivered
    for i in range(len(truck2_route) - 1):
        distance = distance_travelled[truck2_route[i], truck2_route[i + 1]]
        time_taken_between_cities = datetime.timedelta(minutes=(distance / speed))
        truck2_current_time = truck2_current_time + time_taken_between_cities
        # Compares the current time to the checking time
        # If the checking time is greater than the current time then it stops further packages from being delivered
        if checking_time < truck2_current_time:
            break
        for j in range(len(truck2_route) - 2):
            if truck2.truck_packages[j][1] == truck2_route[i + 1]:
                # ensures unique package ID for each location
                if truck2.truck_packages[j] not in truck2_delivered_packages:
                    truck2.truck_packages[j][8] = "Delivered"  # updates status of each package
                    # timestamp of when each package is delivered
                    truck2.truck_packages[j][9] = datetime.datetime.strftime(
                        truck2_current_time, "%H:%M:%S")
                    #  updates current time
                    truck2_delivered_packages.append(truck2.truck_packages[j])

    delivered_packages.append(truck2_delivered_packages)

    # Adds the distance between each Vertex to the distanced_travelled list for truck2
    for i in range(len(truck2_route) - 1):
        miles_between_cities = distance_travelled[truck2_route[i], truck2_route[i + 1]]
        truck2_distance_travelled.append(miles_between_cities)
    total_distance_travelled.append(truck2_distance_travelled)

    #
    #   The third truck is delivering the packages
    #

    truck3_current_time = truck3_start_time  # Current time of the day is the start time of truck3

    # Sets the status' of the packages on truck3 to "En Route'
    if checking_time > truck3_start_time:
        for i in range(len(truck3.truck_packages)):
            truck3.truck_packages[i][8] = "En Route"

    truck3_delivered_packages = []
    truck3_distance_travelled = []

    # If the checking time is equal to or greater than 10:30 AM, corrects the address for package #9
    if checking_time >= datetime.datetime(2022, 6, 8, 10, 20):

        for i in range(len(truck3.truck_packages)):
            if truck3.truck_packages[i][7] == 'Wrong address listed':
                truck3.truck_packages[i][1] = '410 S State St'
                truck3.truck_packages[i][4] = '84111'
                truck3.truck_packages[i][7] = 'Correct Address'

    # Runs through the locations in truck3_route and determines the distance between each Vertex
    # Updates each package with the time it was delivered
    for i in range(len(truck3_route) - 1):
        distance = distance_travelled[truck3_route[i], truck3_route[i + 1]]
        time_taken_between_cities = datetime.timedelta(minutes=(distance / speed))
        truck3_current_time = truck3_current_time + time_taken_between_cities
        # Compares the current time to the checking time
        # If the checking time is greater than the current time then it stops further packages from being delivered
        if checking_time < truck3_current_time:
            break
        for j in range(len(truck3_route) - 2):
            if truck3.truck_packages[j][1] == truck3_route[i + 1]:
                # ensures unique package ID for each location
                if truck3.truck_packages[j] not in truck3_delivered_packages:
                    truck3.truck_packages[j][8] = "Delivered"  # updates status of each package
                    # timestamp of when each package is delivered
                    truck3.truck_packages[j][9] = datetime.datetime.strftime(
                        truck3_current_time, "%H:%M:%S")
                    #  updates current time
                    truck3_delivered_packages.append(truck3.truck_packages[j])

    delivered_packages.append(truck3_delivered_packages)

    # Adds the distance between each Vertex to the distanced_travelled list for truck3
    for i in range(len(truck3_route) - 1):
        miles_between_cities = distance_travelled[truck3_route[i], truck3_route[i + 1]]
        truck3_distance_travelled.append(miles_between_cities)
    total_distance_travelled.append(truck3_distance_travelled)


# Prints the miles driven for truck 1
# Time Complexity 0(1)
# Space Complexity O(1)
def truck1_status():
    print("Miles driven by Truck1:", sum(total_distance_travelled[0]))


# Prints the miles driven for truck 2
# Time Complexity 0(1)
# Space Complexity O(1)
def truck2_status():
    print("Miles driven by Truck2:", sum(total_distance_travelled[1]))


# Prints the miles driven for truck 3
# Time Complexity 0(1)
# Space Complexity O(1)
def truck3_status():
    print("Miles driven by Truck3:", sum(total_distance_travelled[2]))


# Prints the miles driven for all the trucks
# Time Complexity 0(1)
# Space Complexity O(1)
def total_miles_travelled():
    print("Total miles driven by all the trucks:", sum(total_distance_travelled[0]) + sum(total_distance_travelled[1]) +
          sum(total_distance_travelled[2]), "\n")


# Prints the packages on each truck
# Time Complexity O(N)
# Space Complexity O(1)
def print_packages():
    print("Truck 1 Packages: ")
    for i in truck1.truck_packages:
        print(i)
    print("Truck 2 Packages: ")
    for i in truck2.truck_packages:
        print(i)
    print("Truck 3 Packages: ")
    for i in truck3.truck_packages:
        print(i)


# Prints the package given the package id
# Time Complexity O(1)
# Space Complexity O(1)
def find_package_by_id():
    print("Enter Package Number:")
    x = int(input())
    if x in Packages.package_hash.get(x):
        print(Packages.package_hash.get(x))


# Prints the packages with the package address
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_address():
    print("Enter Address:")
    address = str(input())
    for i in truck1.truck_packages:
        if i[1] == address:
            print(i)
    for i in truck2.truck_packages:
        if i[1] == address:
            print(i)
    for i in truck3.truck_packages:
        if i[1] == address:
            print(i)


# Prints the package deadline given an input
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_deadline():
    print("Check Package by deadline:"
          "\n1: 9:00 AM"
          "\n2: 10:30 AM:"
          "\n3: EOD")
    deadline = int(input())
    if deadline == 1:
        for i in truck1.truck_packages:
            if i[5] == '9:00 AM':
                print(i)
        for i in truck2.truck_packages:
            if i[5] == '9:00 AM':
                print(i)
        for i in truck3.truck_packages:
            if i[5] == '9:00 AM':
                print(i)
    if deadline == 2:
        for i in truck1.truck_packages:
            if i[5] == '10:30 AM':
                print(i)
        for i in truck2.truck_packages:
            if i[5] == '10:30 AM':
                print(i)
        for i in truck3.truck_packages:
            if i[5] == '10:30 AM':
                print(i)
    if deadline == 3:
        for i in truck1.truck_packages:
            if i[5] == 'EOD':
                print(i)
        for i in truck2.truck_packages:
            if i[5] == 'EOD':
                print(i)
        for i in truck3.truck_packages:
            if i[5] == 'EOD':
                print(i)


# Prints the packages with the given package city
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_city():
    print("Enter City:")
    city = str(input())
    for i in truck1.truck_packages:
        if i[2] == city:
            print(i)
    for i in truck2.truck_packages:
        if i[2] == city:
            print(i)
    for i in truck3.truck_packages:
        if i[2] == city:
            print(i)


# Prints the packages with the given package zipcode
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_zipcode():
    print("Enter ZipCode:")
    zipcode = int(input())
    for i in truck1.truck_packages:
        if i[4] == zipcode:
            print(i)
    for i in truck2.truck_packages:
        if i[4] == zipcode:
            print(i)
    for i in truck3.truck_packages:
        if i[4] == zipcode:
            print(i)


# Prints the packages with the given package weight
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_weight():
    print("Enter Weight:")
    weight = int(input())
    for i in truck1.truck_packages:
        if i[6] == weight:
            print(i)
    for i in truck2.truck_packages:
        if i[6] == weight:
            print(i)
    for i in truck3.truck_packages:
        if i[6] == weight:
            print(i)


# Prints the package status given an input
# Time Complexity O(N)
# Space Complexity O(1)
def find_package_by_status():
    print("Enter a number to check packages by status:"
          "\n1: Delayed On Flight"
          "\n2: At The Hub"
          "\n3: En Route"
          "\n4: Delivered")
    status_check = int(input())
    if status_check == 1:
        for i in truck1.truck_packages:
            if i[8] == 'Delayed On Flight':
                print(i)
        for i in truck2.truck_packages:
            if i[8] == 'Delayed On Flight':
                print(i)
        for i in truck3.truck_packages:
            if i[8] == 'Delayed On Flight':
                print(i)
    if status_check == 2:
        for i in truck1.truck_packages:
            if i[8] == 'At The Hub':
                print(i)
        for i in truck2.truck_packages:
            if i[8] == 'At The Hub':
                print(i)
        for i in truck3.truck_packages:
            if i[8] == 'At The Hub':
                print(i)
    if status_check == 3:
        for i in truck1.truck_packages:
            if i[8] == 'En Route':
                print(i)
        for i in truck2.truck_packages:
            if i[8] == 'En Route':
                print(i)
        for i in truck3.truck_packages:
            if i[8] == 'En Route':
                print(i)
    if status_check == 4:
        for i in truck1.truck_packages:
            if i[8] == 'Delivered':
                print(i)
        for i in truck2.truck_packages:
            if i[8] == 'Delivered':
                print(i)
        for i in truck3.truck_packages:
            if i[8] == 'Delivered':
                print(i)
