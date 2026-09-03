import streamlit as st
from datetime import date
import calendar

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Age Calculator",
    page_icon="🎂",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.html("""
<style>

.main-title {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 30px;
}

.main-title .emoji {
    font-size: 48px;
}

.main-title h1 {
    font-size: 46px;
    font-weight: 800;
    margin: 5px 0;
}

.main-title p {
    font-size: 16px;
    opacity: 0.65;
    margin: 0;
}

.title-line {
    width: 140px;
    height: 3px;
    margin: 14px auto 0 auto;
    border-radius: 20px;
    background: linear-gradient(90deg, #7c3aed, #ec4899);
}


/* Cards */

.card-title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 19px;
    font-weight: 700;
    margin-bottom: 15px;
}

.icon {
    width: 38px;
    height: 38px;
    border-radius: 12px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 19px;
}

.purple {
    background: rgba(124, 58, 237, 0.14);
}

.orange {
    background: rgba(245, 158, 11, 0.14);
}

.pink {
    background: rgba(236, 72, 153, 0.14);
}

.green {
    background: rgba(22, 163, 74, 0.14);
}


/* Exact age */

.age-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.age-box {
    text-align: center;
    padding: 18px 5px;
    border-radius: 14px;

    background: rgba(128,128,128,0.06);
    border: 1px solid rgba(128,128,128,0.18);
}

.age-number {
    font-size: 31px;
    font-weight: 800;
}

.age-label {
    font-size: 10px;
    font-weight: 700;
    opacity: 0.6;
    margin-top: 5px;
}

.age-purple {
    color: #7c3aed;
}

.age-blue {
    color: #1683ea;
}

.age-green {
    color: #16a34a;
}


/* Time statistics */

.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.stat-box {
    text-align: center;
    padding: 15px 5px;

    border-radius: 14px;

    background: rgba(128,128,128,0.06);
    border: 1px solid rgba(128,128,128,0.18);
}

.stat-icon {
    font-size: 20px;
}

.stat-value {
    font-size: 20px;
    font-weight: 800;
    margin-top: 3px;
}

.stat-label {
    font-size: 9px;
    font-weight: 700;
    opacity: 0.6;
    margin-top: 4px;
}

.stat-orange {
    color: #f59e0b;
}

.stat-blue {
    color: #1683ea;
}

.stat-green {
    color: #16a34a;
}


/* Birthday */

.birthday-box {
    text-align: center;
    padding: 22px 10px;

    border-radius: 14px;

    background: rgba(236,72,153,0.07);
    border: 1px solid rgba(236,72,153,0.25);
}

.birthday-number {
    font-size: 38px;
    font-weight: 800;
    color: #ec4899;
}

.birthday-label {
    font-size: 13px;
    opacity: 0.65;
}

.birthday-date {
    text-align: center;

    margin-top: 9px;
    padding: 8px;

    border-radius: 9px;

    background: rgba(128,128,128,0.06);
    border: 1px solid rgba(128,128,128,0.18);

    font-size: 13px;
    font-weight: 600;
}


/* BMI */

.bmi-result {
    text-align: center;

    padding: 20px;

    margin-top: 12px;

    border-radius: 14px;

    background: rgba(22,163,74,0.07);
    border: 1px solid rgba(22,163,74,0.25);
}

.bmi-number {
    font-size: 38px;
    font-weight: 800;
    color: #16a34a;
}

.bmi-category {
    font-size: 14px;
    font-weight: 700;
    color: #16a34a;
}


/* Footer */

.footer {
    text-align: center;
    margin-top: 25px;
    padding-bottom: 10px;
    font-size: 13px;
    opacity: 0.5;
}


/* Mobile */

@media (max-width: 700px) {

    .main-title .emoji {
        font-size: 42px;
    }

    .main-title h1 {
        font-size: 32px;
    }

    .main-title p {
        font-size: 14px;
    }

    .age-number {
        font-size: 25px;
    }

    .stats-grid {
        grid-template-columns: 1fr;
    }

    .birthday-number {
        font-size: 34px;
    }

    .bmi-number {
        font-size: 35px;
    }
}

</style>
""")


# =========================================================
# HEADER
# =========================================================

st.html("""
<div class="main-title">

    <div class="emoji">🎂</div>

    <h1>Age Calculator</h1>

    <p>
        Discover your exact age, birthday countdown and BMI
    </p>

    <div class="title-line"></div>

</div>
""")


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


def get_next_birthday(birth_date, today):

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
# DATE
# =========================================================

today = date.today()


# =========================================================
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

        st.html("""
        <div class="card-title">
            <div class="icon purple">📅</div>
            <div>Date of Birth</div>
        </div>

        <div style="font-size:13px;opacity:.6;margin-bottom:10px;">
            Select your date of birth
        </div>
        """)

        birth_date = st.date_input(
            "Date of Birth",
            value=date(2000, 1, 1),
            min_value=date(1900, 1, 1),
            max_value=today,
            label_visibility="collapsed"
        )


# =========================================================
# EXACT AGE
# =========================================================

years, months, days = calculate_age(
    birth_date,
    today
)

with right:

    with st.container(border=True):

        st.html("""
        <div class="card-title">
            <div class="icon purple">🎯</div>
            <div>Your Exact Age</div>
        </div>
        """)

        st.html(f"""
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
# TOTAL TIME + BIRTHDAY
# =========================================================

left, right = st.columns(
    [1.1, 1],
    gap="large"
)


# =========================================================
# TIME SINCE BIRTH
# =========================================================

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


with left:

    with st.container(border=True):

        st.html("""
        <div class="card-title">
            <div class="icon orange">⏳</div>
            <div>Time Since Your Birth</div>
        </div>
        """)

        st.html(f"""
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

birthday = get_next_birthday(
    birth_date,
    today
)

days_left = (
    birthday - today
).days


with right:

    with st.container(border=True):

        st.html("""
        <div class="card-title">
            <div class="icon pink">🎉</div>
            <div>Birthday Countdown</div>
        </div>
        """)

        if days_left == 0:

            st.html("""
            <div class="birthday-box">

                <div class="birthday-number">
                    🎂
                </div>

                <div class="birthday-label">
                    Happy Birthday!
                </div>

            </div>
            """)

        else:

            st.html(f"""
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
# BMI
# =========================================================

with st.container(border=True):

    st.html("""
    <div class="card-title">
        <div class="icon green">⚖️</div>
        <div>BMI Calculator</div>
    </div>
    """)

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

    category = get_bmi_category(
        bmi
    )

    st.html(f"""
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

st.html("""
<div class="footer">
    💜 Age Calculator · Built with Python & Streamlit
</div>
""")