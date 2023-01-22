from app.shemas import Data

# data = {
#  "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка "
#                 "существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,"
#                 "</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного "
#                 "наставника.</li><li>Написание автотестов</li></ul>",
#  "employment": "fullDay",
#  "address": {
#    "region": "Кировская",
#    "city": "Киров",
#    "street_type": "",
#    "street": "",
#    "house_type": "",
#    "house": "",
#    "value": "г Киров, ул Володарского, д 157",
#    "lat": 58.593565,
#    "lng": 49.672739
#  },
#  "name": "Junior Backend-developer",
#  "salary": {
#    "from": 30000,
#    "to": 70000,
#    "currency": "RUR",
#    "gross": False
#  },
#  "contacts": {
#    "fullName": "Журавлев Илья",
#    "phone": "79536762399",
#    "email": "ilya.zhuravlev@hrb.software"
#  }
# }

def main(data):
    data["salary"]["from_"] = data["salary"].pop("from")
    person = Data(**data)

    return {
#     "address": person.address.value,
#     "allow_messages": True,
#     "billing_type": "packageOrSingle",
#     "business_area": 1,
#     "contacts": {
#         "email": person.contacts.email,
#         "name": person.contacts.fullName,
#         "phone": {
#             "city": str(person.contacts.phone)[1:4],
#             "country": str(person.contacts.phone)[0],
#             "number": str(person.contacts.phone)[4:7]
#             + "-"
#             + str(person.contacts.phone)[7:9]
#             + "-"
#             + str(person.contacts.phone)[9:11],
#         },
#     },
#     "coordinates": {
#         "latitude": 58.593565,
#         "longitude": 49.672739
#     },
#     "description": person.description,
#     "experience": {
#         "id": "noMatter"
#     },
#     "html_tags": True,
#     "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
#     "name": person.name,
#     "salary": person.salary.to,
#     "salary_range": {
#         "from": person.salary.from_,
#         "to": person.salary.to
#     },
#     "schedule": {
#         "id": person.employment
#     }
# }

# print()
