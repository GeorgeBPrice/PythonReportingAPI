from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import Integer, cast, func, case
from app.models.asset_models import Asset, AssetType


async def get_asset_report_data(db: AsyncSession):
    """
    Fetch asset report data and format into structured report data.
    """
    # Fetch aggregated asset data, including type, name and status breakdown
    result = await db.execute(
        select(
            AssetType.TypeName,
            func.count(Asset.AssetId).label("TotalAssets"),
            func.sum(case((Asset.Status == "Active", 1), else_=0)).label("ActiveAssets"),
            func.sum(case((Asset.Status == "Inactive", 1), else_=0)).label("RetiredAssets"),
            func.sum(case((Asset.Status == "Retired", 1), else_=0)).label("RetiredAssets"),
            cast(func.sum(Asset.AssetValue), Integer).label("TotalAssetValue"),
        )
        .join(AssetType, Asset.AssetTypeId == AssetType.AssetTypeId)
        .group_by(AssetType.TypeName)
    )

    # Transform the query result into the report structure
    report_data = {
        "Asset Type": [],
        "Total Assets": [],
        "Active Assets": [],
        "Inactive Assets": [],
        "Retired Assets": [],
        "Total Value": [],
    }

    for row in result:
        type_name, total_assets, active_assets, inactive_assets, retired_assets, total_value = row
        report_data["Asset Type"].append(type_name)
        report_data["Total Assets"].append(total_assets)
        report_data["Active Assets"].append(active_assets)
        report_data["Inactive Assets"].append(inactive_assets)
        report_data["Retired Assets"].append(retired_assets)
        report_data["Total Value"].append(total_value)

    return report_data
