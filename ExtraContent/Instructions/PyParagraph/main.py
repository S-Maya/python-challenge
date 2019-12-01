import os
import string
import re

num_of_file = 2
Paragraph = ""
sentence_word = []

file = os.path.join('raw_data', 'paragraph_' + str(num_of_file) + '.txt')

para_txt_file = ''
with open(file, 'r') as txtfile:
    para_txt_file = txtfile.read()

sen_split = re.split("(?<=[.!?]) +", Paragraph)
sentence_count = len(sen_split)

letters = string.ascii_letters + " " 

for n in para_txt_file:
    if n not in letters:
       para_txt_file = para_txt_file.replace(n,'')

paragraph_list = para_txt_file.split(" ")

total_letter = 0
for word in paragraph_list:
    total_letter += len(word)

words_count = len(paragraph_list)

words_lenght = total_letter/words_count

sentence_word = words_count/sentence_count

file_to_output = os.path.join('Output', 'paragraph_analysis_' + str(num_of_file)+ '.txt')

with open(file_to_output, 'w') as txtfile:

    txtfile.writelines('Paragraph Analysis\n-------------------\nApproximate Word Count: ' 
                    + str(words_count)+ '\nApproximate Sentence Count: '+ str(sentence_count) + 
                    '\nAverage Letter Count: ' + str(words_lenght) + 
                    '\nAverage Sentence Length: ' + str(sentence_word))

with open(file_to_output, 'r') as txtout:
    print(txtout.read())
