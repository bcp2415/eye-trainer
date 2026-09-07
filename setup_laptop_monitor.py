from psychopy import monitors

mon = monitors.Monitor('laptop40')
mon.setWidth(34.4)
mon.setDistance(40)
mon.setSizePix([3840, 2160])
mon.save()

print("saved:", mon.name)
print("width cm:", mon.getWidth())
print("distance cm:", mon.getDistance())
print("size pix:", mon.getSizePix())