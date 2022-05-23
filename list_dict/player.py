player = ['sound1','sound2','sound3','sound4']
print(player)
name1,name2 = input('Введите первую песню'),input('Введите вторую песню')
name1=player.index(name1)
name2=player.index(name2)
player[name1],player[name2] = player[name2],player[name1]
print(player)