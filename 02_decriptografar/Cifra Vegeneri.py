"""
    Autores: Felipe e Thiago

    Cifra Vegeneri V1.3
"""

def cifragem(texto, chave):
    textoCifrado=""
    for i in range(len(texto)):
        aux = ord(texto[i])-97
        aux2 = ord(chave[i])-97
        temp = ((aux+aux2)%26)+97
        textoCifrado+=chr(temp)
    return textoCifrado

def descifragem(texto, chave, espacos):
    textoDescifrado=""
    for i in range(len(texto)):
        aux = ord(texto[i])-97
        aux2 = ord(chave[i])-97
        temp = ((aux-aux2)%26)+97
        for j in espacos:
            if int(j) == i:
                textoDescifrado+=" "
        textoDescifrado+=chr(temp)
    return textoDescifrado

def montarchave(texto, chave):
    while(len(chave)<len(texto)):
        for i in range(len(chave)):
            if len(chave) < len(texto):
                chave+=chave[i]
            else:
                break
    return chave
    
chave=input("Informe a chave de Segurança: ").replace(" ","").replace("ç","c").lower()

espaços=0
texto=input("Informe o texto a ser cifrado: ").replace("ç","c").lower()

temp=""
vet=''
ant=True
espacos=0
for i in range(len(texto)):
    if texto[i] == " ":
        if ant:
            vet+=str(i)
            ant=False
        else:
            vet+=" "+str(i-espacos)
        espacos+=1
    else:
        temp+=texto[i]
texto=temp

chave=montarchave(texto,chave)
textoCifrado=cifragem(texto,chave)+"\n"
tempo=[textoCifrado,vet]
arq=open("teste.txt", 'w')
arq.writelines(tempo)
arq.close()

arq=open("teste.txt", 'r')
vetor=arq.read().split("\n")
espacos = vetor[1].split(" ")
textoDes=descifragem(texto,chave,espacos)
textoDescifrado=descifragem(vetor[0],chave,espacos)
arq.close()

print("Espaços: "+str(vet))    
print("Chave: "+chave)
print("Texto Original: "+texto)
print("Texto Cifrado: "+textoCifrado)
print("Texto Descifrado: "+textoDes)
