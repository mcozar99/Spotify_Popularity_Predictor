from general_data_gatherer import DataGatherer
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import json
import numpy as np

"""
This class process all the songs included in the millionsong
dataset.
"""
class Preprocess():

    def preprocess_general_data(file):
        """
        Returns the song features related to the general data prepared to include them in the dataset
        """
        def get_data(song_path):
            """
            function that creates the structure of the dataframe with the features for the csv file
            """
            song = DataGatherer(song_path)
            song.read_file()

            data = {
                "hotttness":[song.get_song_hotttnesss()],
                "fade_out": [song.get_start_of_fade_out()/song.get_duration()], # it is rare that some fade outs start later than the end
                "fade_in": [song.get_end_of_fade_in()/song.get_duration()], 
                "danceability": [song.get_danceability()],
                "duration":[song.get_duration()],
                "energy":[song.get_energy()], # all values 0 consider to quit
                "loudness":[song.get_loudness()],
                "year":[song.get_year()],
                "artist_hotttness":[song.get_artist_hotttnesss()],
            }

            artist_terms = json.load(open("data/artist_terms.json"))
            for i in range(len(song.get_artist_terms())):
                term = song.get_artist_terms()[i]
                term_freq = song.get_artist_terms_freq()[i]
                term_weight =song.get_artist_terms_weight()[i]
                artist_terms["artist_term: "+str(term)[2:len(str(term))-1]] = term_freq*term_weight
            data.update(artist_terms)

            artist_mbtags = json.load(open("data/artist_mbtags.json"))
            for i in range(len(song.get_artist_mbtags())):
                mbtag = song.get_artist_mbtags()[i]
                artist_mbtags["artist_mbtags: "+str(mbtag)[2:len(str(mbtag))-1]] = 1
            data.update(artist_mbtags)

            df = pd.DataFrame(data)
            song.close_file()
            return df

        df = pd.DataFrame
        songs = []
        for a in os.listdir('data/MillionSongSubset'):
            for b in os.listdir('data/MillionSongSubset/%s/'%a):
                for c in os.listdir('data/MillionSongSubset/%s/%s'%(a, b)):
                    for d in os.listdir('data/MillionSongSubset/%s/%s/%s'%(a, b, c)):
                        songs.append(get_data(f'data/MillionSongSubset/{a}/{b}/{c}/{d}'))
        df = pd.concat(songs)
        df.to_csv("data/general_data.csv",index=0)
        return print("preprocessed general_data.csv file")

    def preprocess_musical_data():
        """
        Returns the song features related to musical data prepared to include them in the dataset
        """

        def n_len_array(array,n):
            """
            function that converts any array in n length array (add 0 if the length if below n and combines if the length is greater than n)
            """
            narray = [0] * n
            if len(array)<n:
                for i in range(len(array)):
                    narray[i] = array[i]
                return narray
            if len(array)>n:
                times = int(len(array)/n)
                for i in range(len(array)):
                    narray[i%n] += array[i]/times
                return narray
            else:
                return array

        def include_feature(array,feature):
            """
            includes the array in a dictionary to add it to the data dictionary
            """
            feature_dict = {}
            for i in range(len(array)):
                feature_dict[feature+str(i)]=array[i]
            return feature_dict


        songs = []
        def get_data(song_path):
            """
            function that creates the structure of the dataframe with the features for the csv file
            """
            song = DataGatherer(song_path)
            song.read_file()

            data = {
                "hotttness":[song.get_song_hotttnesss()],
                "key":[song.get_key()*song.get_key_confidence()],               # the note or chord the music is centered around, the tonic
                "mode":[song.get_mode()*song.get_mode_confidence()],            # type of scale with distinct melodic characteristics.
                "fade_out": [song.get_start_of_fade_out()/song.get_duration()], # it is rare that some fade outs start later than the end
                "fade_in": [song.get_end_of_fade_in()/song.get_duration()], 
                "duration":[song.get_duration()],
                "tempo":[song.get_tempo()], 
                "time_signature":[song.get_time_signature()*song.get_time_signature_confidence()],
                "analysis_sample_rate":[song.get_analysis_sample_rate()]
            }

            segments_length = 400

            segments_t = n_len_array(song.get_segments_timbre()[:,0]*song.get_segments_confidence(),segments_length)
            segments_s = n_len_array(song.get_segments_start()*song.get_segments_confidence(),segments_length)
            segments_l = n_len_array((song.get_segments_loudness_max_time()-song.get_segments_loudness_start())*song.get_segments_loudness_max()*song.get_segments_confidence(),segments_length)
            
            
            segments_timbre = include_feature(segments_t,"segment_timbre_")
            segments_start = include_feature(segments_s,"segment_start_")
            segments_loudness =include_feature(segments_l,"segment_loudness_")

            data.update(segments_timbre)
            data.update(segments_start)
            data.update(segments_loudness)

            tatums_length= 500
            tatums = n_len_array(song.get_tatums_start()*song.get_tatums_confidence(),tatums_length)
            tatums_start = include_feature(tatums,"tatums_start_")
            data.update(tatums_start)

            sections_length = 10
            sections_s = n_len_array(song.get_sections_start()*song.get_sections_confidence(),sections_length)
            sections_start = include_feature(sections_s,"sections_start_")
            data.update(sections_start)

            bars_length=100
            bars_s = n_len_array(song.get_bars_start()*song.get_bars_confidence(),bars_length)
            bars_start = include_feature(bars_s,"bars_start_")
            data.update(bars_start)

            beats_length = 300
            beats_s = n_len_array(song.get_beats_start()*song.get_beats_confidence(),beats_length)
            beats_start = include_feature(beats_s,"beats_start_")
            data.update(beats_start)

            df = pd.DataFrame(data)
            song.close_file()
            return df

        

        df = pd.DataFrame
        songs = []
        for a in os.listdir('data/MillionSongSubset'):
            for b in os.listdir('data/MillionSongSubset/%s/'%a):
                for c in os.listdir('data/MillionSongSubset/%s/%s'%(a, b)):
                    for d in os.listdir('data/MillionSongSubset/%s/%s/%s'%(a, b, c)):
                        songs.append(get_data(f'data/MillionSongSubset/{a}/{b}/{c}/{d}'))


        df = pd.concat(songs)
        df.to_csv("data/musical_data.csv",index=0)
        return print("preprocessed musical_data.csv file")

if __name__ == "__main__":
    preprocess = Preprocess()
    preprocess.preprocess_general_data()
    preprocess.preprocess_musical_data()

