import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# LOAD DATASET
# -----------------------------------

data = pd.read_csv("dataset/placement.csv")

# -----------------------------------
# DISPLAY FULL DATASET
# -----------------------------------

print("\n========== FULL DATASET ==========\n")
print(data)

# -----------------------------------
# BASIC ANALYSIS
# -----------------------------------

total_students = len(data)
average_cgpa = np.mean(data["CGPA"])
highest_dsa = np.max(data["DSA_Score"])

print("\n========== BASIC ANALYSIS ==========\n")

print("Total Students :", total_students)
print("Average CGPA   :", round(average_cgpa, 2))
print("Highest DSA Score :", highest_dsa)

# -----------------------------------
# PLACED STUDENTS TABLE
# -----------------------------------

placed_students = data[data["Placed"] == "Yes"]

print("\n========== PLACED STUDENTS ==========\n")
print(placed_students)

# -----------------------------------
# NOT PLACED STUDENTS TABLE
# -----------------------------------

not_placed_students = data[data["Placed"] == "No"]

print("\n========== NOT PLACED STUDENTS ==========\n")
print(not_placed_students)

# -----------------------------------
# PLACEMENT PERCENTAGE
# -----------------------------------

placement_percentage = (len(placed_students) / total_students) * 100

print("\nPlacement Percentage :", placement_percentage, "%")

# -----------------------------------
# GRAPH 1 : CGPA BAR GRAPH
# -----------------------------------

plt.figure(figsize=(8,5))

student_numbers = range(1, len(data) + 1)

plt.bar(student_numbers, data["CGPA"])

plt.title("Student CGPA Analysis")
plt.xlabel("Student Number")
plt.ylabel("CGPA")

plt.savefig("graphs/cgpa_bar_graph.png")

plt.show()

# -----------------------------------
# GRAPH 2 : DSA SCORE LINE GRAPH
# -----------------------------------

plt.figure(figsize=(8,5))

plt.plot(student_numbers, data["DSA_Score"], marker='o')

plt.title("DSA Score Analysis")
plt.xlabel("Student Number")
plt.ylabel("DSA Score")

plt.savefig("graphs/dsa_line_graph.png")

plt.show()

# -----------------------------------
# GRAPH 3 : PLACEMENT PIE CHART
# -----------------------------------

placed_count = len(placed_students)
not_placed_count = len(not_placed_students)

labels = ["Placed", "Not Placed"]
sizes = [placed_count, not_placed_count]

plt.figure(figsize=(6,6))

plt.pie(sizes, labels=labels, autopct="%1.1f%%")

plt.title("Placement Distribution")

plt.savefig("graphs/placement_pie_chart.png")

plt.show()

# -----------------------------------
# PLACEMENT PREDICTION SYSTEM
# -----------------------------------

print("\n========== PLACEMENT PREDICTOR ==========\n")

cgpa = float(input("Enter CGPA: "))
dsa = int(input("Enter DSA Score: "))
communication = int(input("Enter Communication Skill Rating (1-10): "))
internships = int(input("Enter Number of Internships: "))
projects = int(input("Enter Number of Projects: "))

# Prediction Logic

if (
    cgpa >= 8.0 and
    dsa >= 80 and
    communication >= 7 and
    internships >= 1 and
    projects >= 2
):
    print("\nPrediction: HIGH CHANCE of Placement")
else:
    print("\nPrediction: LOW CHANCE of Placement")