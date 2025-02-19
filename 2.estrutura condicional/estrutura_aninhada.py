import os
os.system ("clear")

idade=16

#se idade <12
#   escreval ("acesso negado")
#senao se idade <18 entao
#   escreval ("somente com permissao dos pais.")
#senao
#   escreval ("acesso permitido.")
#fimse

if idade < 12:
    print ("acesso negado.")
elif idade <18:
    print ("somente com permissao dos pais.")
else:
    print ("acesso permitido.")

print ("==fim==")