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

        value = ""

        # print(text)
        token_list = []
        for i in parso.parse(text, version="3.9").children:
            # print(i)
            # print(i.children)

            token_list.append(i)

        # print(token_list)

        counter = 0
        check = 1
        while counter != check:

            check = counter
            temp = []
            # print(counter)
            for i in token_list:
                try:
                    # print(i)
                    temp = temp + i.children
                    counter = counter + 1


                except:
                    # print(1)
                    temp.append(i)

                # print(temp)

            # token_list = temp

            token_list = temp
            # print(token_list)

        final_list = []

        for e in token_list:
            # print(e)
            # print(str(e.type))
            if str(e.type) == 'name':
                final_list.append(str(e))
            else:
                final_list.append(str(e))

        # print(final_list)
        return final_list

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