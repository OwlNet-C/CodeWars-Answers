--Question
--It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
--You're given one parameter, the original string. You don't have to worry about strings with less than two characters.


------------------------- Answer
-- # write your SQL statement here: you are given a table 'removechar' with column 's',
--return a table with column 's' and your result in a column named 'res'.

--Using Substring to slice a specific part of the column
FINAL ANSWER:
select s,
SUBSTRING(s,2,LENGTH(s)-2) as res
from removechar

--Examples of Right and Left function
-- Using the right function to remove the first letter
select s,
right(s,length(s)-1) as res 
from removechar

-- Using the left function to remove the last letter
select s,
left(s,length(s)-1) as res
from removechar

-- Using Right and left 
select s,
left(right(s,length(s)-1),length(right(s,length(s)-1))-1) as res
from removechar
