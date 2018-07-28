from flask import Blueprint, request
from .models import rob_Chat_Record
from .staticvariable import staticvarcode
from .wordtest import createWordCloud
import json
import os
path = os.path.abspath("./app/word/")

record = Blueprint('record', __name__)

@record.route('/queryrecord', methods=['GET','POST'])
def queryRecord():
    rc = rob_Chat_Record()
    chstart = request.values.get("chrtstarttime")
    chend = request.values.get("chrtendtime")
    accorduser = request.values.get("accorduser")
    accordrobot = request.values.get("accordrobot")
    if chstart == None and chend == None and accorduser == None and accordrobot == None:
        flag = staticvarcode.FAILURE.value
    else:
        flag = staticvarcode.SUCCESS.value
    resultSet = rc.getchatlog(chstart=chstart, chend=chend, accordrobot=accordrobot, accorduser=accorduser, flag=flag)
    if resultSet != staticvarcode.FAILURE.value:
        result = ""
        data = json.loads(resultSet)
        for record in data:
            result += str(record['save_info'])
        createWordCloud(result, path + r"/text.txt", path + r"/alice.jpg", path + "/a.jpg")
        return staticvarcode.SUCCESS.value
    else:
        return staticvarcode.FAILURE.value
