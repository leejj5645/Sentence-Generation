# -*- coding:utf-8 -*-
import operator

def texttodic(textList, n, freq_n):
    textList = textList.replace('\n', ' ').replace('\r', ' ')
    text = textList.split(' ')
    num_ngram = int(len(text)/(n+1))
    ngram = {}
    for cnt_ngram in range(num_ngram):
        ngram_key_list = []
        freq_this = int(text[cnt_ngram*(n+1)+n])
        if freq_this < freq_n:
            continue;
        for cnt_word in range(n):
            ngram_key_list.append(text[cnt_ngram*(n+1)+cnt_word])

        ngram_key_tuple = tuple(ngram_key_list)
        ngram[ngram_key_tuple] = int(text[cnt_ngram*(n+1)+n])

    return ngram




if (__name__ == "__main__"):
    input_file_name = input("input load file name: ")
    n_gram = int(input("input n-gram: "))
    freq_n = int(input("input frequency limit(more than): "))

    with open(input_file_name, 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)
        sentence = sample_file.replace('(', '').replace(')', '').replace("'",'').replace(",", '').replace('"','')

    texttodic(sentence, n_gram, freq_n)
