import os
from app.generators.asset_generate_pdf import generate_asset_report_pdf

def test_generate_asset_report_pdf():
    # Mock data
    data = {
        "Asset Type": ["Mobile", "Laptop"],
        "Total Assets": [10, 20],
        "Active Assets": [5, 15],
        "Inactive Assets": [3, 3],
        "Retired Assets": [2, 2],
        "Total Value": [1000.0, 2000.0],
    }

    # Generate the PDF
    output_path = generate_asset_report_pdf(data)

    # Assert the file exists
    assert os.path.exists(output_path)

    # Clean up
    os.remove(output_path)
