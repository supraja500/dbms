Q1='''SELECT * FROM  Movie WHERE rank ORDER BY rank DESC Limit 10;'''

Q2='''SELECT * FROM Movie WHERE rank ORDER BY rank DESC Limit 10 OFFSET 10;'''

Q3='''SELECT name FROM Movie WHERE year>2004;'''

Q4='''SELECT name FROM Movie WHERE rank<1.1;'''

Q5='''SELECT * FROM Movie WHERE year in(2004,2005,2006);'''

Q6='''SELECT name,year FROM Movie WHERE name LIKE 'Harry%';'''

Q7='''SELECT * FROM Actor WHERE fname='Christin' and lname<>'Watson';'''

Q8='''SELECT * FROM Actor WHERE fname='Woody' and lname='Watson';'''

Q9='''SELECT name FROM Movie WHERE year=1990 and rank=5;''' 

Q10='''SELECT * FROM Actor WHERE fname='Christin' AND lname='Watson';'''

Q11='''SELECT name FROM Movie WHERE  year BETWEEN 2003 AND 2005;'''

Q12='''SELECT DISTINCT year FROM Movie ORDER BY year ASC;'''

Q13='''SELECT * FROM Actor WHERE (fname='Christin' OR lname='Watson') AND gender='M' ORDER BY fname ASC Limit 10;'''