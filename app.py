from SA import *
from flask import Flask, render_template, request, flash, send_from_directory
import os

sa = SA()
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def main():
    return render_template('mains.html')

@app.route('/search', methods=['POST'])
def search():
    try:
        value = request.form['username']
        req = sa.name_search(value)
        if req['result'] == False:
            return render_template('mains.html')
        req = req['characterInfo']
        try:
            icon = req['profileImageInfo'][0]['user_img']
        except:
            icon = req['profileInfo']['user_img']
        rank_no = req['characterInfo']['rank_no'] 
        if rank_no == "UNRANK":
            rank_no = "UNRANK"
        else:
            rank_no = rank_no + " 위"
        name = value
        winper = req['battleInfo']['win_per']
        kd = req['battleInfo']['kill_death_per']
        kd1 = req['battleInfo']['ar_per']
        kd2 = req['battleInfo']['sr_per']
        id = req['characterInfo']['user_nexon_sn']
        return render_template('realit.html', icon = icon, rank_no = rank_no, name = name, winper =winper, kd= kd, kd1 = kd1, kd2 = kd2, id= id)
    except Exception as e: 
        print(e)
        return render_template('mains.html')

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80)
