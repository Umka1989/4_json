import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=4,ensure_ascii=False))


if __name__ == '__main__':
    loaded_json = load_data(filepath)
    pretty_print_json(loaded_json)

