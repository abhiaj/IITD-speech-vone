# IITD-speech-vone
Github repository for the open source library "IITD-speech-vone", https://pypi.org/project/IITD-speech-vone/

This package is a useful library dealing with speech and text in Hindi
For installing package:
sudo pip3 install IITD_speech_vone

##The package has been updated to python3 and is no longer available for python2

System dependencies required:
1. python3
2. ffmpeg: Install it by: sudo apt-get install ffmpeg
3. gcloud: Install it by: curl https://sdk.cloud.google.com | bash  
and follow the onscreen instructions
4. pyAudioAnalysis >= 0.3: Install it by: sudo pip3 install pyAudioAnalysis==0.3.0
5. scikit-learn>=0.22.2: Install it by: sudo pip3 install scikit-learn==0.22.2
6. sudo apt-get install libpq-dev python-dev
7. polyglot download embeddings2.hi
8. polyglot download ner2.hi

Install system dependencies with pip3 install -r requirements.txt

Once you have installed then just write up a tester script, for eg. test.py
Then put this line in test.py:
from IITD_speech_vone import utils
and then call the below utility functions.

Utility functions:

utils.remove_silence(input_audio):
	given an input audio in WAV format, this function will remove silence periods from it
	and make an audio file named input_audio_rmsilence.wav

utils.remove_silence_url(input_url):
	given an input audio web url, this function will remove silence periods from it
	and make an audio file named temp_rmsilence.wav

utils.get_audio_from_url(input_url, output_file):
	given an input url having mp3 audio file and a output filename, this function generates output audio file

utils.get_transcript(bucket_name, bucket_folder, key_json, audio_folder):
	bucket_name -> name of google cloud bucket
	bucket_folder -> name of the folder in the bucket where we want to upload audio files
	key_json -> json file with credentials
	audio_folder -> the folder containing audio files and we need transcripts of these audio files
	this code outputs a folder named as 'audio_folder'_transcripts which has transcripts in .txt format with same name as audio file

utils.get_gender(input_audio):
	given an  input_audio of a file in mp3, this function will try to predict its gender
	It will return a string denoting male or female

utils.get_gender_url(input_url,download_permanently = False):
	given an input_audio web url of a file in mp3, this function will try to predict its gender
	It will return a string denoting male or female. If download permanently is set to true then the audio data will be permanently saved.

utils.get_themes(input_file):
	this function takes transcpript of audio file in text format as input
	and returns list of themes relevant to this file

utils.get_quality(input_audio):
	given an input_audio, this function will try to predict its quality
	It will return 'reject' if audio is rejected(poor quality) and 'accept' if audio is accepted(good quality).

utils.get_quality_url(input_url,download_permanently = False):
	given an input_audio's web url, this function will try to predict its quality
	It will return 'reject' if audio is rejected(poor quality) and 'accept' if audio is accepted(good quality).
	If download permanently is set to true then the audio data will be permanently saved.

utils.get_loc(input_transcript):
	given an  input_transcript, this function will try to extract embedded location in it
	It will return a list of dictionaries, each dictionary having a labelled State, District, SubDistrict and Confidence value for it.

utils.get_name(input_transcript):
	given an  input_transcript, this function will try to extract embedded name in it
	It will return a list of strings, each string being a viable name in i

utils.get_dob(sentence):
 	given an input hindi sentence , this function will try to extract embedded date in it
	It will return a dictionary in form of Json Object with keys as 'Date', 'Month' and 'Year'. Value for month could be hindi month or english month whatever the input sentence contains.

NOTE:
The version of sklearn library must be "0.22.2" otherwise the models wouldn't give correct results
For using automatic transcript utility(function), you need to have google cloud access.
1. Create account on google cloud.
2. Enable google cloud speech api: Go to Navigation menu and select APIs and Services->Library->Speech API(search) and enable it
3. Create a project and a service account for it by navigating to IAM and admin(on Navigation drop down menu) and then go to Service accounts.
4. Generate service account key for the service account created and download the key.
5. This key's path is to be provided in the utility function.
6. Also create a bucket on the Storage menu of Navigation(Drop down menu) and change its settings to public.
7. You also need to set the bucket's permissions for accessing it, i.e. you need to associate your service account with it by linking your account with Storage Object Admin section of Bucket permissions.
