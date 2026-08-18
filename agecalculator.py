import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date

st.set_page_config(
    page_title="Smart Age & Life Analyzer",
    page_icon="",
    layout="centered"
)

st.title(" Smart Age & Life Analyzer")
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

    st.subheader("📈 Life Progress")

    lifespan = st.slider(
        "🎯 Select your target lifespan",
        min_value=50,
        max_value=120,
        value=100,
        step=1
    )

    # Exact number of days in selected lifespan
    lifespan_end_date = date(
        dob.year + lifespan,
        dob.month,
        dob.day
    )

    total_lifespan_days = (
        lifespan_end_date - dob
    ).days

    days_lived = (
        today - dob
    ).days

    # Calculate percentage
    life_percentage = (
        days_lived / total_lifespan_days
    ) * 100

    # Keep percentage between 0 and 100
    life_percentage = max(
        0,
        min(life_percentage, 100)
    )

    st.progress(
        int(life_percentage)
    )

    st.write(
        f"### {life_percentage:.2f}%"
    )

    st.write(
        f"You have completed approximately "
        f"**{life_percentage:.2f}%** of your selected "
        f"{lifespan}-year lifespan."
    )

    if today < lifespan_end_date:

        remaining_days = (
            lifespan_end_date - today
        ).days

        remaining_age = relativedelta(
            lifespan_end_date,
            today
        )

        st.info(
            f"🌱 Approximately **{remaining_age.years} years, "
            f"{remaining_age.months} months and "
            f"{remaining_age.days} days** remaining "
            f"until age {lifespan}."
        )

        st.write(
            f"📅 Target date: "
            f"**{lifespan_end_date.strftime('%d %B %Y')}**"
        )

    else:

        st.success(
            f"🎉 You have already reached your selected "
            f"{lifespan}-year milestone."
        )

    # --------------------------------------------------
    # FUTURE AGE CALCULATOR
    # --------------------------------------------------

    st.subheader("🔮 Future Age Calculator")

    future_year = st.number_input(
        "📅 Enter the year you want to check",
        min_value=today.year,
        max_value=2200,
        value=today.year + 10,
        step=1
    )

    # Calculate exact future date
    future_date = date(
        int(future_year),
        dob.month,
        dob.day
    )

    # Calculate exact age on that date
    future_age = relativedelta(
        future_date,
        dob
    )

    st.success(
        f"🔮 On **{future_date.strftime('%d %B %Y')}**, "
        f"you will be "
        f"**{future_age.years} years, "
        f"{future_age.months} months and "
        f"{future_age.days} days old.**"
    )

    # --------------------------------------------------
    # FUTURE AGE TABLE
    # --------------------------------------------------

    st.write("### 📅 Future Age Milestones")

    future_ages = [25, 30, 40, 50, 60, 70, 80, 90, 100]

    for target_age in future_ages:

        milestone_date = date(
            birth_year + target_age,
            dob.month,
            dob.day
        )

        if milestone_date > today:

            st.write(
                f"🎯 Age **{target_age}** → "
                f"**{milestone_date.strftime('%d %B %Y')}**"
            )
    # -----------------------------
    # COMPLETION MESSAGE
    # -----------------------------

    st.markdown("---")

    st.success(
        "✨ Your complete Age & Life Timeline has been generated!"
    )