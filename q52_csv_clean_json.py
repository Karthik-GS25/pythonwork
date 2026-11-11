"""52. Clean employee CSV text and write cleaned_data.json when run."""

import csv, json, io


def clean_csv(csv_text, output="cleaned_data.json"):
    records = []
    for row in csv.DictReader(csv_text.strip().splitlines()):
        row = {key: value.strip() for key, value in row.items()}
        if (
            not row.get("age")
            or not row.get("salary")
            or row["salary"].lower() == "unknown"
        ):
            continue
        try:
            age = int(row["age"])
            salary = float(row["salary"])
        except ValueError:
            continue
        records.append(
            {
                "name": row.get("name", ""),
                "age": age,
                "salary": salary,
                "join_date": row.get("join_date", ""),
            }
        )
    with open(output, "w", encoding="utf8") as file:
        json.dump(records, file, indent=2)
    return records


print(clean_csv("name,age,salary,join_date\n Ana ,20,30000,2025-01-01"))
