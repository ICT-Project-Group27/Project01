import numpy as np
# open file
import codecs
import tokenize
import token
# Traverse all paths in a folder
from os import walk
from collections import Counter
# interpreter
import parso
# regular expression
import re
import parser


# read the content of this directory
# start_directory = ''/Users/kiko/Documents/IT project1/c_test/''
# a list contain all the file names in that directory

resultListCount = []
# Traverse the contents of the input paths and return their paths
def walk_dir(start_directory):
    # create list
    f_names = []
    # returns all file names in a folder
    for (dirpath, dirnames, filenames) in walk(start_directory):
        f_names.append(filenames)
    return f_names


# plagiarism check, returns the duplication rate and repeat position for each procedure
def check(rep_path):
    # get all filenames in path
    names = walk_dir(rep_path)
    global resultListCount
    resultListCount = [0, 0, 0, 0]
    from tkinter import messagebox
    if(len(names) < 1 ):
        messagebox.showerror(title='Warning', message="Please select 2 or more files.")
    else:
        names = [names[0][1:]]
        #print(names)
        # the dictionary of token and the dictionary of the position of token in the original text
        code_dict = openfile(rep_path, names)[0]
        pos_dict = openfile(rep_path, names)[1]
        # invoke the repetition rate and location dictionary
        mark, matches_list = greedy_tiling(code_dict, names)

        # loaction of the repeat
        mark_dict = {}

        for i in names[0]:
            count = 0
            name = i
            result = mark[i]
            for e in result:
                if e != '0':
                    count = count + 1

            #print(name + " " + str(count / len(result)))
            mark_dict[i] = str(count / len(result))

            if((count / len(result)) < 0.1):
                resultListCount[0] += 1
            elif ((count / len(result)) >= 0.1 and (count / len(result)) < 0.15):
                resultListCount[1] += 1
            elif ((count / len(result))  >= 0.15 and (count / len(result))  < 0.25):
                resultListCount[2] += 1
            elif ((count / len(result)) >= 0.25):
                resultListCount[3] += 1
        match_dict = {}
        for i in matches_list:
            try:
                match_dict[i[3]].append((pos_dict[i[3]][i[0]], pos_dict[i[3]][i[0] + i[2]]))
            except:
                match_dict[i[3]] = [(pos_dict[i[3]][i[0]], pos_dict[i[3]][i[0] + i[2]])]

            try:
                match_dict[i[4]].append((pos_dict[i[4]][i[1]], pos_dict[i[4]][i[1] + i[2]]))

            except:
                match_dict[i[4]] = [(pos_dict[i[4]][i[1]], pos_dict[i[4]][i[1] + i[2]])]
        messagebox.showinfo(title="Report Generation", message="Plagiarism Result has been generated")
        return mark_dict, match_dict


# read the program, tokenize the program, and return a list of each program token and their location

def openfile(filepath, f_names):
    code_dict = {}
    pos_dict = {}

    # iterate over all filenames
    for i in range(0, (len(f_names[0]))):
        # open file
        with codecs.open(filepath + f_names[0][i], 'r', encoding='utf-8', errors='ignore') as f:
            token_list = []
            lines = f.readlines()
            text = ''
            for line in lines:
                text = text + line
            # Compile the python file and traverse the compilation tree to find all the leaf nodes
            for e in parso.parse(text, version="3.9").children:
                token_list.append(e)
            counter = 0
            check = 1
            # Clear all non-leaf nodes
            while counter != check:
                check = counter
                temp = []
                # Find the children of each nodes, if there is try, if not, except
                for e in token_list:
                    try:
                        temp = temp + e.children
                        counter = counter + 1

                    except:
                        temp.append(e)
                token_list = temp
            # leaf nodes
            print(token_list)
            # location of all tokens
            pos_list = []
            # final token list
            final_list = []
            # add keywords
            for a in token_list:
                # print(a.start_pos)
                if a.type == 'keyword':
                    final_list.append(a)
                    pos_list.append(a.start_pos)
                elif str(a) == '<Operator: =>':
                    final_list.append('assign')
                    pos_list.append(a.start_pos)
                elif re.match('<Name: print@', str(a)) is not None:
                    final_list.append('out')
                    pos_list.append(a.start_pos)
                elif re.match('<Name: write@', str(a)) is not None:
                    final_list.append('out')
                    pos_list.append(a.start_pos)
                elif re.match('<Name: read@', str(a)) is not None:
                    final_list.append('in')
                    pos_list.append(a.start_pos)
                elif re.match('<Name: readline@', str(a)) is not None:
                    final_list.append('in')
                    pos_list.append(a.start_pos)
                elif re.match('<Name: readlines@', str(a)) is not None:
                    final_list.append('in')
                    pos_list.append(a.start_pos)
            print(final_list)
            print(pos_list)
            # The dictionary stores the location of all file tokens and the token itself, 0 is a list, i is a list in
            # a list
            code_dict[f_names[0][i]] = final_list
            pos_dict[f_names[0][i]] = pos_list

    return code_dict, pos_dict


# greedy_tiling algorithm find all repeat part
def greedy_tiling(code_dict, f_names):
    # store mark
    mark = {}
    # store score
    duplicate = {}
    # store location
    matches_list = []

    # loop filename
    for i in range(0, (len(f_names[0]))):
        temp = []
        # initialize mark list for each file
        for e in code_dict[f_names[0][i]]:
            temp.append('0')
        mark[f_names[0][i]] = temp

    # loop file name
    for i in f_names[0]:

        # clean mark
        mark[i] = ['0'] * len(mark[i])

        # loop file name for compare two files
        for a in f_names[0]:
            # choose different file
            if a != i:
                # clean mark other file
                mark[a] = ['0'] * len(mark[a])
                # set minimal repeat value
                maxMatch = 12
                while maxMatch >= 12:

                    # longest repeated
                    matches = []
                    # Max_Repeat count
                    count = 0

                    # check repeat pair
                    for t in range(0, len(code_dict[i])):

                        # without been marked
                        if mark[i][t] == '0':
                            # find repeat pair in other file
                            for b in range(0, len(code_dict[a])):

                                # determine repeat
                                if mark[a][b] == '0' and str(code_dict[i][t]) == str(code_dict[a][b]):

                                    j = 0
                                    flag = True

                                    # determine repeat
                                    while str(code_dict[a][b + j]) == str(code_dict[i][t + j]) and flag:

                                        # don't exceed limited length
                                        if ((b + j + 1) < len(code_dict[a])) and ((t + j + 1) < len(code_dict[i])):
                                            if mark[a][b + j] == '0' and mark[i][t + j] == '0':

                                                j = j + 1

                                            else:
                                                flag = False
                                        else:

                                            flag = False

                                    # save largest repeat count
                                    if j > count:
                                        count = j
                                        matches = [(t, b, j, i, a)]

                                    elif j == count:

                                        matches.append((t, b, j, i, a))

                    # update
                    maxMatch = count

                    # record pair
                    if maxMatch > 12:

                        for f in matches:
                            matches_list.append(f)
                        for m in matches:
                            for c in range(0, m[2]):
                                mark[i][m[0] + c] = a
                                mark[a][m[1] + c] = i
        # calculate mark count calculate plagiarism check rate
        count = 0
        for n in mark[i]:
            if n != '0':
                count = count + 1
        score = count / len(mark[i])

        duplicate[i] = str(score)

    return duplicate, matches_list


