from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:
    
    driver.get("https://www.instagram.com/accounts/login/")

   

    username = "your_username"
    password = "your_password"

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

  
    time.sleep(5)

   
    driver.get("https://www.instagram.com/guviofficial/")

    
    time.sleep(5)

    # Use XPath to locate the elements containing the followers and following count
    followers_element = driver.find_element(By.XPATH, "//a[contains(@href,'followers')]/span")
    following_element = driver.find_element(By.XPATH, "//a[contains(@href,'following')]/span")

    # Extract the number of followers and following
    followers_count = followers_element.get_attribute('title')
    following_count = following_element.text

   
    print("Followers:", followers_count)
    print("Following:", following_count)

finally:
   
    driver.quit()