import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class OrangeHRM(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        #############################################################berhasil login########################################
        
    def test_a_success_login(self): 
    
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        current_url = browser.current_url
        self.assertIn(current_url, 'https://opensource-demo.orangehrmlive.com/index.php/dashboard')


        #############################################################gagal login########################################
        

    def test_a_failed_login(self): 

        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("erlangga")
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        error_message = browser.find_element(By.ID,"spanMessage").text

        self.assertEqual(error_message, 'Invalid credentials')

        #############################################################tanpa akun langsung login########################################

    def test_a_failed_empty_login(self): 

        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        browser.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        error_message = browser.find_element(By.ID,"spanMessage").text

        self.assertEqual(error_message, 'Username cannot be empty')


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
