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

    st.subheader("🎉 Birthday Countdown")

    if days_left == 0:
        st.balloons()
        st.success("Happy Birthday! Have a fantastic day! ")
    else:
        st.info(f" Your next birthday is in **{days_left} days**.")
        st.write(f" Next Birthday: **{next_birthday.strftime('%d %B %Y')}**")