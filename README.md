# CSCI4511W

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

### Modifying Depth Parameters:

To alter depth parameters:

1. Open the `2048.cpp` file in your code editor.
2. Locate the `score_toplevel_move()` function.
3. Adjust the `state.depth_limit` variable to set the desired depth for the algorithm.

For example:
```cpp
state.depth_limit = 3; // Set depth to 3
```

## Greedy

### To run the Greedy program, follow these steps:

1. Cd into the Greedy code repository

2. Start the server:
    ```bash
     python3 -m http.server
    ```
3. Open up the local server in your browser:
   ```bash
   http://localhost:8000/
   ```
5. Open the console (commands given for chrome):
   ```bash
   Ctrl+Shift+J/Cmd+Option+J
   ```
7. Paste the contents of the gistfile1.js file into the console and press enter. Now when you press new game on the 2048 game board it will run the greedy search algorithm.

## Monte Carlo Tree Search (MCTS)

### To run the MCTS program, follow these steps:

1. Cd into the MCTS code repository

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

### Modifying Roll Out Parameters:

To alter roll out parameters:

1. Open the `2048.cpp` file in your code editor.
2. Locate the `main()` and the `find_best_move_montecarlo()` functions.
3. Adjust the `RUNS` variable to set the desired depth for the algorithm.

For example:
```cpp
RUNS = 1000; // Set roll out to 1000
```
