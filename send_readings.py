import sys
import requests

def send_reading(sensor, reading_type, reading_value):
	r = requests.post('http://172.17.0.1:5001/reading', json = {'sensor':sensor, 'reading_type': reading_type, 'reading_value':reading_value}, auth=('admin', 'admin'))
	print r 

if __name__ == "__main__":
	send_reading(sys.argv[1], sys.argv[2], sys.argv[3])
