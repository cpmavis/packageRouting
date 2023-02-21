import csv
from hash_table import Hashmap


# Creates a Package object containing all the information that is read from the package CSV file
class Packages:

    # Reads and extracts the data from the CSV file
    # Creates an instance of a Hashmap object under the name of package_hash
    with open('WGUPS Package File.csv', 'r') as csv_file:
        package_csv = csv.reader(csv_file, delimiter=',')
        package_hash = Hashmap()

        # Iterates through each row of the csv list assigns a variable to each item in the row
        # Time Complexity O(N)
        # Space Complexity O(1)
        for row in package_csv:
            p_ID = int(row[0])
            p_address = row[1]
            p_city = row[2]
            p_state = row[3]
            p_zip = int(row[4])
            p_delivery_deadline = row[5]
            p_mass = int(row[6])
            p_notes = row[7]
            p_delivery_status = "At The Hub"
            p_delivery_time = "Undelivered"

            # Assigns a Key and Value to be inserted into the Hashmap object
            key = p_ID
            value = [p_ID, p_address, p_city, p_state, p_zip, p_delivery_deadline, p_mass, p_notes,
                     p_delivery_status, p_delivery_time]

            # Some packages have not yet arrived so sets their value to being delayed
            for lt in range(len(value)):
                if value[7] == 'Delayed on flight---will not arrive to depot until 9:05 am':
                    value[8] = 'Delayed On Flight'
            # Inserts each Key, Value pair into the Hashmap object
            # Time Complexity O(1)
            # Space Complexity O(1)
            package_hash.insert(key, value)
