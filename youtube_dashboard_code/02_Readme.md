#Steps to execute the project

Pre-Project Work
1. pip install
    pymongo, dnspython, google-api-python-client, pandas, streamlit
2. Ensure the Mongodb configuration
    MongoConfiguration.py 
3. Ensure the utility function are ready
    utility.py


Work-Flow
1. Setup Credentials, YTChannelConfig
    Credentials.py
    YTChannelConfig.py
2. Get Youtube data and load it in mongodb
    YoutubeScrapping.py
3. Create DDL for SQL
    DatabaseDDL.py
4. Load into SQL
    LoadSQL.py
5. Run Streamlit


Terminal commands

for pip install
    python -m pip install pymongo

to run streamlit
    python -m streamlit run finalapp.py










