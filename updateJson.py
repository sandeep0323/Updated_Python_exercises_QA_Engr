import json


ROOT_PATH = '/Users/z993415/Downloads/Updated_Python_exercises_QA_Engr'


def read_json_from_file(file_path):
    f = open(file_path)
    return json.load(f)

# remove the parameter by name (say for example if json_element = "outParams" or "appdate"
def remove_json_element(json_data, json_element):
    for key in json_data.keys():
        if key == json_element:
            del json_data[key]
            break  # data matched , so break loop
        elif type(json_data[key]) == dict:
            json_data[key] = remove_json_element(json_data[key], json_element)  # recursive to go deeper

    return json_data


'''
remove the parameter by entire json (say for example if remove_json_element ,
Note: this will remove if entire nested data matches

ex json_element = "{"outParams": [
    "dateeff",
    "dateterm",
    "coverageresult",
    "calcdescr",
    "errorchk",
    "planresult",
    "covgsummary",
    "prem"
  ]}
  
  or 
  
  json_element = {"appdate": "2019-04-02"}
'''

def remove_json_element_with_entire_data(json_data, json_element):
    for key, value in json_data.items():
        if key == json_element.keys()[0] and value == json_element[json_element.keys()[0]]:
            del json_data[key]
            break  # data matched , so break loop
        elif type(json_data[key]) == dict:
            json_data[key] = remove_json_element(json_data[key], json_element)  # recursive to go deeper

    return json_data


def write_json(file_path, json_data):
    with open(file_path, "w") as outfile:
        json.dump(json_data, outfile, indent=4)
        outfile.flush()
        outfile.close()

# test
def test():
    json_data = read_json_from_file(ROOT_PATH + '/test_payload.json')
    json_data = remove_json_element(json_data=json_data, json_element='outParams')
    write_json(file_path=ROOT_PATH + '/test_payload_output.json', json_data=json_data)

test()
