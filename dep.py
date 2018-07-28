# -*- coding:utf-8 -*-

"""
   Http请求控制类，
   dep部门蓝图
"""


__author__ = "qjq"


from flask import Blueprint
from flask import request
from flask import render_template, redirect, url_for, jsonify
from .models import rob_departments, dictionary
from .staticvariable import staticvarcode
import json

dep = Blueprint('dep', __name__,
                 template_folder='templates',
                 static_folder='static')


@dep.route('/editdep', methods=['GET', 'POST'])
def editdep():
    # 根据部门ID更改部门信息#
    formdata = request.form
    tojson = json.dumps(formdata)
    todic = json.loads(tojson)
    todic["changetime"] = staticvarcode._gettime(self=staticvarcode)
    rd = rob_departments()
    res = rd.edit_departments(int(todic["id"]), todic)
    return res


@dep.route('/deldep', methods=['GET', 'POST'])
def deldep():
    # 根据部门ID删除部门信息#
    formdata = request.form
    if len(formdata) > 0:
       depid = formdata["depid"]
       rd = rob_departments()
       res = rd.del_department(depid)
       return res
    else:
        return staticvarcode.FAILURE.value



@dep.route('/cerdepartment', methods=['GET', 'POST'])
def cer_department():
    # 管理员创建部门 #
    depformdata = request.form
    rob_dep = rob_departments()
    if len(depformdata) > 0:
        dep = rob_departments(org_id=depformdata["org_id"], dept_name=depformdata["dept_name"],other=depformdata["other"],
                              dept_sum_peo=depformdata["dept_sum_peo"], status=depformdata["status"],createname=depformdata["createname"],
                              createtime=staticvarcode._gettime(self=staticvarcode))
    flag = rob_dep.add_departments(dep)
    if staticvarcode.SUCCESS.value == flag:
        return staticvarcode.SUCCESS.value
    else:
        return staticvarcode.FAILURE.value


@dep.route('/depinfo', methods=['GET', 'POST'])
def depinfo():
    # 根据部门id获取部门信息#
    depid = request.values.get("depid")
    resultset = dep.get_depbyid(id=depid)
    todic = json.loads(resultset)
    if resultset != staticvarcode.FAILURE.value:
        return render_template('user/dep_info_edit.html', id=todic["id"], dept_name=todic["dept_name"],
                               dept_sum_peo=todic["dept_sum_peo"], other=todic["other"],createname=todic["createname"],
                               createtime=todic["createtime"], status=todic["status"])
    else:
        return staticvarcode.FAILURE.value


@dep.route('/getdept', methods=['GET', 'POST'])
def get_dept():
	# 获取所有部门 #
	# 获取所有部门 #
	# 获取所有部门 #
    # return  :deptjson 部门集合
    orgid = request.values.get("org_id")

        return deptjson
    return jsonify(data=staticvarcode.FAILURE.value)


@dep.route('/getdictbytype', methods=['GET', 'POST'])
def dept():
    # 根据字典类型获取字典值  #
    # return  :字典值json集合
    type = request.values.get("type")
    dic = dictionary()
    deptjson = dic.getdickeyvaluebytype(type=type)
    return deptjson

