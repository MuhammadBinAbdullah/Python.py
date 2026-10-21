class Playlist:
    
    def __init__ (self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) Is Ready !")
        
    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' Added To {self.name}.")
        
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' Removed.")
        else:
            print(f"'{song}' Not Found In Playlist.")
            
    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")
        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"  {i}. {song}")
        else:
            print(f"   {i}. {song}")
      
    def __del__(self):
        print(f"Playlist '{self.name}' Has Been Deleted. GoodBye !")  
              
my_playlist = Playlist("Road Trip Mix", "Pop")

while True:
    print("\1. Add Song 2. Remove Song 3. View Playlist 4. Delete & Quit")
    choice = input("Enter Your Choice :")
    
    if choice == "1":
        song = input("Enter Song Name :")
        my_playlist.add_song(song)
    elif choice == "2":
        song = input("Enter Song To Remove")
        my_playlist.remove_song(song)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist
        break
    else:
        print("Invalid Choice. Enter 1, 2, 3, Or 4.")