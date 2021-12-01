import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('eeee')
    async def send(self, user_id, message):
        print("getting user id")
        user=client.get_user(user_id)
        print("sending message...")
        await user_id.send(str(message))
        print("message sent")
    #async def on_message(self,user_id,message):

    async def send_m(self, channel_id, message):
        print(0)
        channel = client.get_channel(int(channel_id))
        print(1)
        await channel.send(message)
        print(2)

client = MyClient()
client.run('OTExNDQxNjgxOTE0NjY3MDA5.YZhcNg.mIKBnM9By2M5Q_FcSf1-a00wxFM')


#send channel
#@client.command(name="msg", pass_context=True)
client.send(911440275019296798,"sfhdh")
client.send_m(911446726588657755,"sfhdh")