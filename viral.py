# # import csv
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # # Initialize the Chrome webdriver
# # driver = webdriver.Chrome()

# # # Base URL of the webpage to scrape
# # base_url = "https://mastodon.social/explore"

# # # Function to scrape data
# # def scrape_data(url):
# #     driver.get(url)
    
# #     # Find all elements with class name "bcCauD" for names
# #     likes = driver.find_elements(By.CLASS_NAME, "icon-button__counter")
# #     for like in likes:
# #         print(like.text)
    
# #     # Find all elements with class name "dJxGwQ" for reviews
# #     # reviews = driver.find_elements(By.CLASS_NAME, "kCCGzy")
# #     names = driver.find_elements(By.CLASS_NAME, "display-name__account")
# #     for name in names:
# #         print(name.text)
    
# #     # # Find all elements with class name "dYrjiw" for order type
# #     # orders = driver.find_elements(By.CLASS_NAME, "dYrjiw")

# #     # #Find all elements with class name "rating" for date
# #     # ratings = driver.find_elements(By.CLASS_NAME, "cILgox")
    
# #     # # Find all elements with class name "time-stamp" for date
# #     # dates = driver.find_elements(By.CLASS_NAME, "time-stamp")
    
# #     # Open the CSV file in write mode with newline='' to prevent extra newline characters
# #     with open(r'C:/Users/ASUS/Desktop/Projects/SimPPL Task/viral.csv', mode='a', newline='', encoding='utf-8') as file:
# #         writer = csv.writer(file)
        
# #         # Write headers if the file is empty
# #         if file.tell() == 0:
# #             writer.writerow(['Name','Likes'])
        
# #         # Iterate through the scraped data and write to CSV
# #         for name, like in zip(names, likes):
# #             writer.writerow([name.text, likes.text])

# # # Start iterating through the links
# # page_number = 1
# # while True:
# #     url = base_url.format(page_number)
# #     driver.get(url)

# # driver.quit()
# #     # Check if the page exists
# #     # try:
# #     #     WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-button__counter")))
# #     #     scrape_data(url)
# #     #     page_number += 1
# #     # except:
# #     #     break

# # # Close the webdriver
# # # driver.quit()
# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the Chrome webdriver
# driver = webdriver.Chrome()

# # Base URL of the webpage to scrape
# base_url = "https://mastodon.social/explore"

# # Function to scrape data
# def scrape_data(url):
#     driver.get(url)
    
#     # Find all elements with class name "icon-button__counter" for names
#     names = driver.find_elements(By.CLASS_NAME, "display-name__html")
#     print("these are nammes")
#     print(names)
#     for name in names:
#         print(name.text)

#     likes = driver.find_elements(By.CLASS_NAME, "icon-button__counter")
#     for like in likes:
#         print(like.text)

#     # Open the CSV file in write mode with newline='' to prevent extra newline characters
#     with open(r'C:/Users/ASUS/Desktop/Projects/SimPPL Task/viral.csv', mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
        
#         # Write headers if the file is empty
#         if file.tell() == 0:
#             writer.writerow(['Name','Likes'])
        
#         # Iterate through the scraped data and write to CSV
#         for name in names:
#             writer.writerow([name.text])

# # Start iterating through the links
# page_number = 1
# while True:
#     url = base_url.format(page_number)
#     driver.get(url)

#     # Check if the page exists
#     try:
#         WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-button__counter")))
#         scrape_data(url)
#         page_number += 1
#     except:
#         break

# # Close the webdriver
# driver.quit()
