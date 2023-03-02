cd /home/raymondyan/geekbang/Python-CoreTechnologyAndPractice/quantitative_trading_in_practice/MySQL_log_and_data_storage_system
sudo -E chown -R 1001:1001 /home/raymondyan/docker_volumes/mariadb-persistence
sudo -E docker-compose -f ./docker-compose-mariadb.yml up -d