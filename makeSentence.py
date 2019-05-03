import loadNgram as lng
import findMostFreq as fmf
import operator
import random
import json


def make_dict_ngram_tri(ngram, n):
    ngram_dict = {}

    for ngram_freq in ngram:
        ngram_words = ngram_freq[0]
        ngram_words_key = ngram_words[0:n-1]
        freq = ngram_freq[1]

        if ngram_words_key in ngram_dict:
            ngram_dict[ngram_words_key].append(ngram_words[n-1])

        else :
            ngram_dict[ngram_words_key] = ['@']
            ngram_dict[ngram_words_key].append(ngram_words[n-1])

        json = json.dumps(ngram_dict)
        f = open("dict.json","w")
        f.write(json)
        f.close()
    # print(ngram_dict)
    return ngram_dict


def make_dict_ngram_bi(ngram, n):
    ngram_dict = {}

    for ngram_freq in ngram:
        ngram_words = ngram_freq[0]
        ngram_words_key = ngram_words[0]
        freq = ngram_freq[1]

        if ngram_words_key in ngram_dict:
            ngram_dict[ngram_words_key].append(ngram_words[1])
        else :
            ngram_dict[ngram_words_key] = ['@']
            ngram_dict[ngram_words_key].append(ngram_words[1])

    # print(ngram_dict)
    return ngram_dict


# def randomGenerate_bi(ngram_dict, n, topN_start, topN_next):
#     #most frequency start words N
#
#     ngram_dict_keys = list(ngram_dict.keys())
#
#     start_list = ngram_dict['<start>']
#     start_list = start_list[1:topN_start+1]
#
#     for start_word in start_list:
#         sentence = ''
#         sentence += start_word + ' '
#
#         second_list = ngram_dict[start_word][1:topN_next+1]
#         random_list = random.sample(range(0, 10), 10)
#
#         for random_num in random_list :
#             second_word = second_list[random_num]
#             second_sentence = sentence
#             second_sentence += second_word + ' '
#
#             if '<end>' in second_sentence:
#                 second_sentence = second_sentence.replace('<end>', '')
#                 print("complete sentence : ", second_sentence)
#                 continue
#
#             random_num = random.randrange(0,10)
#             next_list = ngram_dict[second_word][1:topN_next+1]
#             next_word = next_list[random_num]
#
#             if not next_word in ngram_dict:
#                 random_num = random.randrange(0,10)
#                 next_list = ngram_dict[second_word][1:topN_next+1]
#                 next_word = next_list[random_num]
#
#             try_10times = 0
#             next_sentence = second_sentence
#             while try_10times != 10 :
#
#                 next_sentence += next_word + ' '
#
#                 next_list = ngram_dict[next_word][1:]
#                 random_num = random.randrange(0,len(next_list))
#                 next_word = next_list[random_num]
#
#                 if '<end>' == next_word:
#                     next_sentence = next_sentence.replace('<end>', '')
#                     print("complete sentence : ", next_sentence)
#                     break
#
#                 if not next_word in ngram_dict:
#                     next_sentence = second_sentence
#
#                     random_num = random.randrange(0,10)
#                     next_list = ngram_dict[second_word][1:topN_next+1]
#                     next_word = next_list[random_num]
#
#                     try_10times += 1
#
#                 if try_10times == 10:
#                     print("can not make a sentence with this words")




def randomGenerate_tri(ngram_dict, n, topN_start, topN_next):
    #most frequency start words N

    ngram_dict_keys = list(ngram_dict.keys())

    start_list = []
    for keys in ngram_dict_keys:
        if '<start>' in keys:
            start_list.append(keys)
    start_list = start_list[1:topN_start+1]

    for start_word in start_list: # ex) I
        sentence = ''
        sentence += start_word[n-2] + ' '

        second_list = ngram_dict[start_word][1:topN_next+1]
        random_list = random.sample(range(0, 10), 10)

        for random_num in random_list :
            second_word = (start_word[n-2], second_list[random_num])
            second_sentence = sentence
            second_sentence += second_list[random_num] + ' '

            if '<end>' in second_sentence:
                second_sentence = second_sentence.replace('<end>', '')
                print("complete sentence : ", second_sentence)
                continue


            next_list = ngram_dict[second_word][1:]
            random_num = random.randrange(0,len(next_list))
            next_word = (second_word[n-2], next_list[random_num])

            print(next_list)
            while not next_word in ngram_dict :
                random_num = random.randrange(0,len(next_list))
                next_word = (second_word[n-2], next_list[random_num])
                # print("ok")
                if len(next_list) <= 1:
                    print("this words have no data.")


            try_10times = 0
            next_sentence = second_sentence
            while try_10times != 10 :

                last_next_word = next_word
                next_sentence += next_list[random_num] + ' '

                print("pass: ", next_word)
                print("pass: ", ngram_dict[next_word])
                next_list = ngram_dict[next_word][1:]
                random_num = random.randrange(0,len(next_list))
                next_word = (next_word[n-2], next_list[random_num])

                if '<end>' in next_word:
                    next_sentence = next_sentence.replace('<end>', '')
                    print("complete sentence : ", next_sentence)
                    break

                while not next_word in ngram_dict:

                    next_list = ngram_dict[last_next_word][1:]
                    random_num = random.randrange(0,len(next_list))
                    next_word = (last_next_word[n-2], next_list[random_num])

                    try_10times += 1
                    if try_10times == 10:
                        print("can not make a sentence with this words")
                        break

                if try_10times == 10:
                    print("can not make a sentence with this words")
                    break




if (__name__ == "__main__"):
    input_file_name = input("input load file name: ")
    n_gram = int(input("input n-gram: "))

    with open(input_file_name, 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)
        sentence = sample_file.replace('(', '').replace(')', '').replace("'",'').replace(",", '').replace('"','')


    sorted_ngram = list(fmf.find_most_Nfreq(sentence, n_gram))
    if n_gram >= 3:
        ngram_find_dict = make_dict_ngram_tri(sorted_ngram, n_gram)
        randomGenerate_tri(ngram_find_dict, n_gram, 3, 10)

    elif n_gram == 2:
        ngram_find_dict = make_dict_ngram_bi(sorted_ngram, n_gram)
        randomGenerate_bi(ngram_find_dict, n_gram, 3, 10)
