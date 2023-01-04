import sys
import json
import time
import datetime
from pydub import AudioSegment
from pydub.playback import play

def speak(file_path):
  sound = AudioSegment.from_file(file_path)
  play(sound)

def run_index(json_index, task_index):
  for action in json_index :
    index = action["INDEX"]
    if index == task_index :
      file_path = action["FILE"]
      speak(file_path)

def loop(file_task, file_index):
  loop_go_next = True
  json_task = None
  json_index = None
  with open(file_task, "r") as fp :
    json_task = json.load(fp)

  with open(file_index, "r") as fp :
    json_index = json.load(fp)

  routine_list = json_task["ROUTINE"]
  temperary_list = json_task["TEMPERARY"]

  today =  datetime.datetime.today()
  hour = today.hour
  minute = today.minute
  weekday = today.weekday()
  print(weekday, hour, minute)
  cur_time = "%02d:%02d" % (hour, minute)
  tasks = routine_list[weekday]["TASK"]
  for task in tasks :
    task_time = task["TIME"]
    if cur_time == task_time :
      task_action = task["ACTION"]
      for action_index in task_action :
        run_index(json_index, action_index)

  conf = json_task["GLOBAL"]
  loop_go_next = conf["LOOP_GO_NEXT"]

  return loop_go_next

def help(main_name):
  print(" {} <json task> <json index>".format(main_name))
  sys.exit(1)

def main(argc, argv):
  if argc < 3 :
    help(argv[0])

  file_task = argv[1]
  file_index = argv[2]
  LOOP_GO_NEXT = True

  while LOOP_GO_NEXT :
    LOOP_GO_NEXT = loop(file_task, file_index)
    time.sleep(1)

if __name__ == '__main__':
  main(len(sys.argv), sys.argv)

