import sys
dic={
	"Coffee":{
		"ingredients":{
			"milk":0,
			"coffee":20,
			"water":100,
			},
		
	"cost":150
	},
	
	"Latte":{
		"ingredients":{
			"milk":170,
			"coffee":50,
			"water":120,
			},
	"cost":200
	},
	"Cappicino":{
		"ingredients":{
			"milk":200,
			"coffee":60,
			"water":130,
			},
	"cost":250
	},
}

total =0
resources = {
	"milk":1000,
	"coffee":500,
	"water":1000,
	"profit":0
}
y=0
def ma():
	x = input("What would youlike to have :(Coffee,Latte,Cappicino):")
	if x == 'off' :
	 	print("terminate")
	 	sys.exit()
	 
	elif x == 'report':
	 	print(resources)
	 	return False
	 
	def res(drink):
		if  resources["coffee"]>= dic[drink]["ingredients"]["coffee"] and resources["milk"]>= dic[drink]["ingredients"]["milk"] and resources["water"]>= dic[drink]["ingredients"]["water"]:
			resources["coffee"] = resources["coffee"] - dic[drink]["ingredients"]["coffee"]
			resources["milk"] = resources["milk"] - dic[drink]["ingredients"]["milk"]
			resources["water"] = resources["water"] - dic[drink]["ingredients"]["water"]
			return True
		
	def money(drink):
		if res(drink):
			y=int(input("Enter no of Rs5 coins:"))
			z = int(input("Enter no of Rs10 coins:"))
			w= int(input("Enter no of Rs20 coins:"))
			global total
			total = y*5 +z*10 + w*20
			if total>= dic[drink]["cost"] :
				change = total - dic[drink]["cost"]
				print(f"Here is your drink {drink} and your change is {change}")
			elif total <dic[drink]["cost"]: 
				print("You have entered insufficient amount")
		else:
			print("Insufficient resources")
				
	global y 
	y+= dic[x]["cost"]
	resources.update({"profit":y})
	money(x)
is_on = 1
while is_on != 0 :
	ma()
		
				
			
			
			 		
		
		
	

	
		
