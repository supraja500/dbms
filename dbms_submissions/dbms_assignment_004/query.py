Q1='''SELECT count(*) From Movie Where year=2002 AND name LIKE 'Ha%' AND rank>2;'''



   
Q2='''SELECT MAX(rank) From Movie WHERE  name LIKE 'Autom%' AND year BETWEEN 1983 AND 1994;'''


   
Q3='''SELECT count(*) FROM Actor WHERE gender='M' AND (fname LIKE '%ei' OR lname LIKE 'ei%');'''




Q4='''SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE year IN (1993,1995,2000) AND rank>=4.2;'''



Q5='''SELECT sum(rank) From Movie Where name Like '%Hary%' AND year BETWEEN 1981 AND 1984 AND rank<9;'''




Q6='''SELECT MIN(year) FROM Movie WHERE rank=5;'''


Q7='''SELECT count(*)  FROM  Actor WHERE gender='F' OR fname=lname;'''

Q8='''SELECT distinct fname FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100;'''


Q9='''SELECT id,name,year AS movie_title FROM Movie  WHERE year IN (2001,2002,2005,2006) LIMIT 25 OFFSET 10;'''



Q10='''SELECT  distinct lname FROM Director WHERE  fname IN ("Yeud","Wolf","Vicky") ORDER BY lname ASC LIMIT 5;'''