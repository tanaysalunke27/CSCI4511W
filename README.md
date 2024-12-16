# CSCI4511W

This project implements an Expectimax algorithm for playing the 2048 game.

## Expectimax

### To run the Expectimax program, follow these steps:

1. Cd into the Expectimax code repository

2. Configure the build environment:
   ```bash
   ./config
   ```

3. Build the project:
   ```bash
   make
   ```
   If you encounter issues, try specifying the compiler explicitly:
   ```bash
   make CXX=/usr/local/bin/g++-13 CXXFLAGS="-I/usr/local/Cellar/gcc/13.2.0/include/c++/13"
   ```

4. Run the game:
   ```bash
   bin/2048
   ```

### Modifying Depth Parameters

To alter depth parameters:

1. Open the `2048.cpp` file in your code editor.
2. Locate the `score_toplevel_move()` function.
3. Adjust the `state.depth_limit` variable to set the desired depth for the algorithm.

For example:
```cpp
state.depth_limit = 3; // Set depth to 3
```
