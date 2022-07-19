import os

folder_path = "D:/university/研一下期/analyse_emotion/pieces_more_info/treated_files/tei2/"
li_files = os.listdir(folder_path)
command0 = "python3 avgEmoValues.py --dataPath ../pieces_more_info/treated_files/tei2/"
command1 = " --lexPath ELAL-als-lexicon.csv --lexNames valence dominance arousal anger anticipation disgust fear joy sadness surprise trust --savePath "
#print(li_files)

xml_csv_command0 = "python3 pieces_more_info/script/emo_xml_treat.py "
xml_csv_command1 = "tei "
with open("command_list_ed_analyse.txt", "w", encoding="utf-8") as cl:
    for f_name in li_files:
        command = command0 + f_name + command1 + f_name[:-8] + "\n"
        #command = xml_csv_command0 + xml_csv_command1 + f_name + "\n"
        cl.write(command)