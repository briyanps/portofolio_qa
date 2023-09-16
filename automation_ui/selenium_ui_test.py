import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self): # ini untuk buka browser dan install sesuai versi browser laptop
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_verify_success_login(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch18@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch18") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID, "signin_login").click() # klik tombol login
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertIn('Welcome', popup_atas)
        self.assertEqual(popup_bawah, 'Anda Berhasil Login')
        
    def test_verify_failed_login_with_email_registered_and_empty_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch18@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # tidak password, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Password tidak boleh kosong')

    def test_verify_failed_login_with_empty_email_and_pass_registered(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # tidak ada email, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch18") # isi password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Email tidak boleh kosong')

    def test_verify_failed_user_not_found(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch50@gmail.com") # isi email""
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch50") # isi password
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, "User's not found")
        self.assertEqual(popup_bawah, 'Email atau Password Anda Salah')

    def test_verify_failed_login_with_empty_email_and_empty_pass(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # tidak ada email, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # tidak ada password, diberi string kosong ""
        time.sleep(1)
        self.browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID,"swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Email & Password tidak boleh kosong')

    def test_verify_login_with_max_char_for_password(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch18@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch1812345678901234567890") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID, "signin_login").click() # klik tombol login
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Email/Password melebihi maksimal karakter')

    def test_verify_login_with_max_char_for_email(self): # test case, awali dengan def test
        # form login
        self.browser.get("https://barru.pythonanywhere.com") # buka situs
        time.sleep(3)
        self.browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("batch1812345678901234567890123456789012345678901234567890@gmail.com") # isi form email
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("batch18") # isi form password
        time.sleep(1)
        self.browser.find_element(By.ID, "signin_login").click() # klik tombol login
        time.sleep(1)

        # pop up
        popup_atas = self.browser.find_element(By.ID, "swal2-title").text # dapetin teks/tulisan pop up atas
        popup_bawah = self.browser.find_element(By.ID,"swal2-content").text # dapetin teks/tulisan pop up bawah
        time.sleep(2)
        
        # validasi
        self.assertEqual(popup_atas, 'Cek Formulir Anda')
        self.assertEqual(popup_bawah, 'Email/Password melebihi maksimal karakter') 

    def tearDown(self): # ini untuk tutup browser
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()