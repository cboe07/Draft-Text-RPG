import os


class Player(object):
	def __init__(self, name, salary, strength, team):
		self.name = name
		self.salary = salary
		self.strength = strength
		self.team = team

	def print_player(self):
		print "Player: " + self.name
		print "TEAM: "  + self.team
		print "SALARY: " + str(self.salary)
		print "STRENGTH LEVEL: " + str(self.strength)


class Team(object):
	def __init__(self, team_name):
		self.team_name = team_name
		self.team_salary = 0
		self.max_salary = 10000
		self.team_strength = 0
		self.players = []

	def total_team_strength(self):
		self.team_strength = ((self.players[0].strength) + (self.players[1].strength) + (self.players[2].strength))
		print (self.players[0].strength) 
		print (self.players[1].strength)
		print (self.players[2].strength)
		print "TEAM STRENGTH: " + str(self.team_strength)



	def available_salary(self):
		self.team_salary = self.max_salary - ((self.players[0].salary) + (self.players[1].salary) + (self.players[2].salary))
		print "AVAILABLE SALARY: " + str(self.team_salary)


	def print_roster(self):
		for players in self.players:
			print players.name

	def add_player(self, player_obj):
		self.players.append(player_obj)


# Establish Variables
players = []


julio_jones = Player("Julio Jones", 5000, 9, "Falcons")
matt_ryan = Player("Matt Ryan", 1000, 7, "Falcons")
devonta_freeman = Player("Devonta Freeman", 1000, 5, "Falcons")

drew_brees = Player("Drew Brees", 5000, 9, "Saints")
mark_ingram = Player("Mark Ingram", 2000, 3, "Saints")
michael_thomas = Player("Michael Thomas", 1000, 4, "Saints")

cam_newton = Player("Cam Newton", 5000, 10, "Panthers")
greg_olsen = Player("Greg Olsen", 900, 6, "Panthers")
kelvin_benjamin = Player("Kelvin Benjamon", 1000, 3, "Panthers")

falcons = Team("Falcons")
saints = Team("Saints")
panthers = Team("Panthers")

teams = {
		"falcons":falcons, 
		"saints": saints,
		"panthers":panthers
	}

teams['falcons'].add_player(julio_jones)
teams['falcons'].add_player(matt_ryan)
teams['falcons'].add_player(devonta_freeman)

teams['panthers'].add_player(cam_newton)
teams['panthers'].add_player(greg_olsen)
teams['panthers'].add_player(kelvin_benjamin)

teams['saints'].add_player(drew_brees)
teams['saints'].add_player(mark_ingram)
teams['saints'].add_player(michael_thomas)












# ===========================
# ========MAIN LOOP==========
# ============================
while True:
	print "Welcome to the NFC SOUTH TECH BOWL!"
	print "What would you like to do? "
	print "1. CHOOSE TEAM"
	print "2. VIEW ROSTERS"
	user_input = raw_input("> ")
	os.system('clear')
	if (user_input == "1"):
		print "Select your TEAM"
		counter = 0
		for team in teams:
			counter += 1
			print "%d. %s" % (counter, teams[team].team_name)
		user_choose_team = int(raw_input("> "))
		print "\n"
		os.system('clear')
		if (user_choose_team -1 == 0):
			"%s" % (teams['falcons'].players[0].print_player())
			print "\n"
			"%s" % (teams['falcons'].players[1].print_player())
			print "\n"
			"%s" % (teams['falcons'].players[2].print_player())
			print "\n"
			"%s" % (teams['falcons'].available_salary())
			"%s" % (teams['falcons'].total_team_strength())
			
		elif (user_choose_team -1 == 1):
			"%s" % (teams['panthers'].players[0].print_player())
			print "\n"
			"%s" % (teams['panthers'].players[1].print_player())
			print "\n"
			"%s" % (teams['panthers'].players[2].print_player())
			print "\n"	
			"%s" % (teams['panthers'].available_salary())
			"%s" % (teams['panthers'].total_team_strength())
			
		elif (user_choose_team -1 == 2):
			"%s" % (teams['saints'].players[0].print_player())
			print "\n"
			"%s" % (teams['saints'].players[1].print_player())
			print "\n"
			"%s" % (teams['saints'].players[2].print_player())
			print "\n"
			"%s" % (teams['saints'].available_salary())
			"%s" % (teams['saints'].total_team_strength())
			
	if (user_input == "2"):
		counter = 0
		for team in teams:
			counter += 1
			print "%d. %s" % (counter, teams[team].team_name)
			print "%s" % teams[team].players[0].name
			print "%s" % teams[team].players[1].name
			print "%s\n" % teams[team].players[2].name
		

	# if (user_input == "2"):
# players.append(julio_jones)

# print julio_jones.players()










