import pandas as pd

file = open('ml-1m/users.dat', 'r')

userId = []
userGender = []
userAge = []
userJob = []
userZip = []

for i in file:
    i = i.splitlines()
    info = i[0].split('::')
    userId.append(info[0])
    userGender.append(info[1])
    userAge.append(info[2])
    userJob.append(info[3])
    userZip.append(info[4])

'''
Age is chosen from the following ranges:

	*  1:  "Under 18"
	* 18:  "18-24"
	* 25:  "25-34"
	* 35:  "35-44"
	* 45:  "45-49"
	* 50:  "50-55"
	* 56:  "56+"
'''

userAgeParsed = []

for i in range(len(userAge)):
    if userAge[i] == '1':
        userAgeParsed.append('Under 18')
    elif userAge[i] == '18':
        userAgeParsed.append('18-24')
    elif userAge[i] == '25':
        userAgeParsed.append('25-34')
    elif userAge[i] == '35':
        userAgeParsed.append('35-44')
    elif userAge[i] == '45':
        userAgeParsed.append('45-49')
    elif userAge[i] == '50':
        userAgeParsed.append('50-55')
    else:
        userAgeParsed.append('56+')

# print(userAgeParsed)

'''
- Occupation is chosen from the following choices:

	*  0:  "other" or not specified
	*  1:  "academic/educator"
	*  2:  "artist"
	*  3:  "clerical/admin"
	*  4:  "college/grad student"
	*  5:  "customer service"
	*  6:  "doctor/health care"
	*  7:  "executive/managerial"
	*  8:  "farmer"
	*  9:  "homemaker"
	* 10:  "K-12 student"
	* 11:  "lawyer"
	* 12:  "programmer"
	* 13:  "retired"
	* 14:  "sales/marketing"
	* 15:  "scientist"
	* 16:  "self-employed"
	* 17:  "technician/engineer"
	* 18:  "tradesman/craftsman"
	* 19:  "unemployed"
	* 20:  "writer"
'''

userJobParsed = []

for i in userJob:
    if i == '0':
        userJobParsed.append('other')
    elif i == '1':
        userJobParsed.append('academic/educator')
    elif i == '2':
        userJobParsed.append('artist')
    elif i == '3':
        userJobParsed.append('clerical/admin')
    elif i == '4':
        userJobParsed.append('college/grad student')
    elif i == '5':
        userJobParsed.append('customer service')
    elif i == '6':
        userJobParsed.append('doctor/healthcare')
    elif i == '7':
        userJobParsed.append('executive/managerial')
    elif i == '8':
        userJobParsed.append('farmer')
    elif i == '9':
        userJobParsed.append('homemaker')
    elif i == '10':
        userJobParsed.append('K-12 student')
    elif i == '11':
        userJobParsed.append('lawyer')
    elif i == '12':
        userJobParsed.append('programmer')
    elif i == '13':
        userJobParsed.append('retired')
    elif i == '14':
        userJobParsed.append('sales/marketing')
    elif i == '15':
        userJobParsed.append('scientist')
    elif i == '16':
        userJobParsed.append('self-employed')
    elif i == '17':
        userJobParsed.append('technician/engineer')
    elif i == '18':
        userJobParsed.append('tradesman/craftsman')
    elif i == '19':
        userJobParsed.append('unemployed')
    elif i == '20':
        userJobParsed.append('writer')

# print(userJobParsed)

# userDemographics = pd.DataFrame([userId, userGender, userAge, userAgeParsed, userJob, userJobParsed, userZip])

userDemo = pd.DataFrame()

userDemo['userId'] = userId
userDemo['userGender'] = userGender
userDemo['userAge'] = userAge
userDemo['userAgeParsed'] = userAgeParsed
userDemo['userJob'] = userJob
userDemo['userJobParsed'] = userJobParsed
userDemo['userZip'] = userZip

userDemo.set_index('userId')

# print(userDemo)

#userDemo.to_csv('ml-1m/user_demographic.csv')
userDemo.to_pickle('pickles/user_demographic.pickle')
