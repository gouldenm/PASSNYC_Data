import matplotlib.pyplot as plt
import networkx as nx
import csv
import numpy as np

#  dataset filenames
school_explorer = "2016 School Explorer.csv"
D5_SHSAT = "D5 SHSAT Registrations and Testers.csv"

#  Read in datasets
#  haven't read in all of them, because I got bored... Will add the rest later.
school_info = []
with open(school_explorer, "r") as f:
	reader = csv.reader(f)
	for i, line in enumerate(reader):
		school = {}
		school["school_name"] = line[3]
		school["SED_Code"] = line[4]
		school["Location_Code"] = line[5]
		school["District"] = line[6]
		school["Latitude"] = line[7]
		school["Longitude"] = line[8]
		school["Address"] = line[9]
		school["City"] = line[10]
		school["Zip"] = line[11]
		school["Grades"] = line[12]
		school["Grade_low"] = line[13]
		school["Grade_high"] = line[14]
		school["Community_School"] = line[15]
		school["Economic_Need_Index"] = line[16]
		school["School_Income_Estimate"] = line[17]
		school["Percent_ELL"] = line[18]
		school["Percent_Asian"] = line[19]
		school["Percent_Black"] = line[20]
		school["Percent_Hispanic"] = line[21]
		school["Percent_Black_or_Hispanic"] = line[22]
		school["Percent_White"] = line[23]
		school["Student_Attendance_Rate"] = line[24]
		school["Percent_Chronically_Absent"] = line[25]
		school["Rigorous_Instruction_Percent"] = line[26]
		school["Rigorous_Instruction_Rating"] = line[27]
		school["Collaborative_Teachers_Percent"] = line[28]
		school["Collaborative_Teachers_Rating"] = line[29]
		school["Supportive_Environment_Percentage"] = line[30]
		school["Supportive_Environment_Rating"] = line[31]
		school["Effective_School_Leadership_Percentage"] = line[32]
		school["Effective_School_Leadership_Rating"] = line[33]
		school["Strong_Family-Community_Ties_Percentage"] = line[34]
		school["Strong_Family-Community_Ties_Rating"] = line[35]
		school["Trust_Percentage"] = line[36]
		school["Trust_Rating"] = line[37]
		school["Student_Achievement_Rating"] = line[38]
		school["Average_ELA_Proficiency"] = line[39]
		school["Average_Math_Proficiency"] = line[40]
		school["Grade3_ELA"] = line[41]
		school_info.append(school)
        


