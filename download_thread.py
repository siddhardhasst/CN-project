# Authors : Jayaprakash A. Polu Varshith, SST Siddhardha
# Purpose : Computer-Networks-project
# Faculty : Dr. Piyush Kurur
# Download thread

import threading
import time
from threading import Thread
from urllib.request import *
from urllib.error import *

def download_file(start, size, download_object, item_no):
	try:
		req = Request(download_object.url_link, headers={'Range':'bytes=%s-%s'%(start, start + size)})
		download_object.data[item_no] = bytes(urlopen(req).read())

	except (HTTPError, URLError) as error:
		print('Data of %s not retrieved because %s\nURL: %s', download_object.file_name, error, download_object.url_link)
	except timeout:
		print('socket timed out - URL %s', download_object.url_link)
	except:
		print("Something's wrong")
	else:
		pass

def resume_download(start, end, d, i, a):
	req = Request(d.url_link, headers={'Range':'bytes=%s-%s'%(start,end)})
	a += bytes(urlopen(req).read())
	d.data[i] = a



class download_thread(Thread):
	def __init__(self, download, arg) :
		Thread.__init__(self, target=download, args = arg)
		self.state = threading.Condition()

	def run(self):
		Thread.run(self)
		
	def kill(self):
	        Thread.kill(self)
	        
	def pause(self):
	        with self.state:
	                self.paused = True
	                
	
	def resume(self):
	        with self.state:
	                self.paused = False
	                self.state.notify()  # unblock self if waiting
