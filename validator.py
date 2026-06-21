def validate_response(data):

```
checks = []

checks.append(
    (
        "Name Field Present",
        "name" in data
    )
)

checks.append(
    (
        "Email Field Present",
        "email" in data
    )
)

checks.append(
    (
        "Username Field Present",
        "username" in data
    )
)

checks.append(
    (
        "Address Present",
        "address" in data
    )
)

checks.append(
    (
        "Phone Present",
        "phone" in data
    )
)

return checks
```
