from psychopy import visual, event

win = visual.Window(
    size=[800, 600],
    units='pix',
    color=[0, 0, 0],
    fullscr=False
)

target = visual.GratingStim(
    win = win,
    tex = 'sin',
    mask = 'gauss',
    size = 128,
    sf = 0.05,
    ori = 0,
    contrast = 0.5,
    phase = 0.25
)

target.draw()
win.flip()

event.clearEvents()
event.waitKeys(keyList=['space'])
print(win.getActualFrameRate())
win.close()