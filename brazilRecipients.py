#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bethany Jackson
# Still not quite right. Still have to fix issues with country ISO code inside of words. GeograPy seems to not deal with this properly.
# Once that is fixed, much of the individual checking can be taken out

import geograpy
import pandas as pd


# put into dataframe doing that thing
brazil_df = pd.read_csv("C:/Users/Bethany/WorkWorkspace/ABCBrazilOutFinal-translated.csv", encoding='utf-8')

all_titles = pd.concat((brazil_df['project_title'], brazil_df['project_long_description']))
#brazil_df['project_title'] = brazil_df.project_title + brazil_df.project_long_description
place_list = []

print(list(brazil_df.columns.values))
#print(all_titles)
#for cell in brazil_df['project_title']:
#    print str(cell)
# brazil_df['project_title'],brazil_df['project_long_description']

#for cell in brazil_df['project_title']
project_title = brazil_df['project_title'].values.tolist()
project_long_description = brazil_df['project_long_description'].values.tolist()
project_all = zip(project_title, project_long_description)

#for cell_title in brazil_df['project_title'] and cell_long in brazil_df['project_long_description']:
#for cell in brazil_df['project_title'],brazil_df['project_long_description']:
for cell in project_all:
    #print cell_title
    #print cell_long
    #cell = cell_title + cell_long
    #print cell
    #cell = ", ".join(cell)
    #print cell

    try:
        if not pd.isnull(cell[0]):
            placesInCell1 = geograpy.get_place_context(text=cell[0]).countries
        else:
            placesInCell1 = []
        if not pd.isnull(cell[1]):
            placesInCell2 = geograpy.get_place_context(text=cell[1]).countries
        else: 
            placesInCell2 = []

        placesInCell = placesInCell1 + placesInCell2

        if placesInCell:

            if "United States" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ((" US " not in cell[0]) and (" USA " not in cell[0]) and (" United States Of America " not in cell[0]) and ("United States" not in cell[0]) ):
                        if not pd.isnull(cell[1]):
                            if ((" US " not in cell[1]) and (" USA " not in cell[1]) and (" United States Of America " not in cell[1]) and ("United States" not in cell[0])):
                                placesInCell.remove("United States")
                        else:
                            placesInCell.remove("United States")
                elif not pd.isnull(cell[1]):
                    if ((" US " not in cell[1]) and (" USA " not in cell[1]) and (" United States Of America " not in cell[1]) and ("United States" not in cell[0])):
                        placesInCell.remove("United States")
                else:
                    placesInCell.remove("United States")

            if "Equador" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Equador" not in cell[0]) and ("equador" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Equador" not in cell[1]) and ("equador" not in cell[1]):
                                placesInCell.remove("Equador")
                        else:
                            placesInCell.remove("Equador")
                elif not pd.isnull(cell[1]):
                    if ("Equador" not in cell[1]) and ("equador" not in cell[1]):
                        placesInCell.remove("Equador")
                else:
                    placesInCell.remove("Equador")


            if "Panama" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Panama" not in cell[0]) and ("panama" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Panama" not in cell[1]) and ("panama" not in cell[1]):
                                placesInCell.remove("Panama")
                        else:
                            placesInCell.remove("Panama")
                elif not pd.isnull(cell[1]):
                    if ("panama" not in cell[1]) and ("Panama" not in cell[1]):
                        placesInCell.remove("Panama")
                else:
                    placesInCell.remove("Panama")

            if "Bolivia, Plurinational State of" in placesInCell:
                placesInCell[placesInCell.index("Bolivia, Plurinational State of")] = 'Bolivia'


            if "Angola" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Angola" not in cell[0]) and ("angola" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Angola" not in cell[1]) and ("angola" not in cell[1]):
                                placesInCell.remove("Angola")
                        else:
                            placesInCell.remove("Angola")
                elif not pd.isnull(cell[1]):
                    if ("Angola" not in cell[1]) and ("angola" not in cell[1]):
                        placesInCell.remove("Angola")
                else:
                    placesInCell.remove("Angola")

            if "Lao People's Democratic Republic" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Lao" not in cell[0]) and ("lao" not in cell[0]) and ("Laos" not in cell[0]) and ("laos" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Lao" not in cell[1]) and ("lao" not in cell[1]) and ("Laos" not in cell[1]) and ("laos" not in cell[1]):
                                placesInCell.remove("Lao People's Democratic Republic")
                        else:
                            placesInCell.remove("Lao People's Democratic Republic")
                elif not pd.isnull(cell[1]):
                    if ("Lao" not in cell[1]) and ("lao" not in cell[1]) and ("Laos" not in cell[1]) and ("laos" not in cell[1]):
                        placesInCell.remove("Lao People's Democratic Republic")
                else:
                    placesInCell.remove("Lao People's Democratic Republic")

            if "Spain" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Spain" not in cell[0]) and ("spain" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Spain" not in cell[1]) and ("spain" not in cell[1]):
                                placesInCell.remove("Spain")
                        else:
                            placesInCell.remove("Spain")
                elif not pd.isnull(cell[1]):
                    if ("Spain" not in cell[1]) and ("spain" not in cell[1]):
                        placesInCell.remove("Spain")
                else:
                    placesInCell.remove("Spain")

            if "Portugal" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Portugal" not in cell[0]) and ("portugal" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Portugal" not in cell[1]) and ("portugal" not in cell[1]):
                                placesInCell.remove("Portugal")
                        else:
                            placesInCell.remove("Portugal")
                elif not pd.isnull(cell[1]):
                    if ("Portugal" not in cell[1]) and ("portugal" not in cell[1]):
                        placesInCell.remove("Portugal")
                else:
                    placesInCell.remove("Portugal")

            if "Hong Kong" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Hong Kong" not in cell[0]) and ("hong kong" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Hong Kong" not in cell[1]) and ("hong kong" not in cell[1]):
                                placesInCell.remove("Hong Kong")
                        else:
                            placesInCell.remove("Hong Kong")
                elif not pd.isnull(cell[1]):
                    if ("Hong Kong" not in cell[1]) and ("hong kong" not in cell[1]):
                        placesInCell.remove("Hong Kong")
                else:
                    placesInCell.remove("Hong Kong")


            if "Bolivia" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Bolivia" not in cell[0]) and ("bolivia" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Bolivia" not in cell[1]) and ("bolivia" not in cell[1]):
                                placesInCell.remove("Bolivia")
                        else:
                            placesInCell.remove("Bolivia")
                elif not pd.isnull(cell[1]):
                    if ("Bolivia" not in cell[1]) and ("bolivia" not in cell[1]):
                        placesInCell.remove("Bolivia")
                else:
                    placesInCell.remove("Bolivia")

            if "Egypt" in placesInCell:
                if not pd.isnull(cell[0]):
                    if ("Egypt" not in cell[0]) and ("egypt" not in cell[0]):
                        if not pd.isnull(cell[1]): 
                            if ("Egypt" not in cell[1]) and ("egypt" not in cell[1]):
                                placesInCell.remove("Egypt")
                        else:
                            placesInCell.remove("Egypt")
                elif not pd.isnull(cell[1]):
                    if ("Egypt" not in cell[1]) and ("egypt" not in cell[1]):
                        placesInCell.remove("Egypt")
                else:
                    placesInCell.remove("Egypt")




            placesInCell = list(set(placesInCell))
            place_list.append("|".join(placesInCell))
        else:
            place_list.append("")
    except UnicodeEncodeError, err:
        print("UnicodeEncodeError. Continue")

print("Finished dealing with countries.")
df_place_list = pd.DataFrame(place_list, columns=['recipients'])
brazil_df['recipients'] = df_place_list

brazil_df.to_csv("brazilRecipient.csv", encoding='utf-8')
# for item in dataframe_of_title
#for item in brazil_df[]
# place_list.append(geograpy.get_place_context(specific_string_position))

#put into csv