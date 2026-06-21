def validate_response(data):

    checks = []

    checks.append(
        ("Name Present", "name" in data)
    )

    checks.append(
        ("Email Present", "email" in data)
    )

    return checks
