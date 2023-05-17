from selenium import webdriver
from time import sleep
from pathlib import Path
import random

chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
# chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.add_argument('user-data-dir=C:\\Users\\Huy\\AppData\\Local\\Google\\Chrome\\User Data') # ko thêm r phía trước được. Ko chọn đc profile, mở profile gần nhất
chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
chrome_options.add_argument(r'--profile-directory=Profile 9')
# chrome_options.add_argument(r'--profile-directory='+cbx_test.get())
driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)

sleep(1)
driver.get("https://www.youtube.com/channel/UC_jQ64mgxDbvATLv94lMwaw/community?lc=UgxrwmJHfD_TB8op0FZ4AaABAg&lb=Ugz1drCNit5UHQIAAGJ4AaABCQ")
sleep(2)

for i in range(0,10):
	random_decimal_1 = random.randint(110,130)/100
	random_decimal_2 = random.randint(50,60)/100
	random_decimal_3 = random.randint(20,30)/100

	if i ==0:
		driver.find_element_by_id('img').click()
		sleep(random_decimal_3)
		try:
			driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
			sleep(random_decimal_2)
		except:
			print("Không hiện danh sách acc, đóng trình duyệt sau 5s")
			sleep(5)
			driver.quit()
		try:
			driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
		except IndexError:
			sleep(3)
			driver.find_elements_by_id('contentIcon')[i+1].click()
		sleep(random_decimal_1)
		driver.find_elements_by_id("like-button")[1].click()			# Click 1 lần
		sleep(random_decimal_3)
	else:
		driver.find_element_by_id('img').click()
		sleep(random_decimal_3)
		try:
			driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
			sleep(random_decimal_2)
		except:
			print("Không hiện danh sách acc, đóng trình duyệt sau 5s")
			sleep(5)
			driver.quit()
		try:
			driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
		except IndexError:
			sleep(3)
			driver.find_elements_by_id('contentIcon')[i].click()
		sleep(random_decimal_1)
		try:
			driver.find_elements_by_id("like-button")[1].click()		# Click 2 lần
		except IndexError:
			sleep(3)
			driver.find_elements_by_id("like-button")[1].click()
		sleep(random_decimal_3)
driver.quit()
