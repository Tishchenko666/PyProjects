f = open("s_vozvrashjeniem.txt", "r")
full_text = f.read()
f.close()
symbs = ['.', ',', '!', '?', '-']
full_text_no_sumbs = ""
for s in symbs:
  full_text_no_sumbs += full_text.replace(s, '')
f_t_l = full_text_no_sumbs.lower()
text_words = f_t_l.split(" ")
text_dictionary = set(text_words)
word_list = []
n = len(text_words)
for word in text_dictionary:
  k = f_t_l.count(word)
  word_list.append([word, k])
for i in range(1, len(word_list)):
  key = word_list[i]
  j = i - 1
  while j >= 0 and word_list[j][1] < key[1]:
    word_list[j + 1] = word_list[j]
    j = j - 1
    word_list[j + 1] = key
print("20 наиболее часто встречающихся в тексте слов")
for x in word_list[:20]:
  print(x)
