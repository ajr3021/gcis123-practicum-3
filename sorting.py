ROCHESTER_LATITUDE = 43.1566
ROCHESTER_LONGITUDE = 77.6088

"""
Given a csv file containing the following header:
index,name,url,street_address,city,state,zip_code,country,latitude,longitude

Return a list of tuples containing only the street_address, latitude, and longitude.
"""
def get_data(filename):
    pass

"""
Create a custom sorting function to sort by nearest value to rochester,
based on the sum of the difference between the values latitude and rochester's
latitude and the difference between the values longitude and rochester's longitude.
"""
def sort_by_latitude(value):
    pass


def main():
    data = get_data("data/subway.csv")
    # sort the data
    # print the result
    # check for accuracy


if __name__ == '__main__':
    main()