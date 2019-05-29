import operator
import makeNgram as mn
def calProbBi(sl):

  dictidx = {}

  idx = 0
  for s in sl:
    prob = 1
    for i in range(len(s)-2):
       prob *= freq_list_bi[s[i],s[i+1]]/ (freq_list_uni[s[i],])

  dictidx[idx] = prob
  idx += 1

  return dictidx


def calProbTri(sl):

  dictidx = {}

  idx = 0
  for s in sl:
    prob = 1
    for i in range(len(s)-3):
       prob *= freq_list_tri[s[i],s[i+1],s[i+2]]/ freq_list_bi[s[i],s[i+1]]

  dictidx[idx] = prob

  idx += 1

  return dictidx



with open('generatedSentence.txt', 'r', encoding='utf-8-sig', newline='\n') as f:
  file = f.read()
  sample_file = ''.join(file)

  sample_file = sample_file.replace('\r', '<end>').replace('complete sentence : ', '<start>')
  text = sample_file.split('\n')
  text[len(text)-1] += '<end>'

  sentence_list = []
  for s in text:
    sentence_list.append(s.split(' '))


with open('KCCq28_Korean_sentences_UTF8.txt', 'r', encoding='utf-8-sig', newline='\n') as f:
  file = f.read()
  sample_file = ''.join(file)

uni_word_list = mn.word_unigram(sample_file, 1)
freq_list_uni = mn.make_countlist(uni_word_list)

bi_word_list = mn.word_ngram(sample_file, 2)
freq_list_bi = mn.make_countlist(bi_word_list)

tri_word_list = mn.word_ngram(sample_file, 3)
freq_list_tri = mn.make_countlist(tri_word_list)

prob_list = calProbBi(sentence_list)
prob_list = calProbBi(sentence_list)

sortedprob = sorted(prob_list.items(), key=operator.itemgetter(1),reverse=True)
sortedprob = list(sortedprob)

for pair in sortedprob:
  idx = pair[0]
  print(text[idx])
