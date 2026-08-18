import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date

st.set_page_config(
    page_title="Smart Age & Life Analyzer",
    page_icon="🎂",
    layout="centered"
)

st.title("🎂 Smart Age & Life Analyzer")
st.write("Calculate your exact age, birthday countdown, and generate your life timeline.")

# -----------------------------
# DATE OF BIRTH
# -----------------------------

dob = st.date_input(
    "📅 Enter your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    value=date(2000, 1, 1)
)

if st.button("🚀 Analyze My Age"):

    today = date.today()

    # -----------------------------
    # EXACT AGE
    # -----------------------------

    age = relativedelta(today, dob)

    st.success(
        f"🎉 You are {age.years} years, "
        f"{age.months} months and {age.days} days old."
    )

    # -----------------------------
    # TOTAL DAYS LIVED
    # -----------------------------

    total_days = (today - dob).days
    total_hours = total_days * 24
    total_minutes = total_hours * 60

    st.subheader("📊 Your Life Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📅 Days Lived", f"{total_days:,}")
        st.metric("⏰ Hours Lived", f"{total_hours:,}")

    with col2:
        st.metric("🗓️ Weeks Lived", f"{total_days // 7:,}")
        st.metric("⏱️ Minutes Lived", f"{total_minutes:,}")

    # -----------------------------
    # BIRTHDAY COUNTDOWN
    # -----------------------------

    st.subheader("🎂 Birthday Countdown")

    try:
        next_birthday = date(today.year, dob.month, dob.day)
    except ValueError:
        # For February 29 birthdays
        next_birthday = date(today.year, 2, 28)

    if next_birthday < today:

        try:
            next_birthday = date(
                today.year + 1,
                dob.month,
                dob.day
            )
        except ValueError:
            next_birthday = date(today.year + 1, 2, 28)

    days_left = (next_birthday - today).days

    if days_left == 0:
        st.balloons()
        st.success("🥳 HAPPY BIRTHDAY! 🎂🎉")
    else:
        st.info(
            f"🎈 Your next birthday is in **{days_left} days**."
        )

        st.write(
            f"📅 Next Birthday: "
            f"**{next_birthday.strftime('%d %B %Y')}**"
        )

    # -----------------------------
    # BIRTH DAY
    # -----------------------------

    st.subheader("📅 Your Birth Day")

    birth_day_name = dob.strftime("%A")

    st.write(
        f"You were born on **{birth_day_name}**, "
        f"{dob.strftime('%d %B %Y')}."
    )

    # -----------------------------
    # LIFE TIMELINE
    # -----------------------------

    st.subheader("🕰️ Your Life Timeline")

    birth_year = dob.year

    # Birth
    st.write(
        f"**{birth_year}** ─── Born 👶"
    )

    # Started school
    school_year = birth_year + 6

    if school_year <= today.year:
        st.write(
            f"**{school_year}** ─── Started School 🎒"
        )

    # Completed school
    school_completion_year = birth_year + 18

    if school_completion_year <= today.year:
        st.write(
            f"**{school_completion_year}** ─── Completed School 🎓"
        )

    # College
    college_year = birth_year + 18

    if college_year <= today.year:
        st.write(
            f"**{college_year}** ─── Started College 🏫"
        )

    # Current age
    st.write(
        f"**{today.year}** ─── Current Age: "
        f"{age.years} 🎯"
    )

   

    # -----------------------------
    # BIRTH YEAR SUMMARY
    # -----------------------------

    st.subheader("🌎 Birth Information")

    st.write(f"👶 Birth Year: **{birth_year}**")
    st.write(f"📅 Birth Date: **{dob.strftime('%d %B %Y')}**")
    st.write(f"📆 Birth Day: **{birth_day_name}**")

    # -----------------------------
    # COMPLETION MESSAGE
    # -----------------------------

    st.markdown("---")

    st.success(
        "✨ Your complete Age & Life Timeline has been generated!"
    )