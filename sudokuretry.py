#!/usr/bin/env python
from copy import deepcopy
import sys
import logging
sys.setrecursionlimit(1750000)  # set the maximum depth as 1500
class Backcondition(Exception):
    pass
class Forwardcondition(Exception):
    pass
class sudoku:
    def __init__(self):
	self.value = [0]
	self.block = []
	self.sudokudata = []
#	for i in range(9):
#	    self.value.append(0)
        for i in range(9):
	    self.block.append(deepcopy(self.value))
        for i in range(9):
	    self.sudokudata.append(deepcopy(self.block))
	logging.basicConfig(level=logging.INFO, filename='logfile.txt')
#get sudoku value at (blockid, valueid)

    def get_value(self, blockid, valueid):
	return self.sudokudata[blockid-1][valueid-1]

#clean sudoku value
    def clean_value(self, blockid, valueid):
	tmplist = self.get_value(blockid, valueid)
	length = len(tmplist)
	for num in range(length-1):
	    del tmplist[0]
#get sudoku row data at rowid
    def get_row(self, rowid):
	rowid = rowid - 1
	row = []
	for group in range(9):
#	    print 'block = ',(rowid/3)*3+(group/3)
#	    print 'key = ',(rowid%3)*3 + (group%3)
	    row.append(self.get_value((rowid/3)*3+(group/3)+1,(rowid%3)*3 +(group%3)+1)) 
	return row

#get sudoku column data at columnid
    def get_column(self, columnid):
	columnid = columnid - 1
	column = []
	for group in range(9):
#	    print 'block = ',(columnid/3)+(group/3)*3
#	    print 'key = ',(columnid%3)+(group%3)*3
	    column.append(self.get_value((columnid/3)+(group/3)*3+1, (columnid%3)+(group%3)*3+1))
	return column

#get sudoku block data at blockid
    def get_block(self, blockid):
	return self.sudokudata[blockid-1]

#check data whether have same data[1~9]
    def check_samedata(self, checklist): 
	check = []
	for i in range(9):
	    check.append(checklist[i][0])
#	print check
	for element in range(1, 10):
	    if check.count(element)>1:
		return False
	return True

#set sudoku value and check whether has same value
    def set_value(self, blockid, valueid, value):
	if((value > 9)or(value < 0)):
	    logging.info('error value')
	    return False
	self.get_value(blockid, valueid).insert(0, value)
	if not self.check_samedata(self.get_block(blockid)):
	    logging.info('different block')
	    return False
	rowid = ((blockid-1)/3)*3 + ((valueid-1)/3) + 1
	columnid = ((blockid-1)%3)*3 + ((valueid-1)%3) + 1
#	print 'rowid = ', rowid
#	print 'columnid = ', columnid
	if not self.check_samedata(self.get_row(rowid)):
	    logging.info('different row')
	    return False

	if not self.check_samedata(self.get_column(columnid)):
	    logging.info('different columnid')
	    return False
	return True
#allvalue print 
    def allvalue_print(self):
	print '*************************************'
	for i in range(1, 10):
	    print self.get_row(i)
	print '*************************************'
#standard print
    def standard_print(self):
	tmplist = []
	print '#####################################'
	for i in range(1, 10):
	    for j in range(9):
		tmplist.append(self.get_row(i)[j][0])
	    print tmplist
	    for j in range(9):
	    	del tmplist[0]
	print '#####################################'


    def set_auto(self):
	blockid = 1
	valueid = 1
	pos = {}
	pos['block'] = blockid
	pos['value'] = valueid
	mirror = deepcopy(self)
	def get_nextvalue(blockid, valueid):
	    try:
		for difdata in range(1, 10):
		    if self.get_value(blockid, valueid).count(difdata) == 0:
			yield difdata
	    except: pass
	    else:
	    	raise Backcondition
	    finally: pass
	def auto_forward(pos):
	    pos['value'] = pos['value'] + 1
	    if pos['value'] == 10:
		pos['block'] = pos['block'] + 1
		pos['value'] = 1
	    mirrorvalue = mirror.get_value(pos['block'], pos['value'])
	    if mirrorvalue[0]:
		auto_forward(pos)

	def auto_back(pos):
	    pos['value'] = pos['value'] - 1
	    if pos['value'] == 0:
		pos['block'] = pos['block'] - 1
		pos['value'] = 9
	    mirrorvalue = mirror.get_value(pos['block'], pos['value'])
	    if mirrorvalue[0]:
		auto_back(pos)

	def auto_getstartpos(pos):
	    mirrorvalue = mirror.get_value(pos['block'], pos['value'])
	    if mirrorvalue[0]:
		pos['value'] = pos['vlaue'] + 1
		if pos['value'] == 10:
		    pos['block'] = pos['block'] + 1
		    pos['value'] = 1
		auto_getstartpos(pos)

	def add_value(blockid, valueid):
	    logging.info('blockid = %d, valueid = %d', blockid, valueid)
	    try:
		for num in get_nextvalue(blockid, valueid):
		    if self.set_value(blockid, valueid, num):
			logging.info('True, value = %d', num)
			raise Forwardcondition
		    else:
			logging.info('False, value = %d', num)
	    except Backcondition:
		logging.info('<<<<<<<<<<<<<<<<<<<')
		self.clean_value(blockid, valueid)	
		if (blockid == 1)and(valueid  == 1):
		    print 'no result'
		    return False
		auto_back(pos)
		blockid = pos['block']
		valueid = pos['value']
		add_value(blockid, valueid)

	    except Forwardcondition:
		logging.info('>>>>>>>>>>>>>>>>>>')
		if(blockid == 9)and(valueid == 9):
		    print 'right result:'
		    self.standard_print()
		    return True
		auto_forward(pos)
		blockid = pos['block']
		valueid = pos['value']
		add_value(blockid, valueid)

	    finally: pass
	auto_getstartpos(pos)
	blockid = pos['block']
	valueid = pos['value']
	add_value(blockid, valueid)
sudokutest = sudoku()
sudokutest.set_value(1,3,9)
sudokutest.set_value(1,4,5)
sudokutest.set_value(1,7,8)

sudokutest.set_value(2,1,7)
sudokutest.set_value(2,6,2)
sudokutest.set_value(2,8,1)

sudokutest.set_value(3,4,7)
sudokutest.set_value(3,6,9)
sudokutest.set_value(3,9,6)

sudokutest.set_value(4,3,1)
sudokutest.set_value(4,7,7)
sudokutest.set_value(4,9,6)

sudokutest.set_value(5,1,6)
sudokutest.set_value(5,5,4)
sudokutest.set_value(5,9,8)

sudokutest.set_value(6,1,4)
sudokutest.set_value(6,3,5)
sudokutest.set_value(6,7,2)

sudokutest.set_value(7,1,4)
sudokutest.set_value(7,4,6)
sudokutest.set_value(7,6,2)

sudokutest.set_value(8,2,9)
sudokutest.set_value(8,4,3)
sudokutest.set_value(8,9,7)

sudokutest.set_value(9,3,8)
sudokutest.set_value(9,6,4)
sudokutest.set_value(9,7,9)

sudokutest.standard_print()
sudokutest.set_auto()
#print sudokutest.sudokudata


