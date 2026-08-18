import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date

st.title(" Age Calculator")

dob = st.date_input(
    "Enter your DOB",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)
)

if st.button("Check Age"):
    today = date.today()
    age = relativedelta(today, dob)

    st.success(
        f"You are {age.years} years, {age.months} months, and {age.days} days old."
    )

    # Birthday Countdown
    next_birthday = date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, dob.month, dob.day)

    days_left = (next_birthday - today).days

    st.subheader("Birthday Countdown")

    if days_left == 0:
        st.balloons()
        st.success("Happy Birthday! Have a fantastic day! ")
    else:
        st.info(f" Your next birthday is in **{days_left} days**.")
        st.write(f" Next Birthday: **{next_birthday.strftime('%d %B %Y')}**")

#life timeline

st.title("🕰️ Life Timeline Generator")

dob = st.date_input(
    "Enter your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)
)

if st.button("Generate Timeline"):

    today = date.today()
    birth_year = dob.year
    current_age = relativedelta(today, dob).years

    st.subheader("📜 Your Life Timeline")

    # Birth
    st.write(f"**{birth_year}** ─── Born 👶")

    # School
    school_year = birth_year + 6
    st.write(f"**{school_year}** ─── Started School 🎒")

    # Completed School
    school_completion_year = birth_year + 18
    st.write(f"**{school_completion_year}** ─── Completed School 🎓")

    # College
    college_year = birth_year + 18
    st.write(f"**{college_year}** ─── Started College 🏫")

    # Current age
    st.write(f"**{today.year}** ─── Current Age: {current_age} 🎯")

    # Future milestones
    age_40_year = birth_year + 40
    age_50_year = birth_year + 50
    age_60_year = birth_year + 60
    age_70_year = birth_year + 70

    if age_40_year > today.year:
        st.write(f"**{age_40_year}** ─── Age 40 🎯")

    if age_50_year > today.year:
        st.write(f"**{age_50_year}** ─── Age 50 🎯")

    if age_60_year > today.year:
        st.write(f"**{age_60_year}** ─── Age 60 🎯")

    if age_70_year > today.year:
        st.write(f"**{age_70_year}** ─── Age 70 🎯")

    st.success("🎉 Your life timeline has been generated!")