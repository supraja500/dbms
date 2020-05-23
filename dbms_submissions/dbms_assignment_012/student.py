class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
	pass 
class InvalidField(Exception):
	pass
class Student:
	def __init__(self,name,age,score):
		self.student_id=None
		self.name=name
		self.age=age
		self.score=score
	
	@classmethod	
	def get(cls,**kwargs):
		for key,value in kwargs.items():
			cls.key=key
			cls.value=value
		if cls.key!='student_id' and cls.key!='name' and cls.key!='age' and cls.key!='score':
			raise InvalidField
		sql_query="select * from Student where {}='{}'".format(cls.key,cls.value)
		k=read_data(sql_query)
		if len(k)==0:
		   raise DoesNotExist
		elif len(k)>1:
			raise MultipleObjectsReturned
		else:
		   p=Student(k[0][1],k[0][2],k[0][3])
		   p.student_id=k[0][0]
		   return p
		   
	def delete(self):
		sql_query='delete from Student where student_id={}'.format(self.student_id)
		print(self.student_id)
		write_data(sql_query)
		
	def save(self):
		if self.student_id is None:
			sql_query='insert into Student(name,age,score)values("{}",{},{})'.format(self.name,self.age,self.score)
			write_data(sql_query)
			q="select * from student where name='{}' and age={} and score={}".format(self.name,self.age,self.score)
			s=read_data(q)
			self.student_id=s[0][0]
		else:
		    sql_query='insert or replace into Student (student_id,name,age,score)values({},"{}",{},{})'.format(self.student_id,self.name,self.age,self.score)
		    write_data(sql_query)
			#sql_query="Update Student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.value)

		
 
			
		
		
			
            
			
			
			
        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans


