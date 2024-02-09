import pymysql
import os
from app import app
from db_config import mysql
from flask import jsonify, flash, request, make_response, redirect, url_for, render_template,session


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/add_match', methods=['GET'])
def add_match_form():
    return render_template('add_match.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur.execute("SELECT * FROM admins WHERE name = %s", (username))
        users_data = cur.fetchall()
        if users_data:
            for user_data in users_data:
                if user_data['password'] == password:
                    return redirect(url_for('add_match_form'))
                else:
                    print("Incorrect")
    return render_template('login.html')


@app.route('/add_match', methods=['POST'])
def add_match():
    match_id = request.form['matchID']
    date = request.form['date']
    venue = request.form['venue']
    bat_first = request.form['batFirst']
    bat_second = request.form['batSecond']
    target_score = request.form['targetScore']
    winner = request.form['winner']
    chased_successfully = request.form['chasedSuccessfully']
    insert_query = """INSERT INTO MatchInformation 
                      (MatchID, Date, Venue, BatFirst, BatSecond, TargetScore, Winner, ChasedSuccessfully) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.execute(insert_query, (match_id, date, venue, bat_first, bat_second, target_score, winner, chased_successfully))
    conn.commit()

    return redirect(url_for('add_match_form'))

@app.route('/update_match', methods=['POST'])
def update_match():
    match_id = request.form['matchID']
    new_target_score = request.form['newTargetScore']

    update_query = """UPDATE MatchInformation 
                      SET TargetScore = %s
                      WHERE MatchID = %s"""
    cur.execute(update_query, (new_target_score, match_id))
    conn.commit()

    return redirect(url_for('add_match_form'))

@app.route('/guest')
def guest():
    return render_template('guest.html')

@app.route('/search_match', methods=['POST'])
def search_match():
    search_match_id = request.form['searchMatchID']
    search_query = "SELECT * FROM MatchInformation WHERE MatchID = %s"
    cur.execute(search_query, (search_match_id,))
    match_data = cur.fetchone()
    return render_template('match_details.html', match=match_data)

@app.route('/delete_match', methods=['POST'])
def delete_match():
    delete_match_id = request.form['deleteMatchID']
    delq = "delete from MatchInformation where MatchID=%s"
    cur.execute(delq,(delete_match_id))
    conn.commit()
    return redirect(url_for('add_match'))

@app.route('/search_team', methods=['POST'])
def search_team():
    search_team_name = request.form['searchTeamName']
    search_query = "Select * from MatchInformation where BatFirst=%s or BatSecond=%s LIMIT 10;"
    cur.execute(search_query, (search_team_name,search_team_name))
    team_details = cur.fetchall()
    return render_template('team_details.html', details=team_details)

@app.route('/search_batter', methods=['POST'])
def search_batter():
    batter_name = request.form['searchBatterName']
    query = "SELECT Batter, SUM(BatterBallsFaced) AS BatterBallsFaced,SUM(PlayerOutRuns) AS PlayerOutRuns,SUM(PlayerOutBallsFaced) AS PlayerOutBallsFaced FROM BatterDetails where Batter=%s"
    cur.execute(query, (batter_name,))
    batter_results = cur.fetchall()
    if any(value['Batter'] is None for value in batter_results):
        batter_results=None
    return render_template('batter_results.html', batters=batter_results)

@app.route('/search_bowler', methods=['POST'])
def search_bowler():
    bowler_name = request.form['searchBowlerName']
    query = "SELECT Bowler, sum(BowlerRunsConceded) AS wickets FROM BowlerDetails where Bowler=%s"
    cur.execute(query, (bowler_name,))
    bowler_results = cur.fetchall()
    if any(value['Bowler'] is None for value in bowler_results):
        bowler_results=None
    return render_template('bowler_results.html', bowlers=bowler_results)

@app.route('/search_ballbyball', methods=['POST'])
def search_ballbyball():
    match_id = request.form['searchBallByBallMatchID']
    query = "SELECT * FROM BallByBall WHERE MatchID = %s LIMIT 20"
    cur.execute(query, (match_id,))
    ball_by_ball_details = cur.fetchall()
    return render_template('ballbyball_results.html', details=ball_by_ball_details)


if __name__=='__main__':
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    app.run(debug=True)