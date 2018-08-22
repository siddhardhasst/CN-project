
import threading
#from main import set_of_downloads
import download_helper
from os import system
from os import path
import os
import threading
import glob
import download_thread
from urllib.request import *
import time

class HeadRequest(Request):
    def get_method(self):
        return "HEAD"




def downNow(d):
	step = d.size//d.no_of_threads
	init= 0
	for i in range(d.no_of_threads-1):
		d.thread_list.append(download_thread.download_thread(download_thread.download_file, (init, step, d, i)))
		init=step+init
		d.thread_list[i].start()
	step = d.size-init
	d.thread_list.append(download_thread.download_thread(download_thread.download_file, (init, step, d, d.no_of_threads-1)))
	d.thread_list[d.no_of_threads-1].start()
	print(os.getcwd())
	os.chdir('./downloads')
	f=open(d.fileName,"ab+")
	#f.close()
	d_size = 0
	for a in range(d.no_of_threads):
		while(d.data[a] == None):
			pass

	#f=open(d.fileName,"ab+")
	while(d_size<d.size):
		d_size = 0
		for a in range(d.no_of_threads):
			d_size += len(d.data[a])
			d.current_size = d_size


	if(d_size>=d.size):
		for i in range(d.no_of_threads):
			f.write(d.data[i])
		print("Download complete")
		#set_of_downloads.remove(d)
	f.close()
	#os.chdir('../')




def init_download(d):
	req = HeadRequest(d.url_link)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	i=0
	l=glob.glob('*')
	d.size = int(size)

#list for data


	if('downloads' not in l):
		os.makedirs('downloads')
	fileType = content.get('Content-Type')
	fileType = fileType.split('/')
	fileNameTemp = d.url_link.split('/')
	fileNameTemp = fileNameTemp[len(fileNameTemp)-1]
	if('.' in fileNameTemp):
		fileName = fileNameTemp
	else:
		fileName = fileNameTemp+'.'+fileType[1]
	d.fileName = fileName



def pause(download_object):
	if('downloads' not in os.getcwd()):
		os.chdir('downloads')
	f = open('.pause_data'+str(download_object.download_id), 'w')
	download_object.pause_file_name = f.name
	for i in range(len(download_object.data)-1):
		#if(download_object.data[i] == None):
		#	print ('k')
		#	pass
		#else:
		try :
			f.write(download_object.data[i])
		except :
			f.write('')
			print ('killing')
			#print((type((download_object.thread_list)[i])))
			(download_object.thread_list)[i].pause()
			f.write('#####ThreadData#####')
	#if(download_object.data[len(download_object.data)-1] == None):
	#	pass
	#else:
	try :
		f.write(download_object.data[len(download_object.data)-1])
	except :
		f.write('')
		print ('killing')
		#f.write(download_object.data[len(download_object.data)-1])
	download_object.paused = 1
	f.close()
	os.chdir('../')

def play(download_object):
	if('downloads' not in os.getcwd()):
		os.chdir('downloads')
	f = open(download_object.pause_file_name,'r')
	a = f.read()
	a.split('#####ThreadData#####')
	download_object.paused = 0
	req = HeadRequest(download_object.url_link)
	response = urlopen(req)
	response.close()
	content=dict(response.headers.items())
	size = content.get('Content-Length')
	step = int(size)//download_object.no_of_threads
	init, i = 0, 0
	l = glob.glob('*')
	if(len(a) == 0):
		downNow(download_object)
	else:
        #list for data
		f=open(download_object.fileName,"ab+")
		download_object.thread_list = []
		for i in range(download_object.no_of_threads-1):
			download_object.thread_list.append(download_thread.download_thread(download_thread.resume_download, (init+len(a[i]), init + step, download_object, i, a[i])))
			init=step+init
			download_object.thread_list[i].start()
		step = int(size)-init
		download_object.thread_list.append(download_thread.download_thread(download_thread.resume_download, (init+len(a[download_object.no_of_threads-1]), init + step, download_object, download_object.no_of_threads-1, a[download_object.no_of_threads-1])))
		download_object.thread_list[download_object.no_of_threads-1].start()
		d_size = 0
		print(download_object.fileName)
		f=open(fileName,"ab+")
		for a in range(download_object.no_of_threads):
			while(download_object.data[a] == None):
				pass

		while(d_size<int(size)):
			d_size = 0
			for a in range(download_object.no_of_threads):
				d_size += len(download_object.data[a])
				d.current_size = d_size

		if(d_size>=int(size)):
			for i in range(download_object.no_of_threads):
				f.write(download_object.data[i])
			print("Download complete after resuming")
		#set_of_downloads.remove(d)
		f.close()
		#os.chdir('../')
