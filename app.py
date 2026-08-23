import streamlit as st
from datetime import date, datetime
import calendar
import math


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ---------------------------------------------------------
# CUSTOM CSS - MOBILE + DESKTOP RESPONSIVE
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Main page */
    .main {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    /* Main title */
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #777;
        margin-bottom: 25px;
    }

    /* Cards */
    .card {
        padding: 22px;
        border-radius: 18px;
        background: #ffffff;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border: 1px solid #eeeeee;
    }

    .card-title {
        font-size: 22px;
        font-weight: 650;
        margin-bottom: 15px;
    }

    /* Result numbers */
    .result-number {
        font-size: 30px;
        font-weight: 700;
        text-align: center;
    }

    .result-label {
        text-align: center;
        color: #777;
        font-size: 14px;
    }

    /* Countdown */
    .countdown {
        text-align: center;
        font-size: 28px;
        font-weight: 700;
        padding: 15px;
        border-radius: 15px;
        background: #f5f7ff;
        margin-top: 10px;
    }

    /* BMI */
    .bmi-value {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
    }

    .bmi-status {
        text-align: center;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-size: 16px;
        font-weight: 600;
    }

    /* Mobile */
    @media (max-width: 600px) {
        .title {
            font-size: 31px;
        }

        .subtitle {
            font-size: 15px;
        }

        .card {
            padding: 16px;
            border-radius: 15px;
        }

        .card-title {
            font-size: 19px;
        }

        .result-number {
            font-size: 25px;
        }

        .countdown {
            font-size: 21px;
        }

        .bmi-value {
            font-size: 35px;
        }
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------

def calculate_age(birth_date, today):
    """
    Calculate exact age in years, months and days.
    """

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1

        previous_month = today.month - 1

        if previous_month == 0:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_year = today.year

        days_in_previous_month = calendar.monthrange(
            previous_year,
            previous_month
        )[1]

        days += days_in_previous_month

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def calculate_total_days(birth_date, today):
    return (today - birth_date).days


def calculate_total_months(birth_date, today):
    years, months, days = calculate_age(birth_date, today)

    total_months = years * 12 + months

    # Add partial month approximately
    if days > 0:
        total_months += days / 30.4375

    return total_months


def calculate_birthday_countdown(birth_date, today):
    """
    Calculate days until next birthday.
    """

    current_year = today.year

    try:
        next_birthday = date(
            current_year,
            birth_date.month,
            birth_date.day
        )
    except ValueError:
        # Handles February 29
        next_birthday = date(current_year, 2, 28)

    if next_birthday <= today:
        next_year = current_year + 1

        try:
            next_birthday = date(
                next_year,
                birth_date.month,
                birth_date.day
            )
        except ValueError:
            next_birthday = date(next_year, 2, 28)

    days_left = (next_birthday - today).days

    return next_birthday, days_left


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100

    if height_m <= 0:
        return 0

    return weight / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="title">Age Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Calculate your exact age, birthday countdown and BMI</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.markdown(
    '<div class="card"><div class="card-title">📅 Enter Your Date of Birth</div>',
    unsafe_allow_html=True
)

birth_date = st.date_input(
    "Date of Birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# CALCULATIONS
# ---------------------------------------------------------

today = date.today()

if birth_date > today:

    st.error("Date of birth cannot be in the future.")

else:

    years, months, days = calculate_age(
        birth_date,
        today
    )

    total_days = calculate_total_days(
        birth_date,
        today
    )

    total_months = calculate_total_months(
        birth_date,
        today
    )

    total_years = total_days / 365.2425

    next_birthday, birthday_days = calculate_birthday_countdown(
        birth_date,
        today
    )


    # -----------------------------------------------------
    # EXACT AGE
    # -----------------------------------------------------

    st.markdown(
        '<div class="card"><div class="card-title">🎯 Your Exact Age</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="result-number">{years}</div>
            <div class="result-label">Years</div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="result-number">{months}</div>
            <div class="result-label">Months</div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="result-number">{days}</div>
            <div class="result-label">Days</div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # TOTAL TIME LIVED
    # -----------------------------------------------------

    st.markdown(
        '<div class="card"><div class="card-title">⏳ Time Since Your Birth</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Days",
            f"{total_days:,}"
        )

    with col2:
        st.metric(
            "Total Months",
            f"{total_months:,.1f}"
        )

    st.metric(
        "Total Years",
        f"{total_years:,.2f}"
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # BIRTHDAY COUNTDOWN
    # -----------------------------------------------------

    st.markdown(
        '<div class="card"><div class="card-title">🎉 Birthday Countdown</div>',
        unsafe_allow_html=True
    )

    if birthday_days == 0:
        st.success("🎂 Happy Birthday! Have a wonderful day!")

    else:
        st.markdown(
            f"""
            <div class="countdown">
                🎈 {birthday_days} days to go
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            f"Your next birthday: **{next_birthday.strftime('%d %B %Y')}**"
        )

    st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # BMI CALCULATOR
    # -----------------------------------------------------

    st.markdown(
        '<div class="card"><div class="card-title">⚖️ BMI Calculator</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            max_value=300.0,
            value=60.0,
            step=0.5
        )

    with col2:
        height = st.number_input(
            "Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=170.0,
            step=1.0
        )

    bmi = calculate_bmi(
        weight,
        height
    )

    category = bmi_category(bmi)

    st.markdown(
        f"""
        <div class="bmi-value">{bmi:.1f}</div>
        <div class="bmi-status">{category}</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div style="
        text-align:center;
        color:#888;
        font-size:13px;
        padding:15px;
    ">
        Age Calculator • Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)