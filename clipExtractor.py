import re

REGULAR_EXPRESSION = r"(\d+) ?: ?(\d+)(?: +)?-(?: +)?(\d+)? ?:? ?(\d+)"
INPUT_FILE = "test.txt"


def getListofMatchesByLine(input_file, pattern):
    
    regex = re.compile(pattern)

    clips = []

    with open(input_file) as designations_file:
        for line in designations_file:
            line_matches = regex.findall(line)
            if line_matches:
                clips.append(regex.findall(line))
        designations_file.close()
    
    return clips

def printClipList(clipList):
    for clip in clipList:
        print("C()\nD()")
        for section in clip:
            s_pg = int(section[0])
            s_ln = int(section[1])
            e_pg = int(section[2])
            e_ln = int(section[3])
            print("%05d:%02d - %05d:%02d" %(s_pg,s_ln,e_pg,e_ln))
        print("\n")

def printProblemClips(clipList):
    for clip in clipList:
        for section in clip:
            if len(section) is 3:
                s_pg = int(section[0])
                s_ln = int(section[1])
                e_pg = s_pg
                e_ln = int(section[2])
            elif len(section) is 4:
                s_pg = int(section[0])
                s_ln = int(section[1])
                e_pg = int(section[2])
                e_ln = int(section[3])
            else:
                print("problem clip(incomplete):")
                print clip
                return True
            if s_pg > e_pg:
                print("problem clip(starts after it ends):")
                print clips
                return True
            if s_ln > 25 or e_ln > 25:
                print("problem clip(line number too high):")
                print clip
                return True
    return False

if not printProblemClips(getListofMatchesByLine(INPUT_FILE, REGULAR_EXPRESSION)):
    printClipList(getListofMatchesByLine(INPUT_FILE, REGULAR_EXPRESSION))









