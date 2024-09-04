# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkja")
    database.push(data)
    database = aws_lib.connect("AKIAF4SADJFR45BAWSZ9", "hjshnk5ex5u32365AWS354/JKGjhz545d89sldjl")
    database.push(data)
