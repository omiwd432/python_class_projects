def word_reverse() :
		word=input('please enter your word : ')
		result_list=[]
		for i in word :
			result_list.append(i)
		result_list.reverse ()
		result=' '. join(result_list)
		return result
print(word_reverse())