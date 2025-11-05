import xml.etree.ElementTree as ET
tree = ET.parse('example.xml')
root = tree.getroot()

for child in root:
    for subchild in child:
        if subchild.tag == 'timingExbytes':
            new_el = ET.SubElement(subchild, 'new_element')
            new_el.text = 'new_value'

ET.ElementTree(root).write('example.xml')