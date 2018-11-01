import pickle

# wordList = ["cat", "hat", "jump", "house", "orange", "brick", "horse", "word"]

# # do your thing here, like
# wordList.append("monty")
wordList = {}
wordList2 = {}

# wordList["test"] = "testerino"
# wordList2["Test2"] = "TEEEEEST"

wordLists = [wordList, wordList2]
#open a pickle file
newfile = 'mypickle2.pk'
# newfile2 = 'mypickle3.pk'


with open(newfile, 'wb') as fi:
  # dump your data into the file
  pickle.dump(wordLists, fi)

# with open(newfile, 'wb') as di:
#     pickle.dump(wordList2, di)

# with open(newfile, 'rb') as fi:
#   wordLists = pickle.load(fi)

# with open(newfile, 'rb') as di:
#   wordList2 = pickle.load(di)
wordList = wordLists[0]
wordList2 = wordLists[1]
print (wordList["test"])
print (wordList2["Test2"])
