from general_data_gatherer import DataGatherer
import pandas as pd
import os
from sklearn.decomposition import PCA  # to apply PCA
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import json

x = DataGatherer("data/MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5")
y = DataGatherer("data/MillionSongSubset/A/R/G/TRARGBM128F428F65E.h5")
z = DataGatherer("data/MillionSongSubset/A/L/A/TRALAKV12903CBD7F6.h5")
t = DataGatherer("data/MillionSongSubset/B/H/H/TRBHHCU128F148AF19.h5")
s = DataGatherer("data/MillionSongSubset/B/D/D/TRBDDCT12903CEF57E.h5")

test = [x,y,z,t,s]
df = pd.DataFrame
songs = []
def get_data(song_path):
    song = DataGatherer(song_path)
    song.read_file()

    data = {
        "hotttness":[song.get_song_hotttnesss()],
        "key":[song.get_key()*song.get_key_confidence()], # the note or chord the music is centered around, the tonic
        "mode":[song.get_mode()*song.get_mode_confidence()],   # type of scale with distinct melodic characteristics.
        "fade_out": [song.get_start_of_fade_out()/song.get_duration()], # it is rare that some fade outs start later than the end
        "fade_in": [song.get_end_of_fade_in()/song.get_duration()], 
        "duration":[song.get_duration()],
        "tempo":[song.get_tempo()], # este no lo ponemos mejor en music features
        "time_signature":[song.get_time_signature()*song.get_time_signature_confidence()],
        "analysis_sample_rate":[song.get_analysis_sample_rate()]
    }

    df = pd.DataFrame(data)
    song.close_file()
    return df

# a = get_data("data/MillionSongSubset/A/B/A/TRABACN128F425B784.h5")
# print(a)

# for item in test:
#     print(len(item.get_segments_()))

# segments
# tatum_start
# sections


#problems
# a bar is one small segment of music that holds a number of beats.
# bar               no lo pondría en general data

# beat, in music, the basic rhythmic unit of a measure, or bar,
# beats             no lo pondría en general data

# In music, a section is a complete, but not independent, musical idea. 
# Types of sections include the introduction or intro, exposition, 
# development, recapitulation, verse, chorus or refrain, conclusion, 
# coda or outro, fadeout, bridge or interlude.
# get sections      no lo pondría en general data



# artists_familiarity
# analysis_sample_rate
# artist_id
# artist_latitude
# artist_name
# artist_longitude
# artist_location
# artist_mbid
# artist_7digitalid
# artist_playmeid
# artists_terms_freq
# audio_md5
# release
# release_7digitalid
# song_id
# title
# 7digitalid
# track_id
# num_songs
# similar_artists




"""
This class process all the songs included in the millionsong
dataset.
"""
class Process():

    def preprocess_general_data(file):
        """
        Returns the song features prepared to include it in the dataset
        """
        def get_data(song_path):
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
            for i in range(len(x.get_artist_terms())):
                term = x.get_artist_terms()[i]
                term_freq = x.get_artist_terms_freq()[i]
                term_weight =x.get_artist_terms_weight()[i]
                artist_terms["artist_term: "+str(term)[2:len(str(term))-1]] = term_freq*term_weight
            data.update(artist_terms)

            artist_mbtags = json.load(open("data/artist_mbtags.json"))
            for i in range(len(y.get_artist_mbtags())):
                mbtag = y.get_artist_mbtags()[i]
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
        return print("preprocess file")

