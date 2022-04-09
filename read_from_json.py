"""
This file reads data from .json file in the specified format

Created by: Nadeem Abdelkader on 9/4/2022
Last updated by Nadeem Abdelkader on 9/4/2022

"""
# importing the necessary libraries for working with JSON
import json

# Field names
FIELDS = ('User Name', 'Group Name', 'Active Directory Name', 'Password', 'Re-enter Password', 'Host Name',
          'Interface Name', 'IP address', 'Network Name', 'Gateway', 'DNS')


def read_from_json(filename):
    """
    This function reads the previous users data from a .json file that can contain 0 or more json objects
    (stored as an array of json objects)
    :param filename: file to get the records from
    :return: an array of json objects
    """
    input_file = open(filename)
    json_array = json.load(input_file)
    return json_array


"""
Example user info retrieval
"""
# read from users.json
user_list = read_from_json("users.json")
# get the user name of the first user (loop can be used to get all user names or group names, etc...)
print(user_list.get("User Name"))
