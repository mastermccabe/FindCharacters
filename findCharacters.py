# input
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
# # output
# new_list = ['hello','world']

world_list = raw_input("Please enter a string: ")
new_list = []
# output = myList.split(",")
for word in world_list.split():
    if 'o' in word:
        # print word
        new_list.append(word)

print new_list
