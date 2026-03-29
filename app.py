import streamlit as st
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import ttest_ind

st.title("ANOVA + Tukey + T-test App")

# 📂 File upload instead of hardcoded path
file = st.file_uploader("Upload Auto.csv file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Raw Data")
    st.dataframe(df.head())

    # 🔧 Data cleaning
    columns = ['mpg', 'displacement', 'horsepower', 'weight']
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(df[col].mean())

    st.success("Data cleaned!")

    # -------------------------------
    # 🔹 TWO WAY ANOVA (no interaction)
    # -------------------------------
    if st.button("Run ANOVA (No Interaction)"):
        fit1 = ols('horsepower ~ C(origin) + C(cylinders)', data=df).fit()
        anova = sm.stats.anova_lm(fit1, type=2)

        st.subheader("ANOVA (No Interaction)")
        st.dataframe(anova)

    # -------------------------------
    # 🔹 TWO WAY ANOVA (with interaction)
    # -------------------------------
    if st.button("Run ANOVA (With Interaction)"):
        fit2 = ols('horsepower ~ C(origin) * C(cylinders)', data=df).fit()
        anova2 = sm.stats.anova_lm(fit2, type=2)

        st.subheader("ANOVA (With Interaction)")
        st.dataframe(anova2)

    # -------------------------------
    # 🔹 Tukey HSD
    # -------------------------------
    if st.button("Run Tukey HSD"):
        df['groups'] = df['origin'].astype(str) + ' ' + df['cylinders'].astype(str)

        tukey = pairwise_tukeyhsd(
            endog=df['horsepower'],
            groups=df['groups'],
            alpha=0.05
        )

        st.subheader("Tukey HSD Results")
        st.text(tukey.summary())

    # -------------------------------
    # 🔹 T-test (custom groups)
    # -------------------------------
    st.subheader("T-test Between Groups")

    g1_label = st.text_input("Enter Group 1 (e.g., 1 8)", "1 8")
    g2_label = st.text_input("Enter Group 2 (e.g., 3 4)", "3 4")

    if st.button("Run T-test"):
        df['groups'] = df['origin'].astype(str) + ' ' + df['cylinders'].astype(str)

        g1 = df[df['groups'] == g1_label]['horsepower']
        g2 = df[df['groups'] == g2_label]['horsepower']

        if len(g1) > 0 and len(g2) > 0:
            ttest = ttest_ind(g1, g2, alternative='greater')

            st.write("T-test Result:", ttest)

            idx = df[(df['groups'] == g1_label) | (df['groups'] == g2_label)].index
            st.write("Total observations in both groups:", len(idx))
        else:
            st.error("Invalid group names! Check your input.")
