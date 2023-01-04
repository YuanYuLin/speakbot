from gtts import gTTS
import json

text_2_voice_list = [
 {"INDEX":"002", "TEXT":"起床了",   "FILE":"wake_up"},
 {"INDEX":"003", "TEXT":"上廁所",   "FILE":"goto_toilet"},
 {"INDEX":"004", "TEXT":"收書包",   "FILE":"school_bag"},
 {"INDEX":"005", "TEXT":"穿衣服",   "FILE":"wear_cloth"},
 {"INDEX":"006", "TEXT":"穿襪子",   "FILE":"wear_sox"},
 {"INDEX":"007", "TEXT":"吃早餐",   "FILE":"eat_breakfast"},
 {"INDEX":"008", "TEXT":"準備出門", "FILE":"ready_to_go"},
 {"INDEX":"009", "TEXT":"穿鞋子",   "FILE":"wear_shoes"},
 {"INDEX":"010", "TEXT":"上學去",   "FILE":"goto_school"}
]

json_list = []
for obj in text_2_voice_list :
  INDEX = obj['INDEX']
  TEXT = obj['TEXT'] 
  FILE = obj['FILE']
  tts = gTTS(text=TEXT, lang='zh-tw')
  tts_file = "/home/vanish/Devel/voices/{}.m4a".format(FILE)
  tts.save(tts_file)
  json_obj = {"INDEX":INDEX, "TEXT":TEXT, "FILE":tts_file}
  print(json_obj)
  json_list.append(json_obj)

with open("tts_index.json", "w") as outfile:
    json.dump(json_list, outfile)

