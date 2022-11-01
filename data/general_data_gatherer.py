"""
This class receives a parameter filepath indicating an h5 filepath as attribute.
With this attribute read the file and can display all the data or call some getter
We will use it to gather a pandas dataframe with the data of all songs stored in the dataframe
Source: http://millionsongdataset.com/pages/example-track-description/
"""
import tables
import numpy as np

class DataGatherer:

    def __init__(self, filepath):
        self.filepath = filepath
        self.h5 = tables.open_file(self.filepath, mode='r')
        self.data = self.h5

    def read_file(self):
        """
        Reopens a file if we have closed it
        """
        self.h5 = tables.open_file(self.filepath, mode='r')
        self.data = self.h5

    def close_file(self):
        """
        Close the file, automatic if parsedata is called
        """
        try:
            self.h5.close()
            self.data.close()
        except Exception as e:
            print(e)

    def get_num_songs(self):
        """
        Return the number of songs contained in this h5 file, i.e. the number of rows
        for all basic informations like name, artist, ...
        """
        return self.h5.root.metadata.songs.nrows

    def get_artist_familiarity(self, songidx=0):
        """
        Get artist familiarity from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_familiarity[songidx]

    def get_artist_hotttnesss(self, songidx=0):
        """
        Get artist hotttnesss from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_hotttnesss[songidx]

    def get_artist_id(self, songidx=0):
        """
        Get artist id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_id[songidx]

    def get_artist_mbid(self, songidx=0):
        """
        Get artist musibrainz id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_mbid[songidx]

    def get_artist_playmeid(self, songidx=0):
        """
        Get artist playme id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_playmeid[songidx]

    def get_artist_7digitalid(self, songidx=0):
        """
        Get artist 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_7digitalid[songidx]

    def get_artist_latitude(self, songidx=0):
        """
        Get artist latitude from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_latitude[songidx]

    def get_artist_longitude(self, songidx=0):
        """
        Get artist longitude from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_longitude[songidx]

    def get_artist_location(self, songidx=0):
        """
        Get artist location from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_location[songidx]

    def get_artist_name(self, songidx=0):
        """
        Get artist name from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_name[songidx]

    def get_release(self, songidx=0):
        """
        Get release from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.release[songidx]

    def get_release_7digitalid(self, songidx=0):
        """
        Get release 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.release_7digitalid[songidx]

    def get_song_id(self, songidx=0):
        """
        Get song id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.song_id[songidx]

    def get_song_hotttnesss(self, songidx=0):
        """
        Get song hotttnesss from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.song_hotttnesss[songidx]

    def get_title(self, songidx=0):
        """
        Get title from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.title[songidx]

    def get_track_7digitalid(self, songidx=0):
        """
        Get track 7digital id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.track_7digitalid[songidx]

    def get_similar_artists(self, songidx=0):
        """
        Get similar artists array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.similar_artists[self.h5.root.metadata.songs.cols.idx_similar_artists[songidx]:]
        return self.h5.root.metadata.similar_artists[self.h5.root.metadata.songs.cols.idx_similar_artists[songidx]:
                                                     self.h5.root.metadata.songs.cols.idx_similar_artists[songidx + 1]]

    def get_artist_terms(self, songidx=0):
        """
        Get artist terms array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                  self.h5.root.metadata.songs.cols.idx_artist_terms[songidx + 1]]

    def get_artist_terms_freq(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms_freq[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms_freq[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                       self.h5.root.metadata.songs.cols.idx_artist_terms[songidx + 1]]

    def get_artist_terms_weight(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms_weight[
                   self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms_weight[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                         self.h5.root.metadata.songs.cols.idx_artist_terms[songidx + 1]]

    def get_analysis_sample_rate(self, songidx=0):
        """
        Get analysis sample rate from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.analysis_sample_rate[songidx]

    def get_audio_md5(self, songidx=0):
        """
        Get audio MD5 from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.audio_md5[songidx]

    def get_danceability(self, songidx=0):
        """
        Get danceability from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.danceability[songidx]

    def get_duration(self, songidx=0):
        """
        Get duration from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.duration[songidx]

    def get_end_of_fade_in(self, songidx=0):
        """
        Get end of fade in from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.end_of_fade_in[songidx]

    def get_energy(self, songidx=0):
        """
        Get energy from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.energy[songidx]

    def get_key(self, songidx=0):
        """
        Get key from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.key[songidx]

    def get_key_confidence(self, songidx=0):
        """
        Get key confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.key_confidence[songidx]

    def get_loudness(self, songidx=0):
        """
        Get loudness from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.loudness[songidx]

    def get_mode(self, songidx=0):
        """
        Get mode from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.mode[songidx]

    def get_mode_confidence(self, songidx=0):
        """
        Get mode confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.mode_confidence[songidx]

    def get_start_of_fade_out(self, songidx=0):
        """
        Get start of fade out from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.start_of_fade_out[songidx]

    def get_tempo(self, songidx=0):
        """
        Get tempo from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.tempo[songidx]

    def get_time_signature(self, songidx=0):
        """
        Get signature from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.time_signature[songidx]

    def get_time_signature_confidence(self, songidx=0):
        """
        Get signature confidence from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.time_signature_confidence[songidx]

    def get_track_id(self, songidx=0):
        """
        Get track id from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.track_id[songidx]

    def get_segments_start(self, songidx=0):
        """
        Get segments start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_start[self.h5.root.analysis.songs.cols.idx_segments_start[songidx]:]
        return self.h5.root.analysis.segments_start[self.h5.root.analysis.songs.cols.idx_segments_start[songidx]:
                                                    self.h5.root.analysis.songs.cols.idx_segments_start[songidx + 1]]

    def get_segments_confidence(self, songidx=0):
        """
        Get segments confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_confidence[
                   self.h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:]
        return self.h5.root.analysis.segments_confidence[
               self.h5.root.analysis.songs.cols.idx_segments_confidence[songidx]:
               self.h5.root.analysis.songs.cols.idx_segments_confidence[songidx + 1]]

    def get_segments_pitches(self, songidx=0):
        """
        Get segments pitches array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_pitches[
                   self.h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:, :]
        return self.h5.root.analysis.segments_pitches[self.h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                                      self.h5.root.analysis.songs.cols.idx_segments_pitches[
                                                          songidx + 1], :]

    def get_segments_timbre(self, songidx=0):
        """
        Get segments timbre array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_timbre[self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:,
                   :]
        return self.h5.root.analysis.segments_timbre[self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                                     self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx + 1],
               :]

    def get_segments_loudness_max(self, songidx=0):
        """
        Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_max[
                   self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:]
        return self.h5.root.analysis.segments_loudness_max[
               self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:
               self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx + 1]]

    def get_segments_loudness_max_time(self, songidx=0):
        """
        Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_max_time[
                   self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:]
        return self.h5.root.analysis.segments_loudness_max_time[
               self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:
               self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx + 1]]

    def get_segments_loudness_start(self, songidx=0):
        """
        Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_start[
                   self.h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:]
        return self.h5.root.analysis.segments_loudness_start[
               self.h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:
               self.h5.root.analysis.songs.cols.idx_segments_loudness_start[
                   songidx + 1]]

    def get_sections_start(self, songidx=0):
        """
        Get sections start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.sections_start[self.h5.root.analysis.songs.cols.idx_sections_start[songidx]:]
        return self.h5.root.analysis.sections_start[self.h5.root.analysis.songs.cols.idx_sections_start[songidx]:
                                                    self.h5.root.analysis.songs.cols.idx_sections_start[songidx + 1]]

    def get_sections_confidence(self, songidx=0):
        """
        Get sections confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.sections_confidence[
                   self.h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:]
        return self.h5.root.analysis.sections_confidence[
               self.h5.root.analysis.songs.cols.idx_sections_confidence[songidx]:
               self.h5.root.analysis.songs.cols.idx_sections_confidence[songidx + 1]]

    def get_beats_start(self, songidx=0):
        """
        Get beats start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.beats_start[self.h5.root.analysis.songs.cols.idx_beats_start[songidx]:]
        return self.h5.root.analysis.beats_start[self.h5.root.analysis.songs.cols.idx_beats_start[songidx]:
                                                 self.h5.root.analysis.songs.cols.idx_beats_start[songidx + 1]]

    def get_beats_confidence(self, songidx=0):
        """
        Get beats confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.beats_confidence[
                   self.h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:]
        return self.h5.root.analysis.beats_confidence[self.h5.root.analysis.songs.cols.idx_beats_confidence[songidx]:
                                                      self.h5.root.analysis.songs.cols.idx_beats_confidence[
                                                          songidx + 1]]

    def get_bars_start(self, songidx=0):
        """
        Get bars start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.bars_start[self.h5.root.analysis.songs.cols.idx_bars_start[songidx]:]
        return self.h5.root.analysis.bars_start[self.h5.root.analysis.songs.cols.idx_bars_start[songidx]:
                                                self.h5.root.analysis.songs.cols.idx_bars_start[songidx + 1]]

    def get_bars_confidence(self, songidx=0):
        """
        Get bars start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.bars_confidence[self.h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:]
        return self.h5.root.analysis.bars_confidence[self.h5.root.analysis.songs.cols.idx_bars_confidence[songidx]:
                                                     self.h5.root.analysis.songs.cols.idx_bars_confidence[songidx + 1]]

    def get_tatums_start(self, songidx=0):
        """
        Get tatums start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.tatums_start[self.h5.root.analysis.songs.cols.idx_tatums_start[songidx]:]
        return self.h5.root.analysis.tatums_start[self.h5.root.analysis.songs.cols.idx_tatums_start[songidx]:
                                                  self.h5.root.analysis.songs.cols.idx_tatums_start[songidx + 1]]

    def get_tatums_confidence(self, songidx=0):
        """
        Get tatums confidence array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.tatums_confidence[
                   self.h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:]
        return self.h5.root.analysis.tatums_confidence[self.h5.root.analysis.songs.cols.idx_tatums_confidence[songidx]:
                                                       self.h5.root.analysis.songs.cols.idx_tatums_confidence[
                                                           songidx + 1]]

    def get_artist_mbtags(self, songidx=0):
        """
        Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.musicbrainz.songs.nrows == songidx + 1:
            return self.h5.root.musicbrainz.artist_mbtags[
                   self.h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
        return self.h5.root.musicbrainz.artist_mbtags[self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                      self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx + 1]]

    def get_artist_mbtags_count(self, songidx=0):
        """
        Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.musicbrainz.songs.nrows == songidx + 1:
            return self.h5.root.musicbrainz.artist_mbtags_count[
                   self.h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
        return self.h5.root.musicbrainz.artist_mbtags_count[self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                            self.h5.root.metadata.songs.cols.idx_artist_mbtags[
                                                                songidx + 1]]

    def get_year(self, songidx=0):
        """
        Get release year from a HDF5 song file, by default the first song in it
        """
        return self.h5.root.musicbrainz.songs.cols.year[songidx]


    def parse_data(self):
        if self.h5.isopen == 0:
            self.read_file()

        data = {
            'analysis_sample_rate': self.get_analysis_sample_rate(),
            'artist_7digitalid': self.get_artist_7digitalid(),
            'artist_familiarity': self.get_artist_familiarity(),
            'hotttnesss': self.get_artist_hotttnesss(),
            'artist_id': self.get_artist_id(),
            'artist_latitude': self.get_artist_latitude(),
            'artist_longitude': self.get_artist_longitude(),
            'artist_location': self.get_artist_location(),
            'artist_mbid': self.get_artist_mbid(),
            'artist_mbtags': self.get_artist_mbtags(),
            'artist_mbtagscount': self.get_artist_mbtags_count(),
            'artist_name': self.get_artist_name(),
            'artist_playmeid': self.get_artist_playmeid(),
            'artist_terms': self.get_artist_terms(),
            'artist_terms_freq': self.get_artist_terms_freq(),
            'artist_terms_weight': self.get_artist_terms_weight(),
            'audio_md5': self.get_audio_md5(),
            'bars_confidence': self.get_bars_confidence(),
            'bars_start': self.get_bars_start(),
            'beats_confidence': self.get_beats_confidence(),
            'beats_start': self.get_beats_start(),
            'danceability': self.get_danceability(),
            'duration': self.get_duration(),
            'end_of_fade_in': self.get_end_of_fade_in(),
            'energy': self.get_energy(),
            'key': self.get_key(),
            'key_confidence': self.get_key_confidence(),
            'loudness': self.get_loudness(),
            'mode': self.get_mode(),
            'mode_confidence': self.get_mode_confidence(),
            'num_songs': self.get_num_songs(),
            'release': self.get_release(),
            '7digitalid': self.get_release_7digitalid(),
            'sections_confidence': self.get_sections_confidence(),
            'sections_start': self.get_sections_start(),
            'segments_confidence': self.get_segments_confidence(),
            'segments_loudness_max': self.get_segments_loudness_max(),
            'segments_loudness_max_time': self.get_segments_loudness_max_time(),
            'segments_loudness_start': self.get_segments_loudness_start(),
            'segments_pitches': self.get_segments_pitches(),
            'segments_start': self.get_segments_start(),
            'segments_timbre': self.get_segments_timbre(),
            'similar_artists': self.get_similar_artists(),
            'song_hotttnesss': self.get_song_hotttnesss(),
            'song_id': self.get_song_id(),
            'start_of_fade_out': self.get_start_of_fade_out(),
            'tatums_confidence': self.get_tatums_confidence(),
            'tatums_start': self.get_tatums_start(),
            'tempo': self.get_tempo(),
            'time_signature': self.get_time_signature(),
            'time_signature_confidence': self.get_time_signature_confidence(),
            'title': self.get_title(),
            'track_7digitalid': self.get_track_7digitalid(),
            'track_id': self.get_track_id(),
            'year': self.get_year()
        }
        self.close_file()

        # Convert bytes to strings
        for item in data:
            if type(data[item]) == np.bytes_:
                data[item] = data[item].decode('utf-8')
            elif type(data[item]) == np.ndarray:
                try:
                    if type(data[item][0]) == np.bytes_:
                        new_val = []
                        for i in range(len(data[item])):
                            new_val.append(data[item][i].decode('utf-8'))
                        data[item] = new_val
                except:
                    continue
        return data

"""
Retrieve data among the subset
for a in os.listdir('data/MillionSongSubset'):
    for b in os.listdir('data/MillionSongSubset/%s/'%a):
        for c in os.listdir('data/MillionSongSubset/%s/%s'%(a, b)):
            for d in os.listdir('data/MillionSongSubset/%s/%s/%s'%(a, b, c)):
                dg = DataGatherer('data/MillionSongSubset/%s/%s/%s/%s'%(a, b, c, d)).parse_data()
"""