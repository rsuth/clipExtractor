import re
import sys

DESIGNATION_REGEX = r"(\d+) ?: ?(\d+)(?: *)?-(?: *)(\d+)(?::(\d+))?"
INITIALS = "TK"


class Segment:
    def __init__(self):
        self.start_page = 0
        self.start_line = 0
        self.end_page = 0
        self.end_line = 0


class Clip:
    def __init__(self):
        self.name = ''
        self.desc = ''
        self.segments = []


def getListofMatchesByLine(input_file, pattern):
    regex = re.compile(pattern)
    matches = []
    with open(input_file) as designations_file:
        for line in designations_file:
            line_matches = regex.findall(line)
            if line_matches:
                clips.append(regex.findall(line))
        designations_file.close()
    return matches


def printCCS(clipList):
    for clip in clipList:
        print("C(%s)\nD(%s)" % (clip.name, clip.desc))
        for segment in clip.segments:
            print("%05d:%02d - %05d:%02d" % (segment.start_page,
                                             segment.start_line, segment.end_page,
                                             segment.end_line))
        print("\r\n")


def findProblemClips(clipList):
    problemlist = []
    for clip in clipList:
        for section in clip:
            s_pg = int(section[0])
            s_ln = int(section[1])
            if section[3] is '':
                e_pg = s_pg
                e_ln = int(section[2])
            else:
                e_pg = int(section[2])
                e_ln = int(section[3])
            if s_pg > e_pg or (s_pg == e_pg and s_ln > e_ln):
                problemlist.append(("start before end", section))
            if s_ln > 25 or e_ln > 25:
                problemlist.append(("not valid line number", section))
    return problemlist


def buildClips(clipList):
    built_clips = []
    for clip in clipList:
        c = Clip()
        for section in clip:
            s = Segment()
            s.start_page = int(section[0])
            s.start_line = int(section[1])
            if section[3] is '':
                s.end_page = s.start_page
                s.end_line = int(section[2])
            else:
                s.end_page = int(section[2])
                s.end_line = int(section[3])
            c.segments.append(s)
        c.name = "%s%03dL%02d-%03dL%02d" % (INITIALS, c.segments[0].start_page,
                                            c.segments[0].start_line, c.segments[-1].end_page,
                                            c.segments[-1].end_line)
        built_clips.append(c)
    return built_clips


found_clips = getListofMatchesByLine(sys.argv[1], DESIGNATION_REGEX)

if findProblemClips(found_clips):
    for p in findProblemClips(found_clips):
        print("Problem: %s (%s)" % (p[1], p[0]))
else:
    clips = buildClips(found_clips)
    printCCS(clips)
