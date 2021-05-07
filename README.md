pip install tweepy
pip install -U textblob
python -m textblob.download_corpora
pip install elasticsearch

Run Elasticsearch before running main.py
bin\elasticsearch.bat (in the elasticsearch folder)

python main.py keywords
(keyboard interrupt to stop)

then run kibana
bin\kibana.bat (in the kibana folder)
http://localhost:5601
