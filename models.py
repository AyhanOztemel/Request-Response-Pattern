
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class ApartBuildingInfoRecordModel(Base):
        __tablename__ = 'apartBuildingInfoRecordDatabase2'
        dbBuildingInfoId = Column(Integer, primary_key=True, autoincrement=True)
        dbBuildingInfoName = Column(String)
        dbBuildingInfoCity = Column(String)
        dbBuildingInfoDistrict = Column(String)
        dbBuildingInfoNeighborhood = Column(String)
        dbBuildingInfoAvenue = Column(String)
        dbBuildingInfoStreet = Column(String)
        dbBuildingInfoNumber = Column(String)
        dbBuildingInfoExplanation = Column(String)

    
class SiteBuildingInfoRecordModel(Base):
        __tablename__ = 'siteBuildingInfoRecordDatabase2'
        dbBuildingInfoId = Column(Integer, primary_key=True, autoincrement=True)
        dbBuildingInfoName = Column(String)
        dbBuildingInfoCity = Column(String)
        dbBuildingInfoDistrict = Column(String)
        dbBuildingInfoNeighborhood = Column(String)
        dbBuildingInfoAvenue = Column(String)
        dbBuildingInfoStreet = Column(String)
        dbBuildingInfoNumber = Column(String)
        dbBuildingInfoExplanation = Column(String)   

   
