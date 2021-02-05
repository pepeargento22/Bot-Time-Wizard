import discord
from discord.ext import commands
import datetime

bot = discord.ext.commands.Bot(command_prefix="!",description=None)

#Eventos

@bot.event
async def on_ready():
    print('{0.user} PRENDIDO'.format(bot))


#Comandos
# Los argumentos de los comandos van dejando un espacio despues del comando
# Es decir para el comando "!est" si queres ver que hora de aca son 8:30 EST
# pones "!est 8 30" donde 8 y 30 son los argumentos del comando

@bot.command()
async def hora(self):
    horario_actual = datetime.datetime.now() # esto me da el tiempo en hora y minutos
    await self.send("{0}:{1:02d}".format(horario_actual.hour, horario_actual.minute))

@bot.command(aliases = ["EST"])
async def est(self, hora=69, minuto=69):
    if (hora==69 and minuto==69):   
        #aca te pasa la hora local actual a EST
        horario_actual = datetime.datetime.now()
        if (horario_actual.hour == 0):
            hora_EST = 23 
        else:
            hora_EST = horario_actual.hour - 1
        minuto_EST = horario_actual.minute
        await self.send("{0}:{1:02d}  {zona_horaria}".format(hora_EST, minuto_EST, zona_horaria="EST"))
    elif (0 <= hora <= 23 and 0 <= minuto <= 59):     
        #aca te pasa la hora EST que pusiste a hora local
        if (hora == 23):
            hora_local = 0
        else:
            hora_local = hora + 1
        minuto_local = minuto
        await self.send("{0}:{1:02d}  hora Argentina".format(hora_local, minuto_local))
    else:
        #aca te manda este mensaje si pones numeros fuera del rango horario
        await self.send("Esa hora no existe.")

@est.error
async def est_error(self, ValueError):
    if isinstance(ValueError, commands.BadArgument):
        await self.send("No pongas algo que no sean números enteros despues del comando")

@bot.command(aliases = ["PST, PT, pt"])
async def pst(self, hora=69, minuto=69):
    if (hora == 69 & minuto == 69):
        horario_actual = datetime.datetime.now()
        if (horario_actual.hour < 4):
            hora_PST = horario_actual.hour + 20
        else:
            hora_PST = horario_actual.hour - 4
        minuto_PST = horario_actual.minute
        await self.send("{0}:{1:02d}  {zona_horaria}".format(hora_PST, minuto_PST, zona_horaria="PST"))
    elif (0 <= hora <= 23 and 0 <= minuto <= 59):
        if (hora > 19):
            hora_local = hora - 20
        else:
            hora_local = hora + 4
        minuto_local = minuto
        await self.send("{0}:{1:02d}  hora Argentina".format(hora_local, minuto_local))
    else:
        await self.send("Esa hora no existe.")

@pst.error
async def pst_error(self, ValueError):
    if isinstance(ValueError, commands.BadArgument):
        await self.send("No pongas algo que no sean números enteros despues del comando")

@bot.command(aliases = ["UTC", "gmt", "GMT"])
async def utc(self, hora=69, minuto=69):
    if (hora == 69 & minuto == 69):
        horario_actual = datetime.datetime.now()
        if (horario_actual.hour > 20):
            hora_UTC = horario_actual.hour - 21
        else:
            hora_UTC = horario_actual.hour + 3
        minuto_UTC = horario_actual.minute
        await self.send("{0}:{1:02d}  {zona_horaria}".format(hora_UTC, minuto_UTC, zona_horaria="UTC"))
    elif (0 <= hora <= 23 and 0 <= minuto <= 59):
        if (hora < 4):
            hora_local = hora + 21
        else:
            hora_local = hora - 3
        minuto_local = minuto
        await self.send("{0}:{1:02d}  hora Argentina".format(hora_local, minuto_local))
    else:
        await self.send("Esa hora no existe.")

@utc.error
async def utc_error(self, ValueError):
    if isinstance(ValueError, commands.BadArgument):
        await self.send("No pongas algo que no sean números enteros despues del comando")

@bot.command(aliases = ["MSK"])
async def msk(self, hora=69, minuto=69):
    if (hora == 69 & minuto == 69):
        horario_actual = datetime.datetime.now()
        if (horario_actual.hour > 17):
            hora_MSK = horario_actual.hour - 18
        else:
            hora_MSK = horario_actual.hour + 6
        minuto_MSK = horario_actual.minute
        await self.send("{0}:{1:02d}  {zona_horaria}".format(hora_MSK, minuto_MSK, zona_horaria="MSK"))
    elif (0 <= hora <= 23 and 0 <= minuto <= 59):
        if (hora < 6):
            hora_local = hora + 18
        else:
            hora_local = hora - 6
        minuto_local = minuto
        await self.send("{0}:{1:02d}  hora Argentina".format(hora_local, minuto_local))
    else:
        await self.send("Esa hora no existe.")

@msk.error
async def msk_error(self, ValueError):
    if isinstance(ValueError, commands.BadArgument):
        await self.send("No pongas algo que no sean números enteros despues del comando")

@bot.command(aliases = ["WAT"])
async def wat(self, hora=69, minuto=69):
    if (hora == 69 & minuto == 69):
        horario_actual = datetime.datetime.now()
        if (horario_actual.hour > 19):
            hora_WAT = horario_actual.hour - 20
        else:
            hora_WAT = horario_actual.hour + 4
        minuto_WAT = horario_actual.minute
        await self.send("{0}:{1:02d}  {zona_horaria}".format(hora_WAT, minuto_WAT, zona_horaria="WAT"))
    elif (0 <= hora <= 23 and 0 <= minuto <= 59):
        if (hora < 4):
            hora_local = hora + 20
        else:
            hora_local = hora - 4
        minuto_local = minuto
        await self.send("{0}:{1:02d}  hora Argentina".format(hora_local, minuto_local))
    else:
        await self.send("Esa hora no existe.")

@wat.error
async def wat_error(self, ValueError):
    if isinstance(ValueError, commands.BadArgument):
        await self.send("No pongas algo que no sean números enteros despues del comando")

bot.run('NzQyODQwMDU3MDk3ODc5NTcz.XzL9tg.n6n02nSFOOswp1sOxbV3Jne7Rj4')