import pytest
from unittest.mock import AsyncMock
from app.services.asset_service import get_asset_report_data

@pytest.mark.asyncio
async def test_get_asset_report_data():
    """
    Test the get_asset_report_data function with mocked database session.
    """
    # Mock database session
    mock_db = AsyncMock()

    # Mock query results
    mock_query_result = [
        ("Mobile", 10, 5, 3, 2, 1000.0),
        ("Laptop", 20, 15, 3, 2, 2000.0),
    ]

    # Make the db.execute() call return something iterable
    mock_db.execute.return_value.__iter__.return_value = iter(mock_query_result)

    # Call the service function
    result = await get_asset_report_data(mock_db)

    # Expected result
    expected_result = {
        "Asset Type": ["Mobile", "Laptop"],
        "Total Assets": [10, 20],
        "Active Assets": [5, 15],
        "Inactive Assets": [3, 3],
        "Retired Assets": [2, 2],
        "Total Value": [1000.0, 2000.0],
    }

    assert result == expected_result
