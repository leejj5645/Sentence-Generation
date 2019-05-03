#word cloud
from wordcloud import WordCloud
import loadNgram as lng
import findMostFreq as mf
import operator
import matplotlib.pyplot as plt

def make_wordcloud(ngram_dict, word, n):

    correct_keys = {}
    key_list = list(ngram_dict.keys())
    for tuple_key in key_list:
        if word == tuple_key[0]:
            correct_keys[tuple_key] = ngram_dict[tuple_key]

    sortedNgram = sorted(correct_keys.items(), key=operator.itemgetter(1),reverse=True)
    n_correct = sortedNgram[0:20]


    wc_dict = {}
    for words_freq_set in n_correct:
        words_of_set = words_freq_set[0]
        y_word = words_of_set[1]
        for i in range(2,len(words_of_set)):
            y_word += '_' + words_of_set[i]
        freq_of_set = words_freq_set[1]

        wc_dict[y_word] = freq_of_set

    font_path = './font/NanumMyeongjo.ttf'
    wordcloud = WordCloud(font_path=font_path, background_color='white', width=800, height=600).generate_from_frequencies(wc_dict)
    plt.figure(figsize=(12,12))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()



if (__name__ == "__main__"):
    input_file_name = input("input load file name: ")
    n_gram = int(input("wordcloud n-gram, input n: "))
    freq_most_Nth = int(input("Top-level frequency Nth outputs, input N: "))
    num_find_ngram = int(input("n words of n-gram, input n: "))

    with open("1-gram_1000.txt", 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)
        sentence = sample_file.replace('(', '').replace(')', '').replace("'",'').replace(",", '')
        topN_list = mf.find_most_Nfreq(sentence, 1)

    with open(input_file_name, 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)
        sentence = sample_file.replace('(', '').replace(')', '').replace("'",'').replace(",", '').replace('"','')
        ngram_dict = lng.texttodic(sentence, n_gram, 100)

        words = topN_list[freq_most_Nth]
        word = words[0]
        input_word = word[0]
        print(input_word)

    make_wordcloud(ngram_dict,input_word, n_gram)
