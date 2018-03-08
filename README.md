# Yahtzee [![CircleCI](https://circleci.com/gh/LukeBaal/Yahtzee.svg?style=svg&circle-token=55421af71314cc9cb18856c582b34bb4b3a0e40d)](https://circleci.com/gh/LukeBaal/Yahtzee)
A CLI version of the dice game Yahtzee with a custom unit testing library


## Install

Clone this repo
```
  git clone --recurse-submodules https://github.com/lukebaal/Yahtzee
```
NOTE: the --recurse-submodule flag is needed to properly install the custom unit testing library, pest control.
If you do not intend to run the unit testing, then the flag is not needed

Next cd into the directory and run the following command to install dependencies (assuming pip is installed)
``` pip install -r requirements.txt ```
If the above command fails try:
``` pip install colorama ```
to install the dependency directly 
## How to play

For rules on how to play the game Yahtzee refer to:
https://en.wikipedia.org/wiki/Yahtzee


To start the game run with terminal in the directory of the repo:
```python main.py```

NOTE: MUST use python 3.x