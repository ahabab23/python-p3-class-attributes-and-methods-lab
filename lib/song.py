class Song:
    count=0
    genres=[]
    artists=[]
    genre_count={}
    artist_count={}
    def __init__(self,name,artist,genre):
        self.name=name
        self.artist=artist
        self.genre=genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count+=1
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
             cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls. artists.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre]+=1
        else:
            cls.genre_count[genre]=1
    @classmethod
    def add_to_artist_count(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist]=1




Song("Song 1", "Artist 1", "Rock"),
Song("Song 2", "Artist 2", "Pop"),
Song("Song 3", "Artist 1", "Rock"),
Song("Song 4", "Artist 3", "Hip-Hop"),
Song("Song 5", "Artist 2", "Pop"),
Song("Song 6", "Artist 1", "Rock"),
Song("Song 7", "Artist 2", "Pop"),
Song("Song 8", "Artist 1", "Rock"),
Song("Song 9", "Artist 3", "Hip-Hop"),
Song("Song 10", "Artist 6", "Pop"),

print(Song.count)  
print(Song.artists)    
print(Song.artist_count)  
print(Song.genres)
print(Song.genre_count)



