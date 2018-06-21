import time
import sys
from threading import Thread
from threading import Lock

class Th(Thread):
    def __init__ (self, word, esp, texto):
        Thread.__init__(self)
        self.word = word
        self.esp = esp
        self.texto = texto

    def run(self):
        lock.acquire()
        if self.word[7] == 'a':
            with open('WordList.txt', 'a') as arq:
                arq.write(self.word)
        else:
            with open('WordList.txt', 'a') as arq:
                arq.write(" ")
                arq.write(self.word)
        self.chave=montarchave(self.texto,self.word)
        self.textoDes=descifragem(self.texto,self.chave,self.esp)
        if self.textoDes.find('amor') != -1:
            print("Texto Desifrado: "+self.textoDes)
            with open('resposta.txt', 'a') as arq:
                arq.write(textoDes+'\n')
                arq.write("Chave: "+self.word+"\n")
        lock.release()
                
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

lock = Lock()
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
try:
    arq = open('WordList.txt', 'r')
    vet = arq.read().split("\n")
    vet2 = vet[-1].split(" ")
    vet2 = vet2[-1]
    arq.close()
except:
    vet2 ='maaaaaaa'
    with open('WordList.txt', 'a') as arq:
            arq.write(vet2)
palavra=[]

for i in range(len(vet2)):
    palavra.append(vet2[i])

print(vet2)
aux=''
threads=[]
i=0
if palavra[7] == 'z':
    palavra[7] = 'a'
    if palavra[6] == 'z':
        palavra[6] = 'a'
        if palavra[5] == 'z':
            palavra[5] = 'a'
            if palavra[4] == 'z':
                palavra[4] = 'a'
                if palavra[3] == 'z':
                    palavra[3] = 'a'
                    if palavra[2] == 'z':
                        palavra[2] = 'a'
                        if palavra[1] == 'z':
                            palavra[1] = 'a'
                            if palavra[0] == 'z':
                                sys.exit()
                            else:
                                palavra[0]=chr((ord(palavra[0])+1))
                        else:
                            palavra[1]=chr((ord(palavra[1])+1))
                    else:
                        palavra[2]=chr((ord(palavra[2])+1))
                else:
                    palavra[3]=chr((ord(palavra[3])+1))
            else:
                palavra[4]=chr((ord(palavra[4])+1))
        else:
            palavra[5]=chr((ord(palavra[5])+1))
    else:
        palavra[6]=chr((ord(palavra[6])+1))
else:
    palavra[7]=chr((ord(palavra[7])+1))
    
try:
    for a in range(ord(palavra[0]),123):
        for b in range(ord(palavra[1]),123):
            if chr(b) == 'z':
                palavra[1] = 'a'
            for c in range(ord(palavra[2]),123):
                if chr(c) == 'z':
                    palavra[2] = 'a'
                for d in range(ord(palavra[3]),123):
                    if chr(d) == 'z':
                        palavra[3] = 'a'
                    for e in range(ord(palavra[4]),123):
                        if chr(e) == 'z':
                            palavra[4] = 'a'
                        for f in range(ord(palavra[5]),123):
                            if chr(f) == 'z':
                                palavra[5] = 'a'
                            for g in range(ord(palavra[6]),123):
                                if chr(g) == 'z':
                                    palavra[6] = 'a'
                                for h in range(ord(palavra[7]),123):
                                    if aux == 'maaaaaaaa':
                                        sys.exit()
                                    if chr(h) == 'z':
                                        palavra[7] = 'a'
                                    aux = chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+chr(g)+chr(h)
                                    #lock.acquire()
                                    #thread=Th(aux,esp,texto)
                                    #thread.start()
                                    #lock.release()
                                    if chr(h) == 'a':
                                        with open('WordList.txt', 'a') as arq:
                                            arq.write(aux)
                                    else:
                                        with open('WordList.txt', 'a') as arq:
                                            arq.write(" ")
                                            arq.write(aux)
                                    chave=montarchave(texto,aux)
                                    textoDes=descifragem(texto,chave,esp)
                                    teste = textoDes.replace(',','').split(" ")
                                    if textoDes.find('amor') != -1:
                                        print("texto desifrado: "+textoDes)
                                        print("Chave: " +aux)
                                        #op=input("Deseja continuar procurando? s/n: ")
                                        #if op == 'n':
                                        #print("Texto Desifrado: "+textoDes)
                                        with open('resposta.txt', 'a') as arq:
                                            arq.write(textoDes+'\n')
                                            arq.write("Chave: "+aux+"\n")
                                        
                                #for num in range(i):
                                #    lock.acquire()
                                #    threads[num].join()
                                #    lock.release()
                                with open('WordList.txt', 'a') as arq:
                                    arq.write("\n")
except KeyboardInterrupt:
    fim = time.time()
    segundos = fim - inicio
    horas = int(segundos / 3600)
    segundos_rest = segundos % 3600
    minutos = int(segundos_rest / 60)
    segundos_rest = segundos_rest % 60
    print("Tempo de Execução até agora: "+str(horas)+"H "+str(minutos)+"M "+str(segundos_rest)+"S")
    print(segundos)
    sys.exit()

fim = time.time()
segundos = fim - inicio
horas = int(segundos / 3600)
segundos_rest = segundos % 3600
minutos = int(segundos_rest / 60)
segundos_rest = segundos_rest % 60

print("Tempo de Execução: "+str(horas)+"Hora(s)"+str(minutos)+"Minuto(s)"+str(segundos_rest)+"Segundo(s)")
print(segundos)
