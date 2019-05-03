import loadNgram as lng
import operator

def find_most_Nfreq(text_list, n):
    ngram = lng.texttodic(text_list, n, 5)
    sortedNgram = sorted(ngram.items(), key=operator.itemgetter(1),reverse=True)

    return sortedNgram


if (__name__ == "__main__"):

    input_file_name = input("input load file name: ")
    n_gram = int(input("input n-gram: "))

    with open(input_file_name, 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)
        sentence = sample_file.replace('(', '').replace(')', '').replace("'",'').replace(",", '').replace('"','')

    topN_output = find_most_Nfreq(sentence, n_gram)
    print(topN_output)
