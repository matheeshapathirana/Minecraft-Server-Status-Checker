import minestat


server = minestat.MineStat('152.67.101.206', 25565)  # server ip and port
print('<<< Minecraft server status of %s on port %d >>>\n' % (server.address, server.port))

motd = server.motd
server_version = server.version
current_players = server.current_players
max_players = server.max_players
latency = server.latency
server_ip = server.address
server_port = server.port
game_mode = server.gamemode
protocol = server.slp_protocol

if server.online:
    print(f'> Sever IP - {server_ip}')
    print(f'> Sever Port - {server_port}')
    print(f'> Server Version - {server_version}')
    print(f'> Motd - {motd}')
    print(f'> Players - {current_players} out of {max_players} players')
    print(f'> Latency - {latency} ms')
    print(f'> Connected using protocol - {protocol}')

    # Bedrock specific attribute
    if server.slp_protocol is minestat.SlpProtocols.BEDROCK_RAKNET:
        print(f'Game mode - {server.gamemode}')
else:
    print('Server is offline!')
