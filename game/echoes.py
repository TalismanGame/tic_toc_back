from tokenize import group
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

async def echo_when_game_data_update(data):
    group_name = data.get("inviteCode")
    channel_layer = get_channel_layer()

    payload = {
        "inviteCode": data.get('inviteCode'),
        "gameBoard": data.get('gameBoard'),
        "nextPlayer": data.get('nextPlayer'),
        "winner": data.get('winner'),
        "winCondition": data.get('winCondition'),
        "status": data.get('status'),
        "playerO": data.get('playerO'),
        "playerX": data.get('playerX'),
        "oState": data.get('oState'),
        "xState": data.get('xState')
    }

    content = {
        "type": "GAME_DATA",
        "payload": payload,
    }

    await channel_layer.group_send(group_name, {
        "type": "echo",
        "content": content,
    })
