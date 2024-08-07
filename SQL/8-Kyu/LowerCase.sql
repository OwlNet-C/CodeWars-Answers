================= Question
Given a demographics table in the following format:

** demographics table schema **

id
name
birthday
race
you need to return the same table where all letters are lowercase in the race column.

-----------------Answer 
/*  SQL  */
select id,name,birthday,
lower(race) as race
from demographics
