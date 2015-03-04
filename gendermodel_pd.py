from __future__ import division
import numpy as np
import pandas as pd
import csv as csv

filename = "c:\\users\\mcassar\\desktop\\programs\\titanic\\train.csv"
train_df = pd.read_csv(filename)

number_passengers = train_df['Survived'].count()
number_survived = train_df['Survived'].sum()
proportion_survivors = number_survived / number_passengers

women_onboard = train_df[ train_df['Sex'] == 'female']
men_onboard = train_df[ train_df['Sex'] != 'female']

proportion_women_survived = women_onboard['Survived'].sum() / women_onboard['Survived'].count()
proportion_men_survived = men_onboard['Survived'].sum() / men_onboard['Survived'].count()

print('Proportion of women who survived is {0}'.format(proportion_women_survived))
print('Proportion of men who survived is {0}'.format(proportion_men_survived))

test_filename = open("c:\\users\\mcassar\\desktop\\programs\\titanic\\test.csv")
test_df = csv.reader(test_filename)
header = test_df.next()

prediction_file = open('c:\\users\\mcassar\\desktop\\programs\\titanic\\gender_based_model.csv', 'wb')
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(['PassengerId', 'Survived'])
for row in test_df:
#    print(row[1])
    if (row[3] == 'female'):
        prediction_file_object.writerow([row[0], '1'])
    else:
        prediction_file_object.writerow([row[0], '0'])
        
prediction_file.close()
        


