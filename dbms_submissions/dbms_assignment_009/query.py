Q1='''select avg(age) 
      from Player;'''



Q2='''select match_no,play_date 
      from match 
      where audience>50000;'''


Q3='''select team_id,count(win_lose) as won 
      from MatchTeamDetails
      where win_lose='W'
      group by team_id
      order by won desc,team_id asc;'''
      
Q4='''select match_no,play_date 
      from match 
      where stop1_sec>(select avg(stop1_sec) 
      from match) 
      order by match_no desc;'''


Q5=''' select m.match_no,t.name,p.name 
       from match as m
       Inner join MatchCaptain as mc
       On m.match_no=mc.match_no
       Inner join team as t
       On t.team_id=mc.team_id
       Inner join player as p
       on p.player_id=mc.captain
       order by m.match_no,t.name asc;'''
       
Q6='''select match_no,name,jersey_no 
      from match 
      Inner join 
      player 
      on match.player_of_match=player.player_id 
      order by match_no asc;'''
      
      
Q7='''select team.name,avg(age) as avg_age 
    from team  
    Inner Join 
    player 
    on team.team_id=player.team_id 
    group by team.team_id 
    having avg(age)>26 
    order by team.name asc;'''
    
Q8='''select name,jersey_no,age,count(goal_id) as goals
      from goaldetails 
      Inner join 
      player 
      on `goaldetails`.player_id=`player`.player_id  
      where age<=27 
      group by  player.player_id 
      order by goals desc,player.name asc ;'''
      
      
Q9='''select t.team_id as id,
    count(gd.goal_id)*100.0/(select count(*) 
    from goaldetails) 
    from team as t 
    inner join 
    goaldetails as gd 
    on t.team_id=gd.team_id 
    group by t.team_id 
    having count(gd.goal_id)>0;'''
    
Q10='''select avg(total_number) 
    from (select count(goal_id) as total_number  
    from goaldetails group by team_id);'''
       
       
Q11='''select player_id,name,date_of_birth 
    from player 
    where player_id 
    not in
    (select player_id from goaldetails);'''
    
    
 
Q12='''select t.name,m.match_no,m.audience,
       m.audience-(select avg(m1.audience) 
       from (match as m1 
       inner join 
       matchteamdetails as mtd1 
       on m1.match_no==mtd1.match_no) 
       where mtd1.team_id==t.team_id) as difference 
       from match as m 
       inner join  
       matchteamdetails as mtd 
       on m.match_no==mtd.match_no 
       inner join team as t 
       on t.team_id==mtd.team_id 
       order by m.match_no;'''               
    