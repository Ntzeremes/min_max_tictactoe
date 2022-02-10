# min_max_tictactoe

This is a tic tac toe game created in pygame.
The game has a player vs player or a player vs computer mode.

##Algorithm

The algorithm used for the player vs computer is a minmax algorithm.
It is not depth limited and uses alpha beta pruning for better efficiency.

In the algorithm.py, there is a function called algo_tester runs a minmax and a minmax with pruning,
on different test boards and prints the best action and the time it takes for the algorithm to calculate it.
The ab minmax is noticeably faster than the normal minmax.