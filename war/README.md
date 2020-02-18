# To play game
 - run main.py

# Instructions to install
 - add repo directory PYTHONPATH environment variable e.g ```export PYTHONPATH=$PWD:$PYTHONPATH```
 - run main.py
 - python version 3

# Instructions to run tests
 - run tests from root directory using ```python3 -m unittest discover -s test -p "test_*.py"```

# Given more time
 - Implement other game play strategies as the war game has different variants.

# Assumptions
 - A player immediately losses when the player runs out of cards during a war.
 - If the two cards played are of equal value, then there is a "war". Both players place the next card of their pile face down instead of three as seen in some variants and then another card face-up.

# Corner cases
 - Extending the game to more than 2 players
 - Dealing with a larger deck of cards