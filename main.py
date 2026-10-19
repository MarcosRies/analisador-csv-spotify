import pandas as pd
from transform import df


# Top 5 most-played songs

most_played = df.sort_values(by = 'streams' , ascending = False).head(5)
print(most_played[['track_name', 'streams']])

# Songs from The Weeknd

the_weeknd_songs = df.loc[df['artist(s)_name'] == 'The Weeknd']
print(the_weeknd_songs)

# How many streams an artist have in the total, counting the feats

artist = "The Weeknd"
artists_streams = df[df["artist(s)_name"].str.contains(artist, case=False, na=False)]["streams"].sum()
print(f"Total number of streams from {artist}: {artists_streams}")

# Top 5 artits with most_stream summed

top_5_most_stream = df.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(5)

print(top_5_most_stream)