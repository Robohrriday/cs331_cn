# $1 -> {single, mult-threaded, mult-process}
touch analyze_$1.csv
echo "num_clients,total_time" > analyze_$1.csv

for num_clients in 10 20 30 40 50 60 70 80 90 100
do
    bash start.sh client.py $num_clients >> analyze_$1.csv
    echo "Done for $num_clients clients"
done