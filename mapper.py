from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.state import InstanceState
import json
class AutoMapper():
    @staticmethod
    def autoMapperMethod(instance,SourceClass):
        
        if hasattr(instance, '_sa_instance_state') and isinstance(instance._sa_instance_state, InstanceState):
            print("Bu instance bir SQLAlchemy ORM sınıfına aittir.")
            
            def to_dict(instance):
                print("2222222222222222222222222222222222222222222222")
                sourceInstance=SourceClass()
                print("33333333333333333333333333333333333333333333")
                liste=list(sourceInstance.__dict__.keys())
                print("44444444444444444444444444444444444444444444")
                # SQLAlchemy modelindeki sütunları al
                columns = [column.key for column in class_mapper(instance.__class__).columns]           
                return {column: getattr(instance, column) for column in columns if column in liste}
           
            obj_dict = to_dict(instance)  #instance sözlük yapısına dönüştürür
            print("1111111111111111111111111111--->",obj_dict)
            print(type(obj_dict))
            json_data = json.dumps(obj_dict, ensure_ascii=False)  #sözlük yapısını json dönüştürür

            print(json_data)
            #json_data2 = json.dumps(obj_dict, default=lambda x:x.__dict__)
            #print(json_data2)
            print()        
            print(type(json_data))
            print("ffffffffffffffffffffffffffffffffffffffffffffffffffffff")
            return json.loads(json_data,object_hook=lambda i: SourceClass(**i))
            #return json.loads(json_data,object_hook=lambda i: SourceDto(**i))
        else:
            print("Bu instance bir SQLAlchemy ORM sınıfına ait değildir.")
            #SourceDto özelliklerini bir sözlüğe atama
            instanceDict = instance.__dict__
            print(instanceDict)
            print(type(instanceDict))
            json_data2 = json.dumps(instanceDict, ensure_ascii=False)
            print(json_data2)
            print(type(json_data2))# Sözlüğü ekrana yazdır
            #return json.loads(json_data2,object_hook=lambda i: Model(**i))
            return json.loads(json_data2,object_hook=lambda i: SourceClass(**i))
            
