import Pyro4
import uinput

event_names = """
mute
play
playpause
""".split()

def name2key(name):
  return uinput.__getattribute__("KEY_" + name.upper())

[name2key(n) for n in event_names]

device = uinput.Device([name2key(n) for n in event_names])

class MediaControl(object):
  def send_event(self, name):
    return device.emit_click(name2key(name))

  def list_event_names(self):
    return event_names

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(MediaControl())   # register the greeting maker as a Pyro object
ns.register("home.media_control", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls

