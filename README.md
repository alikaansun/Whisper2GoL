# Whisper2GoL
 Basic seeding algorithm applied to Conway's Game of Life
 
 python main.py
 
 #Whisper.py contains seeding algorithm functions:
 
 get_word_to_number, expend_binary, matrix_construct
 
 Returns constructed 2D matrix to be used as initial condition in GoL
 
 #GOL.py contains a class with two main functions:
 
 .initialcond(); Gets user input to either have a random initial cond. if input == "random"
 else it utilizes the whisper.py algorithm
 
 .iter(); Iterates the GoL 1 time for each call
 
 #main.py contains the code for calling the functions and plotting
 
