from psychopy import monitors

mon = monitors.Monitor('ext5k')
mon.setWidth(59.7)
mon.setDistance(70)
mon.setSizePix([5120, 2880])
mon.save()

print("saved:", mon.name)
print("width cm:", mon.getWidth())
print("distance cm:", mon.getDistance())
print("size pix:", mon.getSizePix())