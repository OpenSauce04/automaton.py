# automaton.py
## What it does
A large grid is generated with food randomly placed, and places a cell in the middle. That cell then begins to pathfind to nearby food, not being able to see more than 10 tiles away from itself. If it runs out of food, it dies. If it gets 100 food, it creates an offspring and loses 50 food. 

Yeah that's basically it :P
## How do I run it?
You need to make sure you have python 3 installed on you computer. Once you have done that, you can either:
1. Open the folder with the code in it in your terminal of choice, and run `python ./`

&nbsp;&nbsp;&nbsp;or

2. Double click the `__main__.py` file in the code folder

Note: Adding the `-q` option to the run command will make the program only output the cycle number, cell count and death count to the terminal, and not the actions of individual cells.