# TODO: add type, size, genre, bitrate, length, filename ... if possible all tags
# TODO: remove blanks in the csv
# TODO: save song cover image filename as the song filename 

# TODO: upload all images and csv info to firebase: images have a reference to the document


import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2
import os 
import csv

#use if no metadata available
def splitter(filename):
    culled = filename[:-4]
    culled = filename[12:len(culled)]
    s = culled.split(" - ")
    return [s[1],s[0],"",""]

def rmmp3(filename):
    return filename[:-4]

def reader(directory):
    with open("song_metadata.csv",mode="w") as song_metadata:
        writer = csv.writer(song_metadata, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Title","Artist","Album","Year"])

        for filename in os.listdir(directory):
            if filename.endswith(".mp3"):
                #print(filename)
                fullname = os.path.join(directory,filename)
                dic = mutagen.File(fullname).keys()
                lookfor=["TIT2","TPE1","TPE2","TALB","TDRC"]
                towrite=[]
                tpe1=""
                tpe2=""
                for s in lookfor:
                    if mutagen.File(fullname).tags is None:
                        towrite = splitter(fullname)
                        continue
                    else:
                        for frame in mutagen.File(fullname).tags.getall(s):
                            if s=="TPE1":
                                tpe1=frame
                            elif s =="TPE2":
                                tpe2=frame
                                if tpe1==tpe2:
                                    towrite.append(tpe1)
                                else:
                                    ss = str(tpe1) + " " + str(tpe2)
                                    towrite.append(ss)
                            else:
                                towrite.append(frame)
                            #print(frame)

                writer.writerow(towrite)


def main():
    directory = "../example set"
    reader(directory)
    #imager(directory)



if __name__ == "__main__":
    main()