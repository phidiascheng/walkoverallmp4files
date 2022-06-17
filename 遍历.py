import os
from moviepy.editor import VideoFileClip

g = open('stats.txt','w')

for root,dirs,files in os.walk("/Apple/Volumes/JMicron"):
	for file in files1:
		if file[-4:] == '.mp4':
			durati = VideoFileClip(file).duration
			volume = os.stat(file).st_size/1024/1024
			g.write(file+'   '+'\t'+'   '+durati+'   '+'\t'+'   '+volume+'\n')
g.close()