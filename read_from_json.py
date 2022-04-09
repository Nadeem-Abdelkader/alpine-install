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
    user_list = []

    for user in json_array:
        user_details = {FIELDS[0]: None, FIELDS[1]: None, FIELDS[2]: None, FIELDS[3]: None,
                        FIELDS[4]: None, FIELDS[5]: None, FIELDS[6]: None, FIELDS[7]: None,
                        FIELDS[8]: None, FIELDS[9]: None, FIELDS[10]: None, FIELDS[0]: user[FIELDS[0]],
                        FIELDS[1]: user[FIELDS[1]], FIELDS[2]: user[FIELDS[2]],
                        FIELDS[3]: user[FIELDS[3]], FIELDS[4]: user[FIELDS[4]],
                        FIELDS[5]: user[FIELDS[5]], FIELDS[6]: user[FIELDS[6]],
                        FIELDS[7]: user[FIELDS[7]], FIELDS[8]: user[FIELDS[8]],
                        FIELDS[9]: user[FIELDS[9]], FIELDS[10]: user[FIELDS[10]]}

        user_list.append(user_details)

    return user_list


"""
Example user info retrieval
"""
# read from users.json
user_list = read_from_json("users.json")
# get the user name of the first user (loop can be used to get all user names or group names, etc...)
print(user_list[0].get("User Name"))
