import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
notes_split = notes.split("-")

for i in range(0, len(notes_split)):
    winsound.Beep(freqs.get(notes_split[i].split(',')[0]), int(notes_split[i].split(',')[1]))


