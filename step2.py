from psychopy import visual, event, monitors

mon = monitors.Monitor('ext5k')

win = visual.Window(
    monitor = mon,
    units='deg',
    color=[0, 0, 0],
    fullscr=True,
    screen=1
)

SF = 4.0
SIZE_DEG = 1.0
SEPARATION_LAMBDA = 3.0
offset = SEPARATION_LAMBDA / SF

target = visual.GratingStim(
    win = win,
    tex = 'sin',
    mask = 'gauss',
    size = SIZE_DEG,
    sf = SF,
    ori = 0,
    contrast = 0.15,
    phase = 0.25,
    pos = (0, 0)
)

flanker_top = visual.GratingStim(
    win = win,
    tex = 'sin',
    mask = 'gauss',
    size = SIZE_DEG,
    sf = SF,
    ori = 0,
    contrast = 0.6,
    phase = 0.25,
    pos = (0, offset)
)

flanker_bottom = visual.GratingStim(
    win = win,
    tex = 'sin',
    mask = 'gauss',
    size = SIZE_DEG,
    sf = SF,
    ori = 0,
    contrast = 0.6,
    phase = 0.25,
    pos = (0, -offset)
)

for stim in (flanker_top, target, flanker_bottom):
    stim.draw()

win.flip()
event.clearEvents()
event.waitKeys(keyList=['space', 'escape'])
win.close()

