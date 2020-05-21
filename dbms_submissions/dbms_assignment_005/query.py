

Q1='''select   pid AS actor_id, count(mid) AS no_of_movies  from  Cast GROUP BY pid;'''

Q2='''SELECT   year,count(id) FROM Movie Group by year;'''

Q3='''SELECT   year,avg(rank) AS avg_rank FROM Movie GROUP BY year Having count(id)>=10 ORDER BY year Desc;'''

Q4='''SELECT year,MAX(rank) AS max_rank  FROM Movie GROUP BY year ORDER BY year ASC;'''

Q5='''SELECT  rank,count(id) AS no_of_movies  from movie where name LIKE 'a%' GROUP BY rank;'''