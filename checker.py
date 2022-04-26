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
    with codecs.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        text = ''
        for line in lines:
            text = text + line
        for i in parso.parse(text, version="3.9").children:
            # print(i.type)
        # for line in lines:
        #     print(line)
        #     print(parso.parse(line, version="3.9").children[0])

            yield i.type
        # for line in lines:
        #     yield line

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

print(a)
print(b)
print(np.dot(a, b) / (norm(a) * norm(b)))
