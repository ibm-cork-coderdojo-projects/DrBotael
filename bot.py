import discord
from discord.ext import commands
import asyncio


bot = commands.Bot(command_prefix="dr! ")

msgNew = None


@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print(f"\n-==========[{bot.user.name} Console]==========-\n")



@bot.command(pass_context=True)
async def alert(ctx, targ1, targ2, targ3="*", targ4="*", targ5="*", targ6="*", targ7="*", targ8="*", *msg):
    global michael
    michael = ctx.message.server.get_member("459052653352321024")
    target1 = False
    target2 = False
    target3 = False
    target4 = False
    global msgNew
    for i in range(len(msg)):
        msgNew = " ".join(msg)

    
    stuff = "1 = " + str(targ1) + "\n"
    global stuffNum
    stuffNum = 2
    checked = []
    if targ2 not in checked:
        stuff += f"{stuffNum} = " + str(targ2) + "\n"
        checked += targ2
        stuffNum += 1
    else:
        await bot.say("An Error has occured! Error (404), Must be more then two answers to a poll")
        return
    if targ3 != "*" and targ3 not in checked:
        stuff += f"{stuffNum} = " + str(targ3) + "\n"
        checked += targ3
        stuffNum += 1
    if targ4 != "*" and targ4 not in checked:
        stuff += f"{stuffNum} = " + str(targ4) + "\n"
        checked += targ4
        stuffNum += 1
    if targ5 != "*" and targ5 not in checked:
        stuff += f"{stuffNum} = " + str(targ5) + "\n"
        checked += targ5
        stuffNum += 1
    if targ6 != "*" and targ6 not in checked:
        stuff += f"{stuffNum} = " + str(targ6) + "\n"
        checked += targ6
        stuffNum += 1
    if targ7 != "*" and targ7 not in checked:
        stuff += f"{stuffNum} = " + str(targ7) + "\n"
        checked += targ7
        stuffNum += 1
    if targ8 != "*" and targ8 not in checked:
        stuff += f"{stuffNum} = " + str(targ8) + "\n"
        checked += targ8
        stuffNum += 1
    
        
    dmTargets = ctx.message.server.members

    for member in dmTargets:
        if msgNew != None:
            await bot.send_message(member, msgNew)
        else:
            await bot.say("An Error has occured! Error (369), Must have a poll to send to members")
            return
        await bot.send_message(member, "__*Reply with any following number to answer*__")
        await bot.send_message(member, stuff)

    votedNotMade = True



@bot.event
async def on_message(msg):
    try:
        validResponses = ["1", "2"]
        for x in range(8):
            rangeCheck = stuffNum - 1
            if x <= rangeCheck:
                if x != (1,2):
                    validResponses += str(x)
    except:
        pass
    msgTXT = msg.content.lower()
    print(msgTXT)
    print(str(msg.channel))
    print(msg.author)
    if msg.server is None and msg.author != bot.user:
        if votedNotMade == True:
            global voted
            voted = []
            votedNotMade = False
        if str(msg.author) not in voted: 
            if msgTXT in validResponses:
                print("The user answered {0}.".format(msgTXT))
                await bot.send_message(msg.channel, ":white_check_mark: Thank you for voting!")
                
                michaelTXT = str(msg.author) + " " + msgTXT
                await bot.send_message(michael, michaelTXT)
                voted += str(msg.author)
            else:
                print(f"The user entered {msgTXT}, which is not a valid option.")
                await bot.send_message(msg.channel, ":diamond_shape_with_a_dot_inside: That is not a valid answer.")
        else:
            await bot.send_message(msg.channel, ":x: You have already voted")

    await bot.process_commands(msg)



bot.run(BOT_API_KEY)
