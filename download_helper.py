# Authors : Jayaprakash A. Polu Varshith, SST Siddhardha
# Purpose : Computer-Networks-Assignment
# Faculty : Dr. Piyush Kurur
# Download object code

import threading
class Download_file_object:
	download_id = 0
	def __init__(self, url_link, no_of_threads):
		if(Download_file_object.download_id < 30):
			self.download_id += 1
		else:
			self.download_id = 0
		self.url_link = url_link
		self.current_size, self.size, self.paused = 0, 0, 0
		self.no_of_threads = no_of_threads
		self.data = []
		self.pause_file_name = 'none'
		for i in range(self.no_of_threads):
			self.data.append(None)
		self.thread_list = []
