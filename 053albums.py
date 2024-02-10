def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

# Making three dictionaries representing different albums
album1 = make_album('Artist1', 'Album1')
album2 = make_album('Artist2', 'Album2')
album3 = make_album('Artist3', 'Album3')

# Printing each return value to show the dictionaries are storing the album information correctly
print(album1)
print(album2)
print(album3)

# Making a new function call that includes the number of tracks on an album
album_with_tracks = make_album('Artist4', 'Album4', 12)
print(album_with_tracks)
