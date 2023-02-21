#   Corey Mavis
#   Student ID # 001483445

import trucks


# Time Complexity O(N^2)
# Space Complexity O(N)
def user_interface():
    print("Welcome to the truck delivery hub. We are scheduled to begin the deliveries at 8:00 AM. " +
          "\nWould you like to check on the packages?" + "\nType Yes to check on the packages")

    # initial status of all the packages
    s = str(input())
    if s == 'Yes':
        trucks.print_packages()
    else:
        trucks.check_packages(8, 0, 0)

    print("It is time for the first check."
          "\nEnter a time between 8:35 AM and 9:25 AM in the form of HH:MM:SS")
    s = str(input())
    time_check = s.split(':')
    trucks.check_packages(hour=int(time_check[0]), minute=int(time_check[1]), second=int(time_check[2]))
    # status of the packages between 8:35 AM and 9:25 AM
    print("How would you like to check on the packages?"
          "\n1: Check All"
          "\n2: Check by ID"
          "\n3: Check by Address"
          "\n4: Check by Deadline"
          "\n5: Check by City"
          "\n6: Check by ZipCode"
          "\n7: Check by Weight"
          "\n8: Check by Status"
          "\n9: Hit 9 to skip")

    checker = int(input())
    print("Current time: " + s)
    if checker == 1:
        trucks.print_packages()
    if checker == 2:
        trucks.find_package_by_id()
    if checker == 3:
        trucks.find_package_by_address()
    if checker == 4:
        trucks.find_package_by_deadline()
    if checker == 5:
        trucks.find_package_by_city()
    if checker == 6:
        trucks.find_package_by_zipcode()
    if checker == 7:
        trucks.find_package_by_weight()
    if checker == 8:
        trucks.find_package_by_status()
    if checker == 9:
        print("Check Skipped")

    print("It is time for the second check."
          "\nEnter a time between 9:35 AM and 10:25 AM in the form of HH:MM:SS")
    s = str(input())
    time_check = s.split(':')
    trucks.check_packages(hour=int(time_check[0]), minute=int(time_check[1]), second=int(time_check[2]))
    # status of the packages between 9:35 AM and 10:25 AM
    print("How would you like to check on the packages?"
          "\n1: Check All"
          "\n2: Check by ID"
          "\n3: Check by Address"
          "\n4: Check by Deadline"
          "\n5: Check by City"
          "\n6: Check by ZipCode"
          "\n7: Check by Weight"
          "\n8: Check by Status"
          "\n9: Hit 9 to skip")

    checker = int(input())
    print("Current time: " + s)
    if checker == 1:
        trucks.print_packages()
    if checker == 2:
        trucks.find_package_by_id()
    if checker == 3:
        trucks.find_package_by_address()
    if checker == 4:
        trucks.find_package_by_deadline()
    if checker == 5:
        trucks.find_package_by_city()
    if checker == 6:
        trucks.find_package_by_zipcode()
    if checker == 7:
        trucks.find_package_by_weight()
    if checker == 8:
        trucks.find_package_by_status()
    if checker == 9:
        print("Check Skipped")

    print("It is time for the final check."
          "\nEnter a time between 12:03 PM and 1:12 PM in the form of HH:MM:SS")
    s = str(input())
    time_check = s.split(':')
    trucks.check_packages(hour=int(time_check[0]), minute=int(time_check[1]), second=int(time_check[2]))
    # status of the packages between 12:13 PM and 1:12 PM
    print("How would you like to check on the packages?"
          "\n1: Check All"
          "\n2: Check by ID"
          "\n3: Check by Address"
          "\n4: Check by Deadline"
          "\n5: Check by City"
          "\n6: Check by ZipCode"
          "\n7: Check by Weight"
          "\n8: Check by Status"
          "\n9: Hit 9 to skip")

    checker = int(input())
    print("Current time: " + s)
    if checker == 1:
        trucks.print_packages()
    if checker == 2:
        trucks.find_package_by_id()
    if checker == 3:
        trucks.find_package_by_address()
    if checker == 4:
        trucks.find_package_by_deadline()
    if checker == 5:
        trucks.find_package_by_city()
    if checker == 6:
        trucks.find_package_by_zipcode()
    if checker == 7:
        trucks.find_package_by_weight()
    if checker == 8:
        trucks.find_package_by_status()
    if checker == 9:
        print("Check Skipped")

    trucks.check_packages(23, 59, 59)   # End of the day and all the packages have been delivered
    print("All packages are delivered")

    # Miles driven by truck1
    print("Truck 1 information:")
    trucks.truck1_status()

    # Miles driven by truck1
    print("Truck 2 information")
    trucks.truck2_status()

    # Miles driven by truck1
    print("Truck 3 information")
    trucks.truck3_status()

    # total miles driven by all the trucks
    trucks.total_miles_travelled()


# runs the program for the user to check on the packages
user_interface()
