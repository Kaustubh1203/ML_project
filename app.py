# import streamlit as st
# import pandas as pd
# import joblib

# model_package = joblib.load(
#     "life_insurance_lapse_final_model.pkl"
# )

# model = model_package["model"]
# scaler = model_package["scaler"]
# features = model_package["features"]

# st.set_page_config(
#     page_title="Life Insurance Lapse Prediction",
#     page_icon="📋",
#     layout="wide"
# )

# st.title("Life Insurance Policy Lapse Prediction")
# st.write("Enter customer payment and policy details to predict policy lapse.")

# st.subheader("Customer Payment Information")

# col1, col2 = st.columns(2)

# with col1:
#     late_payments = st.number_input(
#         "Late Payments Last Year",
#         min_value=0,
#         value=0,
#         step=1
#     )

#     missed_payments = st.number_input(
#         "Missed Payments Last Year",
#         min_value=0,
#         value=0,
#         step=1
#     )

#     days_since_payment = st.number_input(
#         "Days Since Last Payment",
#         min_value=0,
#         value=0,
#         step=1
#     )

#     grace_period = st.number_input(
#         "Grace Period Used Count",
#         min_value=0,
#         value=0,
#         step=1
#     )

#     avg_days_to_pay = st.number_input(
#         "Average Days To Pay After Due",
#         min_value=0.0,
#         value=0.0
#     )

# with col2:
#     email_open_rate = st.number_input(
#         "Email Open Rate",
#         min_value=0.0,
#         max_value=1.0,
#         value=0.5
#     )

#     reminder_response_rate = st.number_input(
#         "Premium Reminder Response Rate",
#         min_value=0.0,
#         max_value=1.0,
#         value=0.5
#     )

#     policy_duration = st.number_input(
#         "Policy Duration (Years)",
#         min_value=0,
#         value=5,
#         step=1
#     )

#     service_calls = st.number_input(
#         "Customer Service Calls Last Year",
#         min_value=0,
#         value=0,
#         step=1
#     )

#     complaints = st.number_input(
#         "Complaints Filed Last Year",
#         min_value=0,
#         value=0,
#         step=1
#     )

# if st.button("Predict Policy Lapse"):

#     payment_behaviour_score = (
#         (late_payments * 2)
#         + (missed_payments * 4)
#         + (days_since_payment / 30)
#         + (grace_period * 2)
#     )

#     customer_service_risk_score = (
#         (service_calls * 2)
#         + (complaints * 5)
#     )

#     payment_delay_risk = (
#         late_payments
#         + (2 * missed_payments)
#         + (avg_days_to_pay / 10)
#         + grace_period
#     )

#     input_data = pd.DataFrame({
#         "payment_behaviour_score": [
#             payment_behaviour_score
#         ],
#         "customer_service_risk_score": [
#             customer_service_risk_score
#         ],
#         "policy_duration_years": [
#             policy_duration
#         ],
#         "days_since_last_payment": [
#             days_since_payment
#         ],
#         "payment_delay_risk": [
#             payment_delay_risk
#         ],
#         "email_open_rate": [
#             email_open_rate
#         ],
#         "late_payments_last_year": [
#             late_payments
#         ],
#         "missed_payments_last_year": [
#             missed_payments
#         ],
#         "avg_days_to_pay_after_due": [
#             avg_days_to_pay
#         ],
#         "premium_reminder_response_rate": [
#             reminder_response_rate
#         ]
#     })

#     input_data = input_data[features]

#     input_scaled = scaler.transform(input_data)

#     prediction = model.predict(input_scaled)[0]

#     probability = model.predict_proba(
#         input_scaled
#     )[0][1]

#     st.subheader("Prediction Result")

#     if prediction == 1:
#         st.error("⚠️ Customer is likely to Lapse")
#     else:
#         st.success("✅ Customer is unlikely to Lapse")

#     st.metric(
#         "Lapse Probability",
#         f"{probability * 100:.2f}%"
#     )


import streamlit as st
import pandas as pd
import joblib

model_package = joblib.load("life_insurance_lapse_final_model.pkl")

model = model_package["model"]
scaler = model_package["scaler"]
features = model_package["features"]

st.set_page_config(
    page_title="Life Insurance Lapse Prediction",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Life Insurance Policy Lapse Prediction")
st.write(
    "Predict the probability of a customer lapsing their life insurance policy."
)

st.divider()

st.header("👤 Customer Payment Information")

col1, col2 = st.columns(2)

with col1:
    late_payments = st.number_input(
        "Late Payments Last Year",
        min_value=0,
        value=0,
        step=1
    )

    missed_payments = st.number_input(
        "Missed Payments Last Year",
        min_value=0,
        value=0,
        step=1
    )

    days_since_payment = st.number_input(
        "Days Since Last Payment",
        min_value=0,
        value=0,
        step=1
    )

    grace_period = st.number_input(
        "Grace Period Used Count",
        min_value=0,
        value=0,
        step=1
    )

    avg_days_to_pay = st.number_input(
        "Average Days To Pay After Due",
        min_value=0.0,
        value=0.0,
        step=0.5
    )

with col2:
    email_open_rate = st.number_input(
        "Email Open Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

    reminder_response_rate = st.number_input(
        "Premium Reminder Response Rate",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.01
    )

    policy_duration = st.number_input(
        "Policy Duration (Years)",
        min_value=1,
        value=5,
        step=1
    )

    service_calls = st.number_input(
        "Customer Service Calls Last Year",
        min_value=0,
        value=0,
        step=1
    )

    complaints = st.number_input(
        "Complaints Filed Last Year",
        min_value=0,
        value=0,
        step=1
    )

st.divider()

st.header("⚙️ Calculated Business Scores")

payment_behaviour_score = (
    (late_payments * 2)
    + (missed_payments * 4)
    + (days_since_payment / 30)
    + (grace_period * 2)
)

customer_service_risk_score = (
    (service_calls * 2)
    + (complaints * 5)
)

payment_delay_risk = (
    late_payments
    + (2 * missed_payments)
    + (avg_days_to_pay / 10)
    + grace_period
)

score_col1, score_col2, score_col3 = st.columns(3)

with score_col1:
    st.metric(
        "Payment Behaviour Score",
        f"{payment_behaviour_score:.2f}"
    )

with score_col2:
    st.metric(
        "Customer Service Risk Score",
        f"{customer_service_risk_score:.2f}"
    )

with score_col3:
    st.metric(
        "Payment Delay Risk",
        f"{payment_delay_risk:.2f}"
    )

st.divider()

predict_button = st.button(
    "🔮 Predict Policy Lapse",
    use_container_width=True
)

if predict_button:

    input_data = pd.DataFrame({
        "payment_behaviour_score": [
            payment_behaviour_score
        ],
        "customer_service_risk_score": [
            customer_service_risk_score
        ],
        "policy_duration_years": [
            policy_duration
        ],
        "days_since_last_payment": [
            days_since_payment
        ],
        "payment_delay_risk": [
            payment_delay_risk
        ],
        "email_open_rate": [
            email_open_rate
        ],
        "late_payments_last_year": [
            late_payments
        ],
        "missed_payments_last_year": [
            missed_payments
        ],
        "avg_days_to_pay_after_due": [
            avg_days_to_pay
        ],
        "premium_reminder_response_rate": [
            reminder_response_rate
        ]
    })

    input_data = input_data[features]

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    probability_percentage = probability * 100

    st.divider()

    st.header("📊 Prediction Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:

        if prediction == 1:
            st.error("⚠️ Customer is Likely to Lapse")
        else:
            st.success("✅ Customer is Unlikely to Lapse")

    with result_col2:

        st.metric(
            "Lapse Probability",
            f"{probability_percentage:.2f}%"
        )

    st.progress(
        float(probability)
    )

    if probability >= 0.70:
        risk_level = "HIGH RISK"
        st.error(
            f"🔴 Risk Level: {risk_level}"
        )

    elif probability >= 0.40:
        risk_level = "MEDIUM RISK"
        st.warning(
            f"🟡 Risk Level: {risk_level}"
        )

    else:
        risk_level = "LOW RISK"
        st.success(
            f"🟢 Risk Level: {risk_level}"
        )

    st.divider()

    st.subheader("📋 Model Input Features")

    display_data = input_data.copy()

    st.dataframe(
        display_data,
        use_container_width=True
    )

st.divider()

st.caption(
    "Life Insurance Policy Lapse Prediction System | "
    "Machine Learning Project"
)