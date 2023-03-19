# def find_missing_no(arr):
#     n = len(arr)
#     total = ((n+1)*(n+2))//2
#     return total - sum(arr)


# arr = [1,2,3,5,6]
# print(find_missing_no(arr))

# lst = [[73,1995,-5], ["land", "sea", "sky"]]

# dict = {i:j for i,j in enumerate(lst[1],1)}
# # print(dict)

# original_list = [2,3.75,.04,59.354,6,7.7777,8,9]
# new_lst = [i for i in original_list if type(i)==int]
# # print(new_lst)

# string="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# print([i for i in string if i not in 'aeiouAEIOU '])

# sentence ='In 1984 there were 13 instances of a protest with over 1000 people attending'
# newlst = [i for i in sentence.split() if i.isdigit()]
# print(newlst)

# newlst = [['even',i] if i % 2 ==0 else ['odd',i] for i in range(1,51)]
# print(newlst)

# sentence = 'On a summer day somner smith went simming in the sun and his red skin stung'
# newlst = [i for i in sentence.split() if len(i)>4]
# print(newlst)

# result = [i for i in range(1,100) if True in [True for x in range(2,10) if i%x==0]]
# print(result)
# some_string = 'the slow solid squid swam sumptuously through the slimy swamp'
# print(len([s for s in some_string if s==' ']))
 
# sentence = "Have free hours and love children? Drive kids to school, soccer practice and other activities."
# words = sentence .split(' ')
# bigrams =[]
# for i in range(len(words)-1):    
#     bigram = ((words[i],words[i+1]))
#     bigrams.append(bigram)    
# print(bigrams)
