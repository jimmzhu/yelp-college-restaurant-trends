#This script will transform a business's categories into a vector with the 1-Hot encoding.
# (If a category exists for a business, then we will place a 1 in the corresponding slot in )

import constants
import json

ALL_CATEGORIES = [u'Food', u'Ice Cream & Frozen Yogurt', u'Grocery', u'Coffee & Tea', u'Beer, Wine & Spirits', u'Cheese Shops', u'Specialty Food', u'Sandwiches', u'Restaurants', u'Bakeries', u'Juice Bars & Smoothies', u'Cafes', u'Empanadas', u'Latin American', u'Colombian', u'Shopping', u'Wholesale Stores', u'Event Planning & Services', u'Party Supplies', u'Breakfast & Brunch', u'Butcher', u'Health Markets', u'Donuts', u'Desserts', u'Street Vendors', u'Shaved Ice', u'Meat Shops', u'Automotive', u'Convenience Stores', u'Gas & Service Stations', u'Do-It-Yourself Food', u'Food Trucks', u'Chocolatiers & Shops', u'Burgers', u'Nightlife', u'Bars', u'Wine Bars', u'Italian', u'Soup', u'Home Decor', u'Home & Garden', u'Furniture Stores', u'Vegetarian', u'Florists', u'Flowers & Gifts', u'Farmers Market', u'Candy Stores', u'Bagels', u'Delis', u'Seafood Markets', u'Cupcakes', u'Department Stores', u'Fashion', u'Electronics', u'Beauty & Spas', u'Cosmetics & Beauty Supply', u'American (Traditional)', u'Korean', u'Drugstores', u'Fruits & Veggies', u'Ethnic Food', u'Vegan', u'Kitchen & Bath', u'Internet Cafes', u'Pubs', u'Gift Shops', u'Newspapers & Magazines', u'Books, Mags, Music & Video', u'Pakistani', u'Bubble Tea', u'Fish & Chips', u'Fast Food', u'Pizza', u'Arts & Entertainment', u'Wineries', u'Venues & Event Spaces', u'Tea Rooms', u'Coffeeshops', u'Mexican', u'Patisserie/Cake Shop', u'Vitamins & Supplements', u'Tobacco Shops', u'American (New)', u'Breweries', u'Chinese', u'Portuguese', u'Tapas/Small Plates', u'Music Venues', u'Food Stands', u'Middle Eastern', u'Delicatessen', u'Greek', u'Gluten-Free', u'French', u'African', u'Herbs & Spices', u'Pretzels', u'Sushi Bars', u'Festivals', u'Local Flavor', u'Salad', u'Toy Stores', u'Popcorn Shops', u'Diners', u'Sporting Goods', u'Bikes', u'Hotels & Travel', u'Travel Services', u'Food Delivery Services', u'Barbeque', u'Gelato', u'Car Wash', u'Local Services', u'Pest Control', u'Bookstores', u'Scandinavian', u'Indian', u'Cocktail Bars', u'Thai', u'Asian Fusion', u'Steakhouses', u'Japanese', u'Ramen', u'Caterers', u'Churches', u'Religious Organizations', u'British', u'Taiwanese', u'Live/Raw Food', u'Home Services', u'Building Supplies', u'Hawaiian', u'CSA', u'Organic Stores', u'Caribbean', u'Ethnic Grocery', u'Irish', u'Macarons', u'Windshield Installation & Repair', u'Gastropubs', u'Tours', u'Cajun/Creole', u'Wine Tasting Room', u'Brazilian', u'Seafood', u'Modern European', u'Specialty Schools', u'Education', u'Cooking Schools', u'Laotian', u'Bridal', u'Mobile Phones', u'Nutritionists', u'Traditional Chinese Medicine', u'Health & Medical', u'Canadian (New)', u'Discount Store', u'Mongolian', u'Livestock Feed & Supply', u'Mediterranean', u'German', u'Creperies', u'Lounges', u'Hookah Bars', u'Weight Loss Centers', u'Doctors', u'Landmarks & Historical Buildings', u'Public Services & Government', u'Soul Food', u'Turkish', u'Thrift Stores', u'Gyms', u'Trainers', u'Fitness & Instruction', u'Active Life', u'Photography Stores & Services', u'Comic Books', u'Wine Tours', u'Bistros', u'Beverage Store', u'Appliances', u'Hot Dogs', u'Beer Gardens', u'Distilleries', u'Cafeteria', u'Sports Bars', u'Parking', u'Tex-Mex', u'Casinos', u'Filipino', u'Beer Garden', u'Libraries', u'Buffets', u'Arts & Crafts', u'Australian', u'Performing Arts', u'Cuban', u'Jazz & Blues', u'Kosher', u'Hotels', u'Comfort Food', u'Southern', u'Cooking Classes', u'Halal', u'Dive Bars', u'Art Galleries', u'Vietnamese', u'Pasta Shops', u'Brasseries', u'Cheesesteaks', u'Jewelry', u'Russian', u'Afghan', u'Party & Event Planning', u'Colleges & Universities', u'Pool Halls', u'Food Court', u'Horseback Riding', u'Ethiopian', u"Women's Clothing", u'Medical Spas', u'Party Equipment Rentals', u'Bed & Breakfast', u'Scottish', u'Ukrainian', u'Polish', u'Nurseries & Gardening', u'Chicken Wings', u'Brewing Supplies', u'Backshop', u'Falafel', u'Oil Change Stations', u'Bike Repair/Maintenance', u"Men's Clothing", u'Tanning', u'Auto Parts & Supplies', u'Swimming Pools', u'Dry Cleaning & Laundry', u'Souvenir Shops', u'Post Offices', u'Massage', u'Yoga', u'Tapas Bars', u'Beer Bar', u'Acupuncture', u'Sports Medicine', u'Lebanese', u'Tasting Classes', u'Paintball', u'Amusement Parks', u'Couriers & Delivery Services'];
NUM_UNIQUE_CATEGORIES = 251
CATEGORIES_ATTRIBUTE = 'categories'

def vectorize_categories(business):

	#Initially create a 251 dimensional array. (Or however many unique categories there are.)
	result = [0] * NUM_UNIQUE_CATEGORIES

	#Place 1's in the positions that correspond to where the business's categories are.
	for elt in business[CATEGORIES_ATTRIBUTE]:

		#Ignore all categories not in training set.
		if elt in ALL_CATEGORIES:
			result[ALL_CATEGORIES.index( elt )] = 1


	return result;

def main():

	#Run a quick example
	b1 = json.loads('{"business_id": "5UmKMjUEUNdYWqANhGckJw", "full_address": "4734 Lebanon Church Rd Dravosburg, PA 15034", "hours": {"Friday": {"close": "21:00", "open": "11:00"}, "Tuesday": {"close": "21:00", "open": "11:00"}, "Thursday": {"close": "21:00", "open": "11:00"}, "Wednesday": {"close": "21:00", "open": "11:00"}, "Monday": {"close": "21:00", "open": "11:00"}}, "open": true, "categories": ["Fast Food", "Restaurants"], "city": "Dravosburg", "review_count": 4, "name": "Mr Hoagie", "neighborhoods": [], "longitude": -79.9007057, "state": "PA", "stars": 4.5, "latitude": 40.3543266, "attributes": {"Take-out": true, "Drive-Thru": false, "Good For": {"dessert": false, "latenight": false, "lunch": false, "dinner": false, "brunch": false, "breakfast": false}, "Caters": false, "Noise Level": "average", "Takes Reservations": false, "Delivery": false, "Ambience": {"romantic": false, "intimate": false, "classy": false, "hipster": false, "divey": false, "touristy": false, "trendy": false, "upscale": false, "casual": false}, "Parking": {"garage": false, "street": false, "validated": false, "lot": false, "valet": false}, "Has TV": false, "Outdoor Seating": false, "Attire": "casual", "Alcohol": "none", "Waiter Service": false, "Accepts Credit Cards": true, "Good for Kids": true, "Good For Groups": true, "Price Range": 1}, "type": "business"}')

	print vectorize_categories( b1 )

if __name__ == '__main__':
	main()