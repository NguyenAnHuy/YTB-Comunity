from selenium import webdriver
from time import sleep
from pathlib import Path
import random

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

ser=Service(ChromeDriverManager().install())		# hàm đưa ra vị trí file chromedriver.exe
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)	# Giữ chrome luôn mở
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])	# Tắt thông báo chrome đang bị điều khiển

# prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
# chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
chrome_options.add_argument(r'--profile-directory=Profile 9')
driver = webdriver.Chrome(service=ser, options=chrome_options)

sleep(1)
url='https://www.youtube.com/channel/UCilwZiBBfI9X6yiZRzWty8Q/community?lc=UgyAgS2ABGhPEwTYWd54AaABAg&lb=UgkxiGQCPzk_dRMyZYqZTDB54SHH2zXm1bKx'
driver.get(url)
sleep(2)

diss_number=5



def like_nhieu_cmt(key,y):
	for j in range(1,diss_number + 1):
		random_decimal_4 = random.randint(60,80)/100
		if j == 1: 
			try:
				driver.find_elements(By.ID, key)[j].click()			# Like cmt đầu
			except IndexError:
				sleep(2)
				driver.find_elements(By.ID, key)[j].click()
			finally:
				sleep(random_decimal_4)
		elif j ==diss_number:
			try:
				driver.find_elements(By.ID, 'dislike-button')[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements(By.ID, 'dislike-button')[j].click()		# Lượt like cuối cùng ko có thời gian chờ
		elif j ==4:
			y += 350
			driver.execute_script("window.scrollTo(0, "+str(y)+");")
			sleep(random_decimal_4)
			try:
				driver.find_elements(By.ID, 'dislike-button')[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements(By.ID, 'dislike-button')[j].click()
			finally:
				sleep(random_decimal_4)
		else:
			try:
				driver.find_elements(By.ID, 'dislike-button')[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements(By.ID, 'dislike-button')[j].click()
			finally:
				sleep(random_decimal_4)



for i in range(0,10):
	random_decimal_1 = random.randint(110,130)/100
	random_decimal_2 = random.randint(50,60)/100
	random_decimal_3 = random.randint(20,30)/100

	if i ==0:
		driver.find_element(By.ID, 'img').click()
		sleep(random_decimal_3)
		try:
			driver.find_elements(By.ID, 'right-icon')[2].click()			# Click vào chuyển acc
			sleep(random_decimal_2)
		except:
			print("Không hiện danh sách acc, đóng trình duyệt sau 5s")
			sleep(5)
			driver.quit()
		try:
			driver.find_elements(By.ID, 'contentIcon')[i+1].click()		# Click vào từng acc
		except IndexError:
			sleep(3)
			driver.find_elements(By.ID, 'contentIcon')[i+1].click()
		finally:
			sleep(random_decimal_1)
		# driver.execute_script("window.scrollTo(0, 300);")
		y= driver.find_elements(By.ID, 'like-button')[0].location['y']-100	# Ko hiểu sao lại là phần tử 0
		driver.execute_script("window.scrollTo(0, "+str(y)+");")
		sleep(random_decimal_2)

		like_nhieu_cmt('like-button',y)

		sleep(random_decimal_3)
	else:
		driver.find_element(By.ID, 'img').click()
		sleep(random_decimal_3)
		try:
			driver.find_elements(By.ID, 'right-icon')[2].click()			# Click vào chuyển acc
			sleep(random_decimal_2)
		except:
			print("Không hiện danh sách acc, đóng trình duyệt sau 5s")
			sleep(5)
			driver.quit()
		try:
			driver.find_elements(By.ID, 'contentIcon')[i].click()	# Click vào từng acc
		except IndexError:
			sleep(2)
			driver.find_elements(By.ID, 'contentIcon')[i].click()
		finally:
			sleep(random_decimal_1)
		# driver.execute_script("window.scrollTo(0, 300);")
		y= driver.find_elements(By.ID, 'like-button')[0].location['y']-100	# Ko hiểu sao lại là phần tử 0
		driver.execute_script("window.scrollTo(0, "+str(y)+");")
		sleep(random_decimal_2)

		like_nhieu_cmt("like-button",y)

		sleep(random_decimal_3)
driver.quit()