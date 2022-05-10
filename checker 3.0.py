import numpy as np
import codecs
import tokenize
import token
import parso
from os import walk
from collections import Counter


from numpy.dual import norm

# read the content of this directory
start_directory = '/Users/kiko/Documents/IT project1/c_test/'
# a list contain all the file names in that directory
f_names = []
for (dirpath, dirnames, filenames) in walk(start_directory):
    f_names.append(filenames)

print(f_names)

#open file
def openfile(filepath):
    code_dict = {}
    print(len(f_names) - 1)
    for i in range(0, (len(f_names[0]) - 1)):
        with codecs.open(filepath + f_names[0][i + 1], 'r', encoding='utf-8', errors='ignore') as f:
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

            final_list = []
            for a in token_list:
                if a.type == 'keyword':
                    final_list.append(a)
                elif str(a) == '<Operator: =>':
                    final_list.append('assign')
                elif a.type == 'name':
                    final_list.append('Apply')

            code_dict[f_names[0][i + 1]] = final_list

    return code_dict
    # <Operator: =>


code_dict = openfile('/Users/kiko/Documents/IT project1/c_test/')

f_names = [['test_02.txt', 'test.txt']]


def greedy_tiling(code_dict):
    mark = {}
    for i in range(0, (len(f_names[0]))):
        temp = []
        for e in code_dict[f_names[0][i]]:
            temp.append('0')
        mark[f_names[0][i]] = temp

    for i in f_names[0]:
        for a in f_names[0]:
            if a != i:
                maxMatch = 5
                while maxMatch >= 5:
                    matches = []
                    count = 0

                    for t in range(0, len(code_dict[i])):
                        if mark[i][t] == '0':
                            for b in range(0, len(code_dict[a])):
                                #
                                # print(code_dict[a][b])
                                # print(code_dict[i][t])
                                # print(str(code_dict[i][t]) == str(code_dict[a][b]))
                                if mark[a][b] == '0' and str(code_dict[i][t]) == str(code_dict[a][b]):
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

                                        if ((b + j + 1) < len(code_dict[a])) and ((t + j + 1) < len(code_dict[i])):
                                            if mark[a][b + j] == '0' and mark[i][t + j] == '0':
                                                j = j + 1
                                        else:
                                            # print(1)
                                            flag = False
                                    print(j)
                                    print(j > count)
                                    if j > count:
                                        print(2)
                                        count = j
                                        matches = [(t, b, j)]
                                    elif j == count:
                                        print(3)
                                        matches.append((t, b, j))

                    maxMatch = count
                    # print(count)

                    if maxMatch > 5:
                        print(matches)
                        print(len(mark[i]))
                        for m in matches:
                            for c in range(0, m[2]):
                                # print(t)
                                # print(c)
                                mark[i][m[0] + c] = a
                                mark[a][m[1] + c] = i

    print(mark)
    return mark


result = greedy_tiling(code_dict)
count = 0
for i in result['test.txt']:
    if i != '0':
        count = count + 1
print(count)
print('Test' + " "+ str(count/len(result['test.txt'])))
#change to token
def tokenize_file(filepath):
    it = openfile(filepath)
    # tokens = tokenize.generate_tokens(lambda: next(it))
    return it

    # return iter(lines)
    # print(lines)
    # for line in lines:
    #     yield str(line)
    # print(''.join(f_iter))
    # # print(''.join('%s' %i for i in f_iter))


# for i in readfile('/Users/kiko/Documents/IT project1/c_test/test_02.txt'):
#     print(i)
#calculate  DF
def calculateDF(filepath):
    df = {}
    for i in range(len(f_names[0]) - 1):
        tokens = tokenize_file(start_directory + f_names[0][i + 1])
        for w in tokens:
            try:
                df[w].add(f_names[0][i + 1])

            except:
                df[w] = {f_names[0][i + 1]}
    #print(df)
    return df


# for v in t:
#     print(token.tok_name[v.type])
#     try:
#         DF[token.tok_name[v.type]] = DF[token.tok_name[v.type]] + 1
#     except:
#         DF[token.tok_name[v.type]] = 1

# total_vocab = [x for x in DF]
# print(total_vocab)
#
tf_idf = {}

#calculate tf-idf
def calculate_tf_idf(filepath, token_dict):
    for i in range(len(f_names[0]) - 1):
        tokens = []
        for t in tokenize_file(start_directory + f_names[0][i + 1]):
            tokens.append(t)
        print(tokens)
        counter = Counter(tokens)
        for t in np.unique(tokens):
            tf = counter[t] / len(tokens)
            df = len(token_dict[t]) / (len(f_names[0]) - 1)
            idf = np.log((len(f_names[0]) - 1) / (df+1.2))
            # if idf == 0:
            #     print(t, i)
            tf_idf[f_names[0][i + 1], t] = tf * idf

    return tf_idf


print(calculate_tf_idf('/Users/kiko/Documents/IT project1/c_test/', calculateDF('/Users/kiko/Documents/IT project1/c_test/')))

# test
# D = np.zeros((len(f_paths[0])-1, 30))
vocab = []
for t in tokenize_file('/Users/kiko/Documents/IT project1/c_test/test_02.txt'):
    vocab.append(t)

a = []
b = []
for i in vocab:
    if ('test_02.txt', i) in tf_idf:
        a.append(tf_idf[('test_02.txt', i)])
    else:
        a.append(0.0)

    if ('test.txt', i) in tf_idf:
        b.append(tf_idf[('test.txt', i)])
    else:
        b.append(0.0)

def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA ** 0.5) * (normB ** 0.5)) * 100, 2)

print(a)
print(b)
#print(np.dot(a, b) / (norm(a) * norm(b)))
print(cosine_similarity(a, b))