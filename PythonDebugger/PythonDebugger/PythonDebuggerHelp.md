# CISC475-Project

The following are a list of some of the commands the Python debugger recognizes. More then one command may be entered at a time by using ;; to seperate them.  [] represent optional comments/passable arguments. The brackets must not be typed when entering the command. Stars(**) before the commands were more commonly used during testing.

**
n(ext) : Continue execution until the next line in the current function is reached or it returns. (The difference between next and step is that step stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

**
s(tep) : Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).

Help or h : Generates a list of all the commands that are available. 

Where or w : Returns a stack trace with the most recent frame at the bottom.  There will be an arrow to indicate the current frame, which determines the context of most commands.

Break or b [[filename:]lineno|function[,condition]] : Using the lineno argument will make a break at theat point in the argument. The function argument creates a break in the current function at the first executeable statement.

tbreak [[filename:]lineno|function[,condition]] : Temporary break which will be removed once it is hit

clear or cl  [filename:lineno | bpnumber [bpnumber ...]] : This command clears breaks.  If there is a lineno argument, it clears all the breaks within that line.  When there is a list of numbers, it clears those specific breakpoints.  Lastly, if there is no argument with the command it clears all the breaks.

**
continue or cont or c : This command continues the execution.  It will only stop if a break point is encountered

jump or j lineno : Determines the next line that will be executed.  This allows you to jump back and execute the code again, so you can only use this in the bottom frame

list or l [first, [last]] : Lists the code of the file.  Lists 11 arguments if there is no argument.  If only the first is given, it lists the 11 lines surrounding it.  If both the first and the list are given it will enter both lines and all in between.
