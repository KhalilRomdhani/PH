PH=int(input("PH = "))
if PH<=2 :
    print("acide fort car ph < 2")
elif 3<=PH<=6 :
    print("acide faible car ph entre 2 et 6")
elif PH==7 :
    print("neutre car ph = 7")
elif 8<=PH<=12 :
    print("basique faible")
elif PH>13 :
     print("basique forte car ph > 13")
#Inférieure à 7, la solution est acide. Egale à 7, la solution est neutre. Supérieure à 7, la solution est basique.