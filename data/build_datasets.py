import os
import pandas as pd
from data.lyrics_gatherer import LyricsGatherer


def build_lyrics_subset():
    df = pd.read_csv('data/subdataframe.csv')
    lg = LyricsGatherer()

    data = pd.DataFrame()#columns=[item for sublist in [['artist', 'song'], [i for i in range(768)]] for item in sublist])
    for i in range(len(df)):
        try:
            lg.get_formatted_lyrics(df.iloc[i].song, df.iloc[i].artist)
        except:
            continue
        embedding = list(lg.embedding)
        embedding.insert(0, df.iloc[i].song)
        embedding.insert(0, df.iloc[i].artist)
        data = data.append(pd.Series(embedding), ignore_index=True)
        if i % 100 == 0:
            print(data)
            data.to_csv('data/song_lyrics.csv', index=False)