# CSCI4511W

This project implements an Expectimax algorithm for playing the 2048 game.

## How to Run

To run the Expectimax program, follow these steps:

1. Configure the build environment:
   ```bash
   ./config
Build the project:

make
If you encounter issues, try specifying the compiler explicitly:

Copy code
make CXX=/usr/local/bin/g++-13 CXXFLAGS="-I/usr/local/Cellar/gcc/13.2.0/include/c++/13"
Run the game:
bin/2048


(To alter depth paramaters go into the 2048.cpp file and go into the score_toplevel_move() function. Here you can alter the state.depth_limit variable)
