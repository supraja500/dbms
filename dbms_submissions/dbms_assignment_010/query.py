Q2='''select team.team_id,count(match_no) 
   from matchcaptain  
   inner join 
   team on `matchcaptain`.team_id=`team`.team_id 
   group by team.team_id;'''
   
   
Q4='''select player.player_id, count(captain)as no_of_times_captain  
    from matchcaptain 
    inner join player 
    on `matchcaptain`.captain=`player`.player_id 
    group by player.player_id;'''
    

Q10='''select player.team_id,avg(age) 
       from player 
       group by  player.team_id;'''
       
Q11='''select avg(age) as avg_age_of_captain 
    from player 
    inner join 
    matchcaptain on `player`.player_id=`matchcaptain`.captain;'''
    

   
   
Q8='''select player.jersey_no,count(captain) as no_captains
      from player 
      inner join
      matchcaptain
      on `player`.player_id=`matchcaptain`.captain
      group by player.jersey_no
      order by no_captains desc,player.jersey_no desc;'''
      
      

       



Q5='''select count(distinct captain) as no_players
      from matchcaptain 
      join 
      match
      on `matchcaptain`.match_no=`match`.match_no
      where `matchcaptain`.captain=`match`.player_of_match;'''
      
Q6='''select distinct(captain)
      from matchcaptain 
      where captain not in(select player_of_match from match);'''

Q1='''SELECT  player.player_id,player.team_id,player.jersey_no,player.name,player.date_of_birth,player.age 
      from player  
      join matchcaptain 
      on `player`.player_id=`matchcaptain`.captain
      where  player.player_id 
      not in(select player_id from goaldetails)
      order by matchcaptain.match_no ;'''
      
      
Q7='''select strftime("%m",play_date) as month,count(match_no) as no_of_match 
     from match 
     group by month 
     order by no_of_match desc;'''
     
     
Q12='''select strftime("%m",date_of_birth) as month,count(player_id) as no_of_players  
    from player  
    group by month 
    order by no_of_players desc,month desc;'''
    
    
Q9='''select  player.player_id,avg(audience) as avg_audience
      from match 
      inner join 
      matchteamdetails  
      on `match`.match_no=`matchteamdetails`.match_no
      Inner join 
      player
      on `matchteamdetails`.team_id=`player`.team_id
      group by player.player_id
      order by avg_audience desc,player.player_id desc;'''
      
Q13='''select  distinct matchcaptain.captain,count(matchteamdetails.win_lose) as no_of_wins from
       matchcaptain 
       inner join
       matchteamdetails
       on `matchcaptain`.match_no=`matchteamdetails`.match_no
       where matchteamdetails.win_lose='W' AND `matchcaptain`.team_id=`matchteamdetails`.team_id
       group by matchcaptain.captain
       order by  no_of_wins desc;'''
       
Q3='''select t.team_id,(count(gd.goal_id)*1.0/(select count(player_id) from player group by player.team_id)) as avg_goal_score from team as t 
    inner join 
    goaldetails as gd 
    on t.team_id=gd.team_id 
    group by t.team_id;'''
       
      