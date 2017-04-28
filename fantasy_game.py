

class Player(object):
	def __init__(self, name, salary, skill, team):
		self.name = name
		self.salary = salary
		self.skill = skill
		self.team = team

	def print_player(self):
		print "Player: " + self.name
		print "Team: "  + self.team
		print "Salary: " + str(self.salary)
		print "Skill Level: " + str(self.skill)


class Team(object):
	def __init__(self, team_name, team_salary, team_strength):
		self.team_name = team_name
		self.team_salary = team_salary
		self.max_salary = 10000
		self.team_strength = team_strength
		self.players = []

	def available_salary(self):
		available_salary = max_salary - current_salary

	def print_roster(self):
		for players in Team:
			print players


# Establish Variables
players = []

julio_jones = Player("Julio Jones", 1000, 7, "Falcons")
matt_ryan = Player("Matt Ryan", 1000, 7, "Falcons")
devonta_freeman = Player("Devonta Freeman", 1000, 7, "Falcons")

drew_brees = Player("Drew Brees", 1000, 7, "Saints")
mark_ingram = Player("Mark Ingram", 1000, 7, "Saints")
michael_thomas = Player("Michael Thomas", 1000, 7, "Saints")

cam_newton = Player("Cam Newton", 1000, 7, "Panthers")
greg_olsen = Player("Greg Olsen", 1000, 7, "Panthers")
kelvin_benjamin = Player("Kelvin Benjamon", 1000, 7, "Panthers")

falcons = Team("Falcons", 5000, 25)
saints = Team("Saints", 5000, 25)
panthers = Team("Panthers", 5000, 25)











# ===========================
# ========MAIN LOOP==========
# ============================
# while True:
# 	print "Welcome to the DigitalCrafts Fanatasy Draft!"
# 	print "What would you like to do? "
# 	print "1. CHOOSE TEAM"
# 	print "2. VIEW ROSTERS"
# 	user_input = raw_input("> ")
# 	if (user_input == "1"):
# 		print "Select your TEAM"
# 		print "1. FALCONS"
# 		print "2. SAINTS"
# 		print "3. PANTHERS"
# 		user_input_2 = raw_input("> ")
# 		if (user_input_2 == "1"):
# 			pass

	# if (user_input == "2"):
players.append(julio_jones)

print julio_jones.players()


