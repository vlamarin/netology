import json

def create_common_list_without_comma(initial_list):
    all_news_list = []
    for item in initial_list:
        news_list = item['description'].split(' ')
        for el in news_list:
            if ',' in el:
                el.replace(',', '')
        all_news_list += news_list
    return all_news_list

def del_excess_words(initial_list):
    new_list = []
    for el in initial_list:
        if len(el) > 6:
            new_list.append(el)
    return new_list

def create_top_10_list(initial_list):
    stats_dict = {}
    for el in initial_list:
        stats_dict[el] = initial_list.count(el)
    sort_stats = sorted(stats_dict.items(), key=lambda x: x[1])
    top_10 = []
    for el in sort_stats:
        if sort_stats.index(el) >= sort_stats.index(sort_stats[-10]):
            top_10.append(el)
    top_10.reverse()
    return top_10

def pprint_top_10(initial_list):
    print('Топ 10 самых часто встречающихся в новостях слов (длиннее 6 символов):')
    number = 1
    for el in initial_list:
        print(f'{number}) Слово "{el[0]}" - {el[1]} повторений.')
        number += 1

def create_common_list_without_comma_xml(initial_list):
    descriptions = []
    for item in initial_list:
        description = item.find('description')
        descriptions += description.text.split(' ')
    for el in descriptions:
        if ',' in el:
            el.replace(',', '')
    return descriptions

with open('newsafr.json', encoding='utf8') as f:
    json_f = json.load(f)
    items_f = json_f['rss']['channel']['items']
    news_list = del_excess_words(create_common_list_without_comma(items_f))
    top_10 = create_top_10_list(news_list)
    pprint_top_10(top_10)


import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse('newsafr.xml', parser)

root = tree.getroot()
xml_items = root.findall('channel/item')
descriptions_list = del_excess_words(create_common_list_without_comma_xml(xml_items))
top_10_xml = create_top_10_list(descriptions_list)
pprint_top_10(top_10_xml)
