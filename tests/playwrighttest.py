from playwright.sync_api import sync_playwright
import unittest
import os
import sys

class ClassTest(unittest.TestCase):
    def test_message_email(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:5000/registrar")
            messageEmail = page.inner_text("body > div > div > div > div > div.col-md-8 > form > div:nth-child(1) > div")
            assert "Este campo es obligatorio." == messageEmail
            browser.close()

    def test_titulo_equals_expected(page):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:5000/registrar")
            titulo = page.title()
            assert "Registrar" == titulo
            browser.close()

            
if __name__ == '__main__':
    unittest.main()
    
