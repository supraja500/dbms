


Q1 = '''SELECT d.id, d.fname 
        FROM director d 
        WHERE EXISTS (
        SELECT  m.id
        FROM  movie  m  Inner Join MovieDirector md On  m.id=md.mid
        WHERE md.did=d.id AND m.year>2000
    ) AND NOT EXISTS (
       SELECT m.id 
       FROM movie  m   Inner Join MovieDirector  md On  m.id=md.mid
       WHERE md.did=d.id AND m.year<2000
    )order by d.id asc ;'''




Q2='''select fname,(
      select  name from  movie as m
      Inner join 
      MovieDirector as md ON 
      m.id=md.mid  
      Inner join director as d on d.id=md.did
      where  d.id=p.id order by rank desc limit 1)
      from director as p limit 100;'''



Q3='''select * from actor 
      where  id not in
      (select actor.id from Actor 
      INNER JOIN Cast ON 
      `Actor`.id=`Cast`.pid 
      INNER JOIN Movie ON 
      `Cast`.mid=`Movie`.id 
      WHERE  year BETWEEN 1990 AND 2000) 
      order by actor.id desc limit 100;'''   