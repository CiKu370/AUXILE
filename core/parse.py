##
## parse argument
##
## written by @ciku370
##

def toxic(word,anu):
    len_words = 0
    result = {}
    for i in word:
         if i in anu.split(','):
              try:
                   result.update({word[len_words]:word[len_words+1]})
              except IndexError:
                   continue
         len_words += 1
    return result
