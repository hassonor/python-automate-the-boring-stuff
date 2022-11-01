from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://ng.ctconnect.co.il/forms/form?f=1a4bef5ac4f724089cfbdff3fa1d4227')
messageField = driver.find_element(By.XPATH, '//*[@id="custom_125825"]')
messageField.send_keys("Hello Even")
phoneField = driver.find_element(By.XPATH, '//*[@id="custom_125826"]')
phoneField.send_keys("0525381648")
emailField = driver.find_element(By.XPATH, '//*[@id="custom_125827"]')
emailField.send_keys("anna.zak@gmail.com")
subjectField = driver.find_element(By.XPATH, '//*[@id="custom_125828"]')
subjectField.send_keys("I want to sing")
captchaField = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')
captchaField.click()
