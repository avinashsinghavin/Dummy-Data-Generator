from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from faker import Faker
import random



def home(request):
  return HttpResponse("We Welcome You")


def analyze(request):
  print(request.method)
  if request.method == 'POST':
    print("==============")
    print(request.POST.get('jsonid'))
    print("===============")
    # with open('data.txt', 'w') as outfile:
    #     json.dump(result, outfile)
    return HttpResponse("Capts Section"+request.POST.get('jsonid'))
  else:
    params = [{'name': 'Avin', 'place' : 'mars'},{'name': 'Avin', 'place' : 'mars'},{'name': 'Avin', 'place' : 'mars'},{'name': 'Avin', 'place' : 'mars'}]
    return JsonResponse(params,safe=False)

    
@csrf_exempt
def about(request):
  data = [{"userId": 1,"id": 1,"title": "sup","body": "qui"},{"userId": 1,"id": 3,"title": "aut","body": "et iut"},{"userId": 1,"id": 4,"title": "eu","body": "ullamlo"},{ "userId": 1,"id": 5,"title": "nescio","body": "repudie"},{"userId": 1,"id": 6,"title": "doloa","body": "ut as"}]
  print(request.method)
  if request.method=='POST':
    return JsonResponse(data, safe=False)
  else:
    return JsonResponse(data, safe=False)

@csrf_exempt
def getdata(request):
  if request.method=='POST':
    fakerdata = json.loads(request.body)
    print("===========================")
    print((fakerdata))
    getFakedata(fakerdata)
    print("============================")
    return JsonResponse({'message':'Success', 'data':getFakedata(fakerdata)}, safe=False)
  else:
    return JsonResponse({'message':'Error'}, safe=False)


def getFakedata(value) :
  data = value['data']
  print(data)
  fake = Faker(['en_IN']) #hi_IN
  quantity = data['quantity']
  requiredfields = data['required']
  allkey = requiredfields.keys()
  #print(allkey)
  listofkey = [k for k in allkey]     # converting Dictionary(dict_key(['','']) to list
  #print(list)
  print("===========================================")
  alldata = [] # getting all data of json in key list
  allvalues = []  # getting all data of json value:
  Header = []

  for i in range(0, len(listofkey)):
      if isinstance(requiredfields[listofkey[i]], str):
          alldata.append(listofkey[i])
          allvalues.append(requiredfields[listofkey[i]])
      if isinstance(requiredfields[listofkey[i]], list):
          alldata.append(listofkey[i])
          allvalues.append(requiredfields[listofkey[i]])
      if isinstance(requiredfields[listofkey[i]], dict):
          tempdict = requiredfields[listofkey[i]]
          alldict = tempdict.keys()
          listofdict = [l for l in alldict]

          for j in range(0, len(listofdict)):
              alldata.append(listofdict[j])
              allvalues.append(tempdict[listofdict[j]])
      #print(type(requiredfields[listofkey[i]]))

  for i in range(0, len(alldata)):
      print(alldata[i], " ", allvalues[i])

  # creating Header=======================================
  for i in range(0, len(alldata)):
      if isinstance(allvalues[i], list) and (alldata[i] == 'Name'):
          for j in range(0, len(allvalues[i])):
              Header.append(allvalues[i][j])
      else:
          Header.append(alldata[i])
  #=======================================================
  csv_list = []
  print("------------------------------")

  for i in range(0, int(quantity)):
      dict1 = {}
      for j in range(0, len(alldata)):
          if (alldata[j] == "User-Name"):
              dict1["User-Name"] = fake.name()
          if (alldata[j] == "Email"):
              dict1["Email"] = fake.email()
          if (alldata[j] == "Password"):
              dict1["Password"] = fake.password(length = 12, special_chars=False)
          if(alldata[j] == "Security-Question"):
              if isinstance(allvalues[j], list):
                  dict1['Security-Question'] = allvalues[j][random.randrange(0,len(allvalues[j]))]
              else:
                  dict1['Security-Question'] = fake.sentence() + '?'
          if(alldata[j] == 'Security Answer'):
              dict1["Security Answer"] = fake.sentence()
          if(alldata[j] == 'Preferred Language'):
              if isinstance(allvalues[j], list):
                  dict1['Preferred Language'] = allvalues[j][random.randrange(0, len(allvalues[j]))]
              else:
                  dict1['Preferred Language'] = fake.sentence() + '?'
          if(alldata[j] == 'Name'):
              for a in range(0, len(allvalues[j])):
                  if allvalues[j][a] == 'First':
                      dict1['First'] = fake.first_name()
                  if allvalues[j][a] == 'Middle':
                      dict1['Middle'] = fake.last_name()
                  if allvalues[j][a] == 'Last':
                      dict1['Last'] = fake.last_name()
          if (alldata[j] == 'Gender'):
              if isinstance(allvalues[j], list):
                  dict1['Gender'] = allvalues[j][random.randrange(0, len(allvalues[j]))]
          if(alldata[j] == 'Date of Birth'):
              dict1['Date of Birth'] = fake.date_of_birth()
          if(alldata[j] == 'Occupation'):
              if isinstance(allvalues[j], list):
                  dict1['Occupation'] = allvalues[j][random.randrange(0, len(allvalues[j]))]
              else :
                  dict1['Occupation'] = fake.job()
          if(alldata[j] == 'Marital Status'):
              dict1['Marital Status'] = allvalues[j][random.randrange(0, len(allvalues[j]))]
          if(alldata[j] == 'Country'):
              dict1['Country'] = fake.country()
          if(alldata[j] == 'ISD-Mobile'):
              dict1['ISD-Mobile'] = fake.msisdn()
          if(alldata[j] == "Nationality"):
              dict1['Nationality'] = fake.country()
          if(alldata[j] == 'Flast/Door/Block No.'):
              dict1['Flast/Door/Block No.'] = fake.building_number()
          if (alldata[j] == 'Street/Lane'):
              dict1['Street/Lane'] = fake.street_address()
          if (alldata[j] == 'Area/Locatity'):
              dict1['Area/Locatity'] = fake.street_name()
          if(alldata[j] == 'Pin Code'):
              dict1['Pin Code'] = fake.postcode()
          if(alldata[j] == 'State'):
              dict1['State'] = fake.state()
          if(alldata[j] == 'City/Town'):
              dict1['City/Town'] = fake.city()
          if (alldata[j] == 'Post Office'):
              dict1['Post Office'] = fake.city()
          if (alldata[j] == 'Phone'):
              dict1['Phone'] = fake.phone_number()
          if (alldata[j] == 'Copy Residence to office Address'):
              dict1['Copy Residence to office Address'] = allvalues[j][random.randrange(0, len(allvalues[j]))]

      csv_list.append(dict1)

  # print(csv_list)
  return csv_list