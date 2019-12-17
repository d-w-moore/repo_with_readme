#!/bin/bash
while getopts ":d:vk" opt; do
  case $opt in 
    v) echo 'good option! (-v)';;
    k) echo 'good option! (-k)';;
    d) echo 'good option! (-d)' note, using \$OPTARG="$OPTARG";;
    \?) echo 'unrecognized:  ' -$OPTARG;  exit 1;;
    :)  echo 'needs argument:' -$OPTARG;  exit 1;;
  esac
done
