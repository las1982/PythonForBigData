import pandas as pd

# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
# def split_title_and_name(person):
#     return person.split()[0] + ' ' + person.split()[-1]
#
# #option 1
# for person in people:
#     print(split_title_and_name(person) == (lambda person: '{} {}'.format(person.split()[0], person.split()[-1]))(person))
#
# #option 2
# print list(map(split_title_and_name, people)) == list(map(lambda person: '{} {}'.format(person.split()[0], person.split()[-1]), people))
#
# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range (10):
#             lst.append(i*j)
#     return lst
#
# print times_tables() == [i*j for i in range(10) for j in range(10)]
#
# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
#
# answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]
#
# r = np.arange(36)
# r.resize((6, 6))
# print r
# print r[2:4, 2:4]
#
# import pandas as pd
#
# purchase_1 = pd.Series({'Name': 'Chris',
#                         'Item Purchased': 'Dog Food',
#                         'Cost': 22.50})
# purchase_2 = pd.Series({'Name': 'Kevyn',
#                         'Item Purchased': 'Kitty Litter',
#                         'Cost': 2.50})
# purchase_3 = pd.Series({'Name': 'Vinod',
#                         'Item Purchased': 'Bird Seed',
#                         'Cost': 5.00})
#
# df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
#
# df = df.set_index([df.index, 'Name'])
# df.index.names = ['Location', 'Name']
#
# df = df.append(pd.Series(data={
#                         'Item Purchased': 'Kitty Food',
#                         'Cost': 3.00}, name=('Store 2', 'Kevyn')))
# print df

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
print df

# for col in df.columns:
#     if col[:2]=='01':
#         df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
#     if col[:2]=='02':
#         df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
#     if col[:2]=='03':
#         df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
#     if col[:1]=='№':
#         df.rename(columns={col:'#'+col[1:]}, inplace=True)
#
# names_ids = df.index.str.split('\s\(') # split the index by '('
#
# df.index = names_ids.str[0] # the [0] element is the country name (new index)
# df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
#
# df = df.drop('Totals')
# df.head()