import shutil

from api.models import SpeechEx
from sma_rest.settings import local
import os
import subprocess


def decode_process(patient_id):
    KALDI_ROOT = os.getenv("KALDI_ROOT")
    if not os.path.isdir(KALDI_ROOT + "/src/bin"):
        print("No Kaldi root. Export it.")
        return
    INTEL_ROOT  =  os.getenv("INTEL_ROOT")
    if not os.path.isdir(INTEL_ROOT + "/decode"):
        print("No Intel Root. Export it.")
        return
    print(KALDI_ROOT)
    os.environ["PATH"] += os.pathsep + KALDI_ROOT + "/src/bin"  # change path in the server
    entries = SpeechEx.objects.filter(patient_id=patient_id, is_done=False, task_kind='1')
    i = 0
    wav_string = ""
    utt2spk = ""
    if entries:
        for entry in entries:
            wav_string += str(i) + "-" + entry.recording_file.name + " " + entry.recording_file.path + "\n"
            utt2spk += str(i) + "-" + entry.recording_file.name + " " + str(patient_id) + "\n"
            i += 1
        path_temp = INTEL_ROOT + "/decode/" + str(patient_id)
        if not os.path.isdir(path_temp):
            os.makedirs(path_temp)
            with open(path_temp + "/wav.scp", "w") as f:
                f.write(wav_string)
            with open(path_temp + "/utt2spk", "w") as f:
                f.write(utt2spk)
            with open(path_temp + "/text", "w") as f:
                f.write(utt2spk)
            subprocess.run('./transcript.sh ' + path_temp, cwd=local.INTEL_ROOT, stdout=True, shell=True)
            with open(path_temp + '/transcript') as f:
                text = f.readlines()
                for line in text:
                    import re
                    temp = line.split()
                    index = temp[0].split('-')[0]
                    sentence = temp[0].split('_')[2]
                    transcription = " ".join(temp[1:])
                    entry = entries[int(index)]
                    entry.transcription = transcription
                    process = subprocess.run(
                        'compute-wer --text  --mode=present \"ark:decode/ref_text\" '
                        '\"ark:echo {} {} |\"'.format(sentence, transcription), cwd=local.INTEL_ROOT,
                        stdout=subprocess.PIPE, universal_newlines=True, shell=True)
                    wer = process.stdout
                    wer = re.sub(r'%WER (\d{1,}.\d{1,}).*\n.*\n.*\n', r'\1', wer)
                    entry.is_done = True
                    entry.wer = wer
                    entry.save()
            shutil.rmtree(path_temp)
