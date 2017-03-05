import random,time
from classes import Trainer, Pokemon ,Hospital

pokemon1=Pokemon("이상해씨",25,10,1,"이상해풀")
pokemon2=Pokemon("이상해풀",80,20,1,"이상해꽃")
pokemon3=Pokemon("이상해꽃",120,30,1,"최종 진화")
pokemon4=Pokemon("파이리",25,10,1,"리자드")
pokemon5=Pokemon("꼬부기",25,10,1,"어니부기")


# pokemon_enemy=[이상해씨,이상해풀,이상해꽃




# 			]


print("Welcome To Pokemon World")

playername = input("플레이어 이름을 입력해 주세요 : ")
which_pokemon = input("시작할 포켓몬을 골라주세요[파이리/꼬부기/이상해씨/피카츄]")

if which_pokemon=="피카츄":
	pokemon = Pokemon("피카츄",25,10,1,"라이츄")
elif which_pokemon=="파이리":
	pokemon = Pokemon("파이리",25,10,1,"리자드")
elif which_pokemon=="꼬부기":
	pokemon = Pokemon("꼬부기",25,10,1,"어니부기")
elif which_pokemon=="이상해씨":
	pokemon = Pokemon("이상해씨",25,10,1,"이상해풀")
else:
	print("잘못 입력해주셨네요, 내맘대로 피카츄로 시작합니다.")
	pokemon = Pokemon("피카츄",25,10,1,"라이츄")

trainer =Trainer(playername,pokemon)

print(trainer.pokemon_list[0].name)

trainer.pokemon_list.append(pokemon1)
trainer.pokemon_list.append(pokemon2)
trainer.pokemon_list.append(pokemon3)

trainer.change_pokemon()


# situation=input("야생에 진입 하시겠습니까? Y/N")
# if situation==Y:
# 	while True:
# 		if pokemon.curr_hp>0:
# 			pokemon =random.choice(pokemon_enemy)
# 			print("앗! 야생{}이(가) 나타났다!".format(pokemon.pokemon))

		

