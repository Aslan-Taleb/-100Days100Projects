import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data_frame():
    records = []

    for current_page in range(34):
        endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{current_page + 1}"
        response = requests.get(endpoint)
        print(f"Fetching page {current_page + 1} with status code {response.status_code}...")

        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.select("table.data-table tbody tr")
        print(f"Found {len(rows)} rows on page {current_page + 1}...")

        for row in rows:
            cells = row.select("span.data-table__value")
            record = {
                "Undergraduate Major": cells[1].getText(),
                "Starting Median Salary": float(cells[3].getText().strip("$").replace(",", "")),
                "Mid-Career Median Salary": float(cells[4].getText().strip("$").replace(",", "")),
            }
            records.append(record)
            print(f"Added record for {record['Undergraduate Major']}")

    return pd.DataFrame(records)


def main():
    df = get_data_frame()

    # Afficher le salaire médian de départ moyen pour toutes les majors
    starting_median_salary_mean = df["Starting Median Salary"].mean()
    print(f"Starting median salary mean: ${starting_median_salary_mean:.2f}")

    # Afficher le salaire médian de milieu de carrière moyen pour toutes les majors
    mid_career_median_salary_mean = df["Mid-Career Median Salary"].mean()
    print(f"Mid-career median salary mean: ${mid_career_median_salary_mean:.2f}")

    # Afficher les 10 majors ayant les salaires de départ les plus élevés
    top_starting_median_salaries = df.sort_values(by="Starting Median Salary", ascending=False).head(10)
    print("\nTop 10 majors by starting median salary:")
    print(top_starting_median_salaries[["Undergraduate Major", "Starting Median Salary"]])

    # Afficher les 10 majors ayant les salaires de milieu de carrière les plus élevés
    top_mid_career_median_salaries = df.sort_values(by="Mid-Career Median Salary", ascending=False).head(10)
    print("\nTop 10 majors by mid-career median salary:")
    print(top_mid_career_median_salaries[["Undergraduate Major", "Mid-Career Median Salary"]])
main()