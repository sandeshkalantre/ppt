# 0 - not played
# 1 - player 1
# 2 - player 2
# 3 - player 3
import time
import random
import numpy as np
import matplotlib.pyplot as plt
def print_state(table):
    for i in table:
        print i
    print "\n"

def filter_table(table,flag):
    #flag = 0 return the state unmodified
    #flag = 1 returns the state of player 1 and other entries as 0
    #flag = 2 returns the state of player 2 and other entries as 0
    #flag = 3 returns the state of player 3 and other entries as 0
    if (flag == 0):
        return table
    else:
        table = map(lambda x: map(lambda y: y if (y == flag) else 0, x), table) 
        return table


def evolve(flag):
    #flag = 0 return the state unmodified
    #flag = 1 returns the state of player 1 and other entries as 0
    #flag = 2 returns the state of player 2 and other entries as 0
    #flag = 3 returns the state of player 3 and other entries as 0

    table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    move_number = 0
    while 1:
        if (move_number == 16):
            table = filter_table(table,flag) 
            return table
        else:
            pos1 = random.randint(0,3)
            pos2 = random.randint(0,3)
            if (table[pos1][pos2] == 0):
                #the cell is not occupied
                #so player makes a move
                player_index = move_number % 3
                table[pos1][pos2] = player_index + 1
                move_number = move_number + 1

                #DEBUG: print states
                #print_state(table)
            else:
                #cell already occupied
                #try again
                continue

def evolve_final(flag):
    # number of evolutions
    N = 1000000
    flag = 3
    result = [] 
    final = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(N):
        result.append(evolve(flag))
        final = map(lambda x,y: map(lambda u,v: u/flag+v,x,y),result[i],final)

    return final

# Run the simulation
st = time.time()
final1 = evolve_final(1)
final2 = evolve_final(2)
final3 = evolve_final(3)
print "Completed in",time.time()-st,"seconds."

#plot stage
x = np.array([0,1,2,3,4])
y = np.array([0,1,2,3,4])

plt.subplot(1,3,1)
plt.title("Player 1")
plt.pcolor(x,y,np.array(final1),cmap="Greys")

plt.subplot(1,3,2)
plt.title("Player 2")
plt.pcolor(x,y,np.array(final2),cmap="Greys")

plt.subplot(1,3,3)
plt.title("Player 3")
plt.pcolor(x,y,np.array(final3),cmap="Greys")
plt.show()
