from sma_rest.celery import app

from celery.utils.log import get_task_logger

from phonet.phonet import Phonet
from sma_rest.settings import *

import time
import os

"""
Define here the tasks that should be performed asynchronously e.g. the classification tasks
"""

logger = get_task_logger(__name__)

@app.task
def celery_test():
    logger.info('CELERY TEST!')
    time.sleep(10)
    return logger.info("Good night!")


@app.task
def celery_test2(x, y):
    return logger.info(str(x * y))

"""

The classification tasks for the speech exercises.  

"""

@app.task
def phonet_stop(audio_file):
    file_audio = os.path.join(SPEECH_DIR, audio_file)
    logger.info("Audio path: {}".format(file_audio))

    logger.info("PATAKA")
    phon = Phonet(["stop"])
    # get the "stop" phonological posterior from a single file
    file_feat = "phonet/phonclasses/pataka.csv"
    phon.get_phon_wav(file_audio, file_feat, False)
    logger.info("FININSHED PATAKA")

    return logger.info("FINISHED STOP CLASSIFICATION")


@app.task
def phonet_nasal(audio_file):
    file_audio = os.path.join(SPEECH_DIR, audio_file)
    logger.info("Audio path: {}".format(file_audio))

    logger.info("SENTENCE")
    # get the "nasal" phonological posterior from a single file
    file_feat = "phonet/phonclasses/sentence_nasal.csv"
    phon = Phonet(["nasal"])
    phon.get_phon_wav(file_audio, file_feat, False)
    logger.info("FINISHED NASAL SENTENCE")

    return logger.info("FINISHED NASAL CLASSIFICATION")


@app.task
def phonet_strident(audio_file):
    file_audio = os.path.join(SPEECH_DIR, audio_file)
    logger.info("Audio path: {}".format(file_audio))

    logger.info("SENTENCE STRIDENT")
    # get the "strident" phonological posterior from a single file
    file_feat = "phonet/phonclasses/sentence_strident.csv"
    phon = Phonet(["strident"])
    phon.get_phon_wav(file_audio, file_feat, False)
    logger.info("FINISHED STIDENT SENTENCE")

    return logger.info("FINISHED STRIDENT CLASSIFICATION")


@app.task
def phonet_sentence_all(audio_file):
    file_audio = os.path.join(SPEECH_DIR, audio_file)
    logger.info("Audio path: {}".format(file_audio))

    logger.info("SENTENCE ALL")
    # get "all" phonological posteriors from a single file
    file_feat = "phonet/phonclasses/sentence_all.csv"
    phon = Phonet(["strident", "nasal", "back"])
    phon.get_phon_wav(file_audio, file_feat, True)
    logger.info("FINISHED SENTENCE ALL")

    return logger.info("FINISHED SENTENCE ALL CLASSIFICATION")