from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.ynet.co.il'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
wait = WebDriverWait(driver, 10)

launchRadioButton = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'ynet-radio-gif-wrapper')))
launchRadioButton.click()
