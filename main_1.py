import download_helper
import source
from os import system
from threading import *
down_list= []
while (1):

	print ('Enter 1(Download)\n2(Pause)\n3(resume)\n4(exit)')
	q = int(input('>>'))


	if(q == 1):
		address = input('Enter the url address\n')
		download_object = download_helper.Download_file_object(address, 4)
		if(download_object in down_list):
			print("downloaded_1")
		else:
			down_list.append(download_object)
			source.init_download(download_object)
			#start thread
			t= Thread(target=source.downNow, args = (download_object,))
			t.start()

	elif(q == 2):
		print ('puasing\n')
		i=0
		for down_obj in down_list:
			print (i,down_obj.fileName)
			i += 1
		choice = int(input('Enter your choice no:'))
		if (choice+1 > len(down_list) or (choice < 0)):
			print ('Sorry...entered wromng choice\n')
			continue
		if (down_list[choice].paused==1):
			print ('already paused\n')
			continue
		source.pause(down_list[choice])
		print ('paused\n')
		#.......
	elif(q == 3):
		print ('resuming')
		i=0
		flag = 0
		for down_obj in down_list:
			if (down_obj.paused==1):
				flag=1
				print (i,down_obj.fileName)
			i += 1
		if (flag==0):
			continue
		choice=int(input('Enter your choice no:'))
		if (choice+1 > len(down_list) or (choice < 0)):
			print ('Sorry wrong choice\n')
			continue
		if (down_list[choice].paused!=1):
			print ('already playing\n')
			continue
		source.play(down_list[choice])
		print ("resumed\n")
		#.........
	elif(q == 4):
		break
	else:
		print('Wrong choice')
