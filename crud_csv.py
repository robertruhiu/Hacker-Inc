import csv


def save_csv(file_name, fieldnames, dictionary):
	"""
	The function accepts a file_name, fieldnames and a dictionary to save into a csv file

	:param: file_name, fieldnames as a list, dictionary as dict
	"""
	with open(file_name, 'a+') as csvfile:
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    writer.writeheader()
	    writer.writerow(dictionary)
	   

def read_csv(file_name):
	"""
	The function accepts a file_name and reads from a csv file

	:param: file_name
	"""
	with open(file_name) as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	print(row.values())


         