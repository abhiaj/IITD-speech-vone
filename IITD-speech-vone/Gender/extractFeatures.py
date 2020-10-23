from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from statistics import mean, stdev
import csv
import timeit
import soundfile as sf
import numpy as np

def get_features(input_file):
	'''
	Given an input .wav file and its gender, this function will return a list of lists corresponding to features of each of its chunks
	male is 0
	female is 1;
	by default we will assume gender to be male(0) and then we will compare our test predictions with gender = male and decide what did the model predict the gender as
	'''
	data, samplerate = sf.read(input_file)
	# l1 = []
	[Fs, x] = audioBasicIO.read_audio_file(input_file)
	F,fm = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
	k = 0
	l = []
	for j in range(34):
		l.append(min(F[j]))
		l.append(max(F[j]))
		l.append(mean(F[j]))
		l.append(stdev(F[j]))
	l.append(len(F[j])/399)
	l.append(1)
	# l1.append(l)
	return l

# def get_features(input_file, gender = 0):
# 	'''
# 	Given an input .wav file and its gender, this function will return a list of lists corresponding to features of each of its chunks
# 	male is 0
# 	female is 1;
# 	by default we will assume gender to be male(0) and then we will compare our test predictions with gender = male and decide what did the model predict the gender as
# 	'''
# 	data, samplerate = sf.read(input_file)
# 	i=0
# 	j=1
# 	temp = samplerate*10
# 	n = int(len(data)/temp)
# 	while i < len(data):
# 		sf.write('m' + str(j) + '.wav', data[i:i+temp], samplerate)
# 		i += temp
# 		j += 1
# 	l1=[]
# 	for i in range(1, n+1, 1):
# 		l = []
# 		[Fs, x] = audioBasicIO.read_audio_file("m" + str(i) + ".wav")
# 		F,fm = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
# 		for j in range(34):
# 			l.append(min(F[j]))
# 			l.append(max(F[j]))
# 			l.append(mean(F[j]))
# 			l.append(stdev(F[j]))
# # 		l.append(gender)
# 		l1.append(l)
# 	l1 = np.array(l1)
# 	m = l1.shape[1]
# 	# print(m)
# 	l1 = l1.reshape(m,-1)
# 	# print(l1.shape)
# 	return l1

# def generate_data(output_csv):
# 	'''
# 	This function will read in the entire liste of audio files and extract features from them and append to output_csv
# 	'''
# 	l1=[]
# 	for i in range(1,822,1):
# 		print("f",i)
# 		l = []
# 		[Fs, x] = audioBasicIO.read_audio_file("f" + str(i) + ".wav")
# 		F, fm = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
# 		for j in range(34):
# 			l.append(min(F[j]))
# 			l.append(max(F[j]))
# 			l.append(mean(F[j]))
# 			l.append(stdev(F[j]))
# 		l.append(1)
# 		l1.append(l)
# 	for i in range(1,822,1):
# 		print("m",i)
# 		l = []
# 		[Fs, x] = audioBasicIO.read_audio_file("m" + str(i) + ".wav")
# 		F, fm = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
# 		for j in range(34):
# 			l.append(min(F[j]))
# 			l.append(max(F[j]))
# 			l.append(mean(F[j]))
# 			l.append(stdev(F[j]))
# 		l.append(0)
# 		l1.append(l)
# 	with open(output_csv, "w") as f:
# 		writer = csv.writer(f)
# 		writer.writerows(l1)
# #get_features('ex1.wav')
# #generate_data("../result_models/up_hindi belt_Item_data.csv")
