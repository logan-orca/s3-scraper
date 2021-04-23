# S3 Scraper for AWS CLI

### Create New Directory:

- ``` $ cd ~ ```

- ``` $ cd desktop/orca/{your_directory} ```

- ``` $ cd your_directory ```

- ``` $ pipenv shell ```

### Should look like:

- ``` $ (your_directory) bash-3.2$ ```

- ``` $ <exit> ``` --> to exit virtual environment (must exit before pipenv commands)

- ``` $ pipenv install awscli ```

### Enter AWS Security Credentials --> Create Keys in AWS IAM User and save output.csv.

- ``` $ pipenv shell ```

- ``` $ aws configure ```

- follow entry prompts:

- ``` AWS Access Key ID: ********* ```

- ``` AWS Secret Access Key: ********* ```

- ``` Default region name: us-west-1 ```

- ``` Default output format: csv ```

### List Files in S3 Bucket:

- ``` $ aws s3 ls ```

### List specific file names --> Ex:

- ``` $ aws s3 ls s3://orca.media/videos/knee-anim/ | awk '{print $4}' > ./logs/knee-log.csv ```


## Python

- In sweeper folder - run ```chop.py``` with the appropriate CSV import.
- Copy and Paste values for now
- Doesn't take care of camelCase but it works for everything else...