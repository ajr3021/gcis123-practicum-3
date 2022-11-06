import csv

ROCHESTER_LATITUDE = 43.1566
ROCHESTER_LONGITUDE = -77.6088

"""
Given a csv file containing the following header:
index,name,url,street_address,city,state,zip_code,country,hours,latitude,longitude

Return a list of tuples containing only the street_address, latitude, and longitude.
"""
def get_data(filename):
    data = []
    
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for line in reader:
            data.append((line[3], float(line[9]), float(line[10])))

    return data

"""
Create a custom sorting function to sort by nearest value to rochester,
based on the sum of the difference between the values latitude and rochester's
latitude and the difference between the values longitude and rochester's longitude.

Note: The differences should be in absolute value
"""
def sort_by_latitude_longitude(value):
    return abs(ROCHESTER_LATITUDE - value[1]) + abs(ROCHESTER_LONGITUDE - value[2])

def main():
    data = get_data("data/subway.csv")
    # sort the data
    data.sort(key=sort_by_latitude_longitude)
    # print the result
    print(data)
    # check for accuracy
    print(data[0])


if __name__ == '__main__':
    main()
