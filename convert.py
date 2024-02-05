# import required module
import os
import subprocess
# assign directory
directory = 'Videos'

# iterate over files in
# that directory
for filename in os.listdir(directory):

    # checking if it is a file
    if os.path.isfile(os.path.join(directory, filename)):
        filename_short = filename.split(".")[0]
        os.system(f"MP4Box -add {directory}/{filename_short}.h264 {directory}/MP4/{filename}.mp4") 
