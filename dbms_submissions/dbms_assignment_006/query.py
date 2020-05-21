Q1='''select m.fname,m.lname from (Actor Inner Join Cast  ON id==pid) as m where m.mid=12148;'''


Q2='''select count(m.id) from (Cast INNER JOIN Actor ON pid==id) as m where m.fname='Harrison (I)' AND m.lname='Ford';'''

Q3='''select  distinct(pid) from (Cast INNER JOIN Movie ON  id==mid) as m WHERE m.name  LIKE 'Young Latin Girls%';'''

Q4='''select count(distinct pid) from Cast INNER JOIN Movie ON id==mid  where year BETWEEN 1990 AND 2000;'''