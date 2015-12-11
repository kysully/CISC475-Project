# CISC475-Project

What is it?
-----------
Postgresql is a powerful and popular open source relational database management system. Our client wanted a way to debug the user defined functions being put into the postgres server. Our goal was to create a Python debugger that was able to connect from the postgres server to our local machine, extract the python definition, debug it, and send the code back with relevent debugging information.

Our project utilizes a library called The Python Debugger, or "pdb". This module is an interactive source code debugger for Python programs where one can step through the code and evaluate it.

Where are the files?
--------------------
The files can be found on github at https://github.com/kysully/CISC475-Project.

Files Descriptions
------------------
main: Run this file to run the server.

debuggerConnect: SQL file containing function needed to connect to client server.

PythonDebuggerClient: The python code from debuggerConnect.

PythonDebuggerServer: The python code used to connect to the client server and debug the python code.

testcases: File containing unit test cases of sample python functions.

Example python functions: maxnum, sumnumbers.

PythonDebuggerHelp: Commands useful when debugging python code.

TurnOverDocument: Informs current status of project and where one can continue building the project from there.

Instructions
------------
1) Log into Postgres database. Enter function found in the file debuggerConnect.

2) Run Main.py to open the connection.

3) Run the code entered into Postgres using the following as an example:
    SELECT debuggerConnect('Hello');

4) Refer to PythonDebuggerHelp.md for useful commands to use when debugging code.

Notes for Future Development
----------------------------
1) Determine how postgresql handles indention (tabs) in
   order to properly handle the formatting

2) Make use of python's **compile** function and **exec** function
   in order to compile and run python code (and then debug)

3) Use pdb (python command line debugger) if using command line,
   otherwise use a built in debugger like on visual studio

####Side node
- the following sql statement was used to extract the pl/python
  source code:
  ```sql
  
  SELECT prosrc FROM pg_proc WHERE proname LIKE 'func-name'
  ```