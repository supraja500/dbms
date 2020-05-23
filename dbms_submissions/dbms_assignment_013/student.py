class DoesNotExist(Exception):
    pass
class MultipleObjectsReturned(Exception):
	pass 
class InvalidField(Exception):
	pass
	
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.student_id = None
        self.age = age
        self.score = score
    
    def __repr__(self):
        return "Student(student_id={0}, name={1}, age={2}, score={3})".format(self.student_id,self.name,self.age,self.score)
    
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
	
	@classmethod
	def filter(cls,**kargs):
	    cls.li=[]
        for i,j in kargs.items():
            cls.f=i
            cls.op=j

        a=cls.f
        a=a.split("__")
        if a[0]!='student_id' and a[0]!='name' and a[0]!='age' and a[0]!='score':
            raise InvalidField
        
        
        if(len(a)>1):
            if a[1]=="gt":
                sql_query='select * from Student where {}>{}'.format(a[0],cls.op)
                
            #print(p)
            
            elif a[1]=="lt":
                sql_query='select * from Student where {}<{}'.format(a[0],cls.op)
                
            #print(p)
        
            elif a[1]=='lte':
                sql_query='select * from Student where {}<={}'.format(a[0],cls.op)

            
            elif a[1]=='gte':
                sql_query='select * from Student where {}>={}'.format(a[0],cls.op)
                
            
            elif a[1]=='neq':
                sql_query='select * from Student where {}<>"{}"'.format(a[0],cls.op)
                
            
            elif a[1]=='in':
                sql_query='select * from Student where {} in {}'.format(a[0],tuple(cls.op))
                
        
            elif a[1]=='contains':
                sql_query='select * from Student where {} like "%{}%"'.format(a[0],cls.op)
        else:  
            sql_query='select * from Student where {}="{}"'.format(a[0],cls.op)
            
        p=read_data(sql_query)
        for i in range(len(p)):
            k=Student(p[i][1],p[i][2],p[i][3])
            k.student_id=p[i][0]
            #return k
            cls.li.append(k)
            #print(k)
        return cls.li
	    
		
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
		
		



        
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

 
