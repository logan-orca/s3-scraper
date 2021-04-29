# S3 Scraper for AWS CLI

### Create New Directory:

- ``` $ cd ~ ```

- ``` $ cd desktop/orca/{your_directory} ```

- ``` $ git clone git@github.com:logan-orca/s3-scraper.git ```

- ``` $ cd your_repo ```

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

For files with Underscores "_":

- In sweeper folder - run ```chop.py``` with the appropriate CSV import.

- ex: 

- ``` $ pipenv shell ```

- ``` (scraper) bash-3.2$ cd sweeper ```

- ``` (scraper) bash-3.2$ python chop.py ```

- Copy and Paste output.

For files with camelCase:

- In sweeper folder - run ```camel-to-space.py``` with the appropriate CSV import.

- ex: 

- ``` $ pipenv shell ```

- ``` (scraper) bash-3.2$ cd sweeper ```

- ``` (scraper) bash-3.2$ python camel-to-space.py ```

- Copy and Paste output.

## Command Line for Thumbnails

``` $ for f in *.mp4; do ffmpeg -i "$f" -ss 00:00:03 -vframes 1 -s 480x320 "${f%.mp4}.jpg"; done ```