import random
from psychopy import visual, event, core, monitors, data

mon = monitors.Monitor('laptop40')

win = visual.Window(
    monitor=mon,
    units='deg',
    color=[0, 0, 0],
    fullscr=True,
    screen=0
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
    message.text = str(number)
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

    return int(keys[0]) == target_interval

staircase = data.StairHandler(
    startVal=0.20,
    stepSizes=[0.25, 0.15, 0.10, 0.05],
    stepType='log',
    nUp=1,
    nDown=3,
    nReversals=8,
    nTrials=50,
    minVal=0.001,
    maxVal=1.0
)

for contrast in staircase:
    result = run_trial(contrast)
    if result is None:
        break
    staircase.addResponse(int(result))

reversals = staircase.reversalIntensities
print("reversals:", reversals)
if len(reversals) >= 6:
    threshold = sum(reversals[-6:]) / 6
    print("threshold estimate:", threshold)

win.close()
core.quit()