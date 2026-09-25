import streamlit as st
import requests
from datetime import date

from assessment_questions import get_stage1_questions
from assessment_scoring import calculate_feature_scores
from prediction_engine import predict_stage


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SkillCompass",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# PROFESSIONAL FRONTEND STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Landing page */
    .landing {
        text-align: center;
        padding: 4rem 1rem 2rem 1rem;
    }

    .landing-icon {
        font-size: 4.5rem;
        line-height: 1;
        margin-bottom: 1rem;
    }

    .landing-title {
        font-size: 3.6rem;
        font-weight: 800;
        letter-spacing: -1.5px;
        margin: 0;
        color: #173F8A;
    }

    .landing-tagline {
        font-size: 1.65rem;
        font-weight: 650;
        margin-top: 0.5rem;
        color: #344054;
    }

    .landing-description {
        font-size: 1.05rem;
        color: #667085;
        margin-top: 1rem;
    }

    .landing-copy {
        max-width: 700px;
        margin: 1rem auto 2rem auto;
        color: #667085;
        line-height: 1.7;
        font-size: 1rem;
    }

    /* Feature cards */
    .feature-card {
        min-height: 185px;
        padding: 1.4rem 1rem;
        border: 1px solid #E4E7EC;
        border-radius: 18px;
        background: white;
        text-align: center;
        box-shadow: 0 6px 20px rgba(16, 24, 40, 0.06);
    }

    .feature-icon {
        font-size: 2.1rem;
        margin-bottom: 0.65rem;
    }

    .feature-title {
        font-size: 1.05rem;
        font-weight: 750;
        color: #344054;
        margin-bottom: 0.45rem;
    }

    .feature-text {
        font-size: 0.88rem;
        color: #667085;
        line-height: 1.5;
    }

    /* Auth page */
    .auth-header {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
    }

    .auth-icon {
        font-size: 3.2rem;
        margin-bottom: 0.5rem;
    }

    .auth-title {
        font-size: 2.25rem;
        font-weight: 800;
        color: #173F8A;
        margin-bottom: 0.3rem;
    }

    .auth-subtitle {
        font-size: 1.1rem;
        font-weight: 600;
        color: #344054;
    }

    .auth-description {
        color: #667085;
        margin-top: 0.5rem;
    }

    .auth-card {
        border: 1px solid #E4E7EC;
        border-radius: 18px;
        padding: 1.5rem;
        background: white;
        text-align: center;
        box-shadow: 0 6px 20px rgba(16, 24, 40, 0.06);
        margin-bottom: 0.75rem;
    }

    .auth-card-icon {
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
    }

    .auth-card-title {
        font-size: 1.2rem;
        font-weight: 750;
        color: #344054;
    }

    .auth-card-text {
        font-size: 0.9rem;
        color: #667085;
        line-height: 1.5;
        margin-top: 0.35rem;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        min-height: 2.75rem;
        font-weight: 650;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        border-right: 1px solid #E4E7EC;
    }

    /* Small footer */
    .app-footer {
        text-align: center;
        color: #98A2B3;
        font-size: 0.8rem;
        padding: 2rem 0 0.5rem 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# API CONFIGURATION
# ============================================================

API_URL = "http://127.0.0.1:8000"


# ============================================================
# STAGE CONFIGURATION
# ============================================================

STAGES = {
    "Stage 1": {
        "name": "Post-10th / School Stream Selection",
        "icon": "🎓",
        "description": (
            "Explore suitable school streams based on "
            "your interests, abilities and preferences."
        )
    },
    "Stage 2": {
        "name": "Post-12th / Higher Education Selection",
        "icon": "📚",
        "description": (
            "Explore possible higher-education fields "
            "based on your strengths and interests."
        )
    },
    "Stage 3": {
        "name": "Working Professional / Career Switch",
        "icon": "💼",
        "description": (
            "Explore possible career-switch and "
            "upskilling pathways."
        )
    },
    "Stage 4": {
        "name": "Postgraduate / Next Career Step",
        "icon": "🎯",
        "description": (
            "Explore possible next career steps "
            "after postgraduate study."
        )
    }
}


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "welcome",
    "logged_in": False,
    "username": "",
    "user_id": None,
    "email": "",
    "age": None,
    "date_of_birth": "",
    "stage": "",
    "stage_name": "",
    "access_token": "",
    "is_first_login": False,
    "assessment_result": None,
    "assessment_id": None,
    "selected_stage": None,
    "flash_message": None,
    "flash_type": "success",
    "auth_mode": "choice"
}

for key, value in defaults.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# API HELPER
# ============================================================

def get_auth_headers():

    token = st.session_state.get(
        "access_token",
        ""
    )

    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }


# ============================================================
# NAVIGATION
# ============================================================

def go_to(page):

    st.session_state.page = page
    st.rerun()


# ============================================================
# LOGOUT
# ============================================================

def logout():

    st.session_state.logged_in = False

    st.session_state.username = ""

    st.session_state.user_id = None

    st.session_state.email = ""

    st.session_state.age = None

    st.session_state.date_of_birth = ""

    st.session_state.stage = ""

    st.session_state.stage_name = ""

    st.session_state.access_token = ""

    st.session_state.is_first_login = False

    st.session_state.page = "welcome"

    st.session_state.assessment_result = None
    st.session_state.assessment_id = None

    st.session_state.selected_stage = None

    st.session_state.flash_message = None
    st.session_state.auth_mode = "choice"

    st.rerun()


# ============================================================
# FLASH MESSAGE
# ============================================================

if (
    st.session_state.flash_message
    and st.session_state.logged_in
):

    if st.session_state.flash_type == "success":

        st.success(
            st.session_state.flash_message
        )

    elif st.session_state.flash_type == "info":

        st.info(
            st.session_state.flash_message
        )

    elif st.session_state.flash_type == "warning":

        st.warning(
            st.session_state.flash_message
        )

    elif st.session_state.flash_type == "error":

        st.error(
            st.session_state.flash_message
        )

    st.session_state.flash_message = None


# ============================================================
# SIDEBAR
# ============================================================

if st.session_state.logged_in:

    with st.sidebar:

        st.title("🧭 SkillCompass")

        st.caption(
            "AI-Based Skill Assessment & Career Guidance"
        )

        st.divider()

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):
            go_to("dashboard")

        if st.button(
            "📝 Take Assessment",
            use_container_width=True
        ):
            go_to("assessment")

        if st.button(
            "📜 History",
            use_container_width=True
        ):
            go_to("history")

        if st.button(
            "👤 Profile",
            use_container_width=True
        ):
            go_to("profile")

        if st.button(
            "⚙️ Settings",
            use_container_width=True
        ):
            go_to("settings")

        st.divider()

        st.caption(
            f"Logged in as: "
            f"{st.session_state.username}"
        )

        if st.session_state.stage_name:

            st.caption(
                f"Stage: "
                f"{st.session_state.stage_name}"
            )

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            logout()


# ============================================================
# WELCOME + AUTHENTICATION
# ============================================================

if (
    st.session_state.page == "welcome"
    and not st.session_state.logged_in
):

    # ------------------------------------------------------------
    # LANDING PAGE
    # ------------------------------------------------------------

    st.markdown(
        """
        <div class="landing">
            <div class="landing-icon">🧭</div>
            <div class="landing-title">SkillCompass</div>
            <div class="landing-tagline">
                Discover Your Right Path
            </div>
            <div class="landing-description">
                AI-Based Skill Assessment &amp; Career Guidance
            </div>
            <div class="landing-copy">
                Understand your strengths, explore suitable
                academic and career pathways, and make informed
                decisions through a structured AI-based assessment.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1.2, 1.1, 1.2])

    with center:
        if st.button(
            "🚀  Get Started",
            use_container_width=True,
            type="primary"
        ):
            st.session_state.auth_mode = "choice"
            go_to("auth")

    st.write("")
    st.write("")

    st.markdown(
        """
        <div style="text-align:center;">
            <h2 style="margin-bottom:0.25rem;">Why SkillCompass?</h2>
            <p style="color:#667085;">
                A structured approach to understanding skills and
                exploring possible pathways.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    features = [
        (
            "🎯",
            "Personalized",
            "Recommendations based on your assessment profile."
        ),
        (
            "🤖",
            "AI-Powered",
            "Machine learning helps analyze your skills and interests."
        ),
        (
            "🧭",
            "Multi-Stage",
            "Guidance across academic and professional stages."
        ),
        (
            "📈",
            "Track Progress",
            "Review your assessment results and progress."
        ),
    ]

    for column, (icon, title, description) in zip(
        [col1, col2, col3, col4],
        features
    ):
        with column:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{icon}</div>
                    <div class="feature-title">{title}</div>
                    <div class="feature-text">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div class="app-footer">
            SkillCompass • AI-Based Skill Assessment &amp;
            Career Guidance System
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AUTHENTICATION
# ============================================================

elif (
    st.session_state.page == "auth"
    and not st.session_state.logged_in
):

    # ------------------------------------------------------------
    # AUTH CHOICE
    # ------------------------------------------------------------

    if st.session_state.auth_mode == "choice":

        st.markdown(
            """
            <div class="auth-header">
                <div class="auth-icon">🧭</div>
                <div class="auth-title">
                    Welcome to SkillCompass
                </div>
                <div class="auth-subtitle">
                    Let's get you started
                </div>
                <div class="auth-description">
                    Choose an option below to continue.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        left, center, right = st.columns([1, 1.35, 1])

        with center:

            st.markdown(
                """
                <div class="auth-card">
                    <div class="auth-card-icon">✨</div>
                    <div class="auth-card-title">
                        New to SkillCompass?
                    </div>
                    <div class="auth-card-text">
                        Create your account and start discovering
                        your academic or career pathway.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "📝  Create an Account",
                use_container_width=True,
                type="primary"
            ):
                st.session_state.auth_mode = "register"
                st.rerun()

            st.write("")

            st.markdown(
                """
                <div class="auth-card">
                    <div class="auth-card-icon">👋</div>
                    <div class="auth-card-title">
                        Already have an account?
                    </div>
                    <div class="auth-card-text">
                        Login to continue your SkillCompass journey.
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                "🔐  Login to SkillCompass",
                use_container_width=True
            ):
                st.session_state.auth_mode = "login"
                st.rerun()

        st.write("")

        left, center, right = st.columns([1.2, 1.1, 1.2])

        with center:
            if st.button(
                "← Back to Home",
                use_container_width=True
            ):
                st.session_state.auth_mode = "choice"
                go_to("welcome")


    # ------------------------------------------------------------
    # LOGIN
    # ------------------------------------------------------------

    elif st.session_state.auth_mode == "login":

        st.markdown(
            """
            <div class="auth-header">
                <div class="auth-icon">🔐</div>
                <div class="auth-title">Welcome Back</div>
                <div class="auth-subtitle">
                    Login to your SkillCompass account
                </div>
                <div class="auth-description">
                    Continue your personalized assessment journey.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        left, center, right = st.columns([1, 1.3, 1])

        with center:

            email = st.text_input(
                "Email",
                placeholder="Enter your email",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password",
                key="login_password"
            )

            if st.button(
                "Login →",
                use_container_width=True,
                type="primary"
            ):

                if not email or not password:

                    st.warning(
                        "Please enter your email and password."
                    )

                else:

                    try:

                        response = requests.post(
                            f"{API_URL}/auth/login",
                            json={
                                "email": email,
                                "password": password
                            },
                            timeout=10
                        )

                        if response.status_code == 200:

                            data = response.json()
                            user = data["user"]

                            st.session_state.logged_in = True

                            st.session_state.username = user["name"]
                            st.session_state.user_id = user["id"]
                            st.session_state.email = user["email"]

                            st.session_state.age = user.get("age")

                            st.session_state.date_of_birth = (
                                user.get("date_of_birth", "")
                            )

                            st.session_state.stage = user.get(
                                "stage",
                                ""
                            )

                            st.session_state.stage_name = user.get(
                                "stage_name",
                                ""
                            )

                            st.session_state.selected_stage = user.get(
                                "stage",
                                ""
                            )

                            st.session_state.access_token = (
                                data["access_token"]
                            )

                            st.session_state.is_first_login = (
                                data.get(
                                    "is_first_login",
                                    False
                                )
                            )

                            if st.session_state.is_first_login:

                                st.session_state.flash_message = (
                                    f"🎉 Welcome to SkillCompass, "
                                    f"{user['name']}! "
                                    f"This is your first login."
                                )

                            else:

                                st.session_state.flash_message = (
                                    f"👋 Welcome back, "
                                    f"{user['name']}!"
                                )

                            st.session_state.flash_type = "success"
                            st.session_state.page = "dashboard"

                            st.rerun()

                        else:

                            try:
                                error_data = response.json()
                                error_message = error_data.get(
                                    "detail",
                                    "Login failed."
                                )

                            except Exception:
                                error_message = (
                                    "Login failed. Please try again."
                                )

                            st.error(
                                f"❌ {error_message}"
                            )

                    except requests.exceptions.ConnectionError:

                        st.error(
                            "❌ Cannot connect to SkillCompass Backend."
                        )

                        st.info(
                            "Make sure FastAPI is running on "
                            "http://127.0.0.1:8000"
                        )

                    except requests.exceptions.Timeout:

                        st.error(
                            "❌ Backend request timed out."
                        )

                    except Exception as e:

                        st.error(
                            f"Login error: {e}"
                        )

            st.write("")

            if st.button(
                "📝 New user? Create an account",
                use_container_width=True
            ):
                st.session_state.auth_mode = "register"
                st.rerun()

            if st.button(
                "← Back to account options",
                use_container_width=True
            ):
                st.session_state.auth_mode = "choice"
                st.rerun()


    # ------------------------------------------------------------
    # REGISTER
    # ------------------------------------------------------------

    elif st.session_state.auth_mode == "register":

        st.markdown(
            """
            <div class="auth-header">
                <div class="auth-icon">📝</div>
                <div class="auth-title">
                    Create Your Account
                </div>
                <div class="auth-subtitle">
                    Start your SkillCompass journey
                </div>
                <div class="auth-description">
                    Tell us a little about yourself to personalize
                    your assessment experience.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        left, center, right = st.columns([0.65, 1.7, 0.65])

        with center:

            # ----------------------------------------------------
            # PERSONAL INFORMATION
            # ----------------------------------------------------

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name",
                key="register_name"
            )

            col1, col2 = st.columns(2)

            with col1:

                age = st.number_input(
                    "Age",
                    min_value=10,
                    max_value=100,
                    value=18,
                    step=1,
                    key="register_age"
                )

            with col2:

                date_of_birth = st.date_input(
                    "Date of Birth",
                    value=date(2000, 1, 1),
                    min_value=date(1900, 1, 1),
                    max_value=date.today(),
                    format="DD/MM/YYYY",
                    key="register_dob"
                )

            # ----------------------------------------------------
            # ACCOUNT INFORMATION
            # ----------------------------------------------------

            email = st.text_input(
                "Email",
                placeholder="Enter your email",
                key="register_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Create a password",
                key="register_password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password",
                placeholder="Confirm your password",
                key="register_confirm"
            )

            # ----------------------------------------------------
            # STAGE SELECTION
            # ----------------------------------------------------

            st.subheader("🎯 Select Your Current Stage")

            st.caption(
                "Choose the stage that best describes your "
                "current educational or professional situation."
            )

            stage_options = {
                "Stage 1 — Post-10th / School Stream Selection":
                    "Stage 1",

                "Stage 2 — Post-12th / Higher Education Selection":
                    "Stage 2",

                "Stage 3 — Working Professional / Career Switch":
                    "Stage 3",

                "Stage 4 — Postgraduate / Next Career Step":
                    "Stage 4"
            }

            selected_stage_display = st.radio(
                "Which stage are you currently in?",
                options=list(stage_options.keys()),
                key="register_stage"
            )

            selected_stage = stage_options[
                selected_stage_display
            ]

            # ----------------------------------------------------
            # CREATE ACCOUNT
            # ----------------------------------------------------

            if st.button(
                "Create Account →",
                use_container_width=True,
                type="primary"
            ):

                if not name.strip():

                    st.warning(
                        "Please enter your full name."
                    )

                elif not email.strip():

                    st.warning(
                        "Please enter your email address."
                    )

                elif not password:

                    st.warning(
                        "Please enter a password."
                    )

                elif not confirm_password:

                    st.warning(
                        "Please confirm your password."
                    )

                elif password != confirm_password:

                    st.error(
                        "❌ Passwords do not match."
                    )

                elif len(password) < 6:

                    st.warning(
                        "Password must contain at least "
                        "6 characters."
                    )

                elif age < 10 or age > 100:

                    st.warning(
                        "Please enter a valid age."
                    )

                else:

                    try:

                        response = requests.post(
                            f"{API_URL}/auth/register",

                            json={
                                "name": name.strip(),
                                "age": int(age),
                                "date_of_birth": (
                                    date_of_birth.strftime(
                                        "%Y-%m-%d"
                                    )
                                ),
                                "email": email.strip(),
                                "password": password,
                                "stage": selected_stage
                            },

                            timeout=10
                        )

                        if response.status_code == 200:

                            data = response.json()

                            st.success(
                                "🎉 Account created successfully!"
                            )

                            st.info(
                                f"Selected stage: "
                                f"**{data.get('stage_name', selected_stage_display)}**"
                            )

                            st.session_state.auth_mode = "login"

                            st.info(
                                "Your account has been registered. "
                                "Please login to continue."
                            )

                            if st.button(
                                "🔐 Continue to Login",
                                use_container_width=True,
                                type="primary"
                            ):
                                st.rerun()

                        else:

                            try:

                                error_data = response.json()

                                error_message = error_data.get(
                                    "detail",
                                    "Registration failed."
                                )

                            except Exception:

                                error_message = (
                                    "Registration failed."
                                )

                            st.error(
                                f"❌ {error_message}"
                            )

                    except requests.exceptions.ConnectionError:

                        st.error(
                            "❌ Cannot connect to SkillCompass Backend."
                        )

                        st.info(
                            "Make sure FastAPI is running on "
                            "http://127.0.0.1:8000"
                        )

                    except requests.exceptions.Timeout:

                        st.error(
                            "❌ Backend request timed out."
                        )

                    except Exception as e:

                        st.error(
                            f"Registration error: {e}"
                        )

            st.write("")

            if st.button(
                "🔐 Already have an account? Login",
                use_container_width=True
            ):
                st.session_state.auth_mode = "login"
                st.rerun()

            if st.button(
                "← Back to account options",
                use_container_width=True
            ):
                st.session_state.auth_mode = "choice"
                st.rerun()



# ============================================================
# DASHBOARD
# ============================================================

elif (
    st.session_state.page == "dashboard"
    and st.session_state.logged_in
):

    st.title(
        f"Welcome back, "
        f"{st.session_state.username}! 👋"
    )

    st.subheader(
        "Your personalized SkillCompass dashboard."
    )

    st.divider()

    # ========================================================
    # SELECTED STAGE
    # ========================================================

    st.header("🎯 Your Selected Stage")

    stage = st.session_state.stage

    stage_name = st.session_state.stage_name

    stage_info = STAGES.get(stage)

    if stage_info:

        with st.container(border=True):

            st.subheader(
                f"{stage_info['icon']} "
                f"{stage_name}"
            )

            st.write(
                stage_info["description"]
            )

            st.divider()

            if stage == "Stage 1":

                if st.button(
                    "Start Stage 1 Assessment →",
                    use_container_width=True,
                    type="primary"
                ):

                    st.session_state.selected_stage = (
                        "stage1"
                    )

                    go_to("assessment")

            elif stage == "Stage 2":

                st.info(
                    "Stage 2 assessment will be available soon."
                )

            elif stage == "Stage 3":

                st.info(
                    "Stage 3 assessment will be available soon."
                )

            elif stage == "Stage 4":

                st.info(
                    "Stage 4 assessment will be available soon."
                )

    else:

        st.error(
            "No valid stage is assigned to your account."
        )

    st.divider()

    # ========================================================
    # ACCOUNT SUMMARY
    # ========================================================

    st.header("👤 Account Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Name",
            st.session_state.username
        )

    with col2:

        st.metric(
            "Age",
            (
                str(st.session_state.age)
                if st.session_state.age is not None
                else "Not available"
            )
        )

    with col3:

        st.metric(
            "Stage",
            (
                st.session_state.stage
                if st.session_state.stage
                else "Not assigned"
            )
        )


# ============================================================
# ASSESSMENT
# ============================================================

elif (
    st.session_state.page == "assessment"
    and st.session_state.logged_in
):

    # ========================================================
    # STAGE ACCESS PROTECTION
    # ========================================================

    if st.session_state.stage != "Stage 1":

        st.error(
            "🚫 You do not have access to the Stage 1 assessment."
        )

        st.info(
            f"Your registered stage is: "
            f"{st.session_state.stage_name}"
        )

        if st.button(
            "← Back to Dashboard",
            use_container_width=True
        ):
            go_to("dashboard")

        st.stop()


    # ========================================================
    # STAGE 1 ASSESSMENT
    # ========================================================

    st.title(
        "🎓 Stage 1 — Post-10th Stream Selection"
    )

    st.write(
        "Answer each question based on your own "
        "interests, abilities and preferences."
    )

    questions = get_stage1_questions()

    responses = {}

    answered_count = 0

    st.info(
        f"This assessment contains "
        f"{len(questions)} questions."
    )

    # ========================================================
    # QUESTIONS
    # ========================================================

    for question in questions:

        question_id = question["id"]

        st.subheader(
            f"Question {question_id}"
        )

        st.write(
            question["question"]
        )

        options = question["options"]

        option_labels = [
            option["label"]
            for option in options
        ]

        selected_answer = st.radio(
            "Select your answer:",
            option_labels,
            key=f"assessment_question_{question_id}",
            index=None
        )

        if selected_answer is not None:

            answered_count += 1

            for option in options:

                if option["label"] == selected_answer:

                    responses[question_id] = (
                        option["score"]
                    )

                    break

        st.divider()


    # ========================================================
    # PROGRESS
    # ========================================================

    progress_value = (
        answered_count / len(questions)
    )

    st.progress(
        progress_value,
        text=(
            f"Assessment Progress: "
            f"{answered_count} / {len(questions)}"
        )
    )


    # ========================================================
    # SUBMIT
    # ========================================================

    if st.button(
        "🎯 Submit Assessment",
        use_container_width=True,
        type="primary"
    ):

        if answered_count != len(questions):

            st.warning(
                f"Please answer all questions. "
                f"You have answered "
                f"{answered_count} out of "
                f"{len(questions)}."
            )

        else:

            try:

                # ------------------------------------------------
                # FEATURE SCORES
                # ------------------------------------------------

                feature_scores = calculate_feature_scores(
                    responses,
                    questions
                )

                # ------------------------------------------------
                # ML PREDICTION
                # ------------------------------------------------

                result = predict_stage(
                    "stage1",
                    feature_scores
                )

                # ------------------------------------------------
                # SAVE ASSESSMENT TO FASTAPI / SQLITE
                # ------------------------------------------------

                assessment_payload = {
                    "stage": "Stage 1",
                    "recommendation": result["recommendation"],
                    "responses": responses,
                    "feature_scores": feature_scores
                }

                save_response = requests.post(
                    f"{API_URL}/assessments/",
                    json=assessment_payload,
                    headers=get_auth_headers(),
                    timeout=10
                )

                if save_response.status_code == 401:

                    st.error(
                        "❌ Your login session has expired. "
                        "Please login again."
                    )

                    if st.button("Return to Login"):
                        logout()

                    st.stop()

                if save_response.status_code == 403:

                    st.error(
                        "❌ You are not authorized to submit "
                        "this assessment."
                    )

                    st.stop()

                if save_response.status_code != 200:

                    try:
                        error_data = save_response.json()
                        error_message = error_data.get(
                            "detail",
                            "Unable to save assessment."
                        )
                    except Exception:
                        error_message = (
                            "Unable to save assessment."
                        )

                    st.error(
                        f"❌ {error_message}"
                    )

                    st.stop()

                # ------------------------------------------------
                # ASSESSMENT SAVED SUCCESSFULLY
                # ------------------------------------------------

                saved_data = save_response.json()

                st.session_state.assessment_id = (
                    saved_data.get("assessment_id")
                )

                st.session_state.assessment_result = {
                    "result": result,
                    "feature_scores": feature_scores,
                    "responses": responses,
                    "assessment_id": (
                        saved_data.get("assessment_id")
                    )
                }

                go_to("result")

            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )


# ============================================================
# RESULT PAGE
# ============================================================

elif (
    st.session_state.page == "result"
    and st.session_state.logged_in
    and st.session_state.assessment_result is not None
):

    result_data = st.session_state.assessment_result

    result = result_data["result"]

    feature_scores = result_data["feature_scores"]

    st.title("🎯 Assessment Results")

    st.write(
        "Here is your personalized recommendation."
    )

    st.divider()

    # ========================================================
    # RECOMMENDATION
    # ========================================================

    recommendation = result[
        "recommendation"
    ].replace(
        "_",
        " "
    )

    st.success(
        f"### Recommended Pathway\n\n"
        f"## {recommendation}"
    )

    # ========================================================
    # FEATURE SCORES
    # ========================================================

    st.header(
        "📊 Your Assessment Profile"
    )

    col1, col2 = st.columns(2)

    feature_items = list(
        feature_scores.items()
    )

    for index, (feature, score) in enumerate(
        feature_items
    ):

        column = (
            col1
            if index % 2 == 0
            else col2
        )

        with column:

            feature_name = feature.replace(
                "_",
                " "
            ).title()

            st.write(
                f"**{feature_name}**"
            )

            st.progress(
                min(score / 10, 1.0),
                text=f"{score:.2f} / 10"
            )


    # ========================================================
    # PREDICTION PROBABILITIES
    # ========================================================

    st.header(
        "🎯 Prediction Probabilities"
    )

    for class_name, probability in result[
        "probabilities"
    ].items():

        display_name = class_name.replace(
            "_",
            " "
        )

        st.write(
            f"**{display_name}**"
        )

        st.progress(
            probability,
            text=f"{probability * 100:.2f}%"
        )


    st.warning(
        "This recommendation is generated by the "
        "SkillCompass machine-learning model. "
        "It should be treated as guidance and not "
        "as a definitive decision about your future."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📝 Take Assessment Again",
            use_container_width=True
        ):

            st.session_state.assessment_result = None
            st.session_state.assessment_id = None

            go_to("assessment")

    with col2:

        if st.button(
            "🏠 Back to Dashboard",
            use_container_width=True
        ):

            go_to("dashboard")


# ============================================================
# HISTORY
# ============================================================

elif (
    st.session_state.page == "history"
    and st.session_state.logged_in
):

    st.title("📜 My History")

    st.write(
        "Your SkillCompass activity and assessment history."
    )

    st.divider()

    # ========================================================
    # LOGIN HISTORY
    # ========================================================

    st.header("🔐 Login History")

    try:

        response = requests.get(
            f"{API_URL}/auth/login-history",
            headers=get_auth_headers(),
            timeout=10
        )

        if response.status_code == 200:

            data = response.json()

            total_logins = data.get(
                "total_logins",
                0
            )

            st.metric(
                "Total Logins",
                total_logins
            )

            login_history = data.get(
                "login_history",
                []
            )

            if login_history:

                st.subheader(
                    "Recent Login Activity"
                )

                for index, login in enumerate(
                    login_history
                ):

                    login_time = login.get(
                        "login_time",
                        "Unknown"
                    )

                    st.write(
                        f"**Login {index + 1}** — "
                        f"{login_time}"
                    )

                    st.divider()

            else:

                st.info(
                    "No login history found."
                )

        elif response.status_code == 401:

            st.error(
                "Your session has expired. "
                "Please login again."
            )

            if st.button(
                "Return to Login"
            ):
                logout()

        else:

            st.error(
                "Unable to retrieve login history."
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to the FastAPI backend."
        )

    except requests.exceptions.Timeout:

        st.error(
            "❌ Backend request timed out."
        )

    except Exception as e:

        st.error(
            f"Error loading login history: {e}"
        )


    # ========================================================
    # ASSESSMENT HISTORY
    # ========================================================

    st.header("📝 Assessment History")

    try:

        assessment_response = requests.get(
            f"{API_URL}/assessments/history",
            headers=get_auth_headers(),
            timeout=10
        )

        if assessment_response.status_code == 401:

            st.error(
                "Your session has expired. "
                "Please login again."
            )

            if st.button("Return to Login"):
                logout()

        elif assessment_response.status_code == 200:

            assessment_data = assessment_response.json()

            total_assessments = assessment_data.get(
                "total_assessments",
                0
            )

            assessments = assessment_data.get(
                "assessments",
                []
            )

            st.metric(
                "Total Assessments",
                total_assessments
            )

            if assessments:

                st.subheader(
                    "Previous Assessment Results"
                )

                for index, assessment in enumerate(
                    assessments
                ):

                    assessment_id = assessment.get(
                        "id",
                        "Unknown"
                    )

                    assessment_stage = assessment.get(
                        "stage",
                        "Unknown"
                    )

                    assessment_recommendation = (
                        assessment.get(
                            "recommendation",
                            "Unknown"
                        )
                    )

                    display_recommendation = (
                        assessment_recommendation
                        .replace("_", " ")
                    )

                    completed_at = assessment.get(
                        "completed_at",
                        "Unknown"
                    )

                    with st.container(border=True):

                        st.subheader(
                            f"Assessment {index + 1}"
                        )

                        col1, col2 = st.columns(2)

                        with col1:

                            st.write(
                                f"**Assessment ID:** "
                                f"{assessment_id}"
                            )

                            st.write(
                                f"**Stage:** "
                                f"{assessment_stage}"
                            )

                        with col2:

                            st.write(
                                f"**Recommendation:** "
                                f"{display_recommendation}"
                            )

                            st.write(
                                f"**Completed:** "
                                f"{completed_at}"
                            )

            else:

                st.info(
                    "You have not completed an assessment yet."
                )

        else:

            try:
                error_data = assessment_response.json()
                error_message = error_data.get(
                    "detail",
                    "Unable to retrieve assessment history."
                )
            except Exception:
                error_message = (
                    "Unable to retrieve assessment history."
                )

            st.error(
                f"❌ {error_message}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to the FastAPI backend."
        )

        st.info(
            "Make sure FastAPI is running on "
            "http://127.0.0.1:8000"
        )

    except requests.exceptions.Timeout:

        st.error(
            "❌ Backend request timed out."
        )

    except Exception as e:

        st.error(
            f"Error loading assessment history: {e}"
        )


# ============================================================
# PROFILE
# ============================================================

elif (
    st.session_state.page == "profile"
    and st.session_state.logged_in
):

    st.title("👤 My Profile")

    st.write(
        "Your SkillCompass account information."
    )

    st.divider()

    st.subheader("Personal Information")

    st.text_input(
        "Name",
        value=st.session_state.username,
        disabled=True
    )

    st.text_input(
        "Age",
        value=(
            str(st.session_state.age)
            if st.session_state.age is not None
            else "Not available"
        ),
        disabled=True
    )

    st.text_input(
        "Date of Birth",
        value=(
            st.session_state.date_of_birth
            if st.session_state.date_of_birth
            else "Not available"
        ),
        disabled=True
    )

    st.subheader("Account Information")

    st.text_input(
        "Email",
        value=st.session_state.email,
        disabled=True
    )

    st.text_input(
        "User ID",
        value=str(
            st.session_state.user_id
        ),
        disabled=True
    )

    st.subheader("🎯 Registered Stage")

    stage = st.session_state.stage

    stage_info = STAGES.get(stage)

    if stage_info:

        with st.container(border=True):

            st.subheader(
                f"{stage_info['icon']} "
                f"{stage_info['name']}"
            )

            st.write(
                stage_info["description"]
            )

    else:

        st.warning(
            "No valid stage is assigned to this account."
        )


# ============================================================
# SETTINGS
# ============================================================

elif (
    st.session_state.page == "settings"
    and st.session_state.logged_in
):

    st.title("⚙️ Settings")

    st.write(
        "Application preferences."
    )

    st.divider()

    st.checkbox(
        "Show assessment guidance",
        value=True
    )

    st.checkbox(
        "Enable notifications",
        value=False
    )