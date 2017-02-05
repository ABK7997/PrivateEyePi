import os
import re

#Custom file
import absoluteTime

currentTime = absoluteTime.absoluteTime();

for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    for file in files:

        array = re.findall("\d+", file)
        if (len(array) > 0) :
            dt = int(array[0])

            #delete - currenty measured in seconds
            if (currentTime - dt > 1):
                print "%s was deleted." %file
                os.remove(file);
                
