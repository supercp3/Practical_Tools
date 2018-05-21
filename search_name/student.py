import xlrd 
import os

def open_table(path):
	try:
		data=xlrd.open_workbook(path)
		return data
	except Exception.e:
		print(str(e))

def read_sheet_by_name(data,name):
	table=data.sheet_by_name(name)
	nrows=table.nrows
	ncols=table.ncols
	return table,nrows,ncols

def sex_num(data,rows):
	n=rows-1
	M_num=0
	for i in range(n):
		if data.row_values(i)[3]=='男':
			M_num+=1
	F_num=n-M_num
	return M_num,F_num

def search_by_index(table,rows):
	for i in range(len(table.row_values(0))):
		print(i+1,table.row_values(0)[i],end=' ')
	k=int(input("\nchose one to search:"))
	d=input("input your data:\n")
	for i in range(rows):
		if table.row_values(i)[k-1]==d:
			print("*"*100)
			print(table.row_values(i))
			print("*"*100)
			break
	print("finished")


if __name__=="__main__":
	path="student.xlsx"
	name1=u'硕士名单'
	name2=u'博士名单'
	data=open_table(path)
	table,rows,cols=read_sheet_by_name(data,name1)
	table2,rows2,cols2=read_sheet_by_name(data,name2)
	m,f=sex_num(table,rows)
	print("the basic info about master:")
	print("num:%d"%(rows-1))
	print("male:%d"%m)
	print("female:%d"%f)
	print("*"*20)
	m2,f2=sex_num(table2,rows2)
	print("the basic info about doctor:")
	print("num:%d"%(rows2-1))
	print("male:%d"%m2)
	print("female:%d"%f2)
	print("*"*20)
	next='y'
	while next=='y':
		x=input("plese choose one info to search[master/doctor]:\n")
		if x=='master':
			search_by_index(table,rows)
		elif x=='doctor':
			search_by_index(table2,rows2)
		next=input("continue[y/n]:")
		if next=='n':
			print("you have finished you search!see you later")
	input()


