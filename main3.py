#main3
from part3 import *
from part1 import *
import sys

if __name__ == "__main__":
    #get file path
    command_line_args = sys.argv
    filename = command_line_args[1] #Command_line_input: python main3.py filename
    original_list,desired_list = parse(filename)
    temp = makehash(original_list, desired_list)
    #print('blah',temp)
    ht = temp[0]
    new_original_list = temp[1]
    new_desired_list = temp[2]
    dp = compute_DP_matrix(new_original_list, new_desired_list)
    #print('blah2',dp)
    actions = process_DP_matrix(new_original_list,new_desired_list,dp)
    #print('blah3',actions)
    #print(print_best_path(actions))
    #best = get_best_path(final2)
    best2 = generate2(actions,ht)
    # write to file
    #print('a',best2)
    with open(filename[0:len(filename)-3] + ".out" , "w") as output_file:
        for line in best2:
            output_file.write(line + "\n")
