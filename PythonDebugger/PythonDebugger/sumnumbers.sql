/* CISC 475 - Group 4
* Sumnumbers - returns the sum of 1 to n
* pl/python user defined function code
*/

CREATE OR REPLACE FUNCTION sumnumbers(n integer)
  RETURNS integer AS
$BODY$
  sum = 0
  for i in range(1, x+1):
    sum = i + sum
  return sum
$BODY$
  LANGUAGE plpython3u VOLATILE