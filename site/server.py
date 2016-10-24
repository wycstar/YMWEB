#!/usr/bin/python python
# -*- coding: utf-8 -*-

from flask import Flask, url_for, render_template, request, redirect, session
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, validators
from getGoogleResult import *
from getZhihuResult import *
import globals
app = Flask(__name__)
app.config['SECRET_KEY'] = '0oauiocc'


class textQueryInput(Form):
    keyword = StringField('', [validators.Required(),
                               validators.Length(1, 40)])
    submit = SubmitField('搜 索')


@app.route('/', methods=['GET', 'POST'])
def index():
    indexForm = textQueryInput(request.form)
    if indexForm.validate_on_submit():
        return redirect(url_for('search_result', keyword=indexForm.keyword.data, pageNum=1))
    return render_template('index.html', form=indexForm)


@app.route('/s/<keyword>/<int:pageNum>', methods=['GET', 'POST'])
def search_result(keyword, pageNum):
    queryForm = textQueryInput(request.form)
    rawContent = getRawContent(keyword, pageNum)
    webResult = getResultList(rawContent)
    if queryForm.validate_on_submit():
        return redirect(url_for('search_result', keyword=queryForm.keyword.data, pageNum=1))
    queryForm.keyword.data=keyword
    return render_template('result.html',
                           keyword=keyword,
                           resultNum=globals.resultSum[0],
                           resultTime=globals.resultTime[0],
                           webResultSet=webResult,
                           zhihuResultSet=getZhiHuResultList(keyword)
                                          if session.get(keyword) is None
                                          else session.get(keyword),
                           currentPage=pageNum,
                           queryForm=queryForm)


@app.route('/killIE')
def killIE():
    return render_template('killIE.html')


if __name__ == '__main__':
    # indexForm = textQueryInput()
    # print(str(indexForm.q))
    # print(str(indexForm.s))
    app.run(host='0.0.0.0', debug=True, port=5000)
