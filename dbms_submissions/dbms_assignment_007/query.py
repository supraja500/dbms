#Q1='''select count(id) from movie where year<2000;'''

Q1='''SELECT COUNT(id) FROM Movie WHERE year<2000;'''

#Q2='''select avg(rank) from movie where year=1991;'''

Q2='''SELECT AVG(rank) FROM Movie WHERE year=1991;'''

#Q3='''select min(rank) from movie where year=1991;'''

Q3='''SELECT MIN(rank) FROM Movie WHERE year=1991;'''

Q4='''SELECT m.fname,m.lname FROM (Actor INNER JOIN Cast ON id==pid) as m WHERE m.mid=27;'''

Q5='''SELECT COUNT(a.mid) FROM (Cast INNER JOIN Actor ON id==pid) as a WHERE a.fname='Jon' AND a.lname='Dough';'''

Q6='''SELECT  name FROM movie WHERE name LIKE 'Young Latin Girls%' AND year BETWEEN 2003 AND 2006;'''

Q7='''SELECT Director.fname,Director.lname FROM Director INNER JOIN MovieDirector ON `Director`.id=`MovieDirector`.did INNER JOIN Movie ON `MovieDirector`.mid=`Movie`.id  WHERE name LIKE 'Star Trek%';'''


Q8='''SELECT name FROM Movie INNER JOIN Cast ON `Movie`.id=`Cast`.mid INNER JOIN Actor ON `Cast`.pid=`Actor`.id INNER JOIN 
   
   MovieDirector ON `MovieDirector`.mid=`Movie`.id INNER JOIN Director ON `Director`.id=`MovieDirector`.did 
   
   WHERE (Director.fname='Jackie (I)' AND Director.lname='Chan') AND Actor.fname='Jackie (I)' AND Actor.lname='Chan';'''
   
Q9='''SELECT Director.fname,Director.lname FROM Director INNER JOIN  MovieDirector ON `Director`.id=`MovieDirector`.did INNER JOIN Movie On `MovieDirector`.mid=`Movie`.id where movie.year=2001 GROUP BY Director.id  HAVING count(mid)>=4 ORDER BY Director.fname ASC,Director.lname Desc;'''


Q10='''SELECT gender,COUNT(gender) FROM Actor WHERE gender='F' OR gender='M' GROUP BY gender ORDER BY gender ASC;'''



Q11='''SELECT m.name,n.name,m.rank,m.year FROM  Movie  AS m ,Movie AS n
      WHERE  (m.year==n.year AND m.rank==n.rank AND m.name<>n.name) ORDER BY m.name ASC LIMIT 100;'''
      
      
Q12='''SELECT Actor.fname,Movie.year,Movie.rank FROM Actor INNER JOIN Cast ON `Actor`.id=`Cast`.pid Inner Join Movie On `Cast`.mid=`Movie`.id ORDER BY Actor.fname ASC,Movie.year DESC LIMIT 100;'''


Q13='''SELECT Actor.fname,Director.fname,avg(Movie.rank) AS score FROM Actor INNER JOIN Cast ON 
    `Actor`.id=`Cast`.pid INNER JOIN Movie ON `Cast`.mid=`Movie`.id INNER JOIN MovieDirector ON 
    `MovieDirector`.mid=`Movie`.id INNER JOIN Director ON `MovieDirector`.did=`Director`.id 
    GROUP  BY Director.id,Actor.id HAVING COUNT(Movie.id)>=5 ORDER BY score DESC,Director.fname ASC,Actor.fname DESC LIMIT 100;'''



