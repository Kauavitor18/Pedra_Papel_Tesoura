import random

user_points = 0
computer_points = 0

options = ["r", "t", "p"]


while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choice == 'q':
        break
    
    if user_choice not in options:
        continue

    computer_choice = random.randint(0,2)
    # 0 : R, 1 : T, 2 : P
    computer_options = options[computer_choice]

    print("O computador escolheu " + str(computer_choice))

    if user_choice == computer_options:
        print("Empate!")
    elif user_choice == "r" and computer_options == "t":
        print("Você ganhou!")
        user_points = user_points + 1
    elif user_choice == "p" and computer_options == "r":
        print("Você ganhou!")
        user_points = user_points + 1
    elif user_choice == "t" and computer_options == "p":
        print("Você ganhou!")
        user_points = user_points + 1
    else:
        print("Você perdeu!")
        computer_points = computer_points + 1

print("Sua pontuação: " + str(user_points))
print("Pontuação do Computador: " + str(computer_points))

if user_points > computer_points:
    print("Vitória!!!")
elif user_points == computer_points:
    print("Empate")
else:
    print("Derrota!!")


print("Goodbye!")

    