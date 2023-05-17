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

import threading	# Thư viện đa luồng
số_luồng = 2
program_count = 0
number = 0

#key=""
#user_path=""
class MainApp(Tk):
	def __init__(self):
		super(MainApp,self).__init__()
		# Group1 Frame ----------------------------------------------------------------
		self.group1 = LabelFrame(self, text="Youtube community", padx=5, pady=5)
		self.group1.grid(row=0, column=0, padx=10, pady=10, sticky=E+W+N+S)

		self.lbl_link_cmt = Label(self.group1, text = "Link comment: ")		# Mỗi 1 group vị trí lại tính về 00
		self.lbl_link_cmt.grid(row = 0, column = 0, sticky=W+E)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
		self.etr_link_cmt = Entry(self.group1, width = 55)
		self.etr_link_cmt.grid(row = 1, column = 0, sticky=W)

		# Group2 Frame ------------------------------------------------------------------
		self.group2 = LabelFrame(self, text="Action", padx=5, pady=5)
		self.group2.grid(row=0, column=1, padx=10, pady=10, sticky=E+W+N+S)

		self.btn_like = Button(self.group2,text="Like", command=self.Like_cmt, height=1)	#columnspan là độ rộng của nút
		self.btn_like.grid(row=0, column=0, columnspan=1, sticky = W+E)			#Căn đều ra giữa
		self.btn_diss_like = Button(self.group2,text="Diss Like", command=self.Diss_cmt, height=1)
		self.btn_diss_like.grid(row=1, column=0, columnspan=1, sticky = W+E)			#Căn đều ra giữa

		# Group3 Frame ------------------------------------------------------------------------------
		self.group3 = LabelFrame(self, text="Youtube community Pro", padx=5, pady=5)
		self.group3.grid(row=1, column=0, padx=10, pady=10, sticky=E+W+N+S)

		self.lbl_link_cmt_2 = Label(self.group3, text = "Pase Link")
		self.lbl_link_cmt_2.grid(row = 0, column = 0, sticky=W)		#Vị trí của tiêu đề và Căn lề theo phía Tây hay bên trái
		self.etr_link_cmt_2 = Entry(self.group3, width = 45 )						# Entry ko có thông số columspan và height
		self.etr_link_cmt_2.grid(row = 1, column = 0, sticky=W)

		self.lbl_time_value_1 = Label(self.group3, text = "Number")
		self.lbl_time_value_1.grid(row = 0, column = 1, sticky=E+W+N+S)
		self.list_number = [1,2,3,4,5,6]
		self.cbx_test_1 = ttk.Combobox(self.group3, values=self.list_number, width = 8,state="readonly")		#Chỉ có thể chọn trong danh sách, ko thể điền 
		self.cbx_test_1.current(2)
		self.cbx_test_1.grid(row = 1, column = 1, sticky=W+N)

		# Group4 Frame ------------------------------------------------------------------
		self.group4 = LabelFrame(self, padx=5, pady=5)
		self.group4.grid(row=1, column=1, padx=10, pady=10, sticky=E+W+N+S)

		self.btn_like_2 = Button(self.group4,text="Up", command=self.Like_cmt_2, height=1)	#columnspan là độ rộng của nút
		self.btn_like_2.grid(row=0, column=0, columnspan=1, sticky = E+W)			#Căn đều ra giữa
		self.btn_diss_like_2 = Button(self.group4,text="Down...!", command=self.Diss_cmt_2, height=1)
		self.btn_diss_like_2.grid(row=1, column=0, columnspan=1, sticky = E+W)			#Căn đều ra giữa

		# Group5 Frame --------------------------------------------------------------------------------------
		self.group5 = LabelFrame(self, text="Open browser", padx=5, pady=5)
		self.group5.grid(row=2, column=0, padx=10, pady=10, sticky=E+W+N+S)

		self.list_profile = ['Profile 9', 'Profile 10', 'Profile 11','Profile 12','Profile 13','Profile 14']
		self.cbx_test_2 = ttk.Combobox(self.group5, values=self.list_profile, width = 20,state="readonly")		#Chỉ có thể chọn trong danh sách, ko thể điền 
		self.cbx_test_2.current(0)
		self.cbx_test_2.grid(row = 0, column = 0, sticky=W+N)

		self.lbl_time_value_2 = Label(self.group5, text = "Time Value: ")
		self.lbl_time_value_2.grid(row = 0, column = 1, sticky=E+W+N+S)
		self.lbl_time_value_2 = Entry(self.group5, width = 10)
		self.lbl_time_value_2.grid(row = 0, column = 2, sticky=E)

		self.btn_open = Button(self,text="Open", command=self.open_browser, width = 6, height=1)
		self.btn_open.grid(row=2, column=1, columnspan=2)

		self.btn_pause = Button(self,text="Pause", command=self.pause_program)							# Nút pause
		self.btn_pause.grid(row=3, column=1, columnspan=2)


		self.popup = Menu(self.etr_link_cmt, tearoff = 0)
		self.popup.add_command(label ="Paste", command=self.paste)
		self.popup.add_command(label ="Copy", command=self.copy)
		self.popup.add_separator()
		self.popup.add_command(label ="Delete",command=self.delete)
		self.etr_link_cmt.bind("<Button-3>", self.showMenu)

		self.popup2 = Menu(self.etr_link_cmt_2, tearoff = 0)						# Đơn luồng thì dùng root thay cho self.etr_link_cmt_2 được
		self.popup2.add_command(label ="Paste", command=self.paste2)
		self.popup2.add_command(label ="Copy", command=self.copy2)
		self.popup2.add_separator()
		self.popup2.add_command(label ="Delete",command=self.delete2)
		self.etr_link_cmt_2.bind("<Button-3>", self.showMenu2)

	#-----------------------------------------------------------------------------
	def showMenu(self,event):
	    # global clickedWidget							# Dùng khi copy theo vùng bôi đen
	    # clickedWidget = event.widget
	    self.popup.post(event.x_root, event.y_root)
	def copy(self):
	    #val = clickedWidget.selection_get()			# Copy theo vùng bôi đen
	    self.etr_link_cmt.select_range(0,END)
	    self.url_cmt = self.etr_link_cmt.get()
	    self.clipboard_clear()
	    self.clipboard_append(self.url_cmt)
	def paste(self):
		self.url_cmt = self.clipboard_get()
		self.etr_link_cmt.delete(0,END)
		self.etr_link_cmt.insert(0,self.url_cmt)
		return									# Ko chắc tác dụng của dòng này
	def delete(self):
		self.etr_link_cmt.delete(0,END)
	#--------------------------------------------------------------------------------
	def showMenu2(self,event):
	    # global clickedWidget							# Dùng khi copy theo vùng bôi đen
	    # clickedWidget = event.widget
	    self.popup2.post(event.x_root, event.y_root)
	def copy2(self):
	    #val = clickedWidget.selection_get()			# Copy theo vùng bôi đen
	    self.etr_link_cmt_2.select_range(0,END)
	    self.url_cmt = self.etr_link_cmt_2.get()
	    self.clipboard_clear()
	    self.clipboard_append(self.url_cmt)
	def paste2(self):
		self.url_cmt = self.clipboard_get()
		self.etr_link_cmt_2.delete(0,END)
		self.etr_link_cmt_2.insert(0,self.url_cmt)
		return											# Ko chắc tác dụng của dòng này
	def delete2(self):
		self.etr_link_cmt_2.delete(0,END)

#--------------------------------------------------------------------------------
	def Like_cmt(self):
		# global key
		# key="like-button"
		# # program()
		# program("like-button")
		self.key="like-button"
		new_thread = threading.Thread(target=self.start_program)
		new_thread.start()
	def Diss_cmt(self):
		# global key
		# key="dislike-button"
		# program()
		# program("dislike-button")
		self.key="dislike-button"
		new_thread = threading.Thread(target=self.start_program)
		new_thread.start()
	def Like_cmt_2(self):
		# program_2("like-button")
		a=1
	def Diss_cmt_2(self):
		# program_2("dislike-button")
		b=2

#-----------------------------------------------------------------------------------

# # Thêm hàm này để chia luồng trước khi chạy start_program nên ko bị lag giao diện
# 	def start_here(self):
# 		new_thread = threading.Thread(target=self.start_program)
# 		new_thread.start()

	def pause_program(self):
		self.program_running = False

	def start_program(self):
		global number
		self.program_running = True		# Vòng lặp
		self.số_luồng_hiện_tại = 0
		while self.program_running and program_count < 6: # Chương trình dừng lại khi mở hết 6
			if self.số_luồng_hiện_tại == 0:
				for z in range(số_luồng):			# số_luồng đang set là 2
					# Để chạy tối đa 3 luồng thay vì số_luồng = số cookie clone
					# Sau target là phương thức muốn truyền
					new_thread = threading.Thread(target=self.program, args={program_count + z,})
					new_thread.start()
					number += 1
				sleep(3)


	def program(self,z):				# Biến key nằm trong hàm Action_cmt(driver,key) mà vẫn truyền được >.<
		global program_count
		self.số_luồng_hiện_tại += 1
		profile_number='Profile'+' '+str(9+number)
		try:
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
			self.current_url = self.etr_link_cmt.get()
			driver.get(self.current_url)
			print(self.etr_link_cmt.get())
			sleep(5)

			self.Action_cmt(args={driver,})
			driver.quit()
			sleep(1.5)
		except:
			driver.quit()

		program_count += 1
		self.số_luồng_hiện_tại -= 1		# Sau khi 3 luồng bật lên mỗi luồng trừ đi 1
		self.lbl_link_cmt.configure(text="SUCCESS!")

	def Action_cmt(self,driver):
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
				driver.find_elements_by_id(self.key)[1].click()
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
					driver.find_elements_by_id(self.key)[1].click()
				except IndexError:
					sleep(2)
					driver.find_elements_by_id(self.key)[1].click()				# Tài khoản cuối cùng ko có thời gian chờ
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
					driver.find_elements_by_id(self.key)[1].click()
				except IndexError:
					sleep(2)
					driver.find_elements_by_id(self.key)[1].click()
				sleep(random_decimal_3)
	#------------------------------------------------------------------------------------------------------------------
	def program_2(self,key):
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

	def Action_cmt_2(self,driver,key):
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

	def like_nhieu_cmt(self,driver,key,y):
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
	#------------------------------------------------------------------------------------------------
	def open_browser(self):
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


if __name__ == '__main__': 
	main_app = MainApp()
	main_app.wm_title("❤ Mai mông to ❤")
	main_app.geometry('480x480+1000+350')
	main_app.mainloop()