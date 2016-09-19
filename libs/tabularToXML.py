from xml.dom.minidom import parseString   # Python standard library
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import lxml.etree as etree
from xlrd import open_workbook

# inputs (list,list)
def table_xml(data_sheets,sheet_names):
	xml_section = []
	xml_file = []
	for sh in range(len(data_sheets)):
		rows = len(data_sheets[sh])
		cols = len(data_sheets[sh][0])

		table = {'headers': [], 'values': []}
		table['headers'] = data_sheets[sh][0]
		table['values'] = data_sheets[sh][1:]

		root = etree.Element("table")
		root.set("name", sheet_names[sh])

		header = etree.SubElement(root, "headers")
		values = etree.SubElement(root, "rows")

		col_index = 0

		for header_name in table['headers']:
			header_cell = etree.SubElement(header, 'column')
			header_cell.set('id', str(col_index))
			header_cell.text = header_name

			col_index += 1

		row_index = 0
		for value_list in table['values']:
			value_row = etree.SubElement(values, 'row')
			value_row.set('id', str(row_index))
			col_index = 0

			for value in value_list:
				value_cell = etree.SubElement(value_row, 'column')
				value_cell.set('id', str(col_index))
				if not value:
					value = 0
				value_cell.text = str(value)

				col_index += 1

			row_index += 1

		xml_string = etree.tostring(header)
		xml_string += etree.tostring(values)
		xml_section.append(xml_string)
		xml_file.append(parseString(tostring(root)).toprettyxml())

	return (xml_section,xml_file)


def execel_xml(filename):
	xlfile = open_workbook(filename)

	sheet_names = []
	sheet_names = xlfile.sheet_names()

	sheet_content = []
	for sh in range(len(sheet_names)):
		sheet_content.append(xlfile.sheet_by_name(sheet_names[sh]))

	datasheet = []
	for sh in range(len(sheet_content)):
		rows = sheet_content[sh].nrows
		data_p_sheet = []
		for x in range(rows):
			if any(sheet_content[sh].row_values(x)): # clean empty rows
				data_p_sheet.append(sheet_content[sh].row_values(x))

		datasheet.append(data_p_sheet)

	xml_section,xml_file = table_xml(datasheet,sheet_names)

	return (xml_section,xml_file)
