import pyglet
import time

def play(type):
    edm = pyglet.resource.media('Kav_Verhouzer_LarryKoek_-_People_ft.wav')
    house = pyglet.resource.media('04 Da Funk.wav')
    trap = pyglet.resource.media('01 Know Me.wav')
    rap = pyglet.resource.media('Waves.wav')
    pop = pyglet.resource.media('18 I Really Like You (Liam Keegan Remix Radio Edit).wav')
    player = pyglet.media.Player()
    if type == "same":
        player.queue(house)
    else:
        player.queue(pop)
    player.queue(edm)
    player.volume = 1.0
    while 1:
        try:
            player.play()
            time.sleep(10)
            player.pause()
            return play("same")
            player.next_source()
        except KeyboardInterrupt:
            print "interrupt"
            break

play("a")
sys.exit()
