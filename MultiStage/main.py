import itertools

from utils import get_data, get_index_from_dict, SUPPORT_S

df = get_data()

stock_dictionary = {}
customer_dictionary = {}

MESSAGE = """PASS #1"""
print(MESSAGE)
for index, row in df.iterrows():
    customer = int(row['CustomerID'])
    stock = row['StockCode']

    if customer not in customer_dictionary:
        customer_dictionary[customer] = set()
    customer_dictionary[customer].add(stock)

    if stock not in stock_dictionary:
        stock_dictionary[stock] = {
            'id': get_index_from_dict(stock_dictionary),
            'stock': stock,
            'count': 0
        }
    stock_dictionary[stock]['count'] += 1
MESSAGE = """PASS #2"""
print(MESSAGE)

combination_dictionary = {}

hash1_dict = {}
hash2_dict = {}

for stocks in customer_dictionary.values():
    for subset in itertools.combinations(stocks, 2):
        if subset not in combination_dictionary:
            try:
                combination_dictionary[subset] = {
                    'combination': subset,
                    'count': 0,
                    'hash1': (stock_dictionary[subset[0]]['id'] + stock_dictionary[subset[1]]['id']) % len(
                        stock_dictionary.keys()),
                    'hash2': (stock_dictionary[subset[0]]['id'] + 2 * stock_dictionary[subset[1]]['id']) % len(
                        stock_dictionary.keys())
                }
            except:
                print((stock_dictionary[subset[0]]['id'] + stock_dictionary[subset[1]]['id']))
                print('dd')
                print('dd')
                print('dd')

            combination_dictionary[subset]['count'] += 1

for subset_item in combination_dictionary.values():
    count = subset_item['count']
    hash1 = subset_item['hash1']
    hash2 = subset_item['hash2']
    subset = subset_item['combination']
    if hash1 not in hash1_dict:
        hash1_dict[hash1] = {
            'subsets': set(),
            'count': 0
        }
    if hash2 not in hash2_dict:
        hash2_dict[hash2] = {
            'subsets': set(),
            'count': 0
        }
    hash1_dict[hash1]['subsets'].add(subset)
    hash1_dict[hash1]['count'] += count

    hash2_dict[hash2]['subsets'].add(subset)
    hash2_dict[hash2]['count'] += count

hash1_to_delete = []
for hash1_key in hash1_dict.keys():
    if hash1_dict[hash1_key]['count'] <= SUPPORT_S:
        hash1_to_delete.append(hash1_key)

hash2_to_delete = []
for hash2_key in hash2_dict:
    if hash2_dict[hash2_key]['count'] <= SUPPORT_S:
        hash2_to_delete.append(hash2_key)

for to_delete in hash1_to_delete:
    del hash1_dict[to_delete]

for to_delete in hash2_to_delete:
    del hash2_dict[to_delete]

MESSAGE = """PASS #3"""
print(MESSAGE)
all_true_combinations = set()

for hash1_key in hash1_dict.keys():
    hash1_item = hash1_dict[hash1_key]

    new_list = []

    for index, combination in enumerate(hash1_item['subsets']):
        if stock_dictionary[combination[0]]['count'] > SUPPORT_S and \
                stock_dictionary[combination[1]]['count'] > SUPPORT_S:
            new_list.append(combination)

    hash1_item['subsets'] = new_list
    all_true_combinations = all_true_combinations | set(new_list)

for hash2_key in hash2_dict.keys():
    hash2_item = hash2_dict[hash2_key]

    new_list = []

    for index, combination in enumerate(hash2_item['subsets']):
        if stock_dictionary[combination[0]]['count'] > SUPPORT_S and \
                stock_dictionary[combination[1]]['count'] > SUPPORT_S:
            new_list.append(combination)

    hash2_item['subsets'] = new_list
    all_true_combinations = all_true_combinations | set(new_list)

print('SINGLETONS')
for i in stock_dictionary.keys():
    if stock_dictionary[i]['count'] > SUPPORT_S:
        print(f'(\'{i}\')')

print('DOUBLETONS')
for i in all_true_combinations:
    print(i)
