Install Python Packages <br/>
pip install tweepy <br/>
pip install -U textblob <br/>
python -m textblob.download_corpora <br/>
pip install elasticsearch <br/>

STEPS:<br/>
Run Elasticsearch before running main.py <br/>
bin\elasticsearch.bat (in the elasticsearch folder) <br/>
<br/>
python main.py keywords<br/>
(keyboard interrupt to stop)<br/>

then run kibana<br/>
bin\kibana.bat (in the kibana folder)<br/>
Create index-pattern at http://localhost:5601

Datasets:<br/>
[CDC Data](https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths)
[Twitter Historical Batch Data](https://www.kaggle.com/gpreda/covid19-tweets)

![Realtime twitter data Dashboard](images/realtime_dashboard_1.PNG)

![Realtime twitter data Discover](images/realtime_discover_1.PNG)