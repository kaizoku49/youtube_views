import time

# Changed the method of opening the browser.
# Selenium allows for the page to be refreshed.
from selenium import webdriver

# adding ability to change number of repeats
count = int(input("Number of times to be repeated: "))
# Same as before
url = input("Enter the URL : ")
print("view Length of video:")
minutes = int(input("View Minutes "))
seconds = int(input("View Seconds "))

# Calculating the refreshrate from the user input
refreshrate = minutes * 60 + seconds
# Selecting Firefox as the browser
driver = webdriver.Firefox()
if url.startswith("https://"):
    driver.get(url)
else:
    driver.get("https://" + url)

for i in range(count):
    # Sets the page to refresh at the refreshrate.
    time.sleep(refreshrate)
    driver.refresh()
