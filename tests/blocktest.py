import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from src.blockchaincode  import Bloque

class BlockTest(unittest.TestCase):
    #(django project standard)
    #Nombre de Tests: test_[Feature being tested]

    #Test de la creacion de bloques
    def test_BlockClassCreatesABlock(self):
        test = Bloque("hola@gmail.com","mot1","files1.txt")
        self.assertEqual(test.email,"hola@gmail.com")
        self.assertEqual(test.motive,"mot1")
        self.assertEqual(test.archivo,"files1.txt")

    #Test de la funcion hashing
    def test_BlockHashFunctionWorks(self):
        test = Bloque("Buendia@hola.com","mot6","file4.py","2021-04-19 20:48")        
        self.assertEqual("0c514ca1c4ad18b497e7b0e4094890eb46112979ea7a60b5f922cefc27ab7a7c",test.hash)
    

    #Test de que dos bloques iguales tienen hash iguales y creacion de una cadena
    def test_SimilarBlocksGetSameHash(self):
        b1 = Bloque("hola@out.com","mot1","file1.rar","2021-04-19 20:48")
        b2 = Bloque("hola@out.com","mot1","file1.rar","2021-04-19 20:48")       
        self.assertEqual(b1.hash,b2.hash)

    #Test de que el hash con fecha impar tiene un 0 adelante
    def test_HashFunctionGivesOneZeroWithOddDate(self):
        b1 = Bloque("hola@out.com","mot1","file1.rar","2021-04-19 20:48")
        self.assertEqual('0',b1.hash[0])
    
    #Test de que el hash con fecha impar tiene dos ceros adelante
    def test_HashFunctionGivesTwoZerosWithEvenDate(self):
        b1 = Bloque("hola@out.com","mot1","file1.rar","2021-06-14 22:41")
        self.assertEqual('0',b1.hash[0])
        self.assertEqual('0',b1.hash[1])

if __name__ == "__main__":
    unittest.main()