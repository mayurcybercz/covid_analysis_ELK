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

![Realtime twitter data Dashboard](images/realtime_dashboard_1.png)

![Realtime twitter data Discover](images/realtime_discover_1.png)