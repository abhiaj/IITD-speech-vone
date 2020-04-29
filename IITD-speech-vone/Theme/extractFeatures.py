import numpy as np


def get_countvector(l_pos, vocb): #getting countvector from these files

	dict_vocab = {}

	for i,val in enumerate(vocb):
		dict_vocab[val] = i
	cv_pos =[]
	cnt = 0
	for lst in l_pos:
		lst_tmp = [0]*len(vocb)
		for word in lst:
			try:
				lst_tmp[dict_vocab[word]] = lst_tmp[dict_vocab[word]]+1
			except:
				x = 1

		cv_pos.append(lst_tmp)

	return cv_pos





def get_features(l_pos, vocb, stop_word_list):

	l_p = []

	for lst in l_pos:
		l_ptemp = []
		for word in lst: 
			if  word in stop_word_list:
				continue
			l_ptemp.append(word)
		l_p.append(l_ptemp)

	l_p = get_countvector(l_p,vocb)

	return l_p


