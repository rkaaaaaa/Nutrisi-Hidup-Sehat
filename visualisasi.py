import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# Define column names manually (now 24 columns)
column_names = [
    "Ages",
    "Gender",
    "Height",
    "Weight",
    "Activity Level",
    "Dietary Preference",
    "Daily Calorie Target",
    "Protein",
    "Sugar",
    "Sodium",
    "Calories",
    "Carbohydrates",
    "Fiber",
    "Fat",
    "Breakfast Suggestion",
    "Lunch Suggestion",
    "Dinner Suggestion",
    "Snack Suggestion",
    "Disease",
    "Column 20",
    "Column 21",
    "Column 22",
    "Column 23",
    "Column 24",
]

# Load the CSV file (using readlines to handle the lack of header)
with open("Food_and_Nutrition__.csv", "r") as f:
    lines = f.readlines()

# Create a list of lists to store the data
data = []
for line in lines:
    row = line.strip().split(",")
    data.append(row)

# Create a pandas DataFrame from the data
df = pd.DataFrame(data, columns=column_names)

# Convert relevant columns to numeric
df["Daily Calorie Target"] = pd.to_numeric(df["Daily Calorie Target"], errors='coerce')
df["Protein"] = pd.to_numeric(df["Protein"], errors='coerce')
df["Sodium"] = pd.to_numeric(df["Sodium"], errors='coerce')
df["Calories"] = pd.to_numeric(df["Calories"], errors='coerce')

# Visualization Page
st.title("Food and Nutrition Data Visualization")

# Select chart type
chart_type = st.selectbox(
    "Select Chart Type",
    ["Scatter Plot", "Calorie Target vs Protein", "Sodium vs Calories", "Word Cloud", "Bar Chart"],
)

if chart_type == "Scatter Plot":
    st.header("Scatter Plot")
    # Filter numeric columns for selection
    numeric_columns = df.select_dtypes(include=['number']).columns
    x_axis = st.selectbox("Select X-axis", numeric_columns)
    y_axis = st.selectbox("Select Y-axis", numeric_columns)

    fig, ax = plt.subplots()
    # Convert to float for plotting, handling potential errors
    try:
        # Check if columns are selected *before* accessing them
        if x_axis is not None and y_axis is not None:
            ax.scatter(df[x_axis], df[y_axis])  # No need to convert to float again
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title("Data Visualization")
            st.pyplot(fig)
        else:
            st.warning("Please select both X-axis and Y-axis columns.")
    except ValueError:
        st.error(
            f"Error: Cannot plot '{x_axis}' vs '{y_axis}'. Ensure both columns contain numeric data."
        )

elif chart_type == "Calorie Target vs Protein":
    st.header("Calorie Target vs Protein")
    fig, ax = plt.subplots()
    # Convert to float for plotting, handling potential errors
    try:
        ax.scatter(df["Daily Calorie Target"], df["Protein"])  # No need to convert to float again
    except ValueError:
        st.error(
            "Error: Cannot plot 'Daily Calorie Target' vs 'Protein'. Ensure both columns contain numeric data."
        )
    else:  # Only plot if conversion is successful
        ax.set_xlabel("Daily Calorie Target")
        ax.set_ylabel("Protein")
        ax.set_title("Calorie Target vs Protein")
        st.pyplot(fig)

elif chart_type == "Sodium vs Calories":
    st.header("Sodium vs Calories")
    fig, ax = plt.subplots()
    # Convert to float for plotting, handling potential errors
    try:
        ax.scatter(df["Sodium"], df["Calories"])  # No need to convert to float again
    except ValueError:
        st.error(
            "Error: Cannot plot 'Sodium' vs 'Calories'. Ensure both columns contain numeric data."
        )
    else:  # Only plot if conversion is successful
        ax.set_xlabel("Sodium")
        ax.set_ylabel("Calories")
        ax.set_title("Sodium vs Calories")
        st.pyplot(fig)

elif chart_type == "Word Cloud":
    st.header("Word Cloud")
    # Combine text from relevant columns
    text = " ".join(
        df["Breakfast Suggestion"].astype(str)
        + " "
        + df["Lunch Suggestion"].astype(str)
        + " "
        + df["Dinner Suggestion"].astype(str)
        + " "
        + df["Snack Suggestion"].astype(str)
    )

    # Create and display the word cloud
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(
        width=800, height=400, background_color="white", stopwords=stopwords
    ).generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

elif chart_type == "Bar Chart":
    st.header("Bar Chart")
    column_to_count = st.selectbox("Select Column for Bar Chart", df.columns)

    counts = df[column_to_count].value_counts()

    plt.figure(figsize=(10, 6))
    counts.plot(kind="bar")
    plt.title(f"{column_to_count} Distribution")
    plt.xlabel(column_to_count)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(plt)