import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("Placement Data Predictor")

# -----------------------------------
# LOAD DATASET
# -----------------------------------

data = pd.read_csv("dataset/placement.csv")

# -----------------------------------
# EDITABLE DATASET
# -----------------------------------

st.header("Editable Student Dataset")

edited_data = st.data_editor(
    data,
    num_rows="dynamic",
    use_container_width=True
)

# -----------------------------------
# FIX CASE SENSITIVITY
# -----------------------------------

edited_data["Placed"] = (
    edited_data["Placed"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# -----------------------------------
# BASIC ANALYSIS
# -----------------------------------

st.header("Basic Analysis")

total_students = len(edited_data)

average_cgpa = np.mean(
    edited_data["CGPA"]
)

highest_dsa = np.max(
    edited_data["DSA_Score"]
)

placed_students = edited_data[
    edited_data["Placed"] == "yes"
]

not_placed_students = edited_data[
    edited_data["Placed"] == "no"
]

placement_percentage = (
    len(placed_students) / total_students
) * 100

st.write("Total Students :", total_students)

st.write(
    "Average CGPA :",
    round(average_cgpa, 2)
)

st.write(
    "Highest DSA Score :",
    highest_dsa
)

st.write(
    "Placement Percentage :",
    round(placement_percentage, 2),
    "%"
)

# -----------------------------------
# PLACED STUDENTS TABLE
# -----------------------------------

st.header("Placed Students")

st.dataframe(
    placed_students,
    use_container_width=True
)

# -----------------------------------
# NOT PLACED STUDENTS TABLE
# -----------------------------------

st.header("Not Placed Students")

st.dataframe(
    not_placed_students,
    use_container_width=True
)

# -----------------------------------
# CGPA BAR GRAPH
# -----------------------------------

st.header("CGPA Analysis")

fig1, ax1 = plt.subplots()

student_numbers = range(
    1,
    len(edited_data) + 1
)

ax1.bar(
    student_numbers,
    edited_data["CGPA"]
)

ax1.set_xlabel("Student Number")

ax1.set_ylabel("CGPA")

ax1.set_title(
    "Student CGPA Analysis"
)

st.pyplot(fig1)

# -----------------------------------
# DSA SCORE LINE GRAPH
# -----------------------------------

st.header("DSA Score Analysis")

fig2, ax2 = plt.subplots()

ax2.plot(
    student_numbers,
    edited_data["DSA_Score"],
    marker='o'
)

ax2.set_xlabel("Student Number")

ax2.set_ylabel("DSA Score")

ax2.set_title(
    "DSA Score Analysis"
)

st.pyplot(fig2)

# -----------------------------------
# PLACEMENT PIE CHART
# -----------------------------------

st.header("Placement Distribution")

placed_count = len(
    placed_students
)

not_placed_count = len(
    not_placed_students
)

labels = [
    "Placed",
    "Not Placed"
]

sizes = [
    placed_count,
    not_placed_count
]

fig3, ax3 = plt.subplots()

ax3.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

ax3.set_title(
    "Placement Distribution"
)

st.pyplot(fig3)

# -----------------------------------
# PLACEMENT PREDICTOR
# -----------------------------------

st.header("Placement Predictor")

cgpa = st.number_input(
    "Enter CGPA",
    0.0,
    10.0
)

dsa = st.number_input(
    "Enter DSA Score",
    0,
    100
)

communication = st.number_input(
    "Enter Communication Skill Rating",
    0,
    10
)

internships = st.number_input(
    "Enter Number of Internships",
    0,
    10
)

projects = st.number_input(
    "Enter Number of Projects",
    0,
    20
)

if st.button("Predict Placement"):

    if (
        cgpa >= 8.0 and
        dsa >= 80 and
        communication >= 7 and
        internships >= 1 and
        projects >= 2
    ):

        st.success(
            "HIGH CHANCE of Placement"
        )

    else:

        st.error(
            "LOW CHANCE of Placement"
        )