




#LEVEL SYSTEM

def generateXP():
        return random.randint(1,50)

async def addxp(member):

            xp = generateXP()


            result_xp = db_getXp(member.id)
            if((result_xp) == 0):
                #user not in db
                db_addUser(member.id, member.name, xp)
                log(f"{member} was added to the records", 2)
            else:
                #update xp
                newxp = result_xp + xp
                db_addXp(member.id, newxp)
                log(f"{member} recived {xp} xp ")

                #update level
                result_lvl = db_getLvl(member.id)
                if newxp >= round(4 * (result_lvl ** 5) /2 ): 

                    newlvl = result_lvl + 1
                    db_addLvl(member.id, newlvl)
                    log(f"{member} leveled up to level {newlvl}")
                    channel = bot.get_channel(285430182813368322)
                    await channel.send(f"> <@!{member}> has leveled up to level {newlvl}!")
