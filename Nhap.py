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

	# for i in range(0,10):
		
	# 	random_decimal_1 = random.randint(110,130)/100
	# 	random_decimal_2 = random.randint(50,60)/100
	# 	if i ==0:
	# 		driver.find_element_by_id('img').click()
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
	# 		sleep(random_decimal_1)
	# 		driver.find_elements_by_id(key)[1].click()
	# 		sleep(random_decimal_1)
	# 	else:
	# 		driver.find_element_by_id('img').click()
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
	# 		sleep(random_decimal_2)
	# 		driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
	# 		sleep(random_decimal_1)
	# 		driver.find_elements_by_id(key)[1].click()
	# 		sleep(random_decimal_1)

	# user_path=""
	# # Trả về tên các thư mục trong Forder: Profile chrome
	# folders_profile_chrome = os.listdir(os.getcwd() + '\\Profile chrome\\')
	# #print(folders_profile_chrome)

from selenium import webdriver
from time import sleep
from tkinter import *
# Thư viện khai báo combobox
from tkinter import ttk
import random

# Thư viện hàm lấy đường dẫn thư mục hiện hành
# import os
# Thư viện lấy hàm đường dẫn thư mục gốc
from pathlib import Path

root = Tk()
root.wm_title("❤ Mai mông to ❤")
root.geometry('480x480+1000+350')

#key=""
#user_path=""

def program(key):							# Biến key nằm trong hàm Action_cmt(driver,key) mà vẫn truyền được >.<
	for i in range(9,15):
		try:
			profile_number='Profile'+' '+str(i)
			print(profile_number)
			chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
			chrome_options = webdriver.ChromeOptions()

			#chrome_options.add_argument(r"--user-data-dir=D:\An Huy\My Project Offline\YTB comunity\User Data")
			chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
			chrome_options.add_argument(r'--profile-directory='+profile_number)
			#Chế độ chạy ẩn_ ko thấy like được
			#chrome_options.headless = True
			driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)

			sleep(1)
			current_url = etr_link_cmt.get()
			driver.get(current_url)
			sleep(2)

			Action_cmt(driver,key)
			driver.quit()
			sleep(1.5)
		except:
			driver.quit()
	lbl_link_cmt.configure(text="SUCCESS!")

def Action_cmt(driver,key):
	# #chrome_driver_path = r'C:\Users\Huy\Desktop\Backup\Python\My project\driver\chromedriver.exe'
	# # Lấy đường dẫn thư mục gốc của file py
	# chrome_driver_path = str(Path().absolute()) + '\\driver\\chromedriver.exe'	# Dòng lệnh này trả về kết quả là đường dẫn chỉ có 1 dấu " \ "
	# #print(chrome_driver_path)
	# chrome_options = webdriver.ChromeOptions()
	# #prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
	# #chrome_options.add_experimental_option("prefs",prefs)


	# # #chrome_options.add_argument("user-data-dir=C:\\Users\\Huy\\Desktop\\Backup\\Python\\My project\\Profile chrome\\Profile chrome 1") # ko thêm r phía trước được. Ko chọn đc profile, mở profile gần nhất
	# # chrome_driver_dir = str(Path().absolute()) + '\\Profile chrome\\Profile chrome 1'
	# # print(chrome_driver_dir)
	# # chrome_options.add_argument('user-data-dir='+chrome_driver_dir)
	# # # Ghép vào thành chuỗi "user-data-dir=C:\Users\Huy\Desktop\Backup\Python\My project\Profile chrome\Profile chrome 1"
	# # print('user-data-dir='+chrome_driver_dir)

	# #chrome_options.add_argument(user_path)
	# chrome_options.add_argument(r"--C:\Users\Huy\AppData\Local\Google\Chrome\User Data")
	# chrome_options.add_argument(r'--profile-directory='+Profile_number)



	# driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
	# current_url = etr_link_cmt.get()
	# driver.get(etr_link_cmt.get())
	# sleep(2)
	# #driver.execute_script("window.scrollTo(0, 100);")
	# #sleep(2)


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
				#print("Không hiện List account, đóng trình duyệt sau 5s")
				sleep(5)
				driver.quit()
			try:
				driver.find_elements_by_id('contentIcon')[i+1].click()		# Click vào từng acc
			except IndexError:
				sleep(2)
				driver.find_elements_by_id('contentIcon')[i+1].click()
			sleep(random_decimal_1)
			driver.find_elements_by_id(key)[1].click()
			sleep(random_decimal_3)
		elif i == 10:
			driver.find_element_by_id('img').click()
			sleep(random_decimal_3)
			try:
				driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
				sleep(random_decimal_2)
			except:
				#print("Không hiện List account, đóng trình duyệt sau 5s")
				sleep(5)
				driver.quit()
			try:
				driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
			except IndexError:
				sleep(2)
				driver.find_elements_by_id('contentIcon')[i].click()
			sleep(random_decimal_1)
			try:
				driver.find_elements_by_id(key)[1].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id(key)[1].click()				# Tài khoản cuối cùng ko có thời gian chờ
		else:
			driver.find_element_by_id('img').click()
			sleep(random_decimal_3)
			try:
				driver.find_elements_by_id('right-icon')[3].click()			# Click vào chuyển acc
				sleep(random_decimal_2)
			except:
				#print("Không hiện List account, đóng trình duyệt sau 5s")
				sleep(5)
				driver.quit()
			try:
				driver.find_elements_by_id('contentIcon')[i].click()		# Click vào từng acc
			except IndexError:
				sleep(2)
				driver.find_elements_by_id('contentIcon')[i].click()
			sleep(random_decimal_1)
			try:
				driver.find_elements_by_id(key)[1].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id(key)[1].click()
			sleep(random_decimal_3)


def program_2(key):
	for i in range(9,15):
		try:
			profile_number='Profile'+' '+str(i)
			print(profile_number)
			chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
			chrome_options = webdriver.ChromeOptions()

			#chrome_options.add_argument(r"--user-data-dir=D:\An Huy\My Project Offline\YTB comunity\User Data")
			chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
			chrome_options.add_argument(r'--profile-directory='+profile_number)
			#Chế độ chạy ẩn_ ko thấy like được
			#chrome_options.headless = True
			driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)

			sleep(1)
			current_url = etr_link_cmt_2.get()
			driver.get(current_url)
			sleep(2)

			Action_cmt_2(driver,key)
			driver.quit()
			sleep(1.5)
		except:
			driver.quit()
	lbl_link_cmt_2.configure(text="SUCCESS!")

def Action_cmt_2(driver,key):
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

			like_nhieu_cmt(driver,key,y)
			sleep(random_decimal_3)
		elif i ==10:
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

			like_nhieu_cmt(driver,key,y)		# Tài khoản thứ 10 ko có thời gian chờ
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

			like_nhieu_cmt(driver,key,y)								# Chú ý thứ tự biến phải giống hàm khai báo bên dưới
			sleep(random_decimal_3)

def like_nhieu_cmt(driver,key,y):
	diss_number = int(cbx_test_1.get())	+ 1			# Dữ liệu đổ vào là int nhưng lấy ra vẫn là str
	for j in range(1,diss_number + 1):
		random_decimal_4 = random.randint(60,80)/100
		if j == 1 and key == "like-button": 
			try:
				driver.find_elements_by_id(key)[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id(key)[j].click()
			finally:
				sleep(random_decimal_4)
		elif j == 1 and key == "dislike-button": 
			pass
		elif j ==diss_number:
			try:
				driver.find_elements_by_id("dislike-button")[j].click()
			except IndexError:
				sleep(2)
				driver.find_elements_by_id("dislike-button")[j].click()		# Lượt like cuối cùng ko có thời gian chờ
		elif j ==5:
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


def open_browser():
	try:
		chrome_driver_path = str(Path().absolute()) + '\\driver offline\\chromedriver.exe'
		chrome_options = webdriver.ChromeOptions()
		#chrome_options.add_argument('user-data-dir=C:\\Users\\Huy\\AppData\\Local\\Google\\Chrome\\User Data') # ko thêm r phía trước được. Ko chọn đc profile, mở profile gần nhất
		# prefs = {"profile.default_content_setting_values.notifications" : 2, "profile.default_content_setting_values.images" : 2}	#Gộp lại để vừa tắt thông báo vừa tắt ảnh
		# chrome_options.add_experimental_option("prefs",prefs)
		chrome_options.add_argument(r'--user-data-dir='+ str(Path().absolute())+'\\User Data 1')
		chrome_options.add_argument(r'--profile-directory='+cbx_test_2.get())
		driver2 = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
		sleep(1)
		driver2.get("https://www.youtube.com/")
		time_value=int(lbl_time_value_2.get())
		sleep(time_value)
		driver2.quit()
	except ValueError:
		driver2.quit()

	# else:
	# 	print("Thực hiện nếu không phát sinh lỗi trong khối try")
	# finally:
	# 	print("Luôn thực hiện dù trong khối try có phát sinh lỗi hay không")


def Like_cmt():
	# global key
	# key="like-button"
	# program()
	program("like-button")
def Diss_cmt():
	# global key
	# key="dislike-button"
	# program()
	program("dislike-button")

def Like_cmt_2():
	program_2("like-button")
def Diss_cmt_2():
	program_2("dislike-button")


# Group1 Frame ----------------------------------------------------------------
group1 = LabelFrame(root, text="Youtube community", padx=5, pady=5)
group1.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

lbl_link_cmt = Label(group1, text = "Link comment: ")		# Mỗi 1 group vị trí lại tính về 00
lbl_link_cmt.grid(row = 0, column = 0, sticky=W+E)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
etr_link_cmt = Entry(group1, width = 55)
etr_link_cmt.grid(row = 1, column = 0, sticky=W)

# Group2 Frame ------------------------------------------------------------------
group2 = LabelFrame(root, text="Action", padx=5, pady=5)
group2.grid(row=0, column=1, padx=10, pady=10, sticky=E+W+N+S)

btn_like = Button(group2,text="Like", command=Like_cmt, height=1)	#columnspan là độ rộng của nút
btn_like.grid(row=0, column=0, columnspan=1, sticky = W+E)			#Căn đều ra giữa
btn_diss_like = Button(group2,text="Diss Like", command=Diss_cmt, height=1)
btn_diss_like.grid(row=1, column=0, columnspan=1, sticky = W+E)			#Căn đều ra giữa

# Group3 Frame ------------------------------------------------------------------------------
group3 = LabelFrame(root, text="Youtube community Pro", padx=5, pady=5)
group3.grid(row=1, column=0, padx=10, pady=10, sticky=E+W+N+S)

lbl_link_cmt_2 = Label(group3, text = "Pase Link")
lbl_link_cmt_2.grid(row = 0, column = 0, sticky=W)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
etr_link_cmt_2 = Entry(group3, width = 45 )						# Entry ko có thông số columspan và height
etr_link_cmt_2.grid(row = 1, column = 0, sticky=W)

lbl_time_value_1 = Label(group3, text = "Number")
lbl_time_value_1.grid(row = 0, column = 1, sticky=E+W+N+S)
list_number = [1,2,3,4,5,6]
cbx_test_1 = ttk.Combobox(group3, values=list_number, width = 8,state="readonly")		#Chỉ có thể chọn trong danh sách, ko thể điền 
cbx_test_1.current(2)
cbx_test_1.grid(row = 1, column = 1, sticky=W+N)

# Group4 Frame ------------------------------------------------------------------
group4 = LabelFrame(root, padx=5, pady=5)
group4.grid(row=1, column=1, padx=10, pady=10, sticky=E+W+N+S)

btn_like_2 = Button(group4,text="Up", command=Like_cmt_2, height=1)	#columnspan là độ rộng của nút
btn_like_2.grid(row=0, column=0, columnspan=1, sticky = E+W)			#Căn đều ra giữa
btn_diss_like_2 = Button(group4,text="Down...!", command=Diss_cmt_2, height=1)
btn_diss_like_2.grid(row=1, column=0, columnspan=1, sticky = E+W)			#Căn đều ra giữa

# Group5 Frame --------------------------------------------------------------------------------------
group5 = LabelFrame(root, text="Open browser", padx=5, pady=5)
group5.grid(row=2, column=0, padx=10, pady=10, sticky=E+W+N+S)

list_profile = ['Profile 9', 'Profile 10', 'Profile 11','Profile 12','Profile 13','Profile 14']
cbx_test_2 = ttk.Combobox(group5, values=list_profile, width = 20,state="readonly")		#Chỉ có thể chọn trong danh sách, ko thể điền 
cbx_test_2.current(0)
cbx_test_2.grid(row = 0, column = 0, sticky=W+N)

lbl_time_value_2 = Label(group5, text = "Time Value: ")
lbl_time_value_2.grid(row = 0, column = 1, sticky=E+W+N+S)
lbl_time_value_2 = Entry(group5, width = 10)
lbl_time_value_2.grid(row = 0, column = 2, sticky=E)

btn_open = Button(root,text="Open", command=open_browser, width = 6, height=1)
btn_open.grid(row=2, column=1, columnspan=2)


#-----------------------------------------------------------------------------
def showMenu2(event):
    # global clickedWidget							# Dùng khi copy theo vùng bôi đen
    # clickedWidget = event.widget
    popup2.post(event.x_root, event.y_root)
def copy2():
    #val = clickedWidget.selection_get()			# Copy theo vùng bôi đen
    etr_link_cmt_2.select_range(0,END)
    url_cmt = etr_link_cmt_2.get()
    root.clipboard_clear()
    root.clipboard_append(url_cmt)
def paste2():
	url_cmt = root.clipboard_get()
	etr_link_cmt_2.delete(0,END)
	etr_link_cmt_2.insert(0,url_cmt)
	return									# Ko chắc tác dụng của dòng này
def delete2():
	etr_link_cmt_2.delete(0,END)

popup2 = Menu(root, tearoff = 0)
popup2.add_command(label ="Paste", command=paste2)
popup2.add_command(label ="Copyyyyyyyyy", command=copy2)
popup2.add_separator()
popup2.add_command(label ="Delete",command=delete2)
etr_link_cmt_2.bind("<Button-3>", showMenu2)


#--------------------------------------------------------------------------------
def showMenu(event):
    # global clickedWidget							# Dùng khi copy theo vùng bôi đen
    # clickedWidget = event.widget
    popup.post(event.x_root, event.y_root)
def copy():
    #val = clickedWidget.selection_get()			# Copy theo vùng bôi đen
    etr_link_cmt.select_range(0,END)
    url_cmt = etr_link_cmt.get()
    root.clipboard_clear()
    root.clipboard_append(url_cmt)
def paste():
	url_cmt = root.clipboard_get()
	etr_link_cmt.delete(0,END)
	etr_link_cmt.insert(0,url_cmt)
	return									# Ko chắc tác dụng của dòng này
def delete():
	etr_link_cmt.delete(0,END)

popup = Menu(etr_link_cmt, tearoff = 0)
popup.add_command(label ="Paste", command=paste)
popup.add_command(label ="Copy", command=copy)
popup.add_separator()
popup.add_command(label ="Delete",command=delete)
etr_link_cmt.bind("<Button-3>", showMenu)


#--------------------------------------------------------------------------------

root.mainloop()