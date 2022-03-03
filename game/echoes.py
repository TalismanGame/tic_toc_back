from channels.layers import get_channel_layer

async def echo_when_game_status_updated(data):
    group_name = data.get("code")
    channel_layer = get_channel_layer()
    content = {
        "type": "GAME_STATUS",
        "payload": data.get("gameStatus"),
    }

    await channel_layer.group_send(group_name, {
        "type": "echo",
        "content": content,
    })