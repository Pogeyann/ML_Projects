import pyttsx3                                      # Text to speech conversion library
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import PySimpleGUI as sg                                # to make a graphical user interface
# from ctypes import *
# from ctypes import util

# ctypeslib = util.find_library('ctypes')
# if ctypeslib is None:
#     raise ImportError('Unable to find ctypes library')


# importing the excel data

excel = pd.read_excel('crop.xlsx',header=0)
print(excel)
print(excel.shape)

# engine = pyttsx3.init('sapi5')              #Defining the speech rate,type o voice
# voices = engine.getProperty('voices')    
# rate = engine.getProperty('rate')
# engine.setProperty('rate',rate-20)
# engine.setProperty('voice',voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

le = LabelEncoder()
crop = le.fit_transform(excel['CROP'])  #Mapping the values in weather into numerical form

Nitrogen = excel['NITROGEN']
Phosphorus = excel['PHOSPHORUS']
Potassium = excel['POTASSIUM']
Temperature = excel['TEMPERATURE']
Humidity = excel['HUMIDITY']
Ph = excel['PH']
Rainfall = excel['RAINFALL']
