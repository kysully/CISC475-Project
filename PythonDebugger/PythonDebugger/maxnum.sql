/* CISC 475 - Group 4
* Maxnum - returns the max value out of a and b
* pl/python user defined function code
*/

CREATE OR REPLACE FUNCTION maxnum(
    a integer,
    b integer)
  RETURNS integer AS
$BODY$
  if a > b:
    return a
  return b
$BODY$
  LANGUAGE plpython3u VOLATILE
