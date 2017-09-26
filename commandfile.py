from robot import run
import time
import os, datetime

mydir = os.path.join(r'C:\Users\antons\Desktop\Robot\Solomon\Robot_proj_solomon\TestResults', datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(mydir)
run(r'C:\Users\antons\Desktop\Robot\Solomon\Robot_proj_solomon\Test_Suite',
    include=['168210'],
    outputdir=mydir,
    listener=r'C:\Python27\lib\site-packages\robotide\contrib\testrunner\TestRunnerAgent.py:54516:False',
    variablefile=[r'C:\Users\antons\Desktop\Robot\Solomon\Robot_proj_solomon\Variables\Variable_file.py'
        , r'C:\Users\antons\Desktop\Robot\Solomon\Robot_proj_solomon\Variables\Variable_2.py'])