# devops-bootamp-project-11
Demo for Module 14 - Automation w Python

### Project 1: connect boto3 to aws

1. install boto3 - pip install boto3

![Capture d’écran 2023-01-25 à 13 30 01](https://user-images.githubusercontent.com/62488871/214570972-423e1059-406c-4943-b81f-105aa3f54f63.png)

2. connect boto3 w aws user - check that aws user is already configured, if so boto will automatically pick up credentials for this user

![Capture d’écran 2023-01-25 à 13 32 48](https://user-images.githubusercontent.com/62488871/214570997-56acbfc7-f5d5-474a-9e3b-e16d907ee641.png)

3. use boto client to query resources and check that connection to aws is properly configured - eg. print out vpc info for ec2 instance

![Capture d’écran 2023-01-25 à 13 45 33](https://user-images.githubusercontent.com/62488871/214571034-06fddfd8-3e0d-4c01-bcfd-8b24b155fbce.png)

4. can override default region when connecting to aws w boto

![Capture d’écran 2023-01-25 à 13 47 08](https://user-images.githubusercontent.com/62488871/214571079-d36f1523-c8cf-410b-a3ea-609a5ab4a423.png)

5. use boto resource to create new vpc and subnets in aws

![Capture d’écran 2023-01-25 à 14 05 27](https://user-images.githubusercontent.com/62488871/214571098-67dfb0e3-c626-4b0c-ba29-4a56158a7b06.png)


