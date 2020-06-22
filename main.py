import os
f1 = open("song.txt", "r+")
z = f1.readlines()
a = z[0]
a = a.split(",")

#a.replace("\n", 'a')

f1.close()


os.chdir("/home/adarsha/Music")
os.system("pwd")
n = len(a)
i = 0
while i < n:
    link = a[i]
    song_link = "youtube-dl -x --audio-format mp3 "+link
    os.system(song_link)
    i = i+1
