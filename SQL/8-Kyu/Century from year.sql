-- Question
/*

Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
2742 --> 28
In SQL, you will be given a table years with a column yr for the year. Return a table with a column century.

*/

------------------------
--ANSWER 

select ceiling(yr/100.00) as century from years

-- The celing function will look to take a decimal or fractional number and return higher whole number version
-- so in texample the year 1705 /100 = 17.05 ceiling will take this number to 18 
