import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
async def mock_get_data():
    """
    Fixture to mock the get_asset_report_data function and clean up connections.
    """
    with patch("app.services.asset_service.get_asset_report_data", new_callable=AsyncMock) as mock:
        yield mock
        
    from app.database import engine
    await engine.dispose()



@pytest.mark.asyncio
@pytest.mark.parametrize(
    "mock_data",
    [
        # Test case 1: Standard mock data
        {
            "Asset Type": ["Mobile", "Laptop"],
            "Total Assets": [10, 20],
            "Active Assets": [5, 15],
            "Inactive Assets": [3, 3],
            "Retired Assets": [2, 2],
            "Total Value": [1000.0, 2000.0],
        },
        # Test case 2: Different asset types and values
        {
            "Asset Type": ["Desktop", "Tablet"],
            "Total Assets": [5, 10],
            "Active Assets": [3, 7],
            "Inactive Assets": [1, 2],
            "Retired Assets": [1, 1],
            "Total Value": [500.0, 1200.0],
        },
        # Test case 3: Edge case with no assets
        {
            "Asset Type": [],
            "Total Assets": [],
            "Active Assets": [],
            "Inactive Assets": [],
            "Retired Assets": [],
            "Total Value": [],
        },
    ],
)
async def test_fetch_asset_report_data(mock_get_data, mock_data):
    """
    Test the /assets/fetch-asset-report-data/ endpoint.
    Focus on response structure and behavior, not specific data values.
    """
    # Mock the service response with provided test data
    mock_get_data.return_value = mock_data

    # Make the GET request to the endpoint
    response = client.get("/assets/fetch-asset-report-data/")

    # Assert the status code is correct
    assert response.status_code == 200

    # Validate the response structure
    response_data = response.json()
    assert "Asset Type" in response_data
    assert "Total Assets" in response_data
    assert "Active Assets" in response_data
    assert "Inactive Assets" in response_data
    assert "Retired Assets" in response_data
    assert "Total Value" in response_data

    # Ensure the lengths of lists match for corresponding fields
    assert len(response_data["Asset Type"]) == len(response_data["Total Assets"])
    assert len(response_data["Total Assets"]) == len(response_data["Active Assets"])
    assert len(response_data["Active Assets"]) == len(response_data["Inactive Assets"])
    assert len(response_data["Inactive Assets"]) == len(response_data["Retired Assets"])
    assert len(response_data["Retired Assets"]) == len(response_data["Total Value"])
