#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup
#from lxml import html
#from lxml import etree
import codecs
import goslate
import StringIO
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')


labels = ["Code", "Name", "Objectivo", "Tipo", "Situacao", "Data de inicio", "Data de termino", "Setor", "Sub-setor", "Institution", "Agency"]

payload = {'palavrasChave': ''}
rpost = requests.post('http://www.abc.gov.br/Projetos/pesquisa', data=payload)
print(rpost.status_code)

soup = BeautifulSoup(rpost.text, 'html.parser')

soupLista = soup.find_all("div", "projeto_detalhes_show")

#project = soupLista[0]
#print("Project ", project)
#print("project div ", project.div)
#print("project a ", project.find_all('a'))
#print("project p ", project.find_all('p'))
#print("project span ", project.find_all('span'))
#print("project h3 ", project.find_all('h3'))

# Code and Name Combo
#projectA = project.a
#projectAH3 = project.h3

objectiveList = []
codeList = []
nameList = []
typeList = []
situationList = []
sectorList = []
subsectorList = []
initdateList = []
terminaldateList = []
agencyList = []
institutionList = []

for project in soupLista:

    # Initialize it to an empty string
    objective = ""
    code = ""
    name = ""
    type = ""
    situation = ""
    sector = ""
    subsector = ""
    initdate = ""
    terminaldate = ""
    agency = ""
    institution = ""

    # Code and Name
    projectA = project.a
    projectAH3 = project.h3
    projectAH3span = project.span
    codeAndName = projectAH3span.text
    #print("Code and Name ", codeAndName)
    code, name = codeAndName.split(" - ", 1)
    # print("Code ", code)
    # print("Name ", name)

    # All items inside a p tag
    projectP = project.find_all('p')
    for item in projectP:
        if item.b:
            if "Objetivo:" in item.b:
                objective = item.span.text
                #print("Objective ", objective)
            elif "Tipo:" in item.b:
                type = item.span.text
                #print("Type ", type)
            elif "Situação:" in item.b:
                situation = item.span.text
                #print("Situation ", situation)
            elif "Setor:" in item.b:
                temp,sector = item.text.split(": ", 1)
                #print("Sector ", sector)
            elif "Sub-setor:" in item.b:
                temp,subsector = item.text.split(": ", 1)
                #print ("Subsector ", subsector)
            elif "Data de início:" in item.b:
                temp, initdate = item.text.split(": ", 1)
                #print("Initial Date ", initdate)
            elif "Data de término:" in item.b:
                temp, terminaldate = item.text.split(": ", 1)
                #print("Terminal date ", terminaldate)
        if item.label:
            agency = item.text
            #print("Agency ", agency) 

    # Institution span h3 tag
    projectSpan = project.find_all('span')
    for item in projectSpan:
        if item.h3:
            institution = item.h3.text
            #print("Institution ", institution)

    # Now append each item to the list items
    objectiveList.append(objective)
    codeList.append(code)
    nameList.append(name)
    typeList.append(type)
    situationList.append(situation)
    sectorList.append(sector)
    subsectorList.append(subsector)
    initdateList.append(initdate)
    terminaldateList.append(terminaldate)
    agencyList.append(agency)
    institutionList.append(institution)

# Outside of for loop
labels = ["Code", "Name", "Objectivo", "Tipo", "Situacao", "Data de inicio", "Data de termino", "Setor", "Sub-setor", "Institution", "Agency"]

data = {"Code":codeList, "Name":nameList, "Objectivo":objectiveList, "Tipo":typeList, "Situacao":situationList, "Data de inicio":initdateList, "Data de termino": terminaldateList, "Setor": sectorList, "Sub-setor": subsectorList, "Institution":institutionList, "Agency": agencyList}

df = pd.DataFrame(data, columns = labels)
df.to_csv(path_or_buf=('ABCBrazilOut.csv'), index=False)   
        
# print "to english now"

# engObjectiveList = []
# engCodeList = []
# engNameList = []
# engTypeList = []
# engSituationList = []
# engSectorList = []
# engSubsectorList = []
# engSnitdateList = []
# engTerminaldateList = []
# engAgencyList = []
# engInstitutionList = []

# #gs = goslate.Goslate()

# gs = goslate.Goslate(service_urls=['http://translate.google.de'])
# print gs.translate('hello world', 'de')

# # for item in codeList:
# #     engCodeList.append(gs.translate(item,'en'))
# # for item in nameList:
# #     engNameList.append(gs.translate(item,'en'))
# # for item in objectiveList:
# #     engObjectiveList.append(gs.translate(item,'en'))
# # for item in typeList:
# #     engTypeList.append(gs.translate(item,'en'))
# # for item in situationList:
# #     engSituationList.append(gs.translate(item,'en'))
# # for item in initdateList:
# #     engInitdateList.append(gs.translate(item,'en'))
# # for item in terminaldateList:
# #     engTerminaldateList.append(gs.translate(item,'en'))
# # for item in sectorList:
# #     engSectorList.append(gs.translate(item,'en'))
# # for item in subsectorList:
# #     engSubsectorList.append(gs.translate(item,'en'))
# # for item in institutionList:
# #     engInstitutionList.append(gs.translate(item,'en'))
# # for item in agencyList:
# #     engAgencyList.append(gs.translate(item,'en'))

# engCodeList = (gs.translate(codeList,'en'))
# engNameList = (gs.translate(nameList,'en'))
# engObjectiveList = (gs.translate(objectiveList,'en'))
# engTypeList = (gs.translate(typeList,'en'))
# engSituationList = (gs.translate(situationList,'en'))
# engInitdateList = (gs.translate(initdateList,'en'))
# engTerminaldateList = (gs.translate(terminaldateList,'en'))
# engSectorList = (gs.translate(sectorList,'en'))
# engSubsectorList = (gs.translate(subsectorList,'en'))
# engInstitutionList = (gs.translate(institutionList,'en'))
# engAgencyList = (gs.translate(agencyList,'en'))


# engData = {"Code":engCodeList, "Name":engNameList, "Objective":engObjectiveList, "Type":engTypeList, "Situation":engSituationList, "Initial Date":engInitdateList, "Terminal Date": engTerminaldateList, "Sector": engSectorList, "Sub-sector": engSubsectorList, "Institution":engInstitutionList, "Agency": engAgencyList}
# df = pd.DataFrame(data, columns = labels)
# df.to_csv(path_or_buf=('ABCBrazilEnglishOut.csv'), index=False)   



# gs = goslate.Goslate()
# fp = open('ABCBrazilOut.csv')
# fileText = fp.read()
# translated = gs.translate(fileText, 'en')

# file = codecs.open('ABCBrazilEnglishOut.csv', "wb", "utf-8")
# file.write(translated)
# file.close()

# for text in os.listdir(DownloadPath + "texts/brazilian/"):
#     fp = open(DownloadPath + "texts/brazilian/" + text, 'rb')
#     fileText = fp.read()
#     translated = gs.translate(fileText,'en')
#     #print translated
#     file = codecs.open(DownloadPath + "texts/english/" + (text[:-4] + "English.txt"), "wb", "utf-8")
#     file.write(translated)
#     file.close()

#for project in soupLista:
    #print("Project ", project)
    #print("project div ", project.div)
    #print("project p ", project.find_all('p'))
    #projectSoup = BeautifulSoup(project, 'html.parser')
    #print("project div ", projectSoup.p)
    #tag = projectSoup.div
    #print("tag name ", tag.name)
    #print("tag ", tag)