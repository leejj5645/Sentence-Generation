# -*- coding:utf-8 -*-]

# make ngram (n>=2)
def word_ngram(sentence, n):
  ngrams = []
  sentence = sentence.replace('\n', ' ').replace('\r', ' ').replace('"','')
  text = sentence.split(' ')

  while '' in text:
      text.remove('')

  for i in range(0, len(text)-(n-2)):

      if i < len(text)-2 and len(text[i+n-1]) == 0 :
          del text[i+n-1]
      can_append = 1 # make bigram or not (text[i])
      if i == 0:
          start_ngram = ['<start>']
          for x in range(i,i+n-1):
              start_ngram.append(text[x])
          ngrams.append(tuple(start_ngram))

      elif '.' == text[i+n-2][-1] or '?' == text[i+n-2][-1] or '?' == text[i+n-2][-1]:
          end_ngram = text[i:i+n-1]
          end_ngram.append('<end>')
          ngrams.append(tuple(end_ngram))

      elif '.' == text[i-1][-1] or '?' in text[i-1][-1] or '!' in text[i-1][-1]:
          start_ngram = ['<start>']
          for x in range(i,i+n-1):
              start_ngram.append(text[x])
          ngrams.append(tuple(start_ngram))


      for x in text[i:i+n-1]:
         if '.' == x[-1] or '!' == x[-1] or '?' == x[-1]:
             can_append = 0
             break

      if can_append == 1: ngrams.append(tuple(text[i:i+n]))

  print(ngrams)
  return tuple(ngrams)




# make ngram (n == 1)
def word_unigram(sentence, n):
    ngrams = []
    sentence = sentence.replace('\n', ' ').replace('\r', ' ').replace('"','')
    text = sentence.split(' ')

    while '' in text:
        text.remove('')

    for i in range(0, len(text)):

        if i == 0 or '.' == text[i-1][-1] or '?' == text[i-1][-1] or '!' in text[i-1][-1]:
            start_ngram = ['<start>']
            ngrams.append(tuple(start_ngram))

        uni_gram = text[i:i+1]
        ngrams.append(tuple(uni_gram))

        if '.' == text[i][-1] or '?' == text[i][-1] or '!' == text[i][-1]:
            end_ngram = ['<end>']
            ngrams.append(tuple(end_ngram))
    print(ngrams)
    return tuple(ngrams)


# make frequency dictionary of ngram
def make_countlist(ngramlist):
  countlist = {}
  for ngram in ngramlist:
    if (ngram in countlist):
      countlist[ngram] += 1
    else:
      countlist[ngram] = 1

  return countlist





# dictionary to text file
def make_listToText(ml_countlist, n, freq_base):
    output_file_name = str(n) + '-gram_' + str(freq_base) + '.txt'
    f = open(output_file_name, 'w')

    cnt = 0
    key_list = list(ml_countlist.keys())
    val_list = list(ml_countlist.values())

    for i in range(len(ml_countlist)):
        if val_list[i] >= freq_base:
          line = str(key_list[i]) + ' ' + str(val_list[i]) + '\n'
          cnt += 1
          f.write(line)

    f.close()
    print(cnt)




if (__name__ == "__main__"):
    input_file_name = input("input file name: ")
    n_gram = int(input("input n-gram: "))
    freq_n = int(input("input frequency limit(more than): "))

    with open(input_file_name, 'r', encoding='utf-8-sig', newline='\n') as f:
        file = f.read()
        sample_file = ''.join(file)

    if n_gram > 1:
        word_list = word_ngram(sample_file, n_gram)
        freq_list = make_countlist(word_list)
        make_listToText(freq_list,n_gram, freq_n)
    
    elif n_gram == 1:
        word_list = word_unigram(sample_file, n_gram)
        freq_list = make_countlist(word_list)
        make_listToText(freq_list,n_gram, freq_n)
