#!/usr/bin/python
#Filename: contacter_list.py

import cPickle as p
import os
import sys


filename='addressbook.data'

class member:
	def __init__(self,name,address,tel):
		self.name=name
		self.address=address
		self.tel=tel

def update():
	running=True
	while running:
		s=raw_input('\nPlease input name ,address, tel like this:\n\
	xiaoming,xiaoming@gmail.com,13888888888\n')
		if len(s)==0:
			print'\nError!Empty input!!!\n'
		else:
			running=False
	else:
		s1=s.split(',')
		pp=member(s1[0],s1[1],s1[2])
		f=file(filename)
		conlist=p.load(f)
		conlist[pp.name]=pp.address+','+pp.tel
		f=file(filename,'w')
		p.dump(conlist, f)
		f.close()
		del conlist
	
		#print again
		f=file(filename)
		conlist=p.load(f)
		print conlist

def delete():
	f=file(filename)
	conlist=p.load(f)
	print conlist
	d=raw_input("\nPlease input the persion's name you want to delete-->")
	if conlist.has_key(d): # Or if d in conlist
		del conlist[d]
		print conlist
		f=file(filename, 'w')
		p.dump(conlist, f)
		f.close
		del conlist
	else:
		print"\nNo '%s' found!!!\n" % d

def select():
	f=file(filename)
	conlist=p.load(f)
	print conlist
	s=raw_input('\nPlease input the name which you want to select-->')
	if s in conlist:
		print s,':',conlist[s]
	else:
		print"\nNo '%s' found !!!\n" % s

def main():
	while True:
		meu=raw_input('option provided:\n	1:query\n	2:\
add/modify\n	3:delete\n	x:quit\n------>')
		if meu=='1':
			select()
		elif meu=='2':
			update()
		elif meu=='3':
			delete()
		elif meu=='x':
			sys.exit()
		else:
			print "Don't have this option, please try again!"

if os.path.exists('addressbook.data'):
	main()
else:
	f=file('addressbook.data','w')
	conlist={'yaoming':'ming.yao@intel.com,15230650876'}
	p.dump(conlist, f)
	f.close()
	del conlist
	main()

