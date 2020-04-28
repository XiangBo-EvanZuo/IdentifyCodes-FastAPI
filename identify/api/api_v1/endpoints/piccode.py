from fastapi import APIRouter, HTTPException, Query
from datetime import timedelta
import random
import pymysql
from fastapi.responses import StreamingResponse
from fastapi.responses import UJSONResponse
from pydantic import BaseModel

from identify.core.config import settings
from identify.db.connect import red, read

router = APIRouter()


class Item(BaseModel):
    uid: str
    answer: str


class ReturnItems(BaseModel):
    error: str


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
    # 验证一下是否有code存在
    identify_code = 'image_code_'+code
    if not red.exists(identify_code):
        try:
            red.setex('image_code_{}'.format(code), settings.EXPIRE_TIME, true_num)
        except Exception as e:
            print(e)
    return StreamingResponse(img)



@router.post('/code/confirm/', response_model=ReturnItems)
async def dec(item: Item):
    if red.exists(item.uid):
        true = red.get(item.uid).decode('ascii')
        if true == item.answer:
            return {'error': '验证码正确'}
        return {'error': '验证码错误'}
    else:
        return {'error': '验证码不存在'}


@router.post('/code/confirm1/', response_model=ReturnItems)
async def decs(uid, answer):
    if red.exists(uid):
        true = red.get(uid).decode('ascii')
        if true == answer:
            return {'error': '验证码正确'}
        return {'error': '验证码错误'}
    else:
        return {'error': '验证码不存在'}

if __name__ == '__main__':
    pass
