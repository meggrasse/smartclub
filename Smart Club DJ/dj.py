import pyglet
import time
import requests
import json
import csv
import random
import math

music_corpus = {}
#open music csv file containing the song names and genres.
#using variables, split the genres into one variable genre and the song
#titles in variable filepath
#add all the genres into music_corpus
with open('music.csv', 'rU') as musicfile:
    musicreader = csv.reader(musicfile, dialect=csv.excel_tab)
    for row in musicreader:
        genre = row[0].split(',')[1]
        filepath = row[0].split(',')[0]
        if genre not in music_corpus:
            music_corpus[genre] = [filepath]
        else:
            music_corpus[genre].append(filepath)
player = pyglet.media.Player()

def clear_vote_count():
    r = requests.get('http://smartclub.herokuapp.com/clearvotes')

def play(type):
    clear_vote_count()

    number_of_songs_in_type = len(music_corpus[type])
    random_index = int(math.floor(random.random() * number_of_songs_in_type))
    song = pyglet.resource.media(music_corpus[type][random_index])
    player.queue(song)
    player.next_source()

    player.volume = 1.0
    while 1:
        try:
            player.play()
            time.sleep(10)
            r = requests.get('http://smartclub.herokuapp.com/getvotecount')
            votes = json.loads(r.text)
            if (votes['upvotes'] > votes['downvotes']):
                return play(type)
            else:
                other_types = [key for key, val in music_corpus.iteritems()]
                other_types.remove(type)
                random_index = int(math.floor(random.random() * len(other_types)))
                return play(other_types[random_index])
        except KeyboardInterrupt:
            print "interrupt"
            break

def start_dj(type):
    clear_vote_count()
    number_of_songs_in_type = len(music_corpus[type])
    random_index = int(math.floor(random.random() * number_of_songs_in_type))
    song = pyglet.resource.media(music_corpus[type][random_index])
    player.queue(song)
    player.play()
    time.sleep(10)
    r = requests.get('http://smartclub.herokuapp.com/getvotecount')
    votes = json.loads(r.text)
    if (votes['upvotes'] > votes['downvotes']):
        play(type)
    else:
        other_types = [key for key, val in music_corpus.iteritems()]
        other_types.remove(type)
        random_index = int(math.floor(random.random() * len(other_types)))
        play(other_types[random_index])

start_dj("pop")
sys.exit()
