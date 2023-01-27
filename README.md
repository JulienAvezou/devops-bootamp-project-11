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

-----

### Project 2: EC2 status checks

1. create servers via tf script

2. check instance state using boto 

![Capture d’écran 2023-01-25 à 14 40 32](https://user-images.githubusercontent.com/62488871/214580632-0446032a-b0a3-4e80-b10d-328bdacdfbc6.png)

3. check instance status using boto

![Capture d’écran 2023-01-25 à 14 45 32](https://user-images.githubusercontent.com/62488871/214580654-57df51c3-b3a9-475f-a885-13828f958f85.png)

4. can refactor into 1 single call to retrieve instance state and statuses

![Capture d’écran 2023-01-25 à 14 49 32](https://user-images.githubusercontent.com/62488871/214580681-da90e3f9-2322-4b34-bfc1-98a5d4912f8b.png)

5. Automate scheduling of above checks - install schedule library & add scheduling logic

![Capture d’écran 2023-01-25 à 17 56 48](https://user-images.githubusercontent.com/62488871/214628679-25f3481b-13ab-431b-86a7-cd37d10859e5.png)


-----

### Project 3: Add Environment Tag to EC2 instances

1. fetch all instance ids using boto client, filtered by region

![Capture d’écran 2023-01-26 à 12 27 00](https://user-images.githubusercontent.com/62488871/214824633-9cf34421-310f-465e-99bd-685a1eef98b7.png)

![Capture d’écran 2023-01-26 à 12 27 07](https://user-images.githubusercontent.com/62488871/214824651-f4b3a904-d845-4104-93c9-c043fea199b3.png)

2. create tags using boto resource, and apply the value of the tag to differentiate the environment for each region (prod or dev)

![Capture d’écran 2023-01-26 à 12 27 15](https://user-images.githubusercontent.com/62488871/214824675-6a01ad83-3f44-43f5-9cce-43680d285b73.png)

----

### Project 4: EKS cluster info

1. fetch list of clusters in region using boto client

2. loop through list of cluster names and call .describe_cluster() to access specific info for each cluster in the list (state, endpoint, version etc.)

![Capture d’écran 2023-01-26 à 12 45 56](https://user-images.githubusercontent.com/62488871/214828080-54f6990d-45da-4ed5-8f98-55327858129d.png)

-----

### Project 5: Automate backup of EC2 volumes snapshots 

1. create ec2 client in region using boto

2. fetch all volumes for ec2 client

3. loop through volumes and create a snapshot for each using volume ids

4. can schedule this task to run automatically every day

5. can filter out volumes so you only create snapshots for prod volumes

![Capture d’écran 2023-01-26 à 13 04 06](https://user-images.githubusercontent.com/62488871/214831398-d6c89d29-3b5a-4b5d-a0db-0839abe92d2a.png)

-----

### Project 6: Automate cleanup of EC2 volumes snapshots

1. create ec2 client in region using boto

2. fetch all volumes for ec2 client

![Capture d’écran 2023-01-27 à 11 41 29](https://user-images.githubusercontent.com/62488871/215067246-bfe8031c-1d30-4892-94b6-1858ba785051.png)

3. loop through volumes and fetch snapshots for each volume using its id, and only snapshots created by you

![Capture d’écran 2023-01-27 à 11 42 44](https://user-images.githubusercontent.com/62488871/215067379-5f960417-5b73-4033-9ad9-f744cd48311a.png)

4. sort the fetched snapshots by start time, with help from itemgetter fn 

![Capture d’écran 2023-01-27 à 11 44 16](https://user-images.githubusercontent.com/62488871/215067757-b2ad9ee8-2d2b-4b47-8c30-f7dd2f2fa2b5.png)

5. delete all snapshots except for the 2 most recent ones 

![Capture d’écran 2023-01-27 à 11 44 58](https://user-images.githubusercontent.com/62488871/215067783-d6615611-4212-4d2d-80c0-1ff733ba604c.png)

6. automate the task with help from schedule lib

-----

### Project 7: Automate restoring of EC2 volumes from snapshots

1. create ec2 client & resource in region using boto

2. find volume for specific instance

![Capture d’écran 2023-01-27 à 12 21 50](https://user-images.githubusercontent.com/62488871/215075022-a3e998ba-5357-4805-8194-73fbe4940094.png)

3. fetch all snapshots for that volume and retrieve the latest snapshot

![Capture d’écran 2023-01-27 à 12 22 20](https://user-images.githubusercontent.com/62488871/215075168-c4036fb0-49f7-4d1c-993f-99e3b9c268e7.png)

4. create new volume from that latest snapshot

![Capture d’écran 2023-01-27 à 12 23 04](https://user-images.githubusercontent.com/62488871/215075195-77f2bb5f-7d8c-45fd-b632-4050baea02ab.png)

5. attach that new volume to the instance, wrapped in logic that checks volume state and conditionally attaches volume to instance if volume state is available

![Capture d’écran 2023-01-27 à 12 23 27](https://user-images.githubusercontent.com/62488871/215075212-d6cc44be-1ae8-443f-97fc-88d60edf44e5.png)

-----

