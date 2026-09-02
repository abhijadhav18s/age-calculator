import streamlit as st
from datetime import date
import calendar
import textwrap


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# HTML HELPER
# Prevents indentation from becoming Markdown code
# =========================================================

def html(content):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True
    )


# =========================================================
# PROFESSIONAL CSS
# Light + Dark Mode Compatible
# =========================================================

st.markdown(
    """
<style>

:root {
    --purple: #7c3aed;
    --blue: #1683ea;
    --green: #16a34a;
    --orange: #f59e0b;
    --pink: #ec4899;
    --border: rgba(128,128,128,0.22);
}


/* =====================================================
   MAIN PAGE
===================================================== */

.block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
    padding-bottom: 1rem;
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
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.1;
}

.hero-subtitle {
    margin-top: 8px;
    font-size: 17px;
    opacity: 0.65;
}

.hero-line {
    width: 150px;
    height: 3px;
    margin: 14px auto 0 auto;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        var(--purple),
        var(--pink)
    );
}


/* =====================================================
   SECTION TITLE
===================================================== */

.section-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 19px;
    font-weight: 750;
    margin-bottom: 12px;
}

.section-description {
    font-size: 13px;
    opacity: 0.60;
    margin-top: -7px;
    margin-bottom: 12px;
}


/* =====================================================
   ICON
===================================================== */

.icon {
    width: 38px;
    height: 38px;
    min-width: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 12px;
    font-size: 19px;
}

.icon-purple {
    background: rgba(124,58,237,0.14);
}

.icon-blue {
    background: rgba(22,131,234,0.14);
}

.icon-green {
    background: rgba(22,163,74,0.14);
}

.icon-orange {
    background: rgba(245,158,11,0.15);
}

.icon-pink {
    background: rgba(236,72,153,0.14);
}


/* =====================================================
   AGE RESULT BOXES
===================================================== */

.age-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}

.age-box {
    text-align: center;
    padding: 18px 8px;
    border-radius: 14px;

    background: var(--background-color);

    border: 1px solid var(--border);
}

.age-number {
    font-size: 32px;
    font-weight: 800;
}

.age-label {
    margin-top: 6px;
    font-size: 11px;
    font-weight: 650;
    opacity: 0.60;
}

.age-purple {
    color: var(--purple);
}

.age-blue {
    color: var(--blue);
}

.age-green {
    color: var(--green);
}


/* =====================================================
   TIME STATISTICS
===================================================== */

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.stat-box {
    text-align: center;
    padding: 17px 7px;

    background: var(--background-color);

    border: 1px solid var(--border);
    border-radius: 14px;
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
    font-weight: 650;
    opacity: 0.60;
    margin-top: 4px;
}

.stat-orange {
    color: var(--orange);
}

.stat-blue {
    color: var(--blue);
}

.stat-green {
    color: var(--green);
}


/* =====================================================
   BIRTHDAY COUNTDOWN
===================================================== */

.birthday-box {
    text-align: center;
    padding: 24px 12px;

    border-radius: 15px;

    background: rgba(236,72,153,0.07);

    border: 1px solid rgba(236,72,153,0.25);
}

.birthday-number {
    font-size: 40px;
    font-weight: 800;
    color: var(--pink);
    line-height: 1;
}

.birthday-label {
    font-size: 13px;
    margin-top: 7px;
    opacity: 0.65;
}

.birthday-date {
    text-align: center;

    margin-top: 10px;
    padding: 8px;

    border-radius: 9px;

    background: var(--background-color);

    border: 1px solid var(--border);

    font-size: 13px;
    font-weight: 600;
}


/* =====================================================
   BMI
===================================================== */

.bmi-result {
    min-height: 95px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    margin-top: 15px;

    border-radius: 15px;

    background: rgba(22,163,74,0.08);

    border: 1px solid rgba(22,163,74,0.25);
}

.bmi-number {
    font-size: 40px;
    font-weight: 800;
    color: var(--green);
}

.bmi-category {
    margin-top: 5px;
    font-size: 15px;
    font-weight: 700;
    color: var(--green);
}


/* =====================================================
   INPUTS
===================================================== */

div[data-baseweb="input"] {
    border-radius: 10px;
}

div[data-baseweb="select"] > div {
    border-radius: 10px;
}

label {
    font-weight: 600 !important;
}


/* =====================================================
   FOOTER
===================================================== */

.footer {
    text-align: center;
    margin-top: 20px;
    padding: 10px;
    font-size: 13px;
    opacity: 0.50;
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
        padding-bottom: 20px;
    }

    .hero-icon {
        font-size: 43px;
    }

    .hero-title {
        font-size: 33px;
    }

    .hero-subtitle {
        font-size: 14px;
    }

    .age-grid {
        gap: 7px;
    }

    .age-box {
        padding: 16px 4px;
    }

    .age-number {
        font-size: 26px;
    }

    .age-label {
        font-size: 9px;
    }

    .stats-grid {
        grid-template-columns: 1fr;
        gap: 7px;
    }

    .stat-box {
        padding: 13px;
    }

    .birthday-number {
        font-size: 34px;
    }

    .bmi-number {
        font-size: 36px;
    }
}


/* =====================================================
   SMALL PHONES
===================================================== */

@media (max-width: 420px) {

    .hero-title {
        font-size: 29px;
    }

    .hero-subtitle {
        font-size: 13px;
    }

    .age-number {
        font-size: 23px;
    }

    .age-label {
        font-size: 8px;
    }
}

</style>
""",
    unsafe_allow_html=True
)


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
        previous_year = today.year

        if previous_month == 0:
            previous_month = 12
            previous_year -= 1

        days += calendar.monthrange(
            previous_year,
            previous_month
        )[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def next_birthday(birth_date, today):

    try:
        birthday = date(
            today.year,
            birth_date.month,
            birth_date.day
        )
    except ValueError:
        birthday = date(
            today.year,
            2,
            28
        )

    if birthday <= today:

        try:
            birthday = date(
                today.year + 1,
                birth_date.month,
                birth_date.day
            )
        except ValueError:
            birthday = date(
                today.year + 1,
                2,
                28
            )

    return birthday


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    if bmi < 25:
        return "Normal weight"

    if bmi < 30:
        return "Overweight"

    return "Obesity"


# =========================================================
# HERO
# =========================================================

html("""
<div class="hero">
    <div class="hero-icon">🎂</div>
    <div class="hero-title">Age Calculator</div>
    <div class="hero-subtitle">
        Discover your exact age, birthday countdown and BMI
    </div>
    <div class="hero-line"></div>
</div>
""")


# =========================================================
# CURRENT DATE
# =========================================================

today = date.today()


# =========================================================
# TOP ROW
# DATE OF BIRTH + EXACT AGE
# =========================================================

left, right = st.columns(
    [0.85, 1.5],
    gap="large"
)


# =========================================================
# DATE OF BIRTH
# =========================================================

with left:

    with st.container(border=True):

        html("""
        <div class="section-title">
            <div class="icon icon-purple">📅</div>
            <div>Date of Birth</div>
        </div>

        <div class="section-description">
            Select your date of birth
        </div>
        """)

        birth_date = st.date_input(
            "Date of birth",
            value=date(2000, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=today,
            label_visibility="collapsed"
        )


# =========================================================
# EXACT AGE
# =========================================================

with right:

    with st.container(border=True):

        years, months, days = calculate_age(
            birth_date,
            today
        )

        html("""
        <div class="section-title">
            <div class="icon icon-purple">🎯</div>
            <div>Your Exact Age</div>
        </div>
        """)

        html(f"""
        <div class="age-grid">

            <div class="age-box">
                <div class="age-number age-purple">
                    {years}
                </div>
                <div class="age-label">
                    YEARS
                </div>
            </div>

            <div class="age-box">
                <div class="age-number age-blue">
                    {months}
                </div>
                <div class="age-label">
                    MONTHS
                </div>
            </div>

            <div class="age-box">
                <div class="age-number age-green">
                    {days}
                </div>
                <div class="age-label">
                    DAYS
                </div>
            </div>

        </div>
        """)


# =========================================================
# SECOND ROW
# TIME SINCE BIRTH + BIRTHDAY COUNTDOWN
# =========================================================

left, right = st.columns(
    [1.1, 1],
    gap="large"
)


# =========================================================
# TIME SINCE BIRTH
# =========================================================

with left:

    with st.container(border=True):

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

        html("""
        <div class="section-title">
            <div class="icon icon-orange">⏳</div>
            <div>Time Since Your Birth</div>
        </div>
        """)

        html(f"""
        <div class="stats-grid">

            <div class="stat-box">
                <div class="stat-icon">📅</div>
                <div class="stat-value stat-orange">
                    {total_days:,}
                </div>
                <div class="stat-label">
                    TOTAL DAYS
                </div>
            </div>

            <div class="stat-box">
                <div class="stat-icon">📆</div>
                <div class="stat-value stat-blue">
                    {total_months:,.1f}
                </div>
                <div class="stat-label">
                    TOTAL MONTHS
                </div>
            </div>

            <div class="stat-box">
                <div class="stat-icon">🕐</div>
                <div class="stat-value stat-green">
                    {total_years:,.2f}
                </div>
                <div class="stat-label">
                    TOTAL YEARS
                </div>
            </div>

        </div>
        """)


# =========================================================
# BIRTHDAY COUNTDOWN
# =========================================================

with right:

    with st.container(border=True):

        birthday = next_birthday(
            birth_date,
            today
        )

        days_left = (
            birthday - today
        ).days

        html("""
        <div class="section-title">
            <div class="icon icon-pink">🎉</div>
            <div>Birthday Countdown</div>
        </div>
        """)

        if days_left == 0:

            st.success(
                "🎂 Happy Birthday! Have a wonderful day!"
            )

        else:

            html(f"""
            <div class="birthday-box">

                <div class="birthday-number">
                    {days_left}
                </div>

                <div class="birthday-label">
                    Days until your next birthday
                </div>

            </div>

            <div class="birthday-date">
                🎈 {birthday.strftime("%d %B %Y")}
            </div>
            """)


# =========================================================
# BMI CALCULATOR
# =========================================================

with st.container(border=True):

    html("""
    <div class="section-title">
        <div class="icon icon-purple">⚖️</div>
        <div>BMI Calculator</div>
    </div>
    """)

    col1, col2 = st.columns(
        2,
        gap="large"
    )

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

    category = bmi_category(
        bmi
    )

    html(f"""
    <div class="bmi-result">

        <div class="bmi-number">
            {bmi:.1f}
        </div>

        <div class="bmi-category">
            {category}
        </div>

    </div>
    """)


# =========================================================
# FOOTER
# =========================================================

html("""
<div class="footer">
    💜 &nbsp; Age Calculator &nbsp; · &nbsp;
    Built with Python & Streamlit
</div>
""")