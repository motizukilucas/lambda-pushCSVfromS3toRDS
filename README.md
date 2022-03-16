## References
    https://www.youtube.com/watch?v=C0aj3FjN5e0
    https://datatofish.com/import-csv-sql-server-python/ # both ones are for local guidance


    https://towardsdatascience.com/python-packages-in-aws-lambda-made-easy-8fbc78520e30
    https://www.youtube.com/watch?v=EqAs4lH7dXM # both ones are for setting up lambda triggers

@@@@@@@ keep up on this ones @@@@@@@@
    https://github.com/prabhakar2020/insert_s3_csv_file_content_to_mysql_using_lambda # this one has mysql connection capabilities
    https://towardsdatascience.com/reading-and-writing-files-from-to-amazon-s3-with-pandas-ccaf90bfe86c # both ones for setting boto3 with pandas 

## Local set up steps
    sudo apt install python3-pip

    pip install -r requirements.txt

## Cloud 9 steps
    sudo yum update -y

        mkdir folder
        cd folder
        virtualenv v-env
        source ./v-env/bin/activate
        pip install pandas
        pip install mysql-connector-python
        deactivate

        mkdir python
        cd python
        cp -r ../v-env/lib64/python3.7/site-packages/* .
        cd ..
        zip -r panda_layer.zip python
        aws lambda publish-layer-version --layer-name pandas --zip-file fileb://panda_layer.zip --compatible-runtimes python3.7 ## this line doesn't work

        aws s3 cp read-csv-test.zip s3://read-csv-test2

## OBS:
from Amazon Linux 2 default Python version is 3.7   
    python3 --version
    Python 3.7.10
