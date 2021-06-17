
from datetime import datetime
import hashlib

#Clase singleton
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


#Clase que define la estructura del bloque
class Bloque:
    def __init__(self, mail, motiv, arch, time=datetime.now().strftime("%Y-%m-%d %H:%M")):
        self.email = mail
        self.motive = motiv 
        self.archivo = arch
        self.timestamp = time
        self.hashant = 0
        self.nonce = 1
        hasher = str(self.nonce) + mail + motiv + arch +self.timestamp
        self.hash = self.hashing(hasher)
        
    #Método que obtendrá el hash del bloque
    def hashing(self, hashvar):
        #si la fecha es impar, el hash empezará con un 0, si es par dos ceros
        hasp = hashlib.sha256(hashvar.encode('ascii')).hexdigest()
        if len(self.timestamp)>0 and (int(self.timestamp[9])%2!=0):
            while (hasp[0]!='0'):
                self.nonce +=1
                hashvar = str(self.nonce)+hasp[len(str(self.nonce-1)):]
                hasp = hashlib.sha256(hashvar.encode('ascii')).hexdigest()
        else:
            while (hasp[0]!='0' or hasp[1]!= '0'):
                self.nonce +=1
                hashvar = str(self.nonce)+hasp[len(str(self.nonce-1)):]
                hasp = hashlib.sha256(hashvar.encode('ascii')).hexdigest()
        return hasp

#Clase que maneja la cadena de bloques
@singleton
class BlockManager:
    def __init__(self,cadena):
        self.cadena = cadena

    #Metodo para crear bloque genesis
    def _crear_bloque_genesis_(self):
        bloqg = Bloque("","","","")
        self.cadena.append(bloqg)


    #Método para ingresar un bloque
    def agregar_nuevo(self, bloq):
        # ct = [Bloque]* (len(self.cadena)+1)#Crea el nuevo arreglo más grande
        # for i in range(len(self.cadena)):
        #     ct[i]= self.cadena[i]
        # hant = self.cadena[len(self.cadena)-1].hash
        # bloq.hashant = hant
        # ct[len(self.cadena)]=bloq
        # self.cadena = ct
        self.cadena.append(bloq)

    #Metodo que devuelve un bloque por su indice
    def get_block(self,ind):
        return (self.cadena[ind])
        
    #Metodo que devuelve un bloque buscando su hash
    def busqueda_hash(self,hh):
        for bloque in self.cadena:
            if (bloque.hash == hh):
                return bloque
        return "none"
    
    #Método que limpia los elementos de la cadena
    def remove_chain(self):
        self.cadena.clear()
    
    #Método que pone los hashes de todos los bloques en un archivo
    def hashes_to_file(self):
        file1 = open("file.txt","w")
        for i in self.cadena:
            file1.write(i.hash)
        file1.close()

    #Método de verificacion de cadena
    def chain_verif(self):
        for block in range(0,len(self.cadena)):
            if (block>0):
                if self.cadena[block].hashant!=self.cadena[block-1].hash:
                    return False
            bloq = Bloque(self.cadena[block].email, self.cadena[block].motive,self.cadena[block].archivo,self.cadena[block].timestamp)
            if(bloq.hash!=self.cadena[block].hash):
                return False
        return True
    
    #Metodo que devuelve ultimo bloque
    def get_last(self):
        return self.cadena[len(self.cadena)-1]

