#chess

def is_valid_pawn_move(current_square, new_square):
    current_index = int(current_square)
    new_index = int(new_square)

    # check if the new square is one space above the current square
    if new_index == current_index + 1:
        print("The move is valid. ")

        
    #if both, current square and new square in smae coloum
    elif new_index == current_index :
        return ("You didnt move pawn from its current position")
    

   # otherwise, the move is not valid
    else:
        print("Invalid move.")

# test the function with an example
current_square = int(input("Enter the current position:  "))
new_square = int(input("Enter the new Chall: "))
is_valid_move = is_valid_pawn_move(current_square, new_square)
print(is_valid_move)

# ============================================================================================================================================


# function to swap two variables

def swapVariables (list, var1, var2):
    list[var1], list[var2]= list[var2], list[var1]
    return list
#driver function
list = [12,22]
#here given the index position of variables 
var1, var2 = 0,1

print(swapVariables(list, var1 , var2))
