def assert_status_code(response, expected_status_code):
    assert response.status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {response.status_code}"
    )


def assert_json_structure(data, expected_structure):
    """
    Asserts that the JSON data contains the expected structure and data types.

    :param data: The list of dictionaries returned in the JSON response.
    :param expected_structure: A dictionary where keys are expected fields and values are expected types.
    """
    assert isinstance(data, list), f"Expected response to be a list, but got {type(data)}"

    for item in data:
        assert isinstance(item, dict), f"Expected each item to be a dict, but got {type(item)}"

        for key, expected_type in expected_structure.items():
            assert key in item, f"Missing key '{key}' in response item"
            assert isinstance(item[key], expected_type), (
                f"Expected '{key}' to be of type {expected_type}, but got {type(item[key])}"
            )
