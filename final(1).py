# import numpy as np
import codecs
import tokenize
import token
from os import walk
from collections import Counter
import parso
import re

# import num2words
# import parser

# from numpy.dual import norm


# read the content of this directory
# start_directory = '/Users/Kiko/Desktop/c_test/'
# a list contain all the file names in that directory
# f_names = []


def walk_dir(start_directory):
    f_names = []
    for (dirpath, dirnames, filenames) in walk(start_directory):
        f_names.append(filenames)
    # print(f_names)
    return f_names


def check(rep_path):
    names = walk_dir(rep_path)
    names = [names[0][1:]]
    print(names)

    code_dict = openfile(rep_path, names)[0]
    pos_dict = openfile(rep_path, names)[1]

    mark, matches_list = greedy_tiling(code_dict, names)

    mark_dict = mark

    # for i in names[0]:
    #     count = 0
    #     name = i
    #     result = mark[i]
    #     for e in result:
    #         if e != '0':
    #             count = count + 1
    #
    #     print(name + " " + str(count / len(result)))
    #     mark_dict[i] = str(count / len(result))

    match_dict = {}
    for i in matches_list:
        try:
            match_dict[i[3]].append((pos_dict[i[3]][i[0]], pos_dict[i[3]][i[0] + i[2]], i[4]))
        except:
            match_dict[i[3]] = [(pos_dict[i[3]][i[0]], pos_dict[i[3]][i[0] + i[2]], i[4])]

        try:
            match_dict[i[4]].append((pos_dict[i[4]][i[1]], pos_dict[i[4]][i[1] + i[2]], i[3]))

        except:
            match_dict[i[4]] = [(pos_dict[i[4]][i[1]], pos_dict[i[4]][i[1] + i[2]], i[3])]

    return mark_dict, match_dict
    # return f_names


def openfile(filepath, f_names):
    code_dict = {}
    pos_dict = {}
    print(len(f_names) - 1)
    for i in range(0, (len(f_names[0]))):
        with codecs.open(filepath + f_names[0][i], 'r', encoding='utf-8', errors='ignore') as f:
            token_list = []
            lines = f.readlines()
            text = ''
            for line in lines:
                text = text + line
            for e in parso.parse(text, version="3.9").children:
                token_list.append(e)
            counter = 0
            check = 1
            while counter != check:
                check = counter
                temp = []
                for e in token_list:
                    try:
                        temp = temp + e.children
                        counter = counter + 1

                    except:
                        temp.append(e)
                token_list = temp
            print(token_list)
            pos_list = []
            final_list = []
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

            code_dict[f_names[0][i]] = final_list
            pos_dict[f_names[0][i]] = pos_list

    return code_dict, pos_dict
    # <Operator: =>


# code_dict = openfile('/Users/kiko/Desktop/c_test/')[0]
# pos_dict = openfile('/Users/kiko/Desktop/c_test/')[1]
# print(len(code_dict['test.txt']) == len(pos_dict['test.txt']))

# print(temp)

# token_list = temp


# print(token_list)

# final_list = []
#
# for e in token_list:
#
#     if str(e.type) == 'name':
#         final_list.append(str(e))
#     else:
#         final_list.append(str(e))

# print(final_list)
# return final_list

# for i in final_list:
#     yield i.type
# try:
#     for e in i.children:
#         # print(e)
#         try:
#             t_list = list(e.children)
#             print(t_list)
#             for t in t_list:
#                 print(t)
#                 # value = value + t.tpye
#         except:
#             # print(1)
#             value = e.type
#         # print(value)
#
# except:
#     value = e.type
# print(value)

# print(1)
# print(i.type)
# for line in lines:
#     print(line)
#     print(parso.parse(line, version="3.9").children[0])
# print(code_dict)

# f_names = [['test_02.txt', 'test.txt']]


def greedy_tiling(code_dict, f_names):
    mark = {}
    duplicate = {}
    matches_list = []
    for i in range(0, (len(f_names[0]))):
        temp = []
        for e in code_dict[f_names[0][i]]:
            temp.append('0')
        mark[f_names[0][i]] = temp

    for i in f_names[0]:
        # mark = {}
        # for i in range(0, (len(f_names[0]))):
        #     temp = []
        #     for e in code_dict[f_names[0][i]]:
        #         temp.append('0')
        #     mark[f_names[0][i]] = temp
        mark[i] = ['0'] * len(mark[i])

        for a in f_names[0]:
            if a != i:

                mark[a] = ['0'] * len(mark[a])
                maxMatch = 12
                while maxMatch >= 12:
                    # print(matches)
                    matches = []
                    count = 0
                    # print(maxMatch)

                    for t in range(0, len(code_dict[i])):
                        # print(t)
                        if mark[i][t] == '0':
                            for b in range(0, len(code_dict[a])):
                                #
                                # print(code_dict[a][b])
                                # print(code_dict[i][t])
                                # print(str(code_dict[i][t]) == str(code_dict[a][b]))
                                if mark[a][b] == '0' and str(code_dict[i][t]) == str(code_dict[a][b]):
                                    # if str(code_dict[i][t]) == str(code_dict[a][b]):

                                    # print(5)
                                    j = 0
                                    flag = True
                                    # print(t)
                                    # print(code_dict[i][t])

                                    while str(code_dict[a][b + j]) == str(code_dict[i][t + j]) and flag:
                                        # print(code_dict[a][b + j + 1])
                                        # print(code_dict[i][t + j + 1])
                                        # print(b + j)
                                        # print(t + j)
                                        # print(flag)
                                        if ((b + j + 1) < len(code_dict[a])) and ((t + j + 1) < len(code_dict[i])):
                                            if mark[a][b + j] == '0' and mark[i][t + j] == '0':
                                                # print("yes")
                                                j = j + 1
                                                # print(j)
                                            else:
                                                flag = False
                                        else:
                                            # print(1)
                                            flag = False
                                    # print(j)
                                    # print(j > count)
                                    # print(j)
                                    # print(count)
                                    if j > count:
                                        count = j
                                        matches = [(t, b, j, i, a)]
                                        # print(matches)
                                    elif j == count:
                                        # print(3)
                                        matches.append((t, b, j, i, a))

                    maxMatch = count
                    # print(maxMatch)
                    # print(matches)
                    # print(count)

                    if maxMatch > 12:
                        # print(matches)
                        # print(len(mark[i]))
                        for f in matches:
                            matches_list.append(f)
                        for m in matches:
                            for c in range(0, m[2]):
                                # print(t)
                                # print(c)
                                mark[i][m[0] + c] = a
                                mark[a][m[1] + c] = i

        count = 0
        for n in mark[i]:
            if n != '0':
                count = count + 1
        print(count, len(mark[i]), mark[i])
        score = count / len(mark[i])
        print(score)
        duplicate[i] = str(score)

    print(matches_list)
    print(mark)
    return duplicate, matches_list


print(check('/Users/kiko/Documents/IT project1/c_test/'))