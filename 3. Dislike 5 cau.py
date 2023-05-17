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
driver.get("https://www.youtube.com/channel/UC4-eGDvOe41__-RiE0E9L6A/community?lc=UgxHD7DzIpdpPd3z3-F4AaABAg&lb=Ugx2nDtM5G6Mwk-8wZB4AaABCQ")
sleep(2)

diss_number=4



def like_nhieu_cmt(key,y):
	for j in range(1,diss_number + 1):
		random_decimal_4 = random.randint(60,80)/100
		if j == 1: 
			try:
				driver.find_elements_by_id(key)[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id(key)[j].click()
			finally:
				sleep(random_decimal_4)
		elif j ==diss_number:
			try:
				driver.find_elements_by_id("dislike-button")[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id("dislike-button")[j].click()		# Lượt like cuối cùng ko có thời gian chờ
		elif j ==4:
			y += 350
			driver.execute_script("window.scrollTo(0, "+str(y)+");")
			sleep(random_decimal_4)
			try:
				driver.find_elements_by_id("dislike-button")[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id("dislike-button")[j].click()
			finally:
				sleep(random_decimal_4)
		else:
			try:
				driver.find_elements_by_id("dislike-button")[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id("dislike-button")[j].click()
			finally:
				sleep(random_decimal_4)



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
			sleep(2)
			driver.find_elements_by_id('contentIcon')[i+1].click()
		finally:
			sleep(random_decimal_1)
		# driver.execute_script("window.scrollTo(0, 300);")
		y= driver.find_elements_by_id("like-button")[0].location['y']-100	# Đéo hiểu sao lại là phần tử 0
		driver.execute_script("window.scrollTo(0, "+str(y)+");")
		sleep(random_decimal_2)

		like_nhieu_cmt("like-button",y)

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
			sleep(2)
			driver.find_elements_by_id('contentIcon')[i].click()
		finally:
			sleep(random_decimal_1)
		# driver.execute_script("window.scrollTo(0, 300);")
		y= driver.find_elements_by_id("like-button")[0].location['y']-100	# Đéo hiểu sao lại là phần tử 0
		driver.execute_script("window.scrollTo(0, "+str(y)+");")
		sleep(random_decimal_2)

		like_nhieu_cmt("like-button",y)

		sleep(random_decimal_3)
driver.quit()