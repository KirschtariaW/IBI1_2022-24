# import the required libraries, xml.dom.minidom for parsing XML and xlsxwriter for creating Excel files.
import xml.dom.minidom
import xlsxwriter

domtree = xml.dom.minidom.parse("go_obo.xml")
obo = domtree.documentElement
terms = obo.getElementsByTagName('term')

#childnodes function is defined to calculate the number of child nodes recursively for a given child_id
def find_childnodes(child_id):
    number = 0
    for term_child in terms:
        id_element = term_child.getElementsByTagName("id")[0]
        term_id = id_element.firstChild.data
        
        if term_id == child_id:
            is_a_elements = term_child.getElementsByTagName("is_a")
            for is_a_element in is_a_elements:
                is_a_id = is_a_element.childNodes[0].data
                number += 1 + find_childnodes(is_a_id)
    return number

# create an empty list autophagosome to store the nodes related to 'autophagosome'
autophagosome = []
for term in terms: #iterate through each term element and check if the term's definition contains the word 'autophagosome'
    if "autophagosome" in term.getElementsByTagName('defstr')[0].firstChild.data:
        go_id = term.getElementsByTagName('id')[0].childNodes[0].data
        name = term.getElementsByTagName('name')[0].childNodes[0].data
        defstr_node = term.getElementsByTagName('defstr')[0].childNodes[0].data
        child_nodes = find_childnodes(go_id)
        autophagosome.append((go_id, name, defstr_node, child_nodes))
# create an Excel workbook
workbook = xlsxwriter.Workbook("autophagosome.xlsx")
worksheet = workbook.add_worksheet()

# write the column headers "Go_id", "Name", "Definition", and "Childnodes" 
worksheet.write_row(0, 0, ["Go_id", "Name", "Definition", "Childnodes"])


for row, data in enumerate(autophagosome, start=1):
    worksheet.write_row(row, 0, data)

# Close the workbook
workbook.close()


