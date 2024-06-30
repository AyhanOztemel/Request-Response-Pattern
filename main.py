# main.py (sqlAlchmeyRepostory)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import ApartBuildingInfoRecordModel,SiteBuildingInfoRecordModel,Base
from requestModels import BuildingInfoRecordRequestModel
from responseModels import BuildingInfoRecordResponseModel
from typeguard import typechecked
from abc import ABC, abstractmethod
from mapper import AutoMapper


class AbstractORM(ABC):
    @abstractmethod
    def createTable(self):
        pass

@typechecked
class DatabaseManager(AbstractORM):
    def __init__(self, db_uri: str):
        # Veritabanı bağlantısını oluştur
        self.engine = create_engine(db_uri)
        # sessionmaker ile oturumu tanımla
        self.Session = sessionmaker(bind=self.engine)
        self.createTable()

    def createTable(self):
        # Veritabanı tablosunu oluştur
        Base.metadata.create_all(self.engine)

#*************json veri**********************************
import json
# JSON verisi
jsonData='''{"dbBuildingInfoName":"Karalar","dbBuildingInfoCity":"İstanbul",
           "dbBuildingInfoDistrict":"Beykoz","dbBuildingInfoNeighborhood":"çavuşbaşı",
           "dbBuildingInfoAvenue":"askeryokuşu","dbBuildingInfoStreet":"kanlıca",
           "dbBuildingInfoNumber":"7","dbBuildingInfoExplanation":"Kat 5 D:15"}'''
print("type(jsonData)--->",type(jsonData))

# JSON verisini Python sözlüğüne dönüştür
dbData = json.loads(jsonData)
print("type(dbData)--->",type(dbData))

# sözlük verisi **dbData ile Python class instance döner
buildingInfoRecordRequestModel=BuildingInfoRecordRequestModel(**dbData)

print("****************json converted To requestModel***********************")
print(buildingInfoRecordRequestModel.dbBuildingInfoName)
print(buildingInfoRecordRequestModel.dbBuildingInfoStreet)
print(buildingInfoRecordRequestModel.dbBuildingInfoExplanation)

print("****************requestModel converted To model instance with mapper***********************")
apartInstance=AutoMapper.autoMapperMethod(buildingInfoRecordRequestModel,ApartBuildingInfoRecordModel)
siteInstance=AutoMapper.autoMapperMethod(buildingInfoRecordRequestModel,SiteBuildingInfoRecordModel)

#********DATABASE OLUŞTURMA**************************        
sqlite_db_uri ='sqlite:///buildingInfoRecordDatabase.db'
sqlite_orm = DatabaseManager(sqlite_db_uri)

#***********DATABASE İŞLEMLERİ****************************
sqlite_session = sqlite_orm.Session()
sqlite_session.add(apartInstance )
sqlite_session.add(siteInstance)
sqlite_session.commit()

# ilk kaydı sorgulamak için
#buildingInfoRecordModel_instance = sqlite_session.query(ApartBuildingInfoRecordModel).first()

# id=13 olan kaydı sorgulamak için
buildingInfoRecordModel_instance = sqlite_session.query(ApartBuildingInfoRecordModel).filter(ApartBuildingInfoRecordModel.dbBuildingInfoId == 13).first()
buildingInfoRecordResponseModel=AutoMapper.autoMapperMethod(buildingInfoRecordModel_instance,BuildingInfoRecordResponseModel)
print("********************model query*********************************************************")
print("Building Info ID:", buildingInfoRecordModel_instance.dbBuildingInfoId)
print("Name:", buildingInfoRecordModel_instance.dbBuildingInfoName)
print("City:", buildingInfoRecordModel_instance.dbBuildingInfoCity)
print("District:", buildingInfoRecordModel_instance.dbBuildingInfoDistrict)
print("Neighborhood:", buildingInfoRecordModel_instance.dbBuildingInfoNeighborhood)
print("Avenue:", buildingInfoRecordModel_instance.dbBuildingInfoAvenue)
print("Street:",buildingInfoRecordModel_instance.dbBuildingInfoStreet)
print("Number:", buildingInfoRecordModel_instance.dbBuildingInfoNumber)
print("Explanation:", buildingInfoRecordModel_instance.dbBuildingInfoExplanation)
print()
print("****************modelQuery converted To responseModel with mapper***********************")
print("Building Info ID:", buildingInfoRecordResponseModel.dbBuildingInfoId)
print("Name:", buildingInfoRecordResponseModel.dbBuildingInfoName)
print("City:", buildingInfoRecordResponseModel.dbBuildingInfoCity)
print("District:", buildingInfoRecordResponseModel.dbBuildingInfoDistrict)
print("Neighborhood:", buildingInfoRecordResponseModel.dbBuildingInfoNeighborhood)
print("Avenue:", buildingInfoRecordResponseModel.dbBuildingInfoAvenue)
#print("Street:",buildingInfoRecordResponseModel.dbBuildingInfoStreet) #Bu veri response model'de yok hata verir
#print("Number:", buildingInfoRecordResponseModel.dbBuildingInfoNumber)#Bu veri response model'de yok  hata verir
#print("Explanation:", buildingInfoRecordResponseModel.dbBuildingInfoExplanation)#Bu veri response model'de yok hata verir

print("********************json***********************")
dictResponse =buildingInfoRecordResponseModel.__dict__
print("type(dictResponse)--->",type(dictResponse))
jsonResponse=json.dumps(dictResponse, ensure_ascii=False, indent=4)
print("type(jsonResponse)--->",type(jsonResponse))
print("jsonResponse------->", jsonResponse)


# tüm kayıtları sorgulamak için
"""
query_result = sqlite_session.query(ApartBuildingInfoRecordModel).all()
for row in query_result:
    print("Building Info ID:", row.dbBuildingInfoId)
    print("Name:", row.dbBuildingInfoName)
    print("City:", row.dbBuildingInfoCity)
    print("District:", row.dbBuildingInfoDistrict)
    print("Neighborhood:", row.dbBuildingInfoNeighborhood)
    print("Avenue:", row.dbBuildingInfoAvenue)
    print("Street:", row.dbBuildingInfoStreet)
    print("Number:", row.dbBuildingInfoNumber)
    print("Explanation:", row.dbBuildingInfoExplanation)"""
    


