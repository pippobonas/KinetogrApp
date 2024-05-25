'''
- set path /../flaskr to sys.path for import modules from flaskr
'''
import sys
import os

#setting path
current_directory = os.path.dirname(os.path.realpath(__file__))
flaskr_directory = os.path.dirname(current_directory+'/../flaskr')
sys.path.append(current_directory)
sys.path.append(flaskr_directory)
