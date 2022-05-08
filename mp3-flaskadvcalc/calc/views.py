import csv
import os

from flask import Blueprint, request, render_template, flash, url_for
from flask_login import current_user
from sqlalchemy.exc import SQLAlchemyError

import calc.MyCalc
from base_model import db
from werkzeug.utils import redirect
import math
import statistics
import scipy.stats as stat
import pandas as pd
from statistics import variance
import numpy as np
from statistics import stdev
from .models import SimpleHistory
import ast, math


c = calc.MyCalc.AdvMyCalc()  # here the state is persisted between requests (note it may be shared across users)
mycalc = Blueprint('mycalc', __name__, url_prefix='/mycalc')


def do_adv_calc(eq_ad):
    data_list = eq_ad.split(":")
    ch = data_list[1]
    res = "unsupported"
    try:

        if ch == "SquareA":
            n = int(data_list[0])
            res = n * n
            print('Square of the number is', n * n)

        elif ch == "SquarerootA":
            n = int(data_list[0])
            res = math.sqrt(n)
            print('the Square root of the number is {0}'.format(math.sqrt(n)))

        elif ch == 'MeanA':
            n = (data_list[0])
            v = n.split(' ')
            sum = 0
            for e in v:
                sum = sum + int(e)
            print("The Population Mean is {0}".format(sum / len(v)))
            res = (sum / len(v))

        elif ch == 'MedianA':
            n = list(map(int, data_list[0].split()))
            print('the medain of the numbers is {0}'.format(statistics.median(n)))
            res = statistics.median(n)
        elif ch == 'ModeA':
            n = list(map(int, data_list[0].split()))
            print("the mode of the given numbers is {0}".format(statistics.mode(n)))
            res = statistics.mode(n)
        elif ch == 'sampleStandardDeviationA':
            n = list(map(int, data_list[0].split()))
            print('The Population standard deviation is {0}'.format(statistics.stdev(n)))
            res = statistics.stdev(n)
        elif ch == 'VaA':
            n = list(map(int, data_list[0].split()))
            print('The variance of Population proportion is {0}'.format(statistics.variance(n)))
            res = statistics.variance(n)
        elif ch == 'ZsA':
            n = list(map(int, data_list[0].split()))
            print('The Z score is {0}'.format(stat.zscore(n)))
            res =stat.zscore(n)


        elif ch == 'CinA':
            n = list(map(int, input('Enter numbers: ').split()))
            print(stat.t.interval(alpha=0.99, df=len(n) - 1, loc=np.mean(n), scale=stat.sem(n)))
            res = stat.t.interval(alpha=0.99, df=len(n) - 1, loc=np.mean(n), scale=stat.sem(n))
        elif ch == 'PvarA':
            n = list(map(int, data_list[0].split()))
            print('The population variance is {0}'.format(variance(n)))
            res = variance(n)
        elif ch == 'PvalA':
            p_value = stat.norm.sf(abs(-0.67))
            print('p value is : ' + str(p_value))
            res  = p_value

        elif ch == 'SamplemeanA':
            n = list(map(int, data_list[0].split()))
            print("the sample mean is {0}".format(statistics.mean(n)))
            res = statistics.mean(n)
        elif ch == 'SmA':
            n = list(map(int, data_list[0].split()))
            print(stdev(n))
            res = stdev(n)

        elif ch == 'variance of sample proportionA':
            n = list(map(int, data_list[0].split()))
            res = statistics.variance(n)
    except:
        res = "ERROR"
    if not current_user.is_anonymous:
        sh = SimpleHistory(eq=eq_ad, result=res, user_id=current_user.id)
        db.session.add(sh)
        try:
            db.session.commit()
            print("Recorded calculation history")
            flash("Recorded calculation history", "success")
        except SQLAlchemyError as e:
            print(e)
            flash(str(e), "error")
            db.session.rollback()
    return render_template("my_calc.html", result=res, eq=data_list[0])

@mycalc.route('/history', methods=['GET'])
def get_history():
    if not current_user.is_anonymous:
        results = SimpleHistory.query.filter_by(user_id=current_user.id).order_by(SimpleHistory.created.desc()).limit(
            10).all()
        print(results)
    else:
        results = []
    return render_template("calc-history.html", history=results)


@mycalc.route('/upload', methods=['GET', 'POST'])
def upload_csv():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        print(uploaded_file.filename)
        uploaded_file.save(uploaded_file.filename)
        checks = calc.MyCalc.AdvMyCalc.ops
        try:
            with open(uploaded_file.filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                for row in csv_reader:
                    equation = row[0]
                    print(f'Column names are {", ".join(row)}')
                    for check in checks:
                        print(check)
                        if check in equation:
                            nums = equation.split(check)
                            if nums[0] == '':
                                nums[0] = "ans"
                            try:
                                r = evaluate(equation)
                                print("R is " + str(r))
                            except:
                                r = "ERROR"
                            if not current_user.is_anonymous:
                                sh = SimpleHistory(eq=equation, result=r, user_id=current_user.id)
                                db.session.add(sh)
                                try:
                                    db.session.commit()
                                    print("Recorded calculation history")
                                    flash("Recorded calculation history", "success")
                                except SQLAlchemyError as e:
                                    print(e)
                                    flash(str(e), "error")
                                    db.session.rollback()
                    # TODO pass data to calculator to run/execute and add to history
        except Exception as e:
            print('An exception occurred: {}'.format(e))
        finally:
            os.remove(uploaded_file.filename)
            print("Deleted uploaded file")
    return redirect(url_for("mycalc.do_calc"))


@mycalc.route('/', methods=['GET', 'POST'])
def do_calc():
    # c = calc.MyCalc.AdvMyCalc() # here the state resets each time

    data = request.form
    iSTR = data.get("eq")


    if iSTR == "deleteall":
        del_all = SimpleHistory.query.filter_by(user_id=current_user.id)
        del_all.delete()
        print("deleintg")
        db.session.commit()
        iSTR= None
        return render_template("my_calc.html")

    chk = ":"
    chk_del = ""
    if data.get("result") is not None:
        chk_del = data.get("result")
    if iSTR is not None and "load" not in iSTR and "delete" not in chk_del:
        if chk in iSTR:
            do_adv_calc(iSTR)
            iSTR=None

    loadHistory = data.get("loadHistory", 0, type=int) > 0
    if iSTR is not None:
        checks = calc.MyCalc.AdvMyCalc.ops
        r = "UNSUPPORTED"
        if loadHistory:
            r = data.get("result")
            r.replace("load", "")
            if r == "delete":
                record = SimpleHistory.query.filter_by(eq=iSTR)
                record.delete()
                print("deleintg")
                db.session.commit()
                return render_template("my_calc.html")
            else:
                eqq  = data.get("eq")
                c.ans = c._as_number(r)
        else:
            for check in checks:
                print(check)
                if check in iSTR:
                    nums = iSTR.split(check)
                    if nums[0] == '':
                        nums[0] = "ans"
                    try:
                        r = evaluate(iSTR) #c.calc(nums[0].strip(), check, nums[1].strip())

                        print("R is " + str(r))
                    except:
                        r = "ERROR"
                    if not current_user.is_anonymous:
                        sh = SimpleHistory(eq=iSTR, result=r, user_id=current_user.id)
                        db.session.add(sh)
                        try:
                            db.session.commit()
                            print("Recorded calculation history")
                            flash("Recorded calculation history", "success")
                        except SQLAlchemyError as e:
                            print(e)
                            flash(str(e), "error")
                            db.session.rollback()
                    return render_template("my_calc.html", result=r, eq=iSTR)
        print("The action you tried is not supported, please try again")
        iSTR = iSTR.replace("load", "")
        return render_template("my_calc.html", result=r, eq=iSTR)
    return render_template("my_calc.html")

import ast, math

locals =  {key: value for (key,value) in vars(math).items() if key[0] != '_'}
locals.update({"abs": abs, "complex": complex, "min": min, "max": max, "pow": pow, "round": round})

class Visitor(ast.NodeVisitor):
    def visit(self, node):
       if not isinstance(node, self.whitelist):
           raise ValueError(node)
       return super().visit(node)

    whitelist = (ast.Module, ast.Expr, ast.Load, ast.Expression, ast.Add, ast.Sub, ast.UnaryOp, ast.Num, ast.BinOp,
            ast.Mult, ast.Div, ast.Pow, ast.BitOr, ast.BitAnd, ast.BitXor, ast.USub, ast.UAdd, ast.FloorDiv, ast.Mod,
            ast.LShift, ast.RShift, ast.Invert, ast.Call, ast.Name)

def evaluate(expr, locals = {}):
    if any(elem in expr for elem in '\n#') : raise ValueError(expr)
    try:
        node = ast.parse(expr.strip(), mode='eval')
        Visitor().visit(node)
        return eval(compile(node, "<string>", "eval"), {'__builtins__': None}, locals)
    except Exception: raise ValueError(expr)
