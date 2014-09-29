#!/usr/bin/python3

# Joins all *.MOV files in the specified directory in alphabetical order.

from subprocess import Popen,PIPE
import argparse
import os

filetypes = {'mov','mp4'}

"""
'~/videos/' |-> ['~/videos/a.mp4','~/videos/b.mp4']
"""
def ls(path):
    files = [os.path.join(path,f) for f in os.listdir(path) if any([f.endswith(ft) for ft in filetypes])]
    files.sort()
    return files

"""
Given a list of paths to video files and the path of the output file,
merges the video files in the order they appeared in the list.
The commands will be executed in the directory of the first video file, and the path of the
specified output file will be relative to it.
"""
def join(files,output):
    if not files:
        return
    dirpath = os.path.dirname(files[0])
    for f in files:
        cmd = 'ffmpeg -i %s -c copy -bsf:v h264_mp4toannexb -f mpegts %s.ts'% (f,f)
        proc = Popen(cmd.split(),stdout=PIPE,cwd=dirpath)
        proc.wait()
    joinstr = 'concat:%s'% '|'.join(['%s.ts'% f for f in files])
    cmd = 'ffmpeg -i %s -c copy -bsf:a aac_adtstoasc %s'% (joinstr,output)
    proc = Popen(cmd.split(),stdout=PIPE,cwd=dirpath)
    proc.wait()
    for f in files:
        cmd = 'rm %s.ts'% f
        proc = Popen(cmd.split(),stdout=PIPE,cwd=dirpath)
        proc.wait()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
Concatenate video files of type MOV or MP4.
""")
    parser.add_argument('output',help="Output file. Should be something like 'out.mp4'.")
    parser.add_argument('paths',nargs='+',help="""Paths to each video file. If the path to a
    directory is given, this means that all the video files in that directory will be joined,
    not including subdirectories.""")
    args = parser.parse_args()

    files = [x for y in [ls(p) if not any([p.lower().endswith('.%s'% ft) for ft in filetypes]) else [p] for p in args.paths] for x in y]
    join(files,args.output)

