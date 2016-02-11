#Plan is to import Business JSON's and then turn them into python classes, so that we can store critical attributes of them.

import csv
import json

import peakCheckIn3

class business:
	id = 'none'
	longitude = 0
	latitude = 0
	peakCheckIns = 0

def main():
	
	#Example business string
	b1 = '{"business_id": "5UmKMjUEUNdYWqANhGckJw", "full_address": "4734 Lebanon Church Rd\nDravosburg, PA 15034", "hours": {"Friday": {"close": "21:00", "open": "11:00"}, "Tuesday": {"close": "21:00", "open": "11:00"}, "Thursday": {"close": "21:00", "open": "11:00"}, "Wednesday": {"close": "21:00", "open": "11:00"}, "Monday": {"close": "21:00", "open": "11:00"}}, "open": true, "categories": ["Fast Food", "Restaurants"], "city": "Dravosburg", "review_count": 4, "name": "Mr Hoagie", "neighborhoods": [], "longitude": -79.9007057, "state": "PA", "stars": 4.5, "latitude": 40.3543266, "attributes": {"Take-out": true, "Drive-Thru": false, "Good For": {"dessert": false, "latenight": false, "lunch": false, "dinner": false, "brunch": false, "breakfast": false}, "Caters": false, "Noise Level": "average", "Takes Reservations": false, "Delivery": false, "Ambience": {"romantic": false, "intimate": false, "classy": false, "hipster": false, "divey": false, "touristy": false, "trendy": false, "upscale": false, "casual": false}, "Parking": {"garage": false, "street": false, "validated": false, "lot": false, "valet": false}, "Has TV": false, "Outdoor Seating": false, "Attire": "casual", "Alcohol": "none", "Waiter Service": false, "Accepts Credit Cards": true, "Good for Kids": true, "Good For Groups": true, "Price Range": 1}, "type": "business"}'

	#Convert business to a dictionary
	b1_dict = json.loads( b1.replace('\n','_') )
	#Make sure to ignore the \n in the business JSON's because they mess with json.loads

	#Make b1 into one of our python class objects
	b1_cl = business()
	b1_cl.id = b1_dict['business_id']

	print 'b1_cl.id is ' + b1_cl.id

	#Stuff business data into this structure
	b1_cl.longitude = b1_dict['longitude']
	b1_cl.latitude  = b1_dict['latitude']

	#Calculate info from check in data and place it into business struct, then print.
	example_ci = '{"checkin_info": {"9-5": 1, "7-5": 1, "13-3": 1, "17-6": 1, "13-0": 1, "17-3": 1, "10-0": 1, "18-4": 1, "14-6": 1}, "type": "checkin", "business_id": "cE27W9VPgO88Qxe4ol6y_g"}'
	
	b1_cl.peakCheckIns = peakCheckIn3.findPeakCI( example_ci )

	#declare example.csv as the file we will output to
	with open('example.csv','w') as fout:
		#The 'writer' to fout we will actually call csv_file
		csv_file = csv.writer(fout)

		csv_file.writerow( [ b1_cl.id , b1_cl.longitude , b1_cl.latitude , b1_cl.peakCheckIns ])


if __name__ == '__main__':
	main()