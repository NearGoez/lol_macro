from lcu_driver import Connector

connector = Connector()

@connector.ready
async def connect(connection):
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    summoner_json = await summoner.json()
    print(summoner_json)

connector.start()


