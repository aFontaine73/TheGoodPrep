from django.http import HttpResponse
from django.shortcuts import render

''' 
def home (request):
	dish_name = "Curry Goat"
	dish_price = "£12"
	context = {"dish_name" : dish_name,
				"dish_price" : dish_price
				}
				
	return render(request, "home.html") 
'''

def home(request):
	context = {'dishes' : dishes}
	



    return render(request, 'home.html', context)

class Dishes:
    def __init__(self, name, calories, fat, saturateFats, carbohydrate, sugarCarbs, protein, salt, vegetarian, vegan, allergens, description, price, img_url):
        self.name = name
        self.calories = calories
		self.fat = fat
		self.saturateFats = saturateFats
		self.carbohydrate = carbohydrate
		self.sugarCarbs = sugarCarbs
		self.protein = protein
		self.salt = salt
		self.vegetarian = vegetarian
		self.vegan = vegan
		self.allergens = allergens
		self.description = description
        self.price = price
        self.img_url = img_url

		

dishes = [
	Dish("Cajun Salmon", 260.00, 16.00, 3.00, 0.00, 0.00, 29.00, 0.31, False, False, "Fish", "Garlic, onion powder, chilli flaes, smoked paprika", 6.99, 
			"https://www.schwartz.co.uk/recipes/fish-and-shellfish/salmon-fillets-with-cajun-marinade"),
	Dish("Peppered Sirloin Steak", 265.00, 8.00, 3.00, 0.00, 0.00, 45.00, 0.40, False, False, "beef", Black pepper, parsley, rosemary, thyme, garlic, salt rapseed oil, dijon mustard", 8.99,
			"https://www.schwartz.co.uk/-/media/schwartz/recipes/2000x1125/sirloin_steak_with_creamy_pepper_sauce_2000.ashx?vd=20160802T000236Z&hash=4891E02A80673C210F8AEE525ABB72D85903233E"),
	Dish("Crushed New Potato", 115.00, 2.00, 0.00, 25.00, 2.00, 4.00, 0.20, True, True, "null", "Sage, parsley, thyme, chives, salt",
			"http://www.blushingcook.com/wp-content/uploads/2015/05/131023-078.jpg")
		]