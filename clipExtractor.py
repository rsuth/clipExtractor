import re
import sys

DESIGNATION_REGEX = r"(\d+) ?: ?(\d+)(?: *)?-(?: *)(\d+)(?::(\d+))?"

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

def printCCS(clipList):
    for clip in clipList:
        print("C()\nD()")
        for section in clip:
            s_pg = int(section[0])
            s_ln = int(section[1])
            if section[3] is '':
                e_pg = s_pg
                e_ln = int(section[2])
            else:
                e_pg = int(section[2])
                e_ln = int(section[3])
            print("%05d:%02d - %05d:%02d" %(s_pg, s_ln, e_pg, e_ln))
        print("\r\n")

def findProblemClips(clipList):
    problemlist = []
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
                problemlist.append(("incomplete", section))
            if s_pg > e_pg or (s_pg == e_pg and s_ln > e_ln):
                problemlist.append(("start before end", section))
            if s_ln > 25 or e_ln > 25:
                problemlist.append(("not valid line number", section))
    return problemlist

clip_list = getListofMatchesByLine(sys.argv[1], DESIGNATION_REGEX)

if findProblemClips(clip_list):
    for p in findProblemClips(clip_list):
        print("Problem: %s (%s)" % (p[1], p[0]))
else:
    printCCS(clip_list)
