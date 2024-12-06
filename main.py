from fastapi import FastAPI
from fastapi.responses import RedirectResponse
# from app.routers import asset_routes, expense_routes
from app.routers.asset_routes import router as asset_router

app = FastAPI()

# Include routers
app.include_router(asset_router, prefix="/assets", tags=["Asset Reports"])
# app.include_router(expense_routes.router, prefix="/expenses", tags=["Expenses"])

# Root route redirects to docs
@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

# 
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import FileResponse, RedirectResponse
# from app.services.asset_service import get_asset_report_data
# from app.generators.asset_generate_pdf import generate_asset_report_pdf
# from app.generators.asset_generate_xls import generate_asset_report_excel
# from app.generators.asset_generate_word import generate_asset_report_word
# import os

# app = FastAPI()

# # Redirect to Swagger UI when root is accessed
# @app.get("/")
# async def root():
#     return RedirectResponse(url="/docs")

# @app.post("/generate-asset-report/")
# async def generate_asset_report(report_type: str, output_format: str):
#     if report_type.lower() != "assetreport":
#         raise HTTPException(status_code=400, detail="Unsupported report type")

#     valid_formats = ["pdf", "xls", "docx"]
#     output_format = output_format.lower()  # Force input to lowercase

#     if output_format not in valid_formats:
#         raise HTTPException(status_code=400, detail=f"Unsupported format. Allowed formats: {', '.join(valid_formats)}")

#     # Fetch the data for the report
#     data = get_asset_report_data()

#     # Generate the file based on the requested format
#     try:
#         if output_format == "pdf":
#             file_path = generate_asset_report_pdf(data)
#         elif output_format == "xls":
#             file_path = generate_asset_report_excel(data)
#         elif output_format == "docx":
#             file_path = generate_asset_report_word(data)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating report: {str(e)}")

#     # Verify file existence before serving
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=500, detail=f"File not found: {file_path}")

#     # Serve the generated file back to the requestor
#     media_types = {
#         "pdf": "application/pdf",
#         "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
#         "xls": "application/vnd.ms-excel",
#     }
#     filename = f"AssetReport.{output_format}"
#     media_type = media_types.get(output_format, "application/octet-stream")

#     return FileResponse(file_path, media_type=media_type, filename=filename)
