import numpy as np
import os
import sys

def nine_isation(number=None, *args):
    final_num = None
    if number==None:
        print("\nERROR: nine_isation() takes exactly one argument(none were given)\n")
        return None
    elif len(args) > 0:
        print("\nERROR: nine_isation() takes exactly one argument (2 or more were given)\n")
        return None
    elif number<9 and number >0:
        number*=10

    final_num = number
    while final_num != 9:
        int_num_list =  [ int(i) for i in list(str(final_num)) ]
        final_num = final_num - sum(int_num_list)

    return final_num

option = int(input("\nSelect an option by typing its number and press enter:\n\n1. Type a number to nine-ise\n2. Type a number to check the nine-isation of all the integers up to there \n"))
if option==1:
    number = input("\nType an integer you like: ")
    number = int(number)

    final_num = nine_isation(number)
    if final_num is not None:
        if final_num == 9:
            print("\nNine-ised number %d : %d (SUCCESS !!)\n"%(number, final_num))
        else:
            print("\nNine-ised number %d : %d (FAILURE !!)\n"%(number, final_num))
elif option==2:
    range_to_check = input("\nType an integer as the range: ")
    range_to_check = int(range_to_check)

    # power = 10
    # range_to_check = 10**power

    list_of_nine_ised = [ i for i in range(1,range_to_check+1) if nine_isation(i) == 9 ]

    if len(list_of_nine_ised)>0: 
        print(list_of_nine_ised)


    extention = ".txt"
    filename = "nine_isation_test_" + str(range_to_check) + "range" + extention
    f = open(filename, "w")
    f.write(str(list_of_nine_ised))
    f.close()