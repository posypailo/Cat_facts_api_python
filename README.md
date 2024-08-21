# Cat Facts API Test Automation Framework

This project is an advanced test automation framework for testing the Cat Facts API using Python and `pytest`. The framework is designed to be modular, scalable, and easy to use, with clear separation of concerns and reusable components.

## Project Structure

The repository follows a well-organized structure to separate different aspects of the test automation framework. Below is the directory structure:
```
cat_facts_api_tests/
├── config/
│ └── settings.py # Configuration file (e.g., API base URL)
├── api/
│ └── client.py # API client to interact with the endpoints
├── tests/
│ └── test_facts.py # Test cases for the Cat Facts API
├── utils/
│ └── assertions.py # Utility functions for assertions
├── requirements.txt # Python package dependencies
└── pytest.ini # pytest configuration file
```

## Test Cases

The following test cases have been implemented to validate the `/facts` endpoint of the Cat Facts API:

| Test Case ID | Test Case Description                                                             | Steps                                                                                                 | Expected Result                                                                                               | Validation                                                                                                  |
|--------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| TC01         | Verify that a GET request to the `/facts` endpoint returns a successful response  | 1. Send a GET request to the `/facts` endpoint.<br>2. Check that the response status code is 200.<br>3. Check that the response contains a list of facts. | - The status code should be 200.<br>- The response should contain a list of facts.                            | Assert that the status code is 200.<br>Assert that the response data is a list and contains at least one fact.|
| TC02         | Verify that each fact returned contains the expected fields and data types        | 1. Send a GET request to the `/facts` endpoint.<br>2. Validate that each fact contains the expected fields: `_id`, `text`, and `type`.<br>3. Validate that the fields have the correct data types. | - Each fact should have `_id`, `text`, and `type` fields.<br>- The fields should have the correct data types (e.g., `str`). | Assert that the JSON structure includes the required fields.<br>Assert that the fields have the correct data types. |
| TC03         | Retrieve a specific fact by `_id` and verify it matches the expected data         | 1. Retrieve all facts.<br>2. Extract the `_id` of the first fact.<br>3. Send a GET request to `/facts/{id}` with the extracted `_id`.<br>4. Validate that the response contains the correct fact. | - The `_id` in the response should match the requested `_id`.<br>- The response should contain valid `text` and `type` fields. | Assert that the `_id` in the response matches the one used in the request.<br>Assert that the other fields are present and valid. |
| TC04         | Validate that the `/facts` endpoint supports query parameters (e.g., sorting)     | 1. Send a GET request to the `/facts` endpoint with a query parameter (e.g., `sort=type`).<br>2. Validate that the response respects the query parameter. | - The facts should be sorted or filtered according to the query parameter.                                     | Assert that the facts are sorted or filtered as expected based on the query parameter.                     |

## Validation Used and Why

In this test framework, the following types of validation are used:

### 1. **Status Code Validation**
   - **Why**: The status code is the first indicator of whether the API request was successful. It ensures that the server responded correctly (e.g., status code 200 for success).
   - **How**: Using `assert_status_code` function, the status code returned by the API is compared against the expected status code.

### 2. **JSON Structure Validation**
   - **Why**: Validating the structure of the JSON response ensures that the API returns the expected fields, which is crucial for the consistency of the data and application logic.
   - **How**: The `assert_json_structure` function checks that each fact in the response contains the required fields (`_id`, `text`, `type`).

### 3. **Data Type Validation**
   - **Why**: Ensuring that each field in the JSON response has the correct data type helps prevent data-related issues in downstream processing. For example, ensuring that `_id` is always a string prevents potential errors when working with this data.
   - **How**: The `assert_json_structure` function has been extended to validate that the fields not only exist but also have the correct data types.

### 4. **Content Validation**
   - **Why**: In some cases, it's important to verify that the content returned by the API matches the expected data (e.g., when retrieving a specific fact by `_id`).
   - **How**: Assertions are used to ensure that the content of the response (e.g., `_id`, `text`) matches the expected values.

### How to Run the Tests

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Run the tests:   
 ```bash
   pytest -v
   ```

### Summary

1. **Test Case Table**: The README includes a table with a detailed description of each test case, including the steps, expected results, and validation methods.
2. **Validation Explanation**: It explains why each type of validation is used and how it is implemented in the test cases.
3. **Running the Tests**: The README provides clear instructions on how to install dependencies and run the tests using `pytest`.