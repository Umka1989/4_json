import json
import sys
import os.path


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            json_data = load_data(sys.argv[1])
            pretty_print_json(json_data)
        else:
            print ('need positional first argument - correct path to file')

