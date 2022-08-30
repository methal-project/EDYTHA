#### The final improvements, mostly for generating file paths.

##### pre_treatment

**without specified folder:**
```
python3 pre_treatment/script/emo_xml_treat.py --dir tei-lustig --filename am-letzte-maskebal.xml 
```
**with specified folder to save csv files:**
```
python3 pre_treatment/script/emo_xml_treat.py --dir tei-lustig --filename am-letzte-maskebal.xml --savepath pre_treatment/new_folder
```

##### intermediate
Only file variant_idf_phrases.py has been modified.
```
python3 variant_idf_phrases.py
ou
python3 variant_idf_phrases.py ../pre_treatment/new_folder
``` 
So you can read files from the folder you created before, or if you add nothing, the script reads from the default folder: pre_treatment/treated_files

##### emotions

I changed --savePath, and created a new folder with the name: new_folder
```
python3 avgEmoValues.py --dataPath ../pre_treatment/treated_files/am-letzte-maskebal.out.csv --lexPath ELAL-als-lexicon.csv --lexNames valence dominance arousal anger anticipation disgust fear joy sadness surprise trust --savePath ../new_folder/am-letzte-maskebal --mode tf_idf_phrases
```
*In pre-graphic.py*:
Use ```python3 pre-graphic.py ../new_folder``` to pre-graphic files in ../new_folder made in previous step

```
python3 pre-graphic.py
ou
python3 pre-graphic.py ../new_folder
```

*In split_plays.py*:
Use ```python3 split_plays.py ../new_folder``` with files in ../new_folder made in previous step

```
python3 split_plays.py
ou
python3 pre-graphic.py ../new_folder
```
