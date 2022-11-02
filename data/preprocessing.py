from general_data_gatherer import DataGatherer
import pandas as pd
import os


x = DataGatherer("data/MillionSongSubset/A/A/A/TRAAAAW128F429D538.h5")
y = DataGatherer("data/MillionSongSubset/A/R/G/TRARGBM128F428F65E.h5")
z = DataGatherer("data/MillionSongSubset/B/C/A/TRBCALG128F1483839.h5")
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
        "key":[song.get_key()*song.get_key_confidence()], 
        "mode":[song.get_mode()*song.get_mode_confidence()],   # could be removed
        "fade_out": [song.get_start_of_fade_out()/song.get_duration()], # it is rare that some fade outs start later than the end
        "fade_in": [song.get_end_of_fade_in()/song.get_duration()], 
        "danceability": [song.get_danceability()],
        "duration":[song.get_duration()],
        "energy":[song.get_energy()], # all values 0 consider to quit
        "key": [song.get_key()*song.get_key_confidence()], # no sale no se por qué
        "loudness":[song.get_loudness()],
        "mode":[song.get_mode()*song.get_mode_confidence()], # tampoco sale
        "tempo":[song.get_tempo()], # este no lo ponemos mejor en music features
        "time_signature":[song.get_time_signature()*song.get_time_signature_confidence()],
        "year":[song.get_year()],
        "artist_hotttness":[song.get_artist_hotttnesss()],
        "analysis_sample_rate":[song.get_analysis_sample_rate()]
        
    }
    df = pd.DataFrame(data)
    song.close_file()
    return df
# for i in test:
#     songs.append(get_data(i))


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


#problems
# artist mbtags 
# terms 
# bar
# beats
# get sections
# title
# artist terms
# sections

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
                "key":[song.get_key()*song.get_key_confidence()], 
                "mode":[song.get_mode()*song.get_mode_confidence()],   # could be removed
                "fade_out": [song.get_start_of_fade_out()/song.get_duration()], # it is rare that some fade outs start later than the end
                "fade_in": [song.get_end_of_fade_in()/song.get_duration()], 
                "danceability": [song.get_danceability()],
                "duration":[song.get_duration()],
                "energy":[song.get_energy()], # all values 0 consider to quit
                "key": [song.get_key()*song.get_key_confidence()], # no sale no se por qué
                "loudness":[song.get_loudness()],
                "mode":[song.get_mode()*song.get_mode_confidence()], # tampoco sale
                "tempo":[song.get_tempo()], # este no lo ponemos mejor en music features
                "time_signature":[song.get_time_signature()*song.get_time_signature_confidence()],
                "year":[song.get_year()],
                "artist_hotttness":[song.get_artist_hotttnesss()],
                "analysis_sample_rate":[song.get_analysis_sample_rate()]
                
            }
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

