Q1='''select actor.id,actor.fname,actor.lname,actor.gender 
      from actor 
      inner join 
      cast 
      on `actor`.id=`cast`.pid 
      inner join 
      movie 
      on `cast`.mid=`movie`.id  
      where movie.name like 'Annie%';'''
      
      
Q2='''select movie.id,movie.name,movie.rank as rank,movie.year
      from movie 
        inner join 
        moviedirector
        on `movie`.id=`moviedirector`.mid 
        inner join 
        director 
        on `moviedirector`.did=`director`.id
        where director.fname like 'Biff%' and director.lname like 'Malibu%' and movie.year in (1999,1994,2003) 
        order by movie.rank desc,movie.year asc ;'''
      
Q3='''select year,count(id) as no_of_movies 
      from movie 
      group by year 
      having  avg(rank)>(select avg(rank) from movie) order by year asc;'''
      
      
Q4='''select id,name,year,rank 
      from movie 
      where rank<(select avg(rank) from movie where year=2001) and year=2001
      order by rank desc limit 10;'''



Q5='''select  distinct id as movie_id,
     (select count(gender) as no_of_female
         from actor 
         inner join 
         cast
         on `actor`.id=`cast`.pid
         where  `cast`.mid=`movie`.id and actor.gender='F'),
     (select count(gender) as no_of_male
     from actor 
     inner join 
     cast
     on `actor`.id=`cast`.pid
     where  `cast`.mid=`movie`.id and actor.gender='M'
     
     )
     from movie
     order by movie.id asc
     limit 100;'''

      
      
Q6='''select pid  
      from cast 
      inner join 
      movie
      on `cast`.mid=`movie`.id
      group by  pid,mid
      having count(distinct role)>1 
      order by  pid asc
      limit 100;'''   
      
Q7='''select fname,count(fname) as count  
      from director
      group by fname 
      having count(fname)>1;'''

Q8= '''select distinct  d.id,d.fname,d.lname 
      from director as d 
      inner join 
      moviedirector as md  
      on d.id=md.did 
      inner join cast as c 
      on md.mid=c.mid 
      where d.id not in(select d.id 
      from director as d 
      inner join moviedirector as md 
      on d.id=md.did  
      inner join cast as c 
      on md.mid=c.mid 
      group by md.did,md.mid 
      having count(distinct c.pid)<100) 
      and  d.id in(select d.id 
      from director as d 
      inner join moviedirector as md 
      on d.id=md.did 
      inner join cast as c 
      on md.mid=c.mid 
      group by md.did,md.mid 
      having count(distinct c.pid)>=100) 
      order by d.id;'''

      
      
      
     