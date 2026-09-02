import streamlit as st
import textwrap
from datetime import date
import calendar


st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="wide"
)


def render_html(html):
    st.markdown(
        textwrap.dedent(html).strip(),
        unsafe_allow_html=True
    )

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* =====================================================
       THEME VARIABLES
    ===================================================== */

    :root {
        --card-bg: var(--secondary-background-color);
        --page-bg: var(--background-color);
        --border: rgba(128, 128, 128, 0.20);
        --muted: rgba(128, 128, 128, 0.80);

        --purple: #7c3aed;
        --blue: #1683ea;
        --green: #159957;
        --orange: #f59e0b;
        --pink: #ec4899;
    }


    /* =====================================================
       MAIN CONTAINER
    ===================================================== */

    .block-container {
        max-width: 1100px;
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
    }


    /* =====================================================
       HERO
    ===================================================== */

    .hero {
        text-align: center;
        padding: 10px 10px 28px 10px;
    }

    .hero-icon {
        font-size: 52px;
        line-height: 1;
        margin-bottom: 8px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1.5px;
        line-height: 1.1;
    }

    .hero-subtitle {
        font-size: 17px;
        opacity: 0.65;
        margin-top: 8px;
    }

    .hero-line {
        width: 170px;
        height: 3px;
        margin: 14px auto 0 auto;
        border-radius: 10px;
        background: linear-gradient(
            90deg,
            var(--purple),
            var(--pink)
        );
    }


    /* =====================================================
       GRID
    ===================================================== */

    .dashboard-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 18px;
        align-items: stretch;
    }


    /* =====================================================
       CARD
    ===================================================== */

    .card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 20px;
        min-height: 100%;
        box-sizing: border-box;

        box-shadow:
            0 5px 20px rgba(0, 0, 0, 0.06);
    }

    .card-title {
        display: flex;
        align-items: center;
        gap: 10px;

        font-size: 19px;
        font-weight: 750;

        margin-bottom: 16px;
    }

    .icon-circle {
        width: 38px;
        height: 38px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 12px;

        font-size: 19px;
        flex-shrink: 0;
    }

    .purple-icon {
        background: rgba(124, 58, 237, 0.13);
    }

    .blue-icon {
        background: rgba(22, 131, 234, 0.13);
    }

    .green-icon {
        background: rgba(21, 153, 87, 0.13);
    }

    .orange-icon {
        background: rgba(245, 158, 11, 0.14);
    }

    .pink-icon {
        background: rgba(236, 72, 153, 0.13);
    }


    /* =====================================================
       DATE CARD
    ===================================================== */

    .date-description {
        font-size: 13px;
        opacity: 0.60;
        margin-top: -12px;
        margin-left: 48px;
        margin-bottom: 12px;
    }


    /* =====================================================
       AGE CARD
    ===================================================== */

    .age-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
    }

    .age-box {
        text-align: center;
        padding: 17px 8px;

        border-radius: 13px;

        background: var(--page-bg);

        border: 1px solid var(--border);
    }

    .age-number {
        font-size: 32px;
        font-weight: 800;
        line-height: 1.1;
    }

    .age-label {
        font-size: 11px;
        font-weight: 600;
        opacity: 0.65;
        margin-top: 7px;
    }

    .purple-number {
        color: var(--purple);
    }

    .blue-number {
        color: var(--blue);
    }

    .green-number {
        color: var(--green);
    }


    /* =====================================================
       TIME SINCE BIRTH
    ===================================================== */

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
    }

    .stat-box {
        text-align: center;
        padding: 16px 6px;

        border-radius: 13px;

        background: var(--page-bg);

        border: 1px solid var(--border);
    }

    .stat-icon {
        font-size: 20px;
        margin-bottom: 5px;
    }

    .stat-value {
        font-size: 21px;
        font-weight: 800;
    }

    .stat-label {
        font-size: 10px;
        font-weight: 600;
        opacity: 0.60;
        margin-top: 4px;
    }

    .orange-value {
        color: var(--orange);
    }

    .blue-value {
        color: var(--blue);
    }

    .green-value {
        color: var(--green);
    }


    /* =====================================================
       BIRTHDAY
    ===================================================== */

    .birthday-main {
        min-height: 110px;

        display: flex;
        align-items: center;
        justify-content: center;

        text-align: center;

        border-radius: 14px;

        background: linear-gradient(
            135deg,
            rgba(236, 72, 153, 0.08),
            rgba(236, 72, 153, 0.03)
        );

        border: 1px solid rgba(236, 72, 153, 0.25);

        position: relative;
        overflow: hidden;
    }

    .birthday-number {
        font-size: 38px;
        font-weight: 800;
        color: var(--pink);
        line-height: 1;
    }

    .birthday-days-label {
        font-size: 13px;
        font-weight: 600;
        margin-top: 5px;
        opacity: 0.70;
    }

    .birthday-date {
        margin-top: 10px;

        text-align: center;

        padding: 8px;

        border-radius: 9px;

        background: var(--page-bg);

        border: 1px solid var(--border);

        font-size: 13px;
        font-weight: 600;
    }


    /* =====================================================
       BMI
    ===================================================== */

    .bmi-result {
        margin-top: 16px;

        min-height: 92px;

        display: flex;
        align-items: center;
        justify-content: center;

        flex-direction: column;

        border-radius: 14px;

        background: rgba(21, 153, 87, 0.08);

        border: 1px solid rgba(21, 153, 87, 0.25);
    }

    .bmi-number {
        font-size: 39px;
        font-weight: 800;
        color: var(--green);
        line-height: 1;
    }

    .bmi-category {
        color: var(--green);
        font-size: 15px;
        font-weight: 700;
        margin-top: 6px;
    }


    /* =====================================================
       STREAMLIT INPUTS
    ===================================================== */

    div[data-baseweb="input"],
    div[data-baseweb="select"] > div {
        border-radius: 10px;
    }

    input {
        font-size: 15px !important;
    }

    label {
        font-weight: 600 !important;
    }


    /* =====================================================
       FOOTER
    ===================================================== */

    .footer {
        text-align: center;

        padding-top: 22px;

        font-size: 13px;

        opacity: 0.55;
    }


    /* =====================================================
       MOBILE
    ===================================================== */

    @media (max-width: 750px) {

        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
            padding-top: 1rem;
        }

        .hero {
            padding-bottom: 22px;
        }

        .hero-icon {
            font-size: 43px;
        }

        .hero-title {
            font-size: 34px;
            letter-spacing: -1px;
        }

        .hero-subtitle {
            font-size: 14px;
        }

        .dashboard-grid {
            grid-template-columns: 1fr;
            gap: 14px;
        }

        .card {
            padding: 16px;
            border-radius: 16px;
        }

        .card-title {
            font-size: 18px;
        }

        .age-number {
            font-size: 27px;
        }

        .stats-grid {
            gap: 7px;
        }

        .stat-value {
            font-size: 18px;
        }

        .birthday-number {
            font-size: 33px;
        }

        .bmi-number {
            font-size: 35px;
        }
    }


    /* =====================================================
       SMALL MOBILE
    ===================================================== */

    @media (max-width: 420px) {

        .hero-title {
            font-size: 30px;
        }

        .age-grid {
            gap: 6px;
        }

        .age-box {
            padding: 15px 3px;
        }

        .age-number {
            font-size: 24px;
        }

        .age-label {
            font-size: 9px;
        }

        .stats-grid {
            grid-template-columns: 1fr;
        }

        .stat-box {
            padding: 12px;
        }
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# CALCULATION FUNCTIONS
# =========================================================

def calculate_age(birth_date, today):

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

        days += calendar.monthrange(
            previous_year,
            previous_month
        )[1]

    if months < 0:

        years -= 1
        months += 12

    return years, months, days


def calculate_birthday(birth_date, today):

    try:

        next_birthday = date(
            today.year,
            birth_date.month,
            birth_date.day
        )

    except ValueError:

        # February 29
        next_birthday = date(
            today.year,
            2,
            28
        )

    if next_birthday <= today:

        try:

            next_birthday = date(
                today.year + 1,
                birth_date.month,
                birth_date.day
            )

        except ValueError:

            next_birthday = date(
                today.year + 1,
                2,
                28
            )

    days_left = (
        next_birthday - today
    ).days

    return next_birthday, days_left


def calculate_bmi(weight, height):

    height_m = height / 100

    return weight / (height_m ** 2)


def get_bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obesity"


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

    <div class="hero-title">
        Age Calculator
    </div>

    <div class="hero-subtitle">
        Discover your exact age, birthday countdown and BMI
    </div>

    <div class="hero-line"></div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# DATE OF BIRTH
# =========================================================

st.markdown("""
<div class="dashboard-grid">

    <div class="card">

        <div class="card-title">
            <div class="icon-circle purple-icon">📅</div>
            <div>Date of Birth</div>
        </div>

        <div class="date-description">
            Select your date of birth
        </div>

""", unsafe_allow_html=True)

birth_date = st.date_input(
    "Date of birth",
    value=date(2000, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    label_visibility="collapsed"
)

st.markdown("""
    </div>
""", unsafe_allow_html=True)


# =========================================================
# CALCULATIONS
# =========================================================

today = date.today()

years, months, days = calculate_age(
    birth_date,
    today
)

total_days = (
    today - birth_date
).days

total_months = (
    years * 12 + months
)

if days > 0:
    total_months += days / 30.4375

total_years = (
    total_days / 365.2425
)

next_birthday, birthday_days = calculate_birthday(
    birth_date,
    today
)


# =========================================================
# EXACT AGE CARD
# =========================================================

st.markdown(f"""
    <div class="card">

        <div class="card-title">
            <div class="icon-circle purple-icon">🎯</div>
            <div>Your Exact Age</div>
        </div>

        <div class="age-grid">

            <div class="age-box">
                <div class="age-number purple-number">
                    {years}
                </div>

                <div class="age-label">
                    YEARS
                </div>
            </div>

            <div class="age-box">
                <div class="age-number blue-number">
                    {months}
                </div>

                <div class="age-label">
                    MONTHS
                </div>
            </div>

            <div class="age-box">
                <div class="age-number green-number">
                    {days}
                </div>

                <div class="age-label">
                    DAYS
                </div>
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SECOND ROW
# =========================================================

st.markdown("""
<div class="dashboard-grid">
""", unsafe_allow_html=True)


# =========================================================
# TIME SINCE BIRTH
# =========================================================

st.markdown(f"""
<div class="card">

    <div class="card-title">
        <div class="icon-circle orange-icon">⏳</div>
        <div>Time Since Your Birth</div>
    </div>

    <div class="stats-grid">

        <div class="stat-box">

            <div class="stat-icon">📅</div>

            <div class="stat-value orange-value">
                {total_days:,}
            </div>

            <div class="stat-label">
                TOTAL DAYS
            </div>

        </div>

        <div class="stat-box">

            <div class="stat-icon">📆</div>

            <div class="stat-value blue-value">
                {total_months:,.1f}
            </div>

            <div class="stat-label">
                TOTAL MONTHS
            </div>

        </div>

        <div class="stat-box">

            <div class="stat-icon">🕐</div>

            <div class="stat-value green-value">
                {total_years:,.2f}
            </div>

            <div class="stat-label">
                TOTAL YEARS
            </div>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# BIRTHDAY COUNTDOWN
# =========================================================

if birthday_days == 0:

    birthday_content = """
    <div class="birthday-main">
        <div>
            <div class="birthday-number">🎂</div>
            <div class="birthday-days-label">
                Happy Birthday!
            </div>
        </div>
    </div>
    """

else:

    birthday_content = f"""
    <div class="birthday-main">

        <div>

            <div class="birthday-number">
                {birthday_days}
            </div>

            <div class="birthday-days-label">
                Days until your next birthday
            </div>

        </div>

    </div>

    <div class="birthday-date">
        🎈 {next_birthday.strftime("%d %B %Y")}
    </div>
    """


st.markdown(f"""
<div class="card">

    <div class="card-title">
        <div class="icon-circle pink-icon">🎉</div>
        <div>Birthday Countdown</div>
    </div>

    {birthday_content}

</div>
""", unsafe_allow_html=True)


# =========================================================
# CLOSE SECOND ROW
# =========================================================

st.markdown("""
</div>
""", unsafe_allow_html=True)


# =========================================================
# BMI CARD
# =========================================================

st.markdown("""
<div class="card">

    <div class="card-title">
        <div class="icon-circle purple-icon">⚖️</div>
        <div>BMI Calculator</div>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# BMI INPUTS
# =========================================================

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


# =========================================================
# BMI CALCULATION
# =========================================================

bmi = calculate_bmi(
    weight,
    height
)

bmi_status = get_bmi_category(
    bmi
)


# =========================================================
# BMI RESULT
# =========================================================

st.markdown(f"""
<div class="bmi-result">

    <div class="bmi-number">
        {bmi:.1f}
    </div>

    <div class="bmi-category">
        {bmi_status}
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    💜 &nbsp; Age Calculator &nbsp; · &nbsp;
    Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)