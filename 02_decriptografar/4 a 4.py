import time
import sys
                
def descifragem(texto, chave, espacos):
    textoDescifrado=""
    for i in range(len(texto)):
        aux = ord(texto[i])-97
        aux2 = ord(chave[i])-97
        temp = ((aux-aux2)%26)+97
        for j in espacos:
            if j.find(',') != -1:
                j = j.split(',')
                if int(j[0]) == i:
                    textoDescifrado+=","
            elif j.find('.') != -1:
                j = j.split('.')
                if int(j[0]) == i:
                    textoDescifrado+="."
            elif int(j) == i:
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

texto='mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy'

inicio = time.time()

temp=""
esp=''
ant=True
espacos=0
for i in range(len(texto)):
    if texto[i] == " ":
        if ant:
            esp+=str(i)
            ant=False
        else:
            esp+=" "+str(i-espacos)
        espacos+=1
    elif texto[i] == ',':
        esp+=" "+str(i-espacos)+","
        espacos+=1
    elif texto[i] == '.':
        esp+=" "+str(i-espacos)+"."
        espacos+=1
    else:
        temp+=texto[i]
        
esp = esp.split(' ')
print (esp)
texto=temp
palavra=''
try:
    with open('4x4.txt', 'r') as arq:
        vet = arq.read().split("\n")
    if vet[-1] != "Final":
        raise Exception()
except:
    try:
        with open('ultimo.txt', 'r') as arq:
            vet2 = arq.read().split("\n")
            vet = vet2[-1].split(" ")
            vet = vet[-1]
            print(vet2[-1])
    except:
        with open('ultimo.txt', 'a') as arq:
            arq.write("aaaa")
        vet = 'aaaa'
    palavra=[]
    for i in range(len(vet)):
        palavra.append(vet[i])

    print(vet)
    if palavra[3] == 'z':
        palavra[3] = 'a'
        if palavra[2] == 'z':
            palavra[2] = 'a'
            if palavra[1] == 'z':
                palavra[1] = 'a'
                if palavra[0] == 'z':
                    with open('ultimo.txt', 'w') as arq:
                            arq.writelines('aaaa')
                    sys.exit()
                else:
                    palavra[0]=chr((ord(palavra[0])+1))
            else:
                palavra[1]=chr((ord(palavra[1])+1))
        else:
            palavra[2]=chr((ord(palavra[2])+1))
    else:
        palavra[3]=chr((ord(palavra[3])+1))

    try:
        for a in range(ord(palavra[0]),123):
            for b in range(ord(palavra[1]), 123):
                if chr(b) == 'z':
                    palavra[1] = 'a'
                for c in range(ord(palavra[2]),123):
                    if chr(c) == 'z':
                        palavra[2] = 'a'
                    for d in range(ord(palavra[3]),123):
                        if chr(d) == 'z':
                            palavra[3] = 'a'
                        aux = chr(a)+chr(b)+chr(c)+chr(d)
                        chave=montarchave(texto,aux)
                        textoDes=descifragem(texto,chave,esp)
                        teste = textoDes.replace(',','').split(" ")
                        if teste[2] == 'amor':
                            with open('4x4.txt', 'a') as arq:
                                arq.write("0 1 2 3:"+aux+"\n")
                        elif teste[3] == 'hoje':
                            with open('4x4.txt', 'a') as arq:
                                arq.write("4 5 6 7:"+aux+"\n")

                        with open('ultimo.txt', 'a') as arq:
                            arq.write(" "+aux)
                    with open('ultimo.txt', 'a') as arq:
                        arq.write("\n")
        with open('4x4.txt', 'a') as arq:
            arq.write("Final")
            
    except KeyboardInterrupt:
        fim = time.time()
        segundos = fim - inicio
        horas = int(segundos / 3600)
        segundos_rest = segundos % 3600
        minutos = int(segundos_rest / 60)
        segundos_rest = segundos_rest % 60
        print("Tempo de Execução até agora: "+str(horas)+"H "+str(minutos)+"M "+str(segundos_rest)+"S")
        print(segundos)
        with open('tempo.txt', 'a') as arq:
            arq.write(str(segundos)+"\n")
        sys.exit()


vet=[]
chave=['','','','','','','','']
try:
    with open('4x4.txt', 'r') as arq:
        vet=arq.read().split("\n")
except:
    sys.exit()

for elemento in vet:
    if elemento != "Final":
        temp = elemento.split(":")
        tempV = temp[0].split(" ")
        tempT = temp[1]
        print(tempV)
        for i in range(len(tempT)):
            chave[int(tempV[i])] = tempT[i]

print(chave)
chave = ', '.join(chave).replace(", ","")
chaveF=montarchave(texto,chave)
textoDes=descifragem(texto,chaveF,esp)

with open('resultadoFinal.txt', 'a') as arq:
    arq.writelines(textoDes+"\n")
    arq.writelines("Chave: "+chave)

print("Texto Descriptografado: "+textoDes)
print("Chave: "+chave)
fim = time.time()
segundos = fim - inicio
vet=[]

try:
    with open('tempo.txt','r') as arq:
        vet = arq.read().split("\n")
    for i in vet:
        segundos+=int(i)
    horas = int(segundos / 3600)
    segundos_rest = segundos % 3600
    minutos = int(segundos_rest / 60)
    segundos_rest = segundos_rest % 60
except:
    horas = int(segundos / 3600)
    segundos_rest = segundos % 3600
    minutos = int(segundos_rest / 60)
    segundos_rest = segundos_rest % 60


print("Tempo de Execução: "+str(horas)+"H "+str(minutos)+"M "+str(segundos_rest)+"S")
