def Umrechnung(dezimalzahl):
   if dezimalzahl == 0:
       return ""
   else:
       return Umrechnung(dezimalzahl // 2) + str(dezimalzahl % 2)

dezimalzahl = int(input("Dezimalzahl: "))


binary = Umrechnung(dezimalzahl)
print(binary)