dynamic-theme
=============

Dynamic theme in django app with LESS.

Idea
----
Let user select color and background which are basic theme component. Save them in db and make theme from the variables.

Solution
--------
LESS on the resque. 
LESS CSS is used smartly, to play with user selected color and produce desired theme.  
Celery is used to compile and compress LESS to CSS in server-side.



