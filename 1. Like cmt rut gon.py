		# Like video
		# driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').click()
		# sleep(3)

		# Like comment top
		# driver.find_elements_by_id('like-button')[1].click()
		# sleep(2)

		# Chọn kênh
		# driver.find_elements_by_id('channel-title')[2].click()
		# sleep(0.5)
		# driver.find_element_by_id('img').click()
		# sleep(0.5)
		# driver.find_elements_by_id('right-icon')[3].click()
		# sleep(0.5)
		# driver.find_elements_by_id('channel-title')[3].click()



from selenium import webdriver
from time import sleep
from tkinter import *
from tkinter import ttk				#Thư viện khai báo combobox
import random
from pathlib import Path

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

root = Tk()
root.wm_title("Cún đáng yêu 💘💘 ")
root.geometry('480x480')
# Group1 Frame --------------------------------------------Tạo 1 khung chung
group1 = LabelFrame(root, text="Youtube community", padx=5, pady=5)
group1.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

key=""



def Action_cmt():
	# chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
	ser=Service(ChromeDriverManager().install())		# hàm đưa ra vị trí file chromedriver.exe

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("detach", True)	# Giữ chrome luôn mở
	chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])	# Tắt thông báo chrome đang bị điều khiển

	# prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
	# chrome_options.add_experimental_option("prefs",prefs)
	chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
	chrome_options.add_argument(r'--profile-directory=Profile 9')
	# driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
	driver = webdriver.Chrome(service=ser, options=chrome_options)

	current_url = etr_link_cmt.get()
	driver.get(etr_link_cmt.get())
	sleep(2)
	#driver.execute_script("window.scrollTo(0, 100);")
	#sleep(2)


	for i in range(0,10):
		random_decimal_1 = random.randint(110,130)/100
		random_decimal_2 = random.randint(50,60)/100
		if i ==0:
			# driver.find_element_by_id('img').click()		# Đã bị loại bỏ
			driver.find_element(By.ID, 'img').click()
			sleep(random_decimal_2)
			# driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
			driver.find_elements(By.ID, 'right-icon')[2].click()
			sleep(random_decimal_2)
			# driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
			driver.find_elements(By.ID, 'contentIcon')[i+1].click()
			sleep(random_decimal_1)
			# driver.find_elements_by_id(key)[1].click()
			driver.find_elements(By.ID, key)[1].click()
			sleep(0.5)
		else:
			# driver.find_element_by_id('img').click()
			driver.find_element(By.ID, 'img').click()
			sleep(random_decimal_2)
			# driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
			driver.find_elements(By.ID, 'right-icon')[2].click()
			sleep(random_decimal_2)
			# driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
			driver.find_elements(By.ID, 'contentIcon')[i].click()
			sleep(random_decimal_1)
			# driver.find_elements_by_id(key)[1].click()
			driver.find_elements(By.ID, key)[1].click()
			sleep(0.5)

	sleep(3)
	driver.quit()

def Vote_cmt():
	global key
	key="like-button"
	Action_cmt()
def Diss_cmt():
	global key
	key="dislike-button"
	Action_cmt()


lbl_link_cmt = Label(group1, text = "Link comment: ")
lbl_link_cmt.grid(row = 0, column = 0, sticky=W+E)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
etr_link_cmt = Entry(group1, width = 55)
etr_link_cmt.grid(row = 1, column = 0, sticky=W)


# Group2 Frame ----------------------------------------------------
group2 = LabelFrame(root, text="Action", padx=5, pady=5)
group2.grid(row=0, column=2, padx=10, pady=10, sticky=E+W+N+S)


btn_like = Button(group2,text="Like", command=Vote_cmt, height=1)	#columnspan là độ rộng của nút
btn_like.grid(row=0, column=2, columnspan=1, sticky = W+E)			#Căn đều ra giữa

btn_diss_like = Button(group2,text="Diss Like", command=Diss_cmt, height=1)			#columnspan là độ rộng của nút
btn_diss_like.grid(row=1, column=2, columnspan=1, sticky = W+E)			#Căn đều ra giữa


root.mainloop()