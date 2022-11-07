import pandas as pd
from general_data_gatherer import DataGatherer
import os
import json

if __name__ == "__main__":
    feature_values = {}
    file="artist_mbtags"

    for a in os.listdir('data/MillionSongSubset'):
        for b in os.listdir('data/MillionSongSubset/%s/'%a):
            for c in os.listdir('data/MillionSongSubset/%s/%s'%(a, b)):
                for d in os.listdir('data/MillionSongSubset/%s/%s/%s'%(a, b, c)):
                    song = DataGatherer(f'data/MillionSongSubset/{a}/{b}/{c}/{d}')
                    song.read_file()
                    for term in song.get_artist_mbtags():
                        feature_values[str(term)[2:len(str(term))-1]]=0
                    song.close_file()

    print(feature_values)
    with open("data/"+file+".json", "w") as outfile:
        json.dump(feature_values, outfile)














































































