# coding=utf-8
# Invite module developed by João Vanzuita - https://github.com/converge/

from sopel.module import commands, require_owner, OP

@commands('invite')
def invite(bot, trigger):
    if bot.privileges[trigger.sender][bot.nick] < OP:
        return bot.reply("I'm not a channel operator!")
    if not trigger.groups(3) or not trigger.group(4):
        return bot.reply("Usage: .invite user #channel (the bot must be operator and in the invited channel)")
    bot.invite(trigger.group(3), trigger.group(4))
