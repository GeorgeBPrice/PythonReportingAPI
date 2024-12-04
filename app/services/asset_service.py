
from turtle import pd
from sqlalchemy import func
from app.database import SessionLocal
from app.models.asset_models import Asset, AssetType

def get_asset_report_data():
    """
    Fetch and format asset report data for Quarto templates.
    """
    db = SessionLocal()
    try:
        # Aggregate asset data from the database
        asset_data = (
            db.query(
                Asset.AssetTypeId,
                Asset.Status,
                func.count(Asset.AssetId).label("Total"),
                func.sum(305 * Asset.AssetTypeId).label("TotalValue"),
            )
            .group_by(Asset.AssetTypeId, Asset.Status)
            .all()
        )

        # Transform data into a format suitable for the report
        report_data = {
            "Asset Type": [],
            "Total Assets": [],
            "Active Assets": [],
            "Retired Assets": [],
            "Total Asset Value": []
        }

        for record in asset_data:
            asset_type_name = db.query(AssetType.TypeName).filter_by(AssetTypeId=record.AssetTypeId).first()
            if asset_type_name:
                # Add the asset type
                if asset_type_name.TypeName not in report_data["Asset Type"]:
                    report_data["Asset Type"].append(asset_type_name.TypeName)
                    report_data["Total Assets"].append(0)
                    report_data["Active Assets"].append(0)
                    report_data["Retired Assets"].append(0)
                    report_data["Total Asset Value"].append(0)

                index = report_data["Asset Type"].index(asset_type_name.TypeName)
                report_data["Total Assets"][index] += record.Total
                report_data["Total Asset Value"][index] += record.TotalValue

                if record.Status == "Active":
                    report_data["Active Assets"][index] += record.Total
                elif record.Status == "Retired":
                    report_data["Retired Assets"][index] += record.Total
     
        return report_data
    finally:
        db.close()