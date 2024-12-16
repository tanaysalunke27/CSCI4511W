# CSCI4511W

To run Expectimax. Do: 
./config
make (might need to do make CXX=/usr/local/bin/g++-13 CXXFLAGS="-I/usr/local/Cellar/gcc/13.2.0/include/c++/13")
bin/2048

(To alter depth paramaters go into the 2048.cpp file and go into the score_toplevel_move() function. Here you can alter the state.depth_limit variable)
