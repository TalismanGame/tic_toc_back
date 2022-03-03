from channels.layers import get_channel_layer

#complete this for clean up all echoes
async def echo_when_game_status_updated(data):
    #group_name should be game id 
    group_name = 'it should be game id'
    channel_layer = get_channel_layer()
    content = {
        "type": "GAME_STATUS",
        "payload": data,
    }

    await channel_layer.group_send(group_name, {
        "type": "echo",
        "content": content,
    })