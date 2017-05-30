import pandas as pd
import datetime
from datetime import timedelta
import re
from xml.etree.ElementTree import Element, SubElement, tostring


def el_to_xml(el):
    el_name = 'M'
    el = el.split('/')[1:-1]
    elements = []
    for i in range(len(el), 0, -1):
        level = i
        name = '.' + '.'.join(el[:i]) + '.'
        element = Element(el_name)
        element.attrib = {'Level': str(level), 'Name': name}
        elements.append(element)
    if len(elements) == 0:
        return None
    xml = elements[-1]
    for i in range(len(elements)-1, 0, -1):
        root = elements[i-1]
        root.append(xml)
        xml = root
    return tostring(xml)

date = datetime.date(2099, 12, 21)
df = pd.read_csv('input.tsv', sep='\t', header=None)#, error_bad_lines=False)
df = df.to_records()
columns = ['goal', 'local_id', 'hier_item', 'start_date', 'end_date', 'action', 'attribute', 'name', 'full_name']
df_1 = pd.DataFrame([], columns=columns)

for row in df:
    row = tuple(row)
    goal = row[1]
    hier_item = row[2]
    ind = 0
    for col in row:
        days_to_add = timedelta(ind - 3)
        col = str(col)
        if len(re.findall('.*(s)Attr.*', col)) > 0:
            start_date = date + days_to_add
            action = re.findall('(\d?)s.*', col)[0]
            attribute = re.findall('.*Attr(\d+).*', col)[0]
        if len(re.findall('.*(e$)', col)) > 0:
            end_date = date + days_to_add
            start_date = start_date.year * 10000 + start_date.month * 100 + start_date.day
            end_date = end_date.year * 10000 + end_date.month * 100 + end_date.day
            action = 'Null' if action == '' else action
            attribute = '<Attributes><Attribute Name="' + str(attribute) + '"></Attribute></Attributes>'
            df_1 = df_1.append(pd.DataFrame([[goal, hier_item.replace('/', ''), hier_item, start_date, end_date, action, attribute, hier_item.replace('/', '.'), el_to_xml(hier_item)]], columns=columns), ignore_index=True)
            # print "('{}',\t'{}',\t'{}',\t'{}',\t{},\t'{}',\t'{}'),".format(goal, hier_item, start_date, end_date, action, attribute, el_to_xml(hier_item))
            # print '{}\t{}\t{}\t{}\t{}\t{}'.format(location, hier_item, start_date, end_date, action, attribute)
            start_date = end_date = action = attribute = None
        ind += 1

# pd.set_option('precision', 6)

# set format for columns
df_1[['start_date', 'end_date']] = df_1[['start_date', 'end_date']].astype(int)

# building hier_member
columns=['local_id', 'hier_item', 'name', 'full_name']
hier_member = pd.DataFrame(df_1[columns][1:], columns=columns).drop_duplicates()
print hier_member.to_csv(sep='\t', index=False)

# building hier_member_version
columns=['hier_item', 'start_date', 'end_date', 'attribute']
hier_member_version = pd.DataFrame(df_1[columns][df_1['goal']=='ini'][1:], columns=columns)
hier_member_version[['start_date', 'end_date']] = hier_member_version[['start_date', 'end_date']].astype(int)
print hier_member_version.to_csv(sep='\t', index=False)

# building hier_member_version_inp
columns=['local_id', 'hier_item', 'start_date', 'end_date', 'action', 'attribute']
hier_member_version_inp = pd.DataFrame(df_1[columns][df_1['goal']=='inp'][1:], columns=columns)
print hier_member_version_inp.to_csv(sep='\t', index=False)

# building hier_member_version_res
columns=['hier_item', 'start_date', 'end_date', 'attribute']
hier_member_version_res = pd.DataFrame(df_1[columns][df_1['goal']=='res'][1:], columns=columns)
hier_member_version_res[['start_date', 'end_date']] = hier_member_version_res[['start_date', 'end_date']].astype(int)
print hier_member_version_res.to_csv(sep='\t', index=False)
