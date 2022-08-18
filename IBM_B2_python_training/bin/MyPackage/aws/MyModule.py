"""
In this file we are keeping
    - 0 or more variables
    - 0 or more functions definition
    - 0 or more class definitions
    which we may need to reuse in more than 1 programs/project/person/team

This file is called as PYTHON MODULE or PYTHON LIBRARY
"""

location = "India"


def log_process_func_keyword(*, log_file_path):
    """
    Function will take log file path as an argument, extract info then
    return extracted info in this form
    [(ip,dt,img,url), (ip,dt,img,url),(ip,dt,img,url)]
    :param log_file_path:
    :return list_of_tuples:
    """

    # Get data from log file
    # -----------------------
    my_file_handle = open(log_file_path, 'r')
    list_of_lines = my_file_handle.readlines()
    my_file_handle.close()
    # -----------------------

    # Extract info
    # -----------------------
    final_result = []
    for each_line in list_of_lines:
        if each_line.startswith('123'):

            sp = each_line.split()  # split by space

            ip = sp[0]

            raw_dt = sp[3]  # '[26/Apr/2000:00:23:48'
            first_colon_index = raw_dt.index(":")
            dt = raw_dt[1:first_colon_index]

            raw_img = sp[6]  # '/pics/wpaper.gif'
            if raw_img.startswith('/pics'):
                img = raw_img.lstrip('/pics/')
            else:
                img = "No Image"

            url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
            url = url[1:-1]
            each_line_tuple = (ip, dt, img, url)
            final_result.append(each_line_tuple)
    return final_result
    # -----------------------

