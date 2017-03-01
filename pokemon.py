from classes import Trainer, Pokemon ,Hospital

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
