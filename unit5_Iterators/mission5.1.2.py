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
i = 0
notes_split = notes.split("-")
print(notes_split[0].split(',')[0])
print(notes_split[0].split(',')[1])
print(freqs.get(notes_split[0].split(',')[0]))
for note in notes_split:
    winsound.Beep(freqs.get(note[0].split(',')[0]), int(note[0].split(',')[1]))

