import random
from psychopy import visual, event, core, monitors

mon = monitors.Monitor('ext5k')

win = visual.Window(
    size=[5120, 2880],
    monitor = mon,
    units = 'deg',
    color = [0, 0, 0],
    fullscr = True,
    screen = 1
)

SF = 4.0
SIZE_DEG = 1.0
SEPARATION_LAMBDA = 3.0
FLANKER_CONTRAST = 0.6
offset = SEPARATION_LAMBDA / SF

target = visual.GratingStim(
    win=win,
    tex='sin',
    mask='gauss',
    size=SIZE_DEG,
    sf=SF,
    ori=0,
    phase=0.25,
    pos=(0, 0)
)

flanker_top = visual.GratingStim(
    win=win,
    tex='sin',
    mask='gauss',
    size=SIZE_DEG,
    sf=SF,
    ori=0,
    contrast=FLANKER_CONTRAST,
    phase=0.25,
    pos=(0, offset)
)

flanker_bottom = visual.GratingStim(
    win=win,
    tex='sin',
    mask='gauss',
    size=SIZE_DEG,
    sf=SF,
    ori=0,
    contrast=FLANKER_CONTRAST,
    phase=0.25,
    pos=(0, -offset)
)

fixation = visual.TextStim(
    win=win,
    text='+',
    height=0.5,
    color='white'
)

message = visual.TextStim(
    win=win,
    text='',
    height=0.6,
    color='white',
    pos=(0, -4)
)

def show_interval(number, target_present, contrast):
    message.text = str(number),
    message.draw()
    fixation.draw()
    flanker_top.draw()
    flanker_bottom.draw()
    if target_present:
        target.contrast = contrast
        target.draw()
    win.flip()
    core.wait(0.5)
    win.flip()
    core.wait(0.4)

def run_trial(contrast):
    target_interval = random.choice([1, 2])

    fixation.draw()
    win.flip()
    core.wait(0.6)

    show_interval(1, target_interval == 1, contrast)
    show_interval(2, target_interval == 2, contrast)

    message.text = 'Which interval? 1 or 2'
    message.draw()
    win.flip()

    event.clearEvents()
    keys = event.waitKeys(keyList=['1', '2', 'escape'])

    if 'escape' in keys:
        return None

    response = int(keys[0])
    return response == target_interval

instructions = visual.TextStim(
    win=win,
    text=("Two intervals will be shown, marked 1 and 2. \n\n"
          "A faint patch appears between the two bright ones\n"
          "in ONE of them.\n\n"
          "Press 1 or 2 to say which.\n\n"
          "Keep your eyes on the center.\n\n"
          "Press space to begin."),
    height=0.7,
    color='white',
    wrapWidth=20
)

instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])


correct = run_trial(0.01)
print("correct:", correct)

win.close()
core.quit()