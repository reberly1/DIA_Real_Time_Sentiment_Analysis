echo mongosh | cmd

echo use admin | mongosh
echo rs.remove("127.0.0.1:27018") | mongosh
echo rs.remove("127.0.0.1:27019") | mongosh
echo rs.add({_id: 1, host: "127.0.0.1:27018"}) | mongosh
echo rs.add({_id: 2, host: "127.0.0.1:27019"}) | mongosh
echo exit | mongosh

start cmd /k mongod --replSet rs0 --port 27018 --dbpath "C:\Program Files\MongoDB\Server\7.0\data\27018"

timeout /t 15

start cmd /k mongod --replSet rs0 --port 27019 --dbpath "C:\Program Files\MongoDB\Server\7.0\data\27019"

timeout /t 15

echo use admin | mongosh
echo rs.conf() | mongosh
echo rs.status() | mongosh
echo exit | mongosh

pause
