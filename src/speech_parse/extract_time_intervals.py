'''
Created on Nov 6, 2014

@author: Aaron Levine
@email: aclevine@brandeis.edu

speech_recognition docs:
https://pypi.python.org/pypi/SpeechRecognition/
https://github.com/Uberi/speech_recognition

ISO for time encoding:
http://en.wikipedia.org/wiki/ISO_8601
'''
import pyaudio as pa
import speech_recognition as sr
import datetime
import re

class TimeInterval():
    def __init__(self):
        self.now = datetime.datetime.now()
        self.start = datetime.datetime(self.now.year, self.now.month, self.now.day)
        self.end = self.now.replace(microsecond=0)
        self.duration = datetime.timedelta()

    def load_end(self, end_hour, end_minute = 0):        
        self.end = self.end.replace(hour = end_hour, minute = end_minute)

    def load_start(self, start_hour, start_minute = 0, calc_duration = False):
        self.start = self.start.replace(hour = start_hour, minute = start_minute)

    def load_duration(self, duration_hours = 0, duration_mins = 0):
        self.duration = datetime.timedelta(hours = duration_hours, 
                                           minutes = duration_mins)
   
    def calculate_duration(self):
        self.duration = self.end - self.start

    def calculate_start(self):
        self.start = self.end - self.duration

        
class GetTimeWorked():
    def __init__(self, transcription = ''):
        self.curr_interval = TimeInterval()
        # for testing
        self.transcription = transcription
        
    def get_audio_device_name(self):
        a = pa.PyAudio()
        return a.get_default_host_api_info()

    def speech_to_text(self, input_stream):
        r = sr.Recognizer()
        with input_stream as source:             
            audio = r.record(source)                       
        try:
            self.transcription = r.recognize(audio)
        except LookupError:
            print "Could not understand audio"

    def find_time(self, flag):
        hour_p = "\d{1,2}"
        minute_p = ":(\d\d)"
        hour = re.findall("%s (%s)" %(flag, hour_p), self.transcription)
        minute = re.findall("%s %s%s" %(flag, hour_p, minute_p), self.transcription)
        return hour, minute
        
    def parse_transcription(self):
        # parse transcription to get start and end times
        start_hour, start_minute = self.find_time("from")
        end_hour, end_minute = self.find_time("to")

        # logic to load start and end times        
        if start_hour:
            start_hour = int(start_hour[0])
            if start_minute:
                start_minute = int(start_minute[0])
                self.curr_interval.load_start(start_hour, start_minute)
            else:
                self.curr_interval.load_start(start_hour)
        if end_hour:
            end_hour = int(end_hour[0])
            # set am / pm for end time based on current time
            if self.curr_interval.now.hour > 12:
                end_hour = end_hour + 12
            if end_minute:
                end_minute = int(end_minute[0])
                self.curr_interval.load_end(end_hour, end_minute)
            else:
                self.curr_interval.load_end(end_hour)

                
if __name__ == "__main__":
    
    # DEMO
    transcription = "work from 12:05 to 6:37"

    t = GetTimeWorked(transcription)
    t.parse_transcription()
    print t.curr_interval.start
    print t.curr_interval.end
    
#     transcription = speech_to_text( sr.WavFile("test_3.wav") )
#     print transcription
#     transcription = "work from 12:30 to 5 p.m."


