from api_client import get_device_data
from validator import validate_response
from datetime import datetime

def generate_report(results):

```
report_lines = []

report_lines.append("=" * 50)
report_lines.append("API VALIDATION REPORT")
report_lines.append("=" * 50)
report_lines.append(
    f"Execution Time: {datetime.now()}"
)
report_lines.append("")

overall_status = True

for check, status in results:

    status_text = "PASS" if status else "FAIL"

    report_lines.append(
        f"{check:<30} : {status_text}"
    )

    if not status:
        overall_status = False

report_lines.append("")

report_lines.append(
    f"Overall Result : {'PASS' if overall_status else 'FAIL'}"
)

report_content = "\n".join(report_lines)

print(report_content)

with open(
    "reports/validation_report.txt",
    "w"
) as report_file:

    report_file.write(report_content)
```

def main():

```
print("\nStarting API Validation\n")

data = get_device_data()

print("API Response Received")

results = validate_response(data)

generate_report(results)

print("\nValidation Completed\n")
```

if **name** == "**main**":

```
main()
```
