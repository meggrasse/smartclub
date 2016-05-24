import pyglet
import time
player = pyglet.media.Player()
beep = pyglet.resource.media('beep-01a.wav')
player.queue(beep)
player.play()
edm = pyglet.resource.media('Kav_Verhouzer_LarryKoek_-_People_ft.wav')
house = pyglet.resource.media('04 Da Funk.wav')
trap = pyglet.resource.media('01 Know Me.wav')
rap = pyglet.resource.media('Waves.wav')
pop = pyglet.resource.media('18 I Really Like You (Liam Keegan Remix Radio Edit).wav')
player.queue(house)
player.queue(trap)
player.queue(rap)
player.queue(pop)
player.volume = 1.0
while 1:
    try:
        player.play()
        time.sleep(15)
        player.next_source()
    except KeyboardInterrupt:
        print "interrupt"
        break


player.pause()
pyglet.app.run()
