concatvideos
============

Simple tool for joining two or more video files from the command line.

## Dependencies
* Python 3
* ffmpeg

## Usage
```
usage: concatvideos.py [-h] output paths [paths ...]
Concatenate video files of type MOV or MP4.
positional arguments:
  output      Output file. Should be something like 'out.mp4'.
  paths       Paths to each video file. If the path to a directory is given,
              this means that all the video files in that directory will be
              joined, not including subdirectories.
optional arguments:
  -h, --help  show this help message and exit
```

## Examples
```
$ ls
a.mp4 b.mp4 c.mp4
$ concatvideos.py ./abc.mp4 .
$ ls
a.mp4 b.mp4 c.mp4 abc.mp4
$ concatvideos.py ./cb.mp4 c.mp4 a.mp4
$ ls
a.mp4 b.mp4 c.mp4 cb.mp4 abc.mp4
```
