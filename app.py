import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Analytics Dashboard")
st.write("Analyze and compare student academic performance.")

df = pd.read_csv("student_data.csv")
subjects = ["Python", "Maths", "DBMS", "Statistics"]

st.sidebar.header("Dashboard Filters")

departments = st.sidebar.multiselect(
    "Select Department",
    df["Department"].unique(),
    default=df["Department"].unique().tolist()
)

genders = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique().tolist()
)

data = df[
    df["Department"].isin(departments)
    & df["Gender"].isin(genders)
].copy()

if data.empty:
    st.warning("No students match the selected filters.")
    st.stop()

data["Average Marks"] = data[subjects].mean(axis=1)

c1, c2, c3 = st.columns(3)

c1.metric("Total Students", len(data))
c2.metric("Overall Average", round(data[subjects].values.mean(), 2))

top = data.loc[data["Average Marks"].idxmax()]
c3.metric("Top Performer", top["Name"])

st.subheader("📋 Student Dataset")
st.dataframe(data, use_container_width=True)

st.subheader("📊 Student Marks Analysis")

subject = st.selectbox("Choose Subject", subjects)

fig = px.bar(
    data,
    x="Name",
    y=subject,
    color="Department",
    title=f"{subject} Marks by Student",
    text=subject
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Subject Average Comparison")

averages = data[subjects].mean().reset_index()
averages.columns = ["Subject", "Average Marks"]

fig2 = px.bar(
    averages,
    x="Subject",
    y="Average Marks",
    color="Subject",
    text_auto=".1f",
    title="Average Marks Across Subjects"
)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🏆 Student Performance Ranking")

ranking = data.sort_values("Average Marks", ascending=False)
st.dataframe(
    ranking[["Name", "Department", "Average Marks"]],
    use_container_width=True
)

st.download_button(
    "⬇️ Download Student Data (CSV)",
    data=data.to_csv(index=False).encode("utf-8"),
    file_name="student_performance.csv",
    mime="text/csv"
)

st.caption("Student Performance Analytics Dashboard | Data Visualization Project")