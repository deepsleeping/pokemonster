class Trainer:
	name =""
	badge_list=[]
	pokemon_list=[]
	# pokemon_dict=[]
	money = 500

	def __init__(self,name,pokemon):
		self.name = name
		self.pokemon_list.append(pokemon)

	def change_pokemon(self):
		for pokemon in self.pokemon_list:
			if(pokemon.curr_hp>0):
				print(pokemon.name,"\t")
		notchanged = True

		while notchanged:
			name = input("바꾸고 싶은 포켓몬을 입력해주세요 : ")
			for pokemon in self.pokemon_list:
				if pokemon.name ==name:
					self.pokemon_list.remove(pokemon)
					self.pokemon_list.insert(0,pokemon)
					notchanged = False



class Pokemon:
	name =""
	exp = 0
	level = 0
	curr_hp = 0
	max_hp = 0
	damage = 0
	#skill_list=[]
	upgrade = ""

	def __init__(self,name,max_hp,damage,level,upgrade):
		self.name =name
		self.curr_hp =max_hp
		self.max_hp = max_hp
		self.level =level
		self.upgrade = upgrade

	def attack(self,enemy,trainer):
		enemy.curr_hp-=self.damage
		if(enemy.curr_hp<=0):
			capture = input("이 포켓몬을 정말로 잡으실겁니까? 진짜로? 정말로? [Y/N]")
			if capture =='Y':
				trainer.pokemon_list.append(enemy)
				#trainer.pokemon_dict.append(enemy.name)
				print("{}를 잡았습니다!!!".format(enemy.name))
			self.exp +=enemy.exp
			self.level_up()

	def attack2(self,trainer):
		if trainer.pokemon_list[0].curr_hp<=0:
			print("포켓몬친구가 생을 마감하였습니다.")
			trainer.change_pokemon()


	def level_up(self):
		if self.exp>=self.level*100:
			self.exp-=self.level*100
			self.level +=1
			self.level_up()
			print("당신의 포켓몬{}가 레벨업을 하였습니다!".format(self.name))

		


class NPC:
	name =""
	conversation_list = []

class Hospital:
	global pokemon_list
	pokemon_list=[]

	def heal(self,trainer):
		for pokemon in trainer.pokemon_list:
			pokemon.curr_hp = pokemon.max_hp

	def save_pokemon(self,trainer):
		if trainer.pokemon_list.length>1:
			for pokemon in trainer.pokomon_list:
				print(pokemon.name)
			which_pokemon = input("어느 포켓몬을 넣으시겠습니까? : ")

			for pokemon in trainer.pokemon_list:
				if pokemon.name ==wich_pokemon:
					self.pokemon_list.append(pokemon)
					trainer.pokemon_list.remove(pokemon)
					break

		else:
			print("포켓몬이 2개 이상일때만 맡길 수 있습니다.")



