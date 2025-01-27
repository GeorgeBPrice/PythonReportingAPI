from fastapi.testclient import TestClient
from app.main import app
from tests.test_database import test_database_connection
...
# TODO: finish this off
async def test_fetch_asset_report_data_integration(test_database_connection):
    # using FastAPI TestClient
    with TestClient(app) as client:

        response = client.get("/assets/fetch-asset-report-data/")
        assert response.status_code == 200
        
        # fetch data from actual test DB session
        from app.services.asset_service import get_asset_report_data
        expected_data = await get_asset_report_data(test_database_connection)
        assert response.json() == expected_data

