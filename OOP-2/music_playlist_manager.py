# ---- Music Playlist Manager ----

class        Playlist:

    # STEP 1 - Parameterized constructor: runs the moment the playlist is created
    def __init__(self, name, genre):
        self.name = name
        self.songs  = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    # STEP 2 - Add a song to the playlist
    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")

    # STEP 3 - Remove a song from the playlist
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print (f"'{song}' removed.")
        else:
            print(f"'{song}' not found in playlist")

    # STEP4 - Display all songs
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, so
        

 