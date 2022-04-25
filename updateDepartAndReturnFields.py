import xml.etree.ElementTree as ET
from datetime import date, timedelta

ROOT_PATH = '/Users/z993415/Downloads/Updated_Python_exercises_QA_Engr'


def write_xml_to_file(file_path, xml_tree):
    with open(file_path, 'wb') as f:
        xml_tree.write(f)
        f.flush()
        f.close()


def update_depart_and_return_fields(file_path, depart_days, return_days):
    # read the xml file
    xml_tree = ET.parse(file_path)
    xml_tree.find(".//DEPART").text = (date.today() + timedelta(depart_days)).strftime('%y%m%d')
    xml_tree.find(".//RETURN").text = (date.today() + timedelta(return_days)).strftime('%y%m%d')
    write_xml_to_file(file_path=ROOT_PATH + '/test_payload_output.xml', xml_tree=xml_tree)


# test the program
update_depart_and_return_fields(ROOT_PATH + '/test_payload1.xml', 10, 15)

