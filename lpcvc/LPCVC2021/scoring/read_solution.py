import csv
import sys


def convert_frame_number_into_int(list_items):
    try:
        for i, item in enumerate(list_items):
            if 'frame' in item:
                list_items[i]['frame'] = int(item['frame'])
    except ValueError:
        print('Error: Value Error Inside Code', file=sys.stderr)
        exit()


def get_dict_from_solution(file_name):
    try:
        fp = open(file_name)
        csv_read = csv.DictReader(fp)
        response = [{k.lower(): v for k, v in i.items() if k is not None} for i in csv_read]
        convert_frame_number_into_int(response)
        fp.close()
    except FileNotFoundError:
        print('Error: File Does not Exists', file=sys.stderr)
        response = None
        exit()
    return response
