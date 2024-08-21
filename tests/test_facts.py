import pytest
from api.client import CatFactsAPIClient
from utils.assertions import assert_status_code, assert_json_structure

client = CatFactsAPIClient()


def test_retrieve_facts():
    """
    Test Case 1: Verify that a GET request to the `/facts` endpoint returns a successful response.
    """
    response = client.get_facts()

    assert_status_code(response, 200)

    data = response.json()
    assert isinstance(data, list), "Expected response to be a list"
    assert len(data) > 0, "Expected at least one fact in the response"


def test_facts_structure():
    """
    Test Case 2: Verify that each fact returned contains the expected fields and data types.
    """
    response = client.get_facts()

    # Validate status code
    assert_status_code(response, 200)

    # Expected structure and data types
    expected_structure = {
        "_id": str,
        "text": str,
        "type": str,
    }

    # Validate the structure and data types of the facts
    data = response.json()
    assert_json_structure(data, expected_structure)


def test_retrieve_fact_by_id():
    """
    Test Case 3: Retrieve a specific fact by `_id`.
    """
    response = client.get_facts()
    assert_status_code(response, 200)
    data = response.json()

    fact_id = data[0]['_id']

    specific_fact_response = client.get_fact_by_id(fact_id)
    assert_status_code(specific_fact_response, 200)

    specific_fact_data = specific_fact_response.json()
    assert specific_fact_data['_id'] == fact_id, f"Expected _id {fact_id}, but got {specific_fact_data['_id']}"
    assert 'text' in specific_fact_data, "Fact should have a 'text' field"
    assert 'type' in specific_fact_data, "Fact should have a 'type' field"


def test_facts_with_query_params():
    """
    Test Case 4: Validate that the `/facts` endpoint supports query parameters like sorting.
    """
    params = {'sort': 'type'}
    response = client.get_facts(params=params)
    assert_status_code(response, 200)

    data = response.json()
    assert isinstance(data, list), "Expected response to be a list"
    assert len(data) > 0, "Expected at least one fact in the response"

    types = [fact['type'] for fact in data]
    assert types == sorted(types), "Facts are not sorted by type as expected"
