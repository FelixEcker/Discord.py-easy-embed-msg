"""
msg module for discord.py to make your live with
Discord.py embeds easier!

Version: 1.0
Made By: Felix Eckert
required packages: Discord.py
"""

import discord

class Succes:
    async def succes(bot, ttl, desc, msg, un, inline):
        embed = discord.Embed(title=ttl, description=desc, color=discord.Color.green())
        embed.add_field(name=msg, value=un, inline=inline)
        await bot.say(embed=embed)

class Error:
    async def error(bot, ttl, desc, msg, un, inline):
        embed = discord.Embed(title=ttl, description=desc, color=discord.Color.red())
        embed.add_field(name=msg, value=un, inline=inline)
        await bot.say(embed=embed)

class Other:
    async def userinfo(bot, user):
        embed = discord.Embed(title="{}'s Information".format(user.name), description="Heres the information about {} that i could find!".format(user.name), color=discord.Color.gold())
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest Role", value=user.top_role, inline=True)
        embed.add_field(name="Joined", value=user.joined_at, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.say(embed=embed)

    async def note(bot, ttl, desc, msg, un, inline):
        embed = discord.Embed(title=ttl, description=desc, color=discord.Color.blue())
        embed.add_field(name=msg, value=ub, inline=inline)
        await bot.say(embed=embed)
