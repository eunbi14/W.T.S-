# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:48:40 2019

@author: 은비
"""

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/main', methods=['GET'])
def preview():
    
    return render_template('/main/preview.html')