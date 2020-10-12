#Python code to generate IPL Points Table
#This code works for all cases except DLS

import ast #for string to dict conversion

#Kind of enumeration
enumeration = {"match":0, "win":1, "lost":2, "NR":3, "points":4, "runs_scored":5, "balls_played":6, "runs_conceded":7, "balls_bowled":8, "NRR":9, "recent_form":10} 
fname = "Points_Table.txt"

#All the required inputs
team1 = input("Enter team1: ")
team2 = input("Enter team2: ")
winner = input("Who won?(Enter NR if no result): ")
if winner == "NR" :
	team1_score,team2_score = 0,0
else :
	first_batting = input("Who is batting first?: ")
	if winner != first_batting :
		second_innings_overs_win = input("Overs needed by chasing team?(Enter as XX.X): ")
		overs_played = second_innings_overs_win.split(".")
		overs_played = [int(i) for i in overs_played]
		balls_played = overs_played[0]*6 + overs_played[1]
	team1_score = int(input("Enter {}'s score: ".format(team1)))
	team2_score = int(input("Enter {}'s score: ".format(team2)))

fh = open(fname)
#initial contents of the file are:
#After 0th match : {"CSK":[0,0,0,0,0,0,0,0,0,0,"______"],"DC":[0,0,0,0,0,0,0,0,0,0,"______"],"KKR":[0,0,0,0,0,0,0,0,0,0,"______"],"KXIP":[0,0,0,0,0,0,0,0,0,0,"______"],"MI":[0,0,0,0,0,0,0,0,0,0,"______"],"RCB":[0,0,0,0,0,0,0,0,0,0,"______"],"RR":[0,0,0,0,0,0,0,0,0,0,"______"],"SRH":[0,0,0,0,0,0,0,0,0,0,"______"]}

document = fh.readlines()
total_match_count = len(document)
output_string = "After {}th match : ".format(total_match_count)
last_line = document[-1]
list_lastline = last_line.split("h : ")
table = list_lastline[1]
working_variable = ast.literal_eval(table)

#match column is updated
working_variable[team1][enumeration["match"]]+=1
working_variable[team2][enumeration["match"]]+=1

#Win/lose/NR data, points, recent_form updation

#If there is no result
if winner == "NR" :
	working_variable[team1][enumeration["NR"]] +=1
	working_variable[team2][enumeration["NR"]] +=1

	working_variable[team1][enumeration["points"]] +=1
	working_variable[team2][enumeration["points"]] +=1	

	working_variable[team1][enumeration["recent_form"]] = working_variable[team1][enumeration["recent_form"]][1:]+"T"
	working_variable[team2][enumeration["recent_form"]] = working_variable[team2][enumeration["recent_form"]][1:]+"T"

#If there is a result
else:
	if winner == team1 :
		loser = team2
	else :
		loser = team1

	working_variable[winner][enumeration["win"]] +=1
	working_variable[loser][enumeration["lost"]] +=1

	working_variable[winner][enumeration["points"]]+=2

	working_variable[winner][enumeration["recent_form"]] = working_variable[winner][enumeration["recent_form"]][1:]+"W"
	working_variable[loser][enumeration["recent_form"]] = working_variable[loser][enumeration["recent_form"]][1:]+"L"


#NRR calculation

working_variable[team1][enumeration["runs_scored"]] += team1_score
working_variable[team2][enumeration["runs_scored"]] += team2_score
working_variable[team1][enumeration["runs_conceded"]] += team2_score
working_variable[team2][enumeration["runs_conceded"]] += team1_score

if first_batting == winner :
	working_variable[team1][enumeration["balls_played"]] +=120
	working_variable[team1][enumeration["balls_bowled"]] +=120
	working_variable[team2][enumeration["balls_played"]] +=120
	working_variable[team2][enumeration["balls_bowled"]] +=120

else :
	working_variable[loser][enumeration["balls_played"]] +=120
	working_variable[winner][enumeration["balls_bowled"]] +=120
	working_variable[winner][enumeration["balls_played"]] += balls_played
	working_variable[loser][enumeration["balls_bowled"]] +=balls_played

working_variable[winner][enumeration["NRR"]] = ((working_variable[winner][enumeration["runs_scored"]] / working_variable[winner][enumeration["balls_played"]]) * 6) - ((working_variable[winner][enumeration["runs_conceded"]] / working_variable[winner][enumeration["balls_bowled"]]) * 6)
working_variable[loser][enumeration["NRR"]] = ((working_variable[loser][enumeration["runs_scored"]] / working_variable[loser][enumeration["balls_played"]]) * 6) - ((working_variable[loser][enumeration["runs_conceded"]] / working_variable[loser][enumeration["balls_bowled"]]) * 6)

#Calculation part completed

fh.close()

#append the output to the Points_Table.txt file
fh = open(fname, "a")
output = str(working_variable)
output = output_string + output
fh.write(output)
fh.write("\n")
fh.close()
