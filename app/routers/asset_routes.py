from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db
from app.services.asset_service import get_asset_report_data
from app.generators.asset_generate_pdf import generate_asset_report_pdf
from app.generators.asset_generate_xls import generate_asset_report_excel
from app.generators.asset_generate_word import generate_asset_report_word
import os

router = APIRouter()

@router.post("/generate/")
async def generate_asset_report(report_type: str, output_format: str, db: AsyncSession = Depends(get_db)):
    if report_type.lower() != "assetreport":
        raise HTTPException(status_code=400, detail="Unsupported report type")

    valid_formats = ["pdf", "xls", "docx"]
    output_format = output_format.lower()

    if output_format not in valid_formats:
        raise HTTPException(status_code=400, detail=f"Unsupported format. Allowed formats: {', '.join(valid_formats)}")

    # Fetch the data for the report
    try:
        data = await get_asset_report_data(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching report data: {str(e)}")

    # Generate the file based on the requested format
    try:
        if output_format == "pdf":
            file_path = generate_asset_report_pdf(data)
        elif output_format == "xls":
            file_path = generate_asset_report_excel(data)
        elif output_format == "docx":
            file_path = generate_asset_report_word(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating report: {str(e)}")

    # Verify file existence before serving
    if not os.path.exists(file_path):
        raise HTTPException(status_code=500, detail=f"File not found: {file_path}")

    # Serve the generated file
    media_types = {
        "pdf": "application/pdf",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "xls": "application/vnd.ms-excel",
    }
    filename = f"AssetReport.{output_format}"
    media_type = media_types.get(output_format, "application/octet-stream")

    return FileResponse(file_path, media_type=media_type, filename=filename)


@router.get("/fetch-asset-report-data/")
async def fetch_asset_report_data(db: AsyncSession = Depends(get_db)):
    try:
        data = await get_asset_report_data(db)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching asset report data: {str(e)}")
