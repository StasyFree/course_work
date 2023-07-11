import json
from operations import Operation


def read_file(file):
    operations = []
    with open(file, encoding='utf-8') as f:
        new_file = json.load(f)

    count = 0
    for item in new_file:
        if 'id' not in item.keys():
            count += 1
        else:
            i_amount = item['operationAmount']
            i_currency = i_amount['currency']
            if 'from' in item.keys():
                operate = Operation(item['state'], item['date'], i_amount['amount'], i_currency['name'], item['description'], item['to'], item['from'])
            else:
                operate = Operation(item['state'], item['date'], i_amount['amount'], i_currency['name'], item['description'], item['to'])
            operations.append(operate)
            count += 1
    return operations


def sort_list(operations):
    operations.sort(key=lambda x: x.date, reverse=True)
    return operations


def choose(list_of_operations):
    count = 0
    five_operations = []
    for item in list_of_operations:
        if item.state == "EXECUTED":
            if count < 5:
                five_operations.append(item)
                count += 1
            else:
                return five_operations
