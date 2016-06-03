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

#method to clear votes
def clear_vote_count():
    r = requests.get('http://smartclub.herokuapp.com/clearvotes')
    s = requests.get('http://smartclub.herokuapp.com/resetscreamtracker')
def play(type):
    clear_vote_count()
    print "b"
    number_of_songs_in_type = len(music_corpus[type])
    random_index = int(math.floor(random.random() * number_of_songs_in_type))
    song = pyglet.resource.media(music_corpus[type][random_index])
    player.queue(song)
    player.next_source()
    player.volume = 1.0
    while 1:
        try:
            #player.play()
            time.sleep(10)
            # after 10 seconds, get request to check upvotes/downvotes and possible noise reaction
            r = requests.get('http://smartclub.herokuapp.com/getvotecount')
            scream = requests.get('http://smartclub.herokuapp.com/wasthereascream')
            votes = json.loads(r.text)
            if ((votes['upvotes'] > votes['downvotes']) or (scream.text == "Yes")):
                #go for 1/4th the songs duration and re check again and if response favorable,
                #play the rest of the song and then play another song in the same genre
                print (song.duration/4.0)
                time.sleep(song.duration/4.0)
                r = requests.get('http://smartclub.herokuapp.com/getvotecount')
                scream = requests.get('http://smartclub.herokuapp.com/wasthereascream')
                votes = json.loads(r.text)
                if ((votes['upvotes'] > votes['downvotes']) or (scream.text == "Yes")):
                    print ((3.0*song.duration/4.0)-10.0)
                    time.sleep((3.0* song.duration/4.0)-10.0)
                else:
                    print "a"
                    other_types = [key for key, val in music_corpus.iteritems()]
                    other_types.remove(type)
                    random_index = int(math.floor(random.random() * len(other_types)))
                    return play(other_types[random_index])
                return play(type)
            else:
                #remove genre from the type so program plays a song from another genre
                other_types = [key for key, val in music_corpus.iteritems()]
                other_types.remove(type)
                random_index = int(math.floor(random.random() * len(other_types)))
                return play(other_types[random_index])
        except KeyboardInterrupt:
            print "interrupt"
            break

def start_dj(type):
    #this function will be called first but it does everything similar
    #to the play function. This is necessary to load songs and play immediately.
    print "a"
    clear_vote_count()
    number_of_songs_in_type = len(music_corpus[type])
    random_index = int(math.floor(random.random() * number_of_songs_in_type))
    song = pyglet.resource.media(music_corpus[type][random_index])
    player.queue(song)
    player.play()
    time.sleep(10)
    r = requests.get('http://smartclub.herokuapp.com/getvotecount')
    scream = requests.get('http://smartclub.herokuapp.com/wasthereascream')
    votes = json.loads(r.text)
    if ((votes['upvotes'] > votes['downvotes']) or (scream.text == "Yes")):
        print (song.duration/4.0)
        time.sleep(song.duration/4.0)
        r = requests.get('http://smartclub.herokuapp.com/getvotecount')
        scream = requests.get('http://smartclub.herokuapp.com/wasthereascream')
        votes = json.loads(r.text)
        if ((votes['upvotes'] > votes['downvotes']) or (scream.text == "Yes")):
            print ((3.0*song.duration/4.0)-10.0)
            time.sleep((3.0* song.duration/4.0)-10.0)
        else:
            print "a"
            other_types = [key for key, val in music_corpus.iteritems()]
            other_types.remove(type)
            random_index = int(math.floor(random.random() * len(other_types)))
            return play(other_types[random_index])
        return play(type)
    else:
        other_types = [key for key, val in music_corpus.iteritems()]
        other_types.remove(type)
        random_index = int(math.floor(random.random() * len(other_types)))
        play(other_types[random_index])

start_dj("pop")
sys.exit()
