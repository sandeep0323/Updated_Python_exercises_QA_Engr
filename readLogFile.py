import pytz

timeStamp_i = 0
elapsed_i = 1
label_i = 2
responseCode_i = 3
responseMessage_i = 4
threadName_i = 5
dataType_i = 6
success_i = 7
failureMessage_i = 8
bytes_i = 9
sentBytes_i = 10
grpThreads_i = 11
allThreads_i = 12
URL_i = 13
Latency_i = 14
IdleTime_i = 15
Connect_i = 16

ROOT_PATH = '/Users/z993415/Downloads/Updated_Python_exercises_QA_Engr'

import csv
from datetime import datetime

def read_csv_file(file_name):
    file = open(file_name)
    csv_reader = csv.reader(file)
    headers = next(csv_reader)
    return headers, csv_reader


"""
and in the case if there are any non-successful endpoint responses recorded in the log,
prints out the label, response code, response message, failure message,
and the time of non-200 response in human-readable format in PST timezone
(e.g. 2021-02-09 06:02:55 PST).

"""
def test():
    files_list = ['Jmeter_log1.jtl', 'Jmeter_log2.jtl']

    for file in files_list:
        headers, cvs_reader = read_csv_file(ROOT_PATH + '/' + file)
        # loop over lines
        for row in cvs_reader:
            # check the response codes
            if row[responseCode_i] != '200':
                label = row[label_i]
                response_code = row[responseCode_i]
                response_message = row[responseMessage_i]
                failure_message = row[failureMessage_i]
                time = row[timeStamp_i]
                time = datetime.fromtimestamp(int(time) / 1000.0, tz=pytz.timezone('PST8PDT')).strftime('%Y-%m-%d %H:%M:%S %Z')
                print(time, label, response_code, response_message, failure_message)


test()