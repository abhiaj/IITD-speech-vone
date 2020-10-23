from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from statistics import mean, stdev
import numpy as np
import csv
import timeit
import soundfile as sf

def get_features(input_file):
	'''
	Given an input .wav file, this function will return a list of lists corresponding to features of each of its chunks
	reject is 1
	accept is 2;
	we will not append any target label and just use svm_score to get accept(2) or reject(1)
	here there is no need to break into chunks; this was required when time was a priority
	'''
	data, samplerate = sf.read(input_file)
	l1 = []
	[Fs, x] = audioBasicIO.read_audio_file(input_file)
	F,f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
	k = 0
	l = []
	for j in range(34):
		l.append(np.percentile(F[j, :], 25))
		l.append(np.percentile(F[j, :], 50))
		l.append(np.percentile(F[j, :], 75))
		l.append(np.percentile(F[j, :], 95))
	
	l.append(len(F[j])/399)
	# if fname.startswith("acc"):
	# 	l.append(2)
	# else:
	# 	l.append(1)
	l1.append(l)
	return l1
''' this function will extract the features from a wav audio file and save it to a csv file'''

# def generateFeaturesData(outputData):
# 	l1 =[]
# 	for i in range(1, 1501, 1):
# 		print("Rej",i)
# 		try:
# 			[Fs, x] = audioBasicIO.read_audio_file("rej_" + str(i) + ".wav")
# 			F,f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
# 		except:
# 			continue
# 		k = 0
# 		while k<len(F[0]):
# 			l = []
# 			for j in range(34):
# 				l.append(np.percentile(F[j, k:k+399], 25))
# 				l.append(np.percentile(F[j, k:k+399], 50))
# 				l.append(np.percentile(F[j, k:k+399], 75))
# 				l.append(np.percentile(F[j, k:k+399], 95))
			
# 			l.append(len(F[j])/399)
# 			l.append(1)
# 			l1.append(l)
# 			k = k + 399
# 	for i in range(1, 1501, 1):
# 		print("Acc",i)
# 		try:
# 			[Fs, x] = audioBasicIO.read_audio_file("acc_" + str(i) + ".wav")
# 			F,f_names = ShortTermFeatures.feature_extraction(x, Fs, 0.05*Fs, 0.025*Fs)
# 		except:
# 			continue
# 		k = 0
# 		while k < len(F[0]):
# 			l = []
# 			for j in range(34):
# 				l.append(np.percentile(F[j, k:k+399], 25))
# 				l.append(np.percentile(F[j, k:k+399], 50))
# 				l.append(np.percentile(F[j, k:k+399], 75))
# 				l.append(np.percentile(F[j, k:k+399], 95))
			
# 			l.append(len(F[j])/399)
# 			l.append(2)
# 			l1.append(l)
# 			k = k + 399

# 	with open(outputData, "w") as f:
# 		writer = csv.writer(f)
# 		writer.writerows(l1)

# #get_features('ex1.wav')
# #generateFeaturesData("full_data.csv")
