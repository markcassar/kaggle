import numpy as np
import pandas as pd
import csv as csv

train_file = open("c:\\users\\mcassar\\desktop\\programs\\titanic\\train.csv", 'rb')
train_file_object = csv.reader(train_file)
header_train = train_file_object.next()

data = []

for row in train_file_object:
    data.append(row)

train_file.close()
        
data = np.array(data)

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

women_only_stats = data[0::,4] == 'female'
#women_only_check = data[0::,4] != 'male'
men_only_stats = data[0::,4] != 'female'
#men_only_check = data[0::,4] == 'male'

women_onboard = data[women_only_stats, 1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print('Proportion of women who survived is {0}'.format(proportion_women_survived))
print('Proportion of men who survived is {0}'.format(proportion_men_survived))

test_file = open("c:\\users\\mcassar\\desktop\\programs\\titanic\\test.csv", 'rb')
test_file_object = csv.reader(test_file)
header_test = test_file_object.next()

prediction_file = open('c:\\users\\mcassar\\desktop\\programs\\titanic\\gender_based_model.csv', 'wb')
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(['PassengerId', 'Survived'])
for row in test_file_object:
    print(row[0])
    if row[3] == 'female':
        prediction_file_object.writerow([row[0], '1'])
    else:
        prediction_file_object.writerow([row[0], '0'])
        
test_file.close()
prediction_file.close()
        


