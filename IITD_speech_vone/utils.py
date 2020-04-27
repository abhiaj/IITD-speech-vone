'''
This is the main library file which will have all the basic functions, we want to provide to the user
We will keep on appending gender, transcripts, silence removal and quality classification parts to this file

Authors: Jayanth Reddy, Mohammad Wasih, Aaditeshwar Seth
Last Modified: 7th August, 2018
'''

'''
Necessory Utilities:

HIGH LEVEL:
1. Remove silence from audio
2. Get Gender of audio
3. Obtain Transcripts of audio
4. Obtain quality(accept/reject) of audio

LOW LEVEL:
> get_feature_representation of an audio
> train neural_network for gender
> train svm for quality
> get accuracy of transcript
...
'''
import os
import sys
import pkg_resources
import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib
from subprocess import Popen
import requests
import codecs
import csv
#done with standard imports

import Gender.extractFeatures as GC_exf
import Gender.mp3_to_wav as mtw
import Gender.gender_classifier as  gender_classifier
#done with Gender_Classification imports

import Silence_Removal.sln as sln
#done with Silence_Removal imports

# import Transcript.transcript as Transcript_tr
#done with Automatic_Transcripts imports

import Accept_Reject.extractFeatures as AR_exf
import Accept_Reject.AR_classifier as AR_classifier
#done with Accept_Reject imports

import Theme.extractFeatures as Th_exf
#done with Theme classsification imports

import DOB.main as mainDOB
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#LOW LEVEL routines

# def train_gender(train_file, test_file, model_name):
#  	'''
#  	This function will train the neural network for gender classification;
#  	train_file is input.csv and test_file is test.csv
#  	'''
#  	train_rows = []
# 	with open(train_file, 'r') as csvfile:
# 		csvreader = csv.reader(csvfile)
# 		fields = csvreader.next()
# 		for row in csvreader:
# 			if int(row[136]) < 2:
# 				train_rows.append(row)
# 	train_rows = np.array(train_rows)

#  	test_rows = []
# 	with open(test_file, 'r') as csvfile:
# 		csvreader = csv.reader(csvfile)
# 		fields = csvreader.next()
# 		for row in csvreader:
# 			if int(row[136]) < 2:
# 				test_rows.append(row)
# 	test_rows = np.array(test_rows)

#  	gender_classifier.train_model_CNN(train_rows, test_rows, 'models/'+model_name)
#***************************************************---------------------------------------------------------------------------*************************************************

#***************************************************---------------------------------------------------------------------------*************************************************

# def train_accept_reject(train_file, test_file, model_name):
#  	'''
#  	This function will train the SVM for quality classification;
#  	train_file is input.csv and test_file is test.csv
#  	'''
#  	train_rows = []
# 	with open(train_file, 'r') as csvfile:
# 		csvreader = csv.reader(csvfile)
# 		fields = csvreader.next()
# 		for row in csvreader:
# 			if int(row[136]) < 2:
# 				train_rows.append(row)
# 	train_rows = np.array(train_rows)

#  	test_rows = []
# 	with open(test_file, 'r') as csvfile:
# 		csvreader = csv.reader(csvfile)
# 		fields = csvreader.next()
# 		for row in csvreader:
# 			if int(row[136]) < 2:
# 				test_rows.append(row)
# 	test_rows = np.array(test_rows)

#  	AR_classifier.train_model_SVM(train_rows, test_rows, 'models/'+model_name)
#***************************************************---------------------------------------------------------------------------*************************************************

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#HIGH LEVEL routines
# to be used when the audio is locally stored
def remove_silence(input_audio):
	'''
	This will produce an audio with silent parts removed
	Input: audio file(in .wav format)
	Output: audio file with silence removed(in .wav format); name is <input_audio>+_rmsilence.wav by default
	'''
	output_audio, ext = os.path.splitext(input_audio)
	output_audio += '_rmsilence.wav'
	sln.remove_silence(input_audio, output_audio)

# to be used when we are to download the audio from web url

def remove_silence_url(input_url):
	get_audio_from_url(input_url,'temp.mp3')
	remove_silence(input_audio = 'temp.mp3')
	return
#***************************************************--------------------------------------------------------------------*********************************************************

def get_audio_from_url(input_url, output_file):
	'''
	Given an audio url, this function will fetch it and generate an mp3 file for it;
	output_file should be a proper name for an mp3, i.e. ending with .mp3
	'''
	mp3file = requests.get(input_url)
	FP = open(output_file, 'wb')
	FP.write(mp3file.content)
	FP.close()
#***************************************************--------------------------------------------------------------------*********************************************************

# def get_transcript(bucket_name, bucket_folder, key_json, audio_folder):
# 	'''
# 	bucket_name , bucket_folder, key_json, audio_folder are input arguments
# 	bucket_name -> name of google cloud bucket
# 	bucket_folder -> name of the folder in the bucket where we want to upload audio files
# 	key_json -> json file with credentials
# 	audio_folder -> the folder containing audio files and we need transcripts of these audio files
# 	this code outputs a folder named as 'audio_folder'_transcripts which has transcripts in .txt format with same name as audio file
# 	'''

# 	Transcript_tr.upload(bucket_name, bucket_folder, key_json, audio_folder)
# 	Transcript_tr.get_transcript(bucket_name, bucket_folder, key_json, audio_folder)


#***************************************************--------------------------------------------------------------------*********************************************************
# to be used when the audio is locally stored
def get_gender( input_audio):
	'''
	This will return the predicted gender of the audio file
	Basic Process:
	1. mp3 audio is required as input
	2. Convert to wav format
	5. Load Gender Classification neural network
	6. Forward pass the feature vector and get the corresponding label
	7. Return the gender(label) to user; male is 0 and female is 1
	'''

	mtw.convert_mp3_to_wav(input_audio)
	input_audio_name, ext = os.path.splitext(input_audio)
	input_audio_wav = input_audio_name + '.wav'
	#remove_silence(input_audio_wav)
	features = np.array([GC_exf.get_features(input_audio_name + '.wav')]).astype(float)
	os.remove(input_audio_name + '.wav')
	#os.remove(input_audio_name + '_rmsilence.wav')
	#model_path = pkg_resources.resource_filename('Indian_Speech_Lib', 'models/accept_reject')
	model = joblib.load(open('models/Gender_classifier_rbf_model_python3.pk', 'rb'))
	scaler = pickle.load(open('models/scaler_gender_rbf_python3.pk', 'rb'))
	prediction = model.predict(scaler.transform(features[:,0:136]))
	if prediction[0]=='0':
		return 'male'
	else:
		return 'female'

# to be used when we are to download the audio from web url
def get_gender_url(input_url):
	get_audio_from_url(input_url,'temp.mp3')
	gender = get_gender(input_audio = 'temp.mp3')
	os.remove('temp.mp3')
	return gender
#***************************************************---------------------------------------------------------------------------*************************************************
# to be used when the audio is locally stored
def get_themes(input_file):
	'''
	this function takes transcpript of audio file in text format as input
	and returns list of themes relevant to this file
	'''

	theme_list = ['Local_news', 'Health', 'Education', 'Employment', 'Prices_inequality', 'Industry', 'Migration', 'Infrastructure_services', 'Consumer_issues', 'Culture & entertainment', 'Environment', 'Agriculture', 'Livelihood', 'Social issues', 'Governance', 'Community groups']
	relevant_themes = []

	stop_word_list = []
	F = open('models/stopwords.txt')
	stop_word_list = F.readlines()
	stop_word_list = [ e[:-1] for e in stop_word_list]
	F.close()

	try:
		with codecs.open(input_file, encoding='utf-8') as F:
			input_lst = F.read()
		input_lst = [ e.encode('utf-8') for e in input_lst.split(u' ')]
		F.close()
	except e:
		return [e,'error in reading file or file location not found']

	for theme in theme_list:
		vocb = pickle.load(open('models/'+theme+'_vocab', 'rb'))
		tfidf_transformer = pickle.load(open('models/'+theme+'_tfidf', 'rb'))
		model = pickle.load(open('models/'+theme+'_model', 'rb'))
		features = Th_exf.get_features([input_lst], vocb, stop_word_list)
		features = tfidf_transformer.transform(features)
		#print(features)
		prediction = model.predict(features)
		#print(theme)
		#print(model.predict_proba(features))
		#print(prediction)
		if prediction[0]==1:
			relevant_themes.append(theme)

	return relevant_themes
#********************************************************---------------------------------------------------------------------**************************************************
# to be used when the audio is locally stored
def get_quality(input_audio):
	'''
	This will return the predicted quality of the audio file as characterized by its input_url
	Basic Process:
	1. Get mp3 file from input_url
	2. Convert to wav format
	3. Remove silence periods in the wav file
	4. Get feature representation of the wav file by extracting features to a list
	5. Load Accept reject Classification SVM
	6. Get the corresponding label: 1 for reject and 2 for accept
	7. Return the quality(label) to user; reject is 0 and accept is 1
	'''

	mtw.convert_mp3_to_wav(input_audio)
	input_audio_name, ext = os.path.splitext(input_audio)
	input_audio_wav = input_audio_name + '.wav'
	features = np.array(AR_exf.get_features(input_audio_name + '.wav')).astype(float)
	os.remove(input_audio_name + '.wav')
	#model_path = pkg_resources.resource_filename('Indian_Speech_Lib', 'models/accept_reject')
	model = joblib.load(open('models/AR_python3_SVM.pk', 'rb'))
	scaler = pickle.load(open('models/AR_scaler.pk', 'rb'))
	score = model.score(scaler.transform(features[:, 0:137]), features[:, 137])
	if score > 0.5:
		return 'reject'
	else:
		return 'accept'

# to be used when we are to download the audio from web url
def get_quality_url(input_url):
	get_audio_from_url(input_url,'temp.mp3')
	quality = get_quality(input_audio = 'temp.mp3')
	os.remove('temp.mp3')
	return quality

#*******************************************************************************
# Input to this function would be basically transcript in hindi from some audio file
def find_date(sentence):

  vectorizer, dateModel = pickle.load(open('./DOB/vectorizer','rb')), pickle.load(open('./DOB/dateModel','rb'))
  monthModel, yearModel  = pickle.load(open('./DOB/monthModel','rb')), pickle.load(open('./DOB/yearModel','rb'))

  valid = 0
  inputX = np.array([sentence])
  x_Encoded = np.array([vectorizer.transform(inputX).toarray().squeeze()])

  #First SVM Model will predict if there exists any of Date, Month or Year in the sentence, if it exists then it would call findDate.
  dateP, monthP, yearP = dateModel.predict(x_Encoded), monthModel.predict(x_Encoded), yearModel.predict(x_Encoded)
  valid = 1 if (dateP!=0 or monthP!=0 or yearP!=0) else 0

  if valid == 0:
      finalDOB = json.dumps({'Date':-1,'Month':-1,'Year':-1})
      # print(json.loads(finalDOB))
      return finalDOB
  else:
      #It will call findDate function of main.py file from DOB Module
      finalDOB = mainDOB.findDate(sentence)
      #finalDOB is be a JSON Object converted from python dictionary containing 'Date', 'Month' and 'Year' as key with their values
      # print(json.loads(finalDOB))
      return finalDOB

#***************************************************---------------------------------------------------------------------------*************************************************
#print(get_quality('ex2.mp3'))
#for  e in os.listdir('mpTranscripts'):
#	if e.startswith('Agriculture'):
#		print(e,get_themes('mpTranscripts/'+e))
#train_gender('up_hindi belt_Item_data.csv', 'up_hindi belt_Item_data.csv', 'abc')
#train_accept_reject('full_databihardataitem.csv', 'full_databihardataitem.csv', 'abc')
#get_transcript('iitd01_bucket01', 'Anshu/mpData', 'iitd01-b2466276c2dc.json', 'test')
