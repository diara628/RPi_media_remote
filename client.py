import Pyro4

media_control = Pyro4.Proxy("PYRONAME:home.media_control")    # use name server object lookup uri shortcut

i = ""
while True:
  i = input("Type command:\n").strip()
  if i== "exit" :
    break
  elif i == "list":
    print(media_control.list_event_names())
  else:
    media_control.send_event(i)
