#!/usr/bin/env python3
# simple ear training program
from os import system
from random import randint, choice

##########################
# A few sets of intervals you can use
majorscale_tones = [-12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12] # major scale intervals
big_tones = [-16,-15,-15,-14,-13,-12,-11,-10,-9,-8, 8,9,10,11,12,13,14,15,16] # minor sixth to major tenth
##########################

interval_names = { 0: 'perfect unison', 1: 'minor second', 2: 'major second', 3: 'minor third', 4: 'major third', 5: 'perfect fourth', 6: 'tritone', 7: 'perfect fifth', 8: 'minor sixth', 9: 'major sixth', 10:'minor seventh', 11: 'major seventh', 12: 'perfect octave', 13: 'minor ninth', 14: 'major ninth', 15: 'minor tenth', 16: 'major tenth' }

###########################
# Use this to customize
n = 3 # number of notes to play
interval_list = majorscale_tones # list of intervals
repetitions = 2 # number of times to repeat intervals
##########################

while True: 
    # generate list of tones
    tonic = randint(-12, 12)
    intervals = [ choice(interval_list) for i in range(n-1) ]
    
    cmd = '''play -q "|sox -np synth 2 pluck %''' + str(tonic) + '''"'''
    for note in intervals:
        cmd = cmd + ''' "|sox -np synth 2 pluck %''' + str(tonic + note) + '''"'''
    cmd = cmd + ' -t alsa'

    # play interval
    for i in range(repetitions):
        input('press enter to listen (repetition ' + str(i) + '/' + str(repetitions) + ')')
        system(cmd)
    
    # reveal answer
    input('press enter to reveal answer...')
    for j, note in enumerate(intervals):
        if note > 0:
            print('interval ' + str(j+1) + ': ' + interval_names[note] + ' above')
        elif note < 0:
            print('interval ' + str(j+1) + ': ' + interval_names[-note] + ' below')
        else:
            print('interval ' + str(j+1) + ': ' + interval_names[note])

    print('\n\n')
