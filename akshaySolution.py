from search import *
from nPuzzle import *
from fifteenPuzzle import *
from eightPuzzle import *
import operator, sys


def create_tile_dict(lst, size):
    d = {}
    x = 0
    y = 0
    for val in lst:
        d[val] = (x,y)
        x+=1
        if x == size:
            y += 1
            x = 0
    return d

def manh_dist(p1, p2):
    return (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]))

def heur_exp_distance(state):
    #get manhattan distance of every tile to goal {d1,d2,...,dn}
    #get manhattan distance of every tile to blank tile {g1, g2,...gn}
    #get rank of each distance {r_d1, r_d2,...r_dn}
    #Sum(h(i) = (100*di + gi^r_di)) => prioritises moves close to the empty block
    goal = state.get_goal_state()
    size = state.size
    board = state.positions
    tiles = create_tile_dict(board,size)
    goal_tiles = create_tile_dict(goal, size)
    #print(goal_tiles)
    tile_to_goal = {}
    blank_to_tile = {}
    for pos in board:
        #tile to goal of value i
        cur_pos = tiles[pos]
        goal_pos = goal_tiles[pos]
        dist = manh_dist(cur_pos, goal_pos)
        tile_to_goal[pos] = dist
        #blank to tile of value i
        blank_pos = tiles[-1]
        dist = manh_dist(cur_pos, blank_pos)
        if cur_pos == blank_pos:
            dist = size+1
        blank_to_tile[pos] = dist
        
    #sort dists of tile to goals according to minimum distances
    sorted_ttg_dists = sorted(tile_to_goal.items(), key=operator.itemgetter(1))
    #print(tile_to_goal)
    #print(sorted_ttg_dists)
    total = 0
    for x in sorted_ttg_dists:
        rank = 1
        val = x[0]
        if val == -1:
            continue
        dist = x[1]
        h = (tile_to_goal[val]*100 + blank_to_tile[val]^rank)
        total += h
        rank += 1
        #print(state.state_string())
    return total
