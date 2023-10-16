
# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.


# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

def make_album(artist:str,title:str,tracks=0):
    album = {}
    if tracks:
        album['artist'] = artist.title()
        album['title'] = title.title()
        album['tracks'] = tracks
    else:
        album['artist'] = artist.title()
        album['title'] = title.title()
    print(album)
    return album

make_album('nujabes','metaphorical music',14)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

many_albums = int(input("How many albums do you want to create? "))
while many_albums > 0:
    artist = input("What is the artist name?")
    title = input("How's the album called?")
    insert_tracks = input("Do you want to pass how many tracks the album has? (y/n)")
    if insert_tracks == 'y':
        tracks = int(input("How many tracks does the album have? "))
    make_album(artist,title,tracks)
    many_albums-=1
    
