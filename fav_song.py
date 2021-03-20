class Inspiring_Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def singing_the_song(self):
        for line in self.lyrics:
            print(line)
            
hero_mc = Inspiring_Song(["Look inside you and be strong",
                          "And you'll finally see the truth",
                          "That a hero lies in you",
                          "It's my favorite song"])
                          
hero_mc.singing_the_song()
    