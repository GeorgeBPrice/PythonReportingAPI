from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class AssetReport(Base):
    __tablename__ = "AssetReports"
    __table_args__ = {"schema": "Report"}

    AssetsReportId = Column(Integer, primary_key=True, autoincrement=True)
    TotalAssets = Column(Integer, nullable=True)
    TotalActiveAssets = Column(Integer, nullable=True)
    TotalRetiredAssets = Column(Integer, nullable=True)
    AssetsByCategory = Column(String, nullable=True)
    AssetsByPersonnel = Column(String, nullable=True)
    TotalAssetValue = Column(Float, nullable=True)
    Notes = Column(String(500), nullable=True)
    GeneratedOn = Column(DateTime, default=datetime.now)
    GeneratedBy = Column(String, default="system")

class Asset(Base):
    __tablename__ = "Assets"
    __table_args__ = {"schema": "Asset"}

    AssetId = Column(Integer, primary_key=True, autoincrement=True)
    AssetName = Column(String(255), nullable=True)
    AssetTypeId = Column(Integer, ForeignKey("Asset.AssetTypes.AssetTypeId"), nullable=False)
    BrandId = Column(Integer, nullable=False)
    ModelId = Column(Integer, nullable=True)
    SerialNumber = Column(String(50), nullable=True)
    IMEI = Column(String(20), nullable=True)
    SimCode = Column(String(20), nullable=True)
    MobileNumber = Column(String(15), nullable=True)
    ProviderId = Column(Integer, nullable=True)
    PlanId = Column(Integer, nullable=True)
    PurchaseDate = Column(DateTime, nullable=True)
    AssetValue= Column(Float, nullable=True)
    PurchaseInvoice = Column(String(100), nullable=True)
    WarrantyExpiry = Column(DateTime, nullable=True)
    Status = Column(String(50), nullable=True)
    CreatedAt = Column(DateTime, default=datetime.now)
    CreatedBy = Column(String, default="system")
    UpdatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, default="system")

    # Relationships
    AssetType = relationship("AssetType", back_populates="Assets")


class AssetType(Base):
    __tablename__ = "AssetTypes"
    __table_args__ = {"schema": "Asset"}

    AssetTypeId = Column(Integer, primary_key=True, autoincrement=True)
    TypeName = Column(String(255), nullable=False)

    # Relationship with Assets
    Assets = relationship("Asset", back_populates="AssetType")