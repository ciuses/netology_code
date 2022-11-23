import collections
import xml.etree.ElementTree as el_tree

my_tree = el_tree.ElementTree(file='other\\newsafr.xml')

my_root = my_tree.getroot()
# print(my_root.tag)
any_words = []

for child in my_root:
    # print('tag--', child.tag, 'attrib--', child.attrib)
    for child_in_child in child:
        # print('\ttag---', child_in_child.tag, 'attrib', child_in_child.attrib)
        for child_v2 in child_in_child:
            # print('\ttag---', child_v2.tag, 'attrib', child_v2.attrib, child_v2.text)
            if child_v2.tag == 'description':
                # print(type(child_v2.text), child_v2.text)
                nechto = [word for word in child_v2.text.split(' ') if len(word) > 6]
                any_words.extend(nechto)

# print(any_words)
coun = collections.Counter(any_words)

for my_tuple in coun.most_common(10):
    print(my_tuple)
