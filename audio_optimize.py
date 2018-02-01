from pydub import AudioSegment
import sys
import os

#functions for trimming sound at start and end
def find_silence_start(sound, threshold = -50.0, step_size = 10):
    start_ms = 0
    assert step_size > 0
    while sound[start_ms : start_ms + step_size].dBFS < threshold and start_ms < len(sound):
        start_ms += step_size
    return start_ms

def get_filenames(directory, extension):
    filenames = []
    for fn in os.listdir(directory):
        if fn.endswith(extension):
            filenames.append(fn)
    return filenames

def get_trimmed_sound(sound):
    trim_start = find_silence_start(sound)
    trim_end = find_silence_start(sound.reverse())
    duration = len(sound)
    
    trimmed = sound[trim_start : duration - trim_end]

    return trimmed

#functions for going from stereo to mono
def to_mono(stereo):
    return stereo.set_channels(1)

#functions for normalizing
def normalize(sound, target_dBFS):
    delta = target_dBFS - sound.dBFS
    return sound.apply_gain(delta)


####

dir_in = sys.argv[1]
dir_out = sys.argv[2]
ext_in = sys.argv[3]
ext_out = sys.argv[4]

#optimize sound files
print("Creating output directory " + dir_out + " if not present")

if not os.path.exists(dir_out):
    os.makedirs(dir_out)

for filename_with_ext in (get_filenames(dir_in, ext_in)):
    
    filename = os.path.splitext(filename_with_ext)[0]
    f_in = dir_in + "/" + filename_with_ext
    
    print("Reading " + f_in)

    sound = normalize(to_mono(get_trimmed_sound(AudioSegment.from_file(f_in, format = ext_in))), -20.0)
    
    f_out = dir_out + "/" + filename + "." + ext_out

    print("Writing to " + f_out)
    
    sound.export(f_out, format = ext_out)

