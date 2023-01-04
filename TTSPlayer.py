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

def run_with_task(json_index, tasks, cur_time):
  for task in tasks :
    task_time = task["TIME"]
    if cur_time == task_time :
      task_action = task["ACTION"]
      for action_index in task_action :
        run_index(json_index, action_index)

def run_routine_task(json_index, routine_list, cur_time, weekday):
  tasks = routine_list[weekday]["TASK"]
  run_with_task(json_index, tasks, cur_time)

def run_temperary_task(json_index, temperary_list, cur_time, cur_date):
  for temp in temperary_list :
    temp_date = temp["DATE"]
    if cur_date == temp_date :
      tasks = temp["TASK"]
      run_with_task(json_index, tasks, cur_time)

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
  weekday = today.weekday()
  cur_date = "%d/%02d/%02d" % (today.year, today.month, today.day)
  cur_time = "%02d:%02d" % (today.hour, today.minute)
  #print(cur_date, cur_time)

  run_routine_task(json_index, routine_list, cur_time, weekday)
  run_temperary_task(json_index, temperary_list, cur_time, cur_date)

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

