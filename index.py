import random
import os

sobreviventes = []

recursos = {
    "madeira": 0,
    "pedra": 0,
    "comida": 0,
    "agua": 0,
    "ferro": 0,
    "tecido": 0,
    "corda": 0,
    "remedio": 0,
    "pecas_radio": 0
}

inventario = []


dia = 1

def limpar_tela():
    os.system("cls")

def cadastrar_sobrevivente():
    nome = input("Digite o nome do sobrevivente: ")

    sobrevivente = {
        "nome": nome,
        "vida": 100,
        "fome": 0,
        "sede": 0
    }
    
    sobreviventes.append(sobrevivente)
    print(f"{nome} foi cadastrado com sucesso!")

def coletar_recursos():
    print("=== COLETA DE RECURSOS ===")
    print("1 - Madeira")
    print("2 - Pedra")
    print("3 - Comida")
    print("4 - Água")
    print("5 - Ferro")
    print("6 - Tecido")
    print("7 - Corda")
    print("8 - Remédio")
    print("9 - Radio")

    opcao = input("Escolha o recurso: ")

    if opcao == "1":
        qtd = random.randint(2, 6)
        recursos["madeira"] += qtd
        print(f"Você coletou {qtd} de madeira.")

    elif opcao == "2":
        qtd = random.randint(1, 5)
        recursos["pedra"] += qtd
        print(f"Você coletou {qtd} de pedra.")

    elif opcao == "3":
        qtd = random.randint(1, 4)
        recursos["comida"] += qtd
        print(f"Você coletou {qtd} de comida.")

    elif opcao == "4":
        qtd = random.randint(1, 4)
        recursos["agua"] += qtd
        print(f"Você coletou {qtd} de água.")

    elif opcao == "5":
        qtd = random.randint(1, 3)
        recursos["ferro"] += qtd
        print(f"Você coletou {qtd} de ferro.")

    elif opcao == "6":
        qtd = random.randint(1, 3)
        recursos["tecido"] += qtd
        print(f"Você coletou {qtd} de tecido.")

    elif opcao == "7":
        qtd = random.randint(1, 2)
        recursos["corda"] += qtd
        print(f"Você coletou {qtd} de corda.")
        
    elif opcao == "8":
        qtd = random.randint(1, 2)
        recursos["remedio"] += qtd
        print(f"Você coletou {qtd} de remédio.")
        
    elif opcao == "9":
            qtd = random.randint(1, 2)
            recursos["pecas_radio"] += qtd
            print(f"Você coletou {qtd} peças do rádio.")
    else:
        print("Opção inválida.")

def construir_item():
    print("=== CONSTRUÇÃO DE ITENS ===")
    print("1 - Machadinha (2 madeira, 1 pedra)")
    print("2 - Lança (3 madeira, 1 corda)")
    print("3 - Fogueira (4 madeira, 2 pedra)")
    print("4 - Mochila (2 tecido, 2 corda)")
    print("5 - Armadilha (2 madeira, 2 corda, 1 pedra)")
    print("6 - Abrigo (6 madeira, 4 pedra, 2 corda)")
    print("7 - Kit Médico (1 tecido, 1 remédio, 1 corda)")
    print("8 - Rádio (8 peças do rádio)")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if recursos["madeira"] >= 2 and recursos["pedra"] >= 1:
            recursos["madeira"] -= 2
            recursos["pedra"] -= 1
            inventario.append("Machadinha")
        else:
            print("Recursos insuficientes.")
    elif opcao == "2":
            if recursos["madeira"] >= 3 and recursos["corda"] >= 1:
                recursos["madeira"] -= 3
                recursos["corda"] -= 1
                inventario.append("Lança")
            else:
                print("Recursos insuficientes.")
    elif opcao == "3":
                if recursos["madeira"] >= 4 and recursos["pedra"] >= 2:
                    recursos["madeira"] -= 4
                    recursos["pedra"] -= 2
                    inventario.append("Fogueira")
                else:
                    print("Recursos insuficientes.")
    elif opcao == "4":
                    if recursos["tecido"] >= 2 and recursos["corda"] >= 2:
                        recursos["tecido"] -= 2
                        recursos["corda"] -= 2
                        inventario.append("Mochila")
                    else:
                        print("Recursos insuficientes.")
    elif opcao == "5":
                        if recursos["madeira"] >= 2 and recursos["corda"] >= 2 and recursos["pedra"] >= 1:
                            recursos["madeira"] -= 2
                            recursos["corda"] -= 2
                            recursos["pedra"] -= 1
                            inventario.append("Armadilha")
                        else:
                            print("Recursos insuficientes.")
    elif opcao == "6":
                                if recursos["madeira"] >= 6 and recursos["corda"] >= 2 and recursos["pedra"] >= 4:
                                    recursos["madeira"] -= 6
                                    recursos["corda"] -= 2
                                    recursos["pedra"] -= 4
                                    inventario.append("Abrigo")
                                else:
                                    print("Recursos insuficientes.")
    elif opcao == "7":
                                    if recursos["tecido"] >= 1 and recursos["remedio"] >= 1 and recursos["corda"] >= 1:
                                        recursos["tecido"] -= 1
                                        recursos["remedio"] -= 1
                                        recursos["corda"] -= 1
                                        inventario.append("Kit Médico")
                                    else:
                                        print("Recursos insuficientes.")
    elif opcao == "8":
                if recursos["pecas_radio"] >= 8:
                    recursos["pecas_radio"] -= 8
                    inventario.append("Radio")
                    print("Você construiu o Rádio! Agora precisa sobreviver até o resgate.")
                else:
                    print("Peças do rádio insuficientes.")
    
def mostrar_inventario():
    print("=== INVENTÁRIO ===")
    
    
    print("Madeira:", recursos["madeira"])
    print("Pedra:", recursos["pedra"])
    print("Comida:", recursos["comida"])
    print("Água:", recursos["agua"])
    print("Ferro:", recursos["ferro"])
    print("Tecido:", recursos["tecido"])
    print("Corda:", recursos["corda"])
    print("Remédio:", recursos["remedio"])


    if inventario:
        for item in inventario:
            print(f"- {item}")
    else:
        print("- Nenhum item construído.")
        
def mostrar_sobreviventes():
    print("=== SOBREVIVENTES ===")
    print("")
    if sobreviventes:
        for sobrevivente in sobreviventes:
            print(f"Nome: {sobrevivente['nome']}")
            print(f"Vida: {sobrevivente['vida']}")
            print(f"Fome: {sobrevivente['fome']}")
            print(f"Sede: {sobrevivente['sede']}")
            print("-" * 20)
    else:
        print("- Nenhum sobrevivente cadastrado.")
    
def passar_tempo():
    global dia

    dia += 1

    for sobrevivente in sobreviventes[:]:
        sobrevivente["fome"] += 5
        sobrevivente["sede"] += 5


        if sobrevivente["fome"] >= 80 or sobrevivente["sede"] >= 80:
            sobrevivente["vida"] -= 10
            print(f"{sobrevivente['nome']} está muito fraco e perdeu 10 de vida.")

        if sobrevivente["vida"] <= 0 or sobrevivente["fome"] >= 100 or sobrevivente["sede"] >= 100:
            print(f"{sobrevivente['nome']} morreu.")
            sobreviventes.remove(sobrevivente)

def mostrar_objetivo():
    print("OBJETIVO:")

    if "Abrigo" not in inventario or "Fogueira" not in inventario:
        print("Monte um acampamento: construa Abrigo e Fogueira.")
    elif "Lança" not in inventario:
        print("Prepare a defesa do acampamento: construa uma Lança.")
    elif "Radio" not in inventario:
        print("Encontre 8 peças e construa o Rádio.")
    elif recursos["comida"] < 5 or recursos["agua"] < 5:
        print("Prepare a evacuação: guarde 5 comidas e 5 águas.")
    else:
        print("Tudo pronto! Use a opção 9 para pedir resgate.")

def pedir_resgate():
    print("=== PEDIR RESGATE ===")

    if "Abrigo" not in inventario:
        print("O acampamento não é seguro. Construa um Abrigo primeiro.")
    elif "Fogueira" not in inventario:
        print("A equipe não conseguirá enxergar seu acampamento. Construa uma Fogueira.")
    elif "Lança" not in inventario:
        print("A viagem até o ponto de resgate é perigosa. Construa uma Lança.")
    elif "Radio" not in inventario:
        print("Você ainda não tem um Rádio para pedir socorro.")
    elif recursos["comida"] < 5 or recursos["agua"] < 5:
        print("Faltam suprimentos para a viagem: são necessárias 5 comidas e 5 águas.")
    else:
        recursos["comida"] -= 5
        recursos["agua"] -= 5
        print("O rádio transmitiu sua localização!")
        print("A fogueira guiou a equipe de resgate até o acampamento.")
        print("Parabéns, você e seu grupo sobreviveram!")
        return True

    return False

def consumir_recurso():
    if not sobreviventes:
        print("Não há sobreviventes para alimentar ou hidratar.")
        return

    print("=== CONSUMIR RECURSO ===")
    print("1 - Dar comida para todos")
    print("2 - Dar água para todos")
    escolha = input("Escolha o que consumir: ")

    if escolha == "1":
        for sobrevivente in sobreviventes:
            if recursos["comida"] > 0:
                recursos["comida"] -= 1
                sobrevivente["fome"] -= 30

                if sobrevivente["fome"] < 0:
                    sobrevivente["fome"] = 0

                print(f"{sobrevivente['nome']} comeu.")
            else:
                print("A comida acabou.")
                break

    elif escolha == "2":
        for sobrevivente in sobreviventes:
            if recursos["agua"] > 0:
                recursos["agua"] -= 1
                sobrevivente["sede"] -= 30

                if sobrevivente["sede"] < 0:
                    sobrevivente["sede"] = 0

                print(f"{sobrevivente['nome']} bebeu água.")
            else:
                print("A água acabou.")
                break

    else:
        print("Opção inválida.")
  
def evento_aleatorio():
    evento = random.randint(1, 9)       
    if evento == 1:
            print("Você encontrou uma caixa de suprimentos!")
            recursos["comida"] += 2
            recursos["agua"] += 2
            print("Ganhou 2 comidas e 2 águas.")

    elif evento == 2:
            print("Você encontrou uma fonte de água limpa!")
            recursos["agua"] += 4
            print("Ganhou 4 águas.")

    elif evento == 3:
            if sobreviventes:
                alvo = random.choice(sobreviventes)

                print(f"Um lobo atacou {alvo['nome']}!")

                if "Lança" in inventario:
                    print("A lança protegeu o sobrevivente!")
                else:
                    alvo["vida"] -= 20
                    print(f"{alvo['nome']} perdeu 20 de vida.")
            else:
                print("Não há sobreviventes para atacar.")   
                
    elif evento == 4:
        print("Uma tempestade atingiu o acampamento!")

        if "Abrigo" in inventario:
            print("O abrigo protegeu seus recursos.")
        else:
            perda = random.randint(1, 4)
            perda = min(perda, recursos["madeira"])

            recursos["madeira"] -= perda
            print(f"Você perdeu {perda} madeiras.")  
    
    elif evento == 5:
        print("Você encontrou uma árvore frutífera!")
        recursos["comida"] += 3
        print("Ganhou 3 comidas.")

    elif evento == 6:
        print("Um sobrevivente encontrou um kit abandonado!")
        recursos["remedio"] += 1
        recursos["tecido"] += 1
        print("Ganhou 1 remédio e 1 tecido.")

    elif evento == 7:
        print("Você encontrou uma mina de ferro abandonada!")
        recursos["ferro"] += 2
        print("Ganhou 2 ferros.")

    elif evento == 8:
        if "Armadilha" in inventario:
            print("Sua armadilha capturou um animal!")
            recursos["comida"] += 4
            print("Ganhou 4 comidas.")
        else:
            print("Você encontrou rastros de animais, mas não tinha uma armadilha.")

    elif evento == 9:
        if sobreviventes:
            alvo = random.choice(sobreviventes)
            print(f"{alvo['nome']} ficou doente!")

            if "Kit Médico" in inventario:
                print("O Kit Médico curou o sobrevivente.")
            elif recursos["remedio"] >= 1:
                recursos["remedio"] -= 1
                print("Você usou 1 remédio para tratar o sobrevivente.")
            else:
                alvo["vida"] -= 15
                print(f"{alvo['nome']} perdeu 15 de vida.")
        else:
            print("Não há sobreviventes para ficarem doentes.")
     
def evento_radio():
    if "Radio" not in inventario:
        print("Você ainda não possui um rádio.")
        return

    sinal = random.randint(1, 12)

    print("\n--- SINAL DE RÁDIO ---")


    if sinal == 1:
        print("“Encontramos comida perto do rio... coordenadas enviadas...”")
        qtd = random.randint(2, 5)
        recursos["comida"] += qtd
        print(f"Você encontrou {qtd} comidas.")

    elif sinal == 2:
        print("“Há água limpa na floresta ao norte.”")
        qtd = random.randint(2, 5)
        recursos["agua"] += qtd
        print(f"Você encontrou {qtd} águas.")


    elif sinal == 3:
        print("“Socorro! Estou preso em um prédio abandonado!”")
        escolha = input("1 - Resgatar | 2 - Ignorar: ")

        if escolha == "1":
            if random.randint(1, 2) == 1:
                novo = {
                    "nome": "Sobrevivente resgatado",
                    "vida": 80,
                    "fome": 20,
                    "sede": 20
                }
                sobreviventes.append(novo)
                print("Um novo sobrevivente entrou no acampamento!")
            else:
                print("Era uma armadilha. Você voltou sem encontrar ninguém.")
        else:
            print("Você decidiu não correr o risco.")


    elif sinal == 4:
        print("“Um grupo perigoso está se aproximando do acampamento!”")

        if "Lança" in inventario:
            print("A lança ajudou a defender o acampamento.")
        else:
            perda = random.randint(1, 3)
            perda = min(perda, recursos["comida"])
            recursos["comida"] -= perda
            print(f"O grupo roubou {perda} comidas.")

    elif sinal == 5:
        print("“Há uma farmácia abandonada perto da cidade.”")
        escolha = input("1 - Procurar | 2 - Ignorar: ")

        if escolha == "1":
            qtd = random.randint(1, 3)
            recursos["remedio"] += qtd
            print(f"Você encontrou {qtd} remédios.")
        else:
            print("Você permaneceu no acampamento.")

    elif sinal == 6:
        print("“Uma tempestade forte chegará em breve!”")

        if "Abrigo" in inventario:
            print("O abrigo protegeu todos durante a tempestade.")
        else:
            recurso = random.choice(["madeira", "pedra", "tecido", "corda"])
            perda = random.randint(1, 3)
            perda = min(perda, recursos[recurso])

            recursos[recurso] -= perda
            print(f"A tempestade destruiu {perda} de {recurso}.")


    elif sinal == 7:
        print("“Encontramos um depósito com materiais de construção.”")
        qtd_madeira = random.randint(1, 4)
        qtd_pedra = random.randint(1, 3)

        recursos["madeira"] += qtd_madeira
        recursos["pedra"] += qtd_pedra

        print(f"Você ganhou {qtd_madeira} madeiras e {qtd_pedra} pedras.")

    elif sinal == 8:
        print("“Cuidado: lobos foram vistos próximos ao acampamento!”")

        if sobreviventes:
            alvo = random.choice(sobreviventes)

            if "Lança" in inventario:
                print(f"A lança protegeu {alvo['nome']} dos lobos.")
            else:
                dano = random.randint(10, 25)
                alvo["vida"] -= dano
                print(f"Um lobo atacou {alvo['nome']}, que perdeu {dano} de vida.")
        else:
            print("Não há sobreviventes no acampamento.")

    elif sinal == 9:
        print("“Um avião deixou uma caixa de suprimentos na região!”")

        if random.randint(1, 2) == 1:
            recursos["comida"] += 2
            recursos["agua"] += 2
            recursos["remedio"] += 1
            print("Você encontrou 2 comidas, 2 águas e 1 remédio.")
        else:
            print("Você não conseguiu encontrar a caixa.")

    elif sinal == 10:
        print("“Uma mina abandonada pode ter ferro, mas é perigosa.”")
        escolha = input("1 - Explorar | 2 - Ignorar: ")

        if escolha == "1":
            if random.randint(1, 3) <= 2:
                qtd = random.randint(1, 3)
                recursos["ferro"] += qtd
                print(f"Você encontrou {qtd} ferros.")
            else:
                print("Parte da mina desabou. Ninguém se feriu, mas você fugiu.")
        else:
            print("Você decidiu não explorar a mina.")
    
    elif sinal == 11:
        print("“Um acampamento amigável oferece troca de materiais.”")
        escolha = input("1 - Trocar 2 madeiras por 2 comidas | 2 - Recusar: ")

        if escolha == "1":
            if recursos["madeira"] >= 2:
                recursos["madeira"] -= 2
                recursos["comida"] += 2
                print("Troca realizada: 2 madeiras por 2 comidas.")
            else:
                print("Você não tem madeira suficiente para a troca.")
        else:
            print("Você recusou a proposta.")

    elif sinal == 12:
        print("“A transmissão revela a localização de um gerador abandonado!”")
        qtd = random.randint(1, 2)
        recursos["ferro"] += qtd
        recursos["corda"] += 1
        print(f"Você encontrou {qtd} ferros e 1 corda.")



def menu():
    print("=== SOBREVIVA ATÉ O RESGATE ===")
    print("Missão: prepare o acampamento, chame o resgate e sobreviva.")
    print("Cada ação importante faz um dia passar. Cuide do seu grupo!")
    input("Pressione Enter para começar...")

    while True:
        limpar_tela()
        
        print("=== SIMULADOR DE SOBREVIVÊNCIA ===")
        print("Dia:", dia)
        print("Sobreviventes:", len(sobreviventes))
        mostrar_objetivo()
        print("")
        print("1 - Cadastrar sobrevivente")
        print("2 - Coletar recursos")
        print("3 - Construir item")
        print("4 - Mostrar inventário")
        print("5 - Mostrar sobreviventes")
        print("6 - Evento aleatório")
        print("7 - Ouvir rádio")
        print("8 - Consumir comida ou água")
        print("9 - Pedir resgate")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_sobrevivente()
        elif opcao == "2":
            coletar_recursos()
        elif opcao == "3":
            construir_item()
        elif opcao == "4":
            mostrar_inventario()
        elif opcao == "5":
            mostrar_sobreviventes()
        elif opcao == "6":
            evento_aleatorio()
        elif opcao == "7":
            evento_radio()
        elif opcao == "8":
            consumir_recurso()
        elif opcao == "9":
            if pedir_resgate():
                break
        elif opcao == "0":
            break
        else:
            print("Opção Inválida.")

        if opcao == "2" or opcao == "3" or opcao == "6" or opcao == "7" or opcao == "8":
            passar_tempo()

            if sobreviventes and random.randint(1, 3) == 1:
                print("Algo aconteceu durante o dia...")
                evento_aleatorio()

        if len(sobreviventes) == 0 and dia > 1:
            print("Todos os sobreviventes morreram. Fim de jogo.")
            break

         # se pensar em alguma funcao adiciomal me avise
        input("Pressione Enter para continuar...")
     
     
        
menu()

