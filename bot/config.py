#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = 8569540
    API_HASH = "7643fb62451cd21337678f1f241f7b79"
    BOT_TOKEN = "5310112270:AAEa-6-kXeBDxDJWLV7IN2wD5onuscXBSxk"
    DEV = 766289260
    OWNER = 1722652154
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By DV Movies (https://t.me/dvmoviesbackup)' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
