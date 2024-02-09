# CrickData
A sophisticated WebApp and Dashboard were created to analyze data related to the Indian Premier League (2008-2023)

Project Description:
In this project report, we present the development of a comprehensive web platform designed to serve as a dynamic dashboard and website dedicated to the Indian Premier League (IPL). Our dataset encompasses information from the inaugural season of IPL in 2008 through the most recent season in 2023, meticulously gathered from the Indian Premier League (IPL) Ball-by-Ball Data hosted on Kaggle. Within this comprehensive web application, we have thoughtfully incorporated features to cater to both administrators and guests. The administrator login provides privileged access, allowing authorized individuals to manage and modify the database, ensuring data accuracy and relevance. On the other hand, our user-friendly guest interface provides easy access for IPL enthusiasts to explore the data from various perspectives, facilitating a deeper understanding of the league's dynamics, performance trends, and player statistics.

Data:
We are using the "Indian Premier League (IPL) Ball-by-Ball Data" available on Kaggle, a dataset created by Jamie Welsh. This dataset encompasses information from the inaugural IPL season in 2008 up to the most recent season, which includes the data for the 2023 season. The Indian Premier League is a professional Twenty20 cricket league in India. It is one of the most popular and lucrative cricket leagues in the world. IPL features franchise teams representing different cities, and it has attracted top international and domestic cricketers. The league typically takes place annually, and teams compete for the IPL trophy. This dataset was initially generated to devise a metric for player ranking in T20 Internationals and IPL leagues. It comprises 35 columns, including Match ID, Venue, Innings, and more, with about 239,694 data entries.

Functionalities:
In this web app, we have 2 kinds of functionalities for implementing CRUD operations in the database. On the homepage, we have a part for the admin to login and another for guest users who don’t need any login. Firstly, talking about the admin, they are the only people who can login and add new match information, update information (updating any match’s target score using Match ID) and delete a match record from all the tables.
Regarding the guest usage of this web app, once a guest gets to the respective page, they can see any match information. We created 5 kinds of functionalities:
1. Search any match with MatchID:
  ● Using the match ID, a guest can see total information regarding the match like venue, date, first batter, second batter and Target score.
2. Search for any Batter information:
  ● A guest can search for the total information of a batter like total runs, total innings etc.
3. Search for any Bowler information:
  ● Using the name of any bowler, a guest can see the total information of a bowler in the IPL.
4. Search for any Team information:
  ● Searching for a team name would give us all the information on every match the team played in every IPL season.
5. Search for any Match information:
  ● Using the match ID, a guest can see the information of every ball from that match.

Tools Used:
Front End: HTML, Java Script, CSS
Back End: Flask, PyMysql, Python
Database: MySQL
Tools: Visual Studio Code, Python, MySQL workbench, Postman
Model: The model is developed using Flask RESTful APIs and PyMysql to deal with databases.
View: The views are developed using Flask rendered templated with HTML, JavaScript and CSS.
Controller: The controllers are developed using Flask Web Application routers.
Deployment Platform: Used the PythonAnywhere platform to deploy the web application.
