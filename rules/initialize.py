import os
import xmltodict
import pprint
from collections.abc import Iterable
from data_structs import profileType, characteristicType, categoryEntries

#first_edition_dataset = os.path.join(os.path.join(os.pardir, 'data_files'), "Star Wars Xwing.gst")
first_edition_dataset = os.path.join('data_files', "Star Wars Xwing.gst")
second_edition_dataset = os.path.join("..\\data_files", "Star_Wars_X_Wing_2e.gst")

with open(first_edition_dataset, 'r') as file:
    my_xml = file.read()

my_dict = xmltodict.parse(my_xml)

#print(my_dict)

new_dict = {}
for type in my_dict['gameSystem']:
    if type in ['profileTypes', 'categoryEntries','selectionEntries','forceEntries'] and isinstance(my_dict['gameSystem'][type], Iterable):
        for item in my_dict['gameSystem'][type]:
            item_dict = {}
            for entry in my_dict['gameSystem'][type][item]:
                if item == 'profileType':
                    characteristicsList = []
                    for characteristType in entry['characteristicTypes']:
                        characteristicDict = {}
                        if isinstance(entry['characteristicTypes']['characteristicType'], dict):
                            id = entry['characteristicTypes']['characteristicType']['@id']
                            name = entry['characteristicTypes']['characteristicType']['@name']
                            # characteristicDict[id] = name
                            characteristicDict[id] = characteristicType(id, name)
                            characteristicsList.append(characteristicDict)
                        else:
                            for characteristic in entry['characteristicTypes']['characteristicType']:
                                id = characteristic['@id']
                                name = characteristic['@name']
                                # characteristicDict[id] = name
                                characteristicDict[id] = characteristicType(id, name)
                            characteristicsList.append(characteristicDict)
                    profile = { 'name': entry['@name'],
                                'characteristicTypes': characteristicsList }
                    item_dict[entry['@id']] = profileType(entry['@id'], entry['@name'], characteristicDict)
                if item == 'categoryEntry':
                    # item_dict[entry['@id']] = { 'name': entry['@name'],
                    #                             'hidden': entry['@hidden'] }
                    item_dict[entry['@id']] = categoryEntries(entry['@id'], entry['@name'], entry['@hidden'])
            new_dict[type] = item_dict

pprint.pprint(new_dict, indent=2)
print(new_dict['profileTypes']['876b5288-62fa-bc8e-32fe-989964372b8f'].characteristicTypes)
print(new_dict['profileTypes']['3250696c6f74204162696c69747923232344415441232323'].characteristicTypes)