# automaton.py
A random cellular automaton I made because I was bored

A large grid is generated with food randomly placed, and places a cell in the middle. That cell then begins to pathfind to nearby food, not being able to see more than 10 tiles away from itself. If it runs out of food, it dies. If it gets 100 food, it creates an offspring and loses 50 food. 

Yeah that's basically it :P
