from fastapi import APIRouter, HTTPException
from datetime import timedelta
import random
import pymysql
from fastapi.responses import StreamingResponse
from fastapi.responses import UJSONResponse

from identify.core.config import settings
from identify.db.connect import red, read

router = APIRouter()


@router.get('/{code}')
async def identify(code):
    n = random.randint(1, 10000 + 1)
    file_path = 'C:/Users/Administrator/Desktop/identify_code/identify/static/{}.png'.format(n)
    img = open(file_path, "rb")
    # n -> true num
    # mysql 储存的
    true_num = read(n)
    # print(true_num)
    # code 与 true num 之间的orm 放到redis之中
    try:
        red.setex('image_code_{}'.format(code), settings.EXPIRE_TIME, true_num)
    except Exception as e:
        print(e)
    return StreamingResponse(img)


if __name__ == '__main__':
    pass
