from playwright.sync_api import sync_playwright
import unittest
import os
import sys

class ClassTest(unittest.TestCase):
    def test_title(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:5000/registrar")

            # Ingresamos el archivo
            page.fill('text=Archivo', '123422.exe')

            # Ingresamos el motivo
            page.fill('text=Motivo', '1')

            # Ingresamos el email
            page.fill('text=Email', 'hola@123.com')

            #Presionamos el boton Enviar
            page.click('button#submit')

            self.assertEqual("El que sea el nombre de la pagina siguiente",page.title())

            browser.close()

            

if __name__ == '__main__':
    unittest.main()
    
