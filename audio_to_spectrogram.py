import sunau
import os
import pylab


genres = ["blues","classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]

def graph_spectrogram(au_file,i,j,name):
    sound_info, frame_rate = get_info(au_file,name)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)

    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('images/spectrogram'+str(j)+str(i)+'.png')
    pylab.close()


def get_info(au_file,name):
    file = sunau.open("genres/"+name+"/"+au_file, 'r')
    frames = file.readframes(file.getnframes())
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = file.getframerate()
    file.close()
    return sound_info, frame_rate


def loadData():

    bluesList = os.listdir("genres/blues")
    classicalList = os.listdir("genres/classical")
    countryList = os.listdir("genres/country")
    discoList = os.listdir("genres/disco")
    hiphopList = os.listdir("genres/hiphop")
    jazzList = os.listdir("genres/jazz")
    metalList = os.listdir("genres/metal")
    popList = os.listdir("genres/pop")
    reggaeList = os.listdir("genres/reggae")
    rockList = os.listdir("genres/rock")

    listAll = [bluesList,classicalList,countryList,discoList,hiphopList,jazzList,metalList,popList,reggaeList,rockList]

    j=0

    for genre in listAll:
        i=0
        if j == 0:
            name = "blues"
        elif j == 1:
            name = "classical"
        elif j == 2:
            name = "country"
        elif j == 3:
            name = "disco"
        elif j == 4:
            name = "hiphop"
        elif j == 5:
            name = "jazz"
        elif j == 6:
            name = "metal"
        elif j == 7:
            name = "pop"
        elif j == 8:
            name = "reggae"
        elif j == 9:
            name = "rock"
        for song in listAll[j]:
            # print(song)
            graph_spectrogram(song,i,j,name)
            i=i+1
        j=j+1


if __name__ == '__main__':
    loadData()

