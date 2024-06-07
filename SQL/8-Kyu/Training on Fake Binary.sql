/*Question : 

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
Note: input will never be an empty string
*/

----------------
--Answer

-- # write your SQL statement here: you are given a table 'fakebin' with column 'x',
--return a table with column 'x' and your result in a column named 'res'.

--select * from fakebin
select x,
TRANSLATE(X,'1234567890','0000111110') as res
from fakebin

--Translate here is used to directly switch characters out for characters you intend 
-- It is important to note the 2nd and 3rd input have to be of same length so that SQL recognises the like for like change
-- if i had a 2nd input of 123 and 3rd in put of abcdef , 'def' dont have a corresponding translate option

--Translate is case sensetive and mainly used for swapping out characters
-- the REPLACE function would be the equivalent for words
-- SELECT REPLACE(column_name, 'cat', 'dog') AS replaced_column 
-- this exmaple will replace the word CAT for DOG in a column
