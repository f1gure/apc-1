#Comece executando as instruções de atribuição:
#>>> s1 = 'ant'
#>>> s2 = 'bat'
#>>> s3 = 'cod'
#Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
#(a) 'ant bat cod'
#(b) ant ant ant ant ant ant ant ant ant ant'
#(c) 'ant bat bat cod cod cod'
#(d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
#(e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(str(s1) + " " + str(s2 ) + " " + str(s3))
print((str(s1) + " ") * 10)
print((str(s1) + " ") + ((str(s2) + " ") *2) + ((str(s3) + " ") * 3))
print(((str(s1) + " " + str(s2) + " ")* 7))
print((((str(s2)*2)+str(s3) + " " )*5))


