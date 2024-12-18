# CSCI4511W - Parker Johnson and Tanay Salunke

## Expectimax
Base Expectimax code originally from [Expectimax Link](https://github.com/nneonneo/2048-ai). With edits made by us to gather metrics for testing.

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
Base Greedy code originally from [Greedy Link](https://gist.github.com/aznn/9482114). With edits made by us to run on a local server.

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
Base MCTS code originally from [MCTS Link](https://github.com/ronzil/2048-ai-cpp). With edits made by us to gather metrics for testing.

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

## Deep-Q Learning 
Base Deep-Q learning code originally from [Deep-Q Link](https://github.com/JakubZojdzik/2048DeepQLearning/tree/master). With edits made by us to gather metrics for testing.

### To run the Deep-Q program, follow these steps:

1. Cd into the Deep-Q code repository

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the code:
   ```bash
   python main.py
   ```

### To train/run the model:
For ease we have included our trained data via the model.pth file. Running the python main.py command will run the already trained model. To train your own model delete the model.pth file, and in the main.py file uncomment out the line a.train(num_episodes=1000). Running the python main.py command will now train your own model and store it in a new model.pth file. 

