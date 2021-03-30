print('''
Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
Centro de Informática (CIn) (http://www.cin.ufpe.br)
Graduando em Sistemas de Informação
IF968 - Programação 1

Autor: Vinícius Luiz da Silva França (vlsf2)
Email: vlsf2@cin.ufpe.br
Data: 2019-09-12

Copyright(c) 2019 Vinícius Luiz da Silva França
''')

print('CAPÍTULO 26 - A CAVERNA\n') 
print('''< Comandos >

andar p/ frente   : w
andar p/ esquerda : a
andar p/ direita  : d

-> Utilize todos os comandos com a letra MINÚSCULA
-> Digite apenas os comandos que o jogo descreve como possíveis
-> A cada passo, considere que o jogador se movimentou 2 metros
-> NÃO é possível andar para trás\n''')

skip=input('Aperte Enter para iniciar\n')

localizacao      = 40 #xy
hab_forca        = False #Para habilidade força
hab_velocidade   = False #Para habilidade velocidade
hab_inteligencia = False #Para habilidade inteligência
acao             = 0
acao42           = False #Condições que se alteram dependendo do que ocorrer
acao24           = False
acao32           = False
acao33v          = False
acao33           = False
acao36           = False
acao62           = False
acao72           = False
acao54           = False
acao64           = False
acao74           = False
acao55           = False
acao65           = False
acao85v          = False
acao85           = False
acao47           = False
acao76           = False
acao68           = False
acao48           = False
acao26           = False
acao18           = False

inferius         = [15, 'São defuntos enfeitiçados para cumprir ordens de um bruxo das trevas'] #Quantidade de HP que o monstro tira, descrição do monstro
voldemort        = [43, 'Tom Servolo Riddle, melhor conhecido como Lord Voldemort, é um bruxo mestiço considerado o mais poderoso bruxo das trevas de todos os tempos']
morcego          = 10 #Quantidade de HP que o morcego tira
ninhoInferius    = 300 #Quantidade de HP que o ninho tira
hp               = 100 #HP do personagem



while(localizacao): #Enquanto localização for True, irá rodar

    
    while(localizacao == 'null'):
        print("!!!SEU HP ESTÁ ZERADO!!!")
        for x in range(4):
            print('''<<< PARABÉNS, !!!VOCÊ MORREU!!! >>>''')
        localizacao = False     #Quando o HP zerar, localização = False
            
    
    while(localizacao == 40):
        felicis = input('''\n<<< Você agora se tornou Harry Potter! Num mundo alternativo, onde Dumbledore morre na caverna após duelar com Voldemort em busca de sua horcrux, você terá de escapar da caverna sem a ajuda do maior bruxo de todos os tempos que estava vivo a momentos atrás. Harry tem o auxílio da Felix Felicis, que lhe dará sorte por tempo um limitado que seja suficiente para escapar da caverna. Voldemort está fraco após o duelo, portanto, ele irá esperar um vacilo do jovem bruxo para ataca-lo. >>>\n<< Como resta apenas poucas gotas, você poderá escolher entre: ter sorte quando for utilizar a força, ter sorte quando utilizar a inteligência ou ter sorte quando utilizar a velocidade. >>\n\n**Você deseja ter sorte na força (digite f) velocidade (digite v) inteligencia (digite i)\n''')
        if felicis == 'f':
            hab_forca = True
            print('\nVocê terá sorte ao usar a força, isso pode ser útil (ou não)\n\n')
        elif felicis == 'v':
            hab_velocidade = True
            print('\nVocê terá sorte ao usar a velocidade, isso pode ser útil (ou não)\n\n')
        elif felicis == 'i':
            hab_inteligencia = True
            print('\nVocê terá sorte ao usar a inteligência, isso pode ser útil (ou não)\n\n')
        localizacao = 41

    while(localizacao == 41):
        acao = input('''\n<< Há muitos seres mágicos e não mágicos que podem lhe causar dano, tome cuidado ao avançar pela caverna >>\n<< OBS: Sua varinha caiu no escuro, portanto, não poderá usa-la >>\n**Há enormes paredes escuras em ambos lados, você pode: andar p/ frente (w)\n''')        
        if acao == 'w':
            localizacao = 42

    while(localizacao == 42): 
        if acao42 == False: #Se não aconteceu a acao42 no jogo, irá rodar este input
            acao = input(f'''\n<< Você chutou sem querer um medalhão que era uma falsa Horcrux, Harry está desnorteado, Dumbledore está morto! há um caminho pela esquerda e pela direita, qual seguir? >>\nVOCÊ TEM {hp} HP\n**Há uma parede enorme em sua frente, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif acao42 == True: #Se aconteceu a acao42 no jogo, irá rodar este input
            acao = input('''\n<< Você pisou no medalhão, Harry está muito confuso, não sabe por qual caminho seguir >>\n**Você pode: andar p/ esquerda (a), direita (d)\n''')
        if acao == 'a': #Se movimento for esquerda
            localizacao = 32 #Nova localização
            acao42 = True #Ação42 aconteceu
        elif acao == 'd': 
            localizacao = 52
            acao42 = True

    while(localizacao == 32):
        if acao32 == False:
            acao = input('''\nVOLDEMORT: Você é meu Potter!\n\n** Ao seu lado esquerdo há um lago muito profundo, vozes saem dentro dela, há um caminho longo em sua frente, você pode: andar p/ frente (w), direita (d)\n''')
        elif acao32 == True:
            acao = input('''\n** Ao seu lado esquerdo há um lago muito profundo, vozes saem dentro dela, há um caminho longo em sua frente, você pode: andar p/ frente (w), direita (d)\n''')
        if acao == 'w':
            localizacao = 33
            acao32 = True
        elif acao == 'd':
            localizacao = 42
            acao32 = True

    while(localizacao == 52):
        acao = input('''\n<< Você sente um vento gelado em sua frente, parece ter uma passagem por lá >>\n**Você pode: andar p/ frente (w), esquerda (a), direita (d)\n''')
        if acao == 'w':
            localizacao = 53
        elif acao == 'a':
            localizacao = 42
        elif acao == 'd':
            localizacao = 62
        
    while(localizacao == 62):
        if acao62 == False:
            acao = input('''\nVOLDEMORT: Ele descobriu nosso segredinho Nagini\n\n**Há um lago em sua frente, muitos Inferius inertes estão lá, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif acao62 == True:
            acao = input('''\n**Há um lago em sua frente, muitos Inferius inertes estão lá\n**Você pode: andar p/ esquerda (a), direita (d)\n''')
        if acao == 'a':
            localizacao = 52
            acao62 = True
        elif acao == 'd':
            localizacao = 72
            acao62 = True

    while(localizacao == 72):
        if acao72 == False:
            acao = input('''\n<< Harry tenta invocar sua varinha com 'accio varinha' mas não consegue >>\n**Há uma enorme parede de pedra atrás de você e em sua direita, existe um caminho em sua frente, você pode: andar p/ frente (w), esquerda (a)\n''')
        elif acao72 == True:
            acao = input('''\n<< Harry tenta novamente pegar sua varinha com 'accio varinha', Harry é muito burro >>\n**Há uma enorme parede de pedra atrás de você e em sua direita, existe um caminho em sua frente, você pode: andar p/ frente (w), esquerda (a)\n''')
        if acao == 'w':
            localizacao = 73
            acao72 = True
        elif acao == 'a':
            localizacao = 62
            acao72 = True

    while(localizacao == 53):
        hp -= 10
        acao = input(f'''<<< VOCÊ FOI ATACADO POR MORCEGOS! >>>\n<< Você perdeu {(morcego)} de HP >>\n<< VOCÊ TEM {(hp)} HP >>\n**Há uma parede enorme em sua direita, em seu lado esquerdo há um lago com Inferius inertes, você pode: andar p/ frente (w)\n''')
        if hp <= 0:
                localizacao = 'null'
        elif acao == 'w':
            localizacao = 54

    while(localizacao == 73):
        acao = input('''\n<< Você está entre dois lagos profundos, você jura que ouviu uma voz dizendo 'Corrige meu jogo da l2', que estranho >>\n**Você pode: andar p/ frente (w)\n''')
        if acao == 'w':
            localizacao = 74

    while(localizacao == 54):
        if acao54 == False:
            acao = input('''\nVOLDEMORT: Não seja covarde Potter! Seja corajoso igual seu pai, um corajoso morto!\n**Há uma enorme parede em seu lado esquerdo, você pode: andar p/ frente (w), direita (d)\n''')
        elif acao54 == True:
            acao = input('''\nVOLDEMORT: Venha até mim!\n\n**Há uma enorme parede em seu lado esquerdo, você pode: andar p/ frente (w), direita (d)\n''')
        if acao == 'w':
            localizacao = 55
            acao54 = True
        elif acao == 'd':
            localizacao = 64
            acao54 = True

    while(localizacao == 64):
        if felicis != 'i' and acao64 == False:
            acao = input('''\n<< O clima está estranho, você sente que está perto da saída >>\n**Você pode: andar p/ frente (w), esquerda (a), direita (d)\n''')
        elif felicis == 'i' and acao64 == False:
            acao = input('''\n<< O clima está ficando calmo, você sente que deve ir para direita, não sabe o porquê >>\n**Você pode: andar p/ frente (w), esquerda (a), direita (d)\n''')
        elif felicis != 'i' and acao64 == True:
            acao = input('''\n<< Harry está desesperado, Voldemort está próximo e não há ninguém que possa protegê-lo >>\n**Você pode: andar p/ frente (w), esquerda (a), direita (d)\n''')
        elif felicis == 'i' and acao64 == True:
            acao = input('''\n<< Harry parece ter visto sua varinha a 4 metros à sua direita >>\n**Você pode: andar p/ frente (w), esquerda (a), direita (d)\n''')
        if acao == 'w':
            localizacao = 65
            acao64 = True
        elif acao == 'a':
            localizacao = 54
            acao64 = True
        elif acao == 'd':
            localizacao = 74
            acao64 = True

    while(localizacao == 74):
        if felicis == 'i' and acao74 == False:
            acao = input('''\n<< Você se sente muito confiante pelo caminho que está seguindo >>\n**Há um lago de Inferius em sua frente, não notaram sua presença, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif felicis != 'i' and acao74 == False:
            acao = input('''\nVOLDEMORT: Não fuja de mim Potter\n\n**Há um lago de Inferius em sua frente, não notaram sua presença, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif felicis == 'i' and acao74 == True:
            acao = input('''\n<< Você se sente muito confiante pelo caminho que estava seguindo >>\n**Há um lago de Inferius em sua frente, não notaram sua presença, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif felicis != 'i' and acao74 == True:
            acao = input('''\nVOLDEMORT: Você é fraco, e vai perder\n\n**Há um lago de Inferius em sua frente, não notaram sua presença, você pode: andar p/ esquerda (a), direita (d)\n''')    
        if acao == 'a':
            localizacao = 64
            acao74 = True
        elif acao == 'd':
            localizacao = 84
            acao74 = True

    while(localizacao == 84):
        acao = input('''\n**Uma parede muito alta e gélida está em sua direita, há um caminho amplo em sua frente, você pode: andar p/ frente (w), esquerda (a)\n''')
        if acao == 'w':
            localizacao = 85
        elif acao == 'a':
            localizacao = 74

    while(localizacao == 55):
        if acao55 == False and acao65 == False:
            hp -= voldemort[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO POR VOLDEMORT! >>>\n"{(voldemort[1])}"\n<< Você perdeu {(voldemort[0])} de HP >>\n<< VOCÊ TEM {(hp)} HP >>\n\n**Há parede de rochas em sua esquerda e sua frente, você pode: andar p/ direita (d)\n')
            if hp <= 0:
                localizacao = 'null'
        elif acao55 != False or acao65 != False:
            acao = input('''\n**Há parede de rochas em sua esquerda e sua frente, você pode: andar para direita (d)\n''')
        if acao == 'd':
            localizacao = 65
            acao55 = True

    while(localizacao == 65):
        if acao55 == False and acao65 == False:
            hp -= voldemort[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO POR VOLDEMORT! >>>\n"{(voldemort[1])}"\n<< Você perdeu {(voldemort[0])} de HP >>\n<< VOCÊ TEM {(hp)} HP >>\n**Existe um lago em sua direita, há um amplo caminho em sua frente, você pode: andar p/ frente (w)\n')
            if hp <= 0:
                localizacao = 'null'
        elif acao55 != False or acao65 != False:
            acao = input('''\n**Existe um lago em sua direita, há um amplo caminho em sua frente, você pode: andar p/ frente (w)\n''')
        if acao == 'w':
            localizacao = 66
            acao65 = True

    while(localizacao == 85):
        if felicis == 'v':
            print('''\n<<< VOCÊ QUASE FOI ATACADO POR UM INFERIUS >>>\n<< Você utilizou sua sorte líquida em caso de velocidade, logo, você correu 2 metros para frente e não foi alcançado\n''')
            localizacao = 86
            acao85v = True
        elif felicis != 'v':
            hp -= inferius[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO POR UM INFERIUS QUE SAIU DO LAGO EM SUA ESQUERDA! >>>\n"{inferius[1]}"\n<< Você perdeu {inferius[0]} de HP >>\n<< VOCÊ TEM {hp} HP >>\n**Você está pressionado por um lago em sua esquerda e a parede da caverna em sua direita, você pode: andar p/ frente (w)\n')
            acao85 = True
            if hp <= 0:
                localizacao = 'null'
            elif acao == 'w':
                localizacao = 86

    while(localizacao == 86):
        if acao85v == True and acao76 == False:
            acao = input('''\n<< Harry está muito nervoso, por um triz o Inferius não puxou seu pé para dentro do lago, se ao menos tivesse a varinha para se defender >>\n**Há uma parede da caverna em sua frente e em sua direita também. Existe um caminho amplo em sua esquerda, você pode: andar para esquerda (a)\n''')
        elif acao85 == True and acao76 == False:
            acao = input('''\n<< Harry está mancando, o Inferius causou um profundo ferimento em sua perna esquerda >>\n**Há uma parede da caverna em sua frente e em sua direita também. Existe um caminho amplo em sua esquerda, você pode: andar p/ esquerda (a)\n''')
        elif acao85 == True or acao85v == True and acao76 == True:
            acao = input('''\n<< Você está em dúvida se deve ou não seguir a luz? >>\n**Há uma parede da caverna em sua frente, existe um caminho amplo em sua esquerda, você pode: andar p/ esquerda (a)\n''')
        if acao == 'a':
             localizacao = 76

    while(localizacao == 76):
        if felicis == 'i':
            acao = input('''\n<< Harry nota que há uma luz reluzente no caminho em sua esquerda, o que será? Ele está muito confiante! >>\n**Uma parede não tão escura da caverna está em sua frente, você pode: andar p/ esquerda (a), direita (d)\n''')
        elif felicis != 'i':
            acao = input('''\n<< Harry nota que há uma luz reluzente no caminho em sua esquerda, ele teme ser o Lord das Trevas >>\n**Uma parede não tão escura da caverna está em sua frente, você pode: andar p/ esquerda (a), direita (d)\n''')
        if acao == 'a':
            localizacao = 66
            acao76 = True
        elif acao == 'd':
            localizacao = 86
            acao76 = True

    while(localizacao == 66):
        acao = input('''\n**Há um extenso caminho em sua frente, a luz está mais reluzente que nunca! Você pode: andar p/ frente (w), direita (d)\n''')
        if acao == 'w':
            localizacao = 67
        elif acao == 'd':
            localizacao = 76

    while(localizacao == 67):
        if felicis == 'i':
            resp = input('''\n<<< VOCÊ CHEGOU A UM QUEBRA-CABEÇA >>>\n\n***Lord Voldemort com certeza não deixará qualquer um sair tão fácil desta caverna, em sua esquerda há uma parede escrito:\n- Que objeto estava no lugar da Horcrux verdadeira?\n''')
            if resp == "medalhão" or resp == "medalhao":
                acao = input('''\n<<< VOCÊ ACERTOU! >>>\n a parede em sua direita onde estava a luz reluzente se transformou numa passagem\n**Há uma parede em sua esquerda, você pode: andar p/ frente (w), direita (d)\n''')
                if acao == 'w':
                    localizacao = 68
                elif acao == 'd':
                    localizacao = 77
        elif felicis != 'i':
            acao = input('''\n<< A luz reluzente vem de uma parede da caverna em sua direita, você tenta algum tipo de interação, mas sem varinha é improvável >>\n**Há uma parede em sua esquerda, você pode? andar p/ frente (w)\n''')
            if acao == 'w':
                localizacao = 68
            elif acao == 'd':
                acao = input('\nVocê não sabe como passar deste quebra-cabeça, tente outro modo de sair da caverna, existe apenas caminho em sua frente (w)\n')
                if acao == 'w':
                    localizacao = 68

    while(localizacao == 77):
        acao = input('''\n**Você vê uma luz ao fim do túnel, considere que a entrada da passagem na qual você entrou está em suas costas, você pode: andar p/ frente (w)\n''')
        if acao == 'w':
            localizacao = 87

    while(localizacao == 87):
            hp -= inferius[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO POR UM INFERIUS QUE ESTAVA DEITADO NO CHÃO! >>>\n<< Você perdeu {inferius[0]} de HP >>\n<< VOCÊ TEM {hp} HP >>\n**Você está muito próximo da luz! Você pode: andar p/ frente (w)\n')
            if hp <= 0:
                localizacao = 'null'
            elif acao == 'w':
                localizacao = 97

    if(localizacao == 97):
        for win in range (4):
            print('!!!PARABÉNS, VOCÊ CONSEGUIU ESCAPAR DA CAVERNA!!!')
            localizacao = False

    while(localizacao == 68):
        if acao48 == False:
            if felicis != 'f':
                acao = input('''\n**Há uma parede muito escura e gelada, já em sua frente e em sua esquerda a parede não parece ser tão firme, porém, você não tem forças para ultrapassar, você pode: andar p/ direita (d)\n''')
                if acao == 'd':
                    localizacao = 78
            elif felicis == 'f':
                acao = input('''\n**Há uma parede muito escura e gelada em sua frente, ja na esquerda a parede não parece ser tão firme, tente empurrar as rochas na parede, você pode: empurrar rochas na parede esquerda (f), andar p/ direita (d)\n''')
                if acao == 'd':
                    localizacao = 78
                elif acao == 'f':
                    localizacao = 48
                    acao68 = True
        elif acao48 == True:
            acao = input('''\n**Você passou pelas rochas e está em outro caminho completamente diferente, você pode: andar p/ direita (d), retornar pela passagem da parede (a)\n''')
            if acao == 'd':
                localizacao = 78
            elif acao == 'a':
                localizacao = 48

    while(localizacao == 78):
        print('''\nVOLDEMORT: Estupore!\n\n<<< O feitiço atingiu o teto, que fez cair muitos escombros onde você estava! Você pulou mas está encurralado! >>>\n''')
        print('''\nVOLDEMORT: Harry Potter, o menino que sobreviveu, vai morrer! AVADAKEDAVRA!!!\n\n''')
        for a in range(4):
            print('''<<< PARABÉNS, !!!VOCÊ MORREU!!! >>>''')
        localizacao = False

    while(localizacao == 33):
        if felicis == 'v':
            print('''\n<<< VOCÊ QUASE FOI ATACADO POR UM INFERIUS QUE SAIU DO LAGO EM SUA ESQUERDA>>>\n<< Você utilizou sua sorte líquida em caso de velocidade, logo, você correu 2 metros para frente e não foi alcançado\n''')
            localizacao = 34
            acao33v = True
        elif felicis != 'v':
            hp -= inferius[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO POR UM INFERIUS QUE SAIU DO LAGO EM SUA ESQUERDA! >>>\n"{inferius[1]}"\n<< Você perdeu {inferius[0]} de HP >>\n<< VOCÊ TEM {hp} HP >>\n**Você está pressionado por um lago em sua esquerda e a parede da caverna, você pode: andar p/ frente (w)\n')
            acao33 = True
            if hp <= 0:
                localizacao = 'null'
            elif acao == 'w':
                localizacao = 34

    while(localizacao == 34):
        if acao24 == False:
            acao = input('''\n**Há uma parede enorme em sua direita, porém, existe uma pequena entrada a sua esquerda e em sua frente há um amplo caminho, você pode: andar p/ frente (w), esquerda (a)\n''')
            if acao == 'a':
                localizacao = 24
        elif acao24 == True:
            acao = input('''\n**Voldemort desaparatou após o ataque, mas você ouviu passos deles a metros de distância, há uma parede enorme em sua direita e em sua frente há um amplo caminho, você pode: andar p/ frente (w)\n''')
        if acao == 'w':
            localizacao = 35
        
    while(localizacao == 24):
        hp -= voldemort[0]
        acao = input(f'\n<<< VOCÊ FOI ATACADO POR VOLDEMORT! >>>\n"{voldemort[1]}"\n<< Você perdeu {voldemort[0]} de HP >>\n"<< VOCÊ TEM {(hp)} HP >>\n**O impacto do ataque fez você voltar para a posição anterior\n**Você pode: andar p/ frente (w)\n')
        if hp <= 0:
                localizacao = 'null'
        else:
            localizacao = 34
        acao24 = True

    while(localizacao == 35):
        if acao24 == True:
            acao = input('''\n << Você tropecou, o ataque do Lord das Trevas lhe deixou atordoado >>\n**Não é possível ir para os lados, pois, há um lago e um grande paredão da caverna lhe cercando, você pode: ir p/ frente (w)\n''')
            if acao == 'w':
                localizacao = 36
        elif acao24 == False:
            acao = input('''\n**Não é possível ir para os lados, pois, há um lago e um grande paredão da caverna lhe cercando, você pode: ir p/ frente (w)\n''')
            if acao == 'w':
                localizacao = 36


    while(localizacao == 36):
        if felicis == 'i' and acao36 == False and acao26 == False:
            acao = input('''\n<< Potter está com grande dúvida agora, há passagem apenas pela esquerda e direita, você jura que viu alguma varinha pela direita, é o que você mais deseja ter agora! >>\n**Você pode, andar p/ esquerda (a), direita (d)\n''')
        elif felicis != 'i' and acao36 == False and acao26 == False:
            acao = input('''\n<< Potter está com grande dúvida agora, há passagem apenas pela esquerda e direita, você já escolheu ir pra esquerda uma vez, por que não escolher outra? >>\n**Você pode, andar p/ esquerda (a), direita (d)\n''')
        elif felicis == 'i' or felicis != 'i' and acao36 == True:
            acao = input('''\n<< A dúvida segue em sua mente brilhante? >>\n**Você pode, andar p/ esquerda (a), direita (d)\n''')
        elif felicis == 'i' or felicis != 'i' and acao26 == True:
            acao = input('''\n<< Voldemort está te deixando muito fraco >>\n**Você pode, andar p/ esquerda (a), direita (d)\n''')
        if acao == 'a':
            localizacao = 26
            acao36 = True
        elif acao == 'd':
            localizacao = 46
            acao36 = True

    while(localizacao == 46):
        acao = input('''\n**Há um caminho em sua frente! Há um Inferius que não se move a poucos passos em sua frente, não é possível ir para direita, pois, há uma parede fria da caverna, você pode: andar p/ frente (w), esquerda (a)\n''')
        if acao == 'w':
            localizacao = 47
        elif acao == 'a':
            localizacao = 36

    while(localizacao == 47):
        if felicis == 'v':
            print('''\n<<< VOCÊ QUASE FOI ATACADO PELO INFERIUS >>>\n<< Você utilizou sua sorte líquida em caso de velocidade, logo, você correu 2 metros para frente e não foi alcançado\n''')
            localizacao = 48
        elif felicis != 'v':
            hp -= inferius[0]
            acao = input(f'\n<<< VOCÊ FOI ATACADO PELO INFERIUS QUE ESTAVA NO CHÃO! >>>\n<< Você perdeu {inferius[0]} de HP >>\n<< VOCÊ TEM {hp} HP >>\n**Você está pressionado por um lago em sua esquerda e a parede da caverna, você pode: andar p/ frente (w)\n')
            acao47 = True
            if hp <= 0:
                localizacao = 'null'
            elif acao == 'w':
                localizacao = 48

    while(localizacao == 48):
        if acao68 == False:
            if felicis == 'i':
                acao = input('''\n<< Você consegue ver algo brilhoso em sua frente! >>\n**Há uma parede não tão densa em sua direita, porém, não chama a sua atenção, você pode: andar para frente (w), esquerda (a)\n''')
            elif felicis == 'f':
                acao = input('''\n<< Harry está numa dúvida tremenda, há caminho pela frente e pela esquerda, porém, em sua direita existe uma parede que parece não ser tão firme >>\n**Você pode: ultrapassar a parede da direita usando a força (f), andar p/ frente (w), esquerda (a)\n''')
                if acao == 'f':
                    localizacao = 68
                    acao48 = True
            elif felicis != 'i' and felicis != 'f':
                acao = input('''\n**Há uma parede não tão densa em sua direita, porém, não chama a sua atenção, você pode: andar para frente (w), esquerda (a)\n''')
            if acao == 'w':
                localizacao = 49
            elif acao == 'a':
                localizacao = 38
        elif acao68 == True:
            if felicis == 'i':
                acao = input('''\n**Você passou pelas rochas e está em outro caminho diferente\n<< Você consegue ver algo brilhoso em sua frente! >>\n**Você pode: andar para frente (w), esquerda (a), retornar pela passagem da parede (d)\n''')
            elif felicis != 'i':
                acao = input('''\n**Você passou pelas rochas e está em outro caminho completamente diferente, você pode: andar para frente (w), esquerda (a), retornar pela passagem da parede (d)\n''')
            if acao == 'w':
                localizacao = 49
            elif acao == 'a':
                localizacao = 38
            elif acao == 'd':
                localizacao = 68

    while(localizacao == 49):
        for win in range (4):
            print('!!!PARABÉNS, VOCÊ CONSEGUIU ESCAPAR DA CAVERNA!!!')
            localizacao = False

    while(localizacao == 26):
            hp -= voldemort[0]
            acao = input(f'\nVOLDEMORT: Venha e me enfrente seu covarde!\n<<< VOCÊ FOI ATACADO POR VOLDEMORT! >>>\n<< Você perdeu {(voldemort[0])} de HP >>\n"<< VOCÊ TEM {(hp)} HP >>\n**Há um enorme lago em sua esquerda, você pode: andar p/ frente (w), direita (d)\n')
            if hp <= 0:
                localizacao = 'null'
            elif acao == 'd':
                localizacao = 36
                acao26 = True
            elif acao == 'w':
                localizacao = 27
                acao26 = True

    while(localizacao == 27):
        acao = input('''**Você está entre dois lagos, você pode: andar para frente (w)\n''')
        if acao == 'w':
            localizacao = 28

    while(localizacao == 28):
        if acao18 == False and felicis != 'f': 
            acao = input('''\n<< Harry observa que há muitas pedras que impedem sua passagem para esquerda>>\n**Você pode: andar p/ frente (w), direita (d)\n''')
            if acao == 'w':
                localizacao = 29
            elif acao == 'd':
                localizacao = 38
        elif acao18 == False and felicis == 'f':
            acao = input('''\n<< Harry observa que há muitas pedras que impedem sua passagem para esquerda>>\n**Você pode: usar a força para ir p/ esquerda (f) andar p/ frente (w), direita (d)\n''')
            if acao == 'f':
                localizacao = 18
            elif acao == 'w':
                localizacao = 29
            elif acao == 'd':
                localizacao = 38
        elif acao18 == True:
            acao = input('''\n<< Potter se sente melhor após a barra de chocolate que revigorou um pouco suas energias >>\n**Você pode: andar p/ frente (w), direita (d)\n''')
            if acao == 'w':
                localizacao = 29
            elif acao == 'd':
                localizacao = 38

    while(localizacao == 18):
        hp += 25
        print(f'''\n<< Você encontrou uma barra de chocolate! Seguindo a dica de Remo Lupin, chocolate revigora os nervos, você ganhou 25 de HP >>\n\nVOCÊ TEM {hp} HP\n\n**Você voltou para a direita\n''')
        localizacao = 28
        acao18 = True

    while(localizacao == 29):  
        print('''\n<<< VOCÊ ENTROU NUM NINHO DE INFERIUS, NÃO E POSSÍVEL ESCAPAR >>>\n\n''')
        for c in range (4):
            ('''<<< PARABÉNS, !!!VOCÊ MORREU!!! >>>\n''')
        localizacao = False

    while(localizacao == 38):
        acao = input('''\n<< Potter não sabe como contar aos seus amigos o que aconteceu, ele não sabe nem se irá voltar para seus amigos >>\n**Você não pode ir para frente, pois, existe uma enorme parede, você pode:andar p/ esquerda (a), direita (d)\n''')
        if acao == 'a':
            localizacao = 28
        if acao == 'd':
            localizacao = 48
        
        

        
        
        
        
        
        
    
                
        
        

    
            
        
