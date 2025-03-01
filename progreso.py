import time

"""=========Variables Globales=========="""
sec = 0

"""==========Barra de Progreso============"""
def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='●'
			else: make_text+='○'
			index_make+=1
		make_text += ']'
		return make_text
	except Exception as ex:
			return ''


"""============Progreso de Descarga==========="""
def progressddl(current, total,message,bots,filename,start):
    porcent = int(current * 100 / total)
    act = time.time() - start
    velo = round((round(current/1000000,2)/act),2)
    global sec
    if sec != time.localtime().tm_sec:
        try:
            text = f"⏬**Descargando de Telegram**\n\n💾**Nombre**: {filename} \n"
            text += f'{text_progres(current,total)} {current * 100 / total:.1f}%\n\n'
            text += f'🗓**Total**:{round(total/1000000,2)} MiB \n'
            text += f'📥**Descargado**: {round(current/1000000,2)}MiB\n'
            text += f'📥**Velocidad**: {velo} MiB/S\n'
            bots.edit_message_text(message.chat.id,message.id,text)
        except:pass 
        sec = time.localtime().tm_sec


"""============Progreso de Subida==============="""
def progressub(current, total,message,bots,filename,start):
    porcent = int(current * 100 / total)
    act = time.time() - start
    velo = round((round(current/1000000,2)/act),2)
    global sec
    if sec != time.localtime().tm_sec:
        try:
            text = f"⏫**Subiendo a Telegram**\n\n💾**Nombre**: {filename} \n"
            text += f'{text_progres(current,total)} {current * 100 / total:.1f}%\n\n'
            text += f'🗓**Total **:{round(total/1000000,2)} MiB \n'
            text += f'📤**Subido**: {round(current/1000000,2)}MiB\n'
            text += f'📥**Velocidad**: {velo} MiB/S\n'
            bots.edit_message_text(message.chat.id,message.id,text)
        except:pass
        sec = time.localtime().tm_sec

"""============Progreso de Descarga de Youtube==============="""
def progressytdl(current, total,speed,filename,tiempo,message,bots):
    porcent = int(current * 100 / total)
    filename =filename.split('/')[-1]
    global sec
    if sec != time.localtime().tm_sec:
        try:
            text = f"⏬**Descargando de Youtube**\n\n💾**Nombre**: {filename} \n"
            text += f'{text_progres(current,total)} {current * 100 / total:.1f}%\n\n'
            text += f'🗓**Total**:{round(total/1000000,2)} MiB \n'
            text += f'📥**Descargado**: {round(current/1000000,2)}MiB\n'
            text += f'📥**Velocidad**: {round(float(speed)/1000000,2)} MiB/S\n'
            text += f'⏱**Tiempo**: {tiempo}\n'
            bots.edit_message_text(message.chat.id,message.id,text)
        except:pass 
        sec = time.localtime().tm_sec

"""=============Progreso de Descarga de Twitch================"""
def progresstwitch(current,speed,filename,tiempo,message,bots):
    filename =filename.split('/')[-1]
    global sec
    if sec != time.localtime().tm_sec:
        try:
            text = f"⏬**Descargando de Twitch**\n\n💾**Nombre**: {filename} \n\n"
            text += f'📥**Descargado**: {round(current/1000000,2)}MiB\n'
            text += f'📥**Velocidad**: {round(float(speed)/1000000,2)} MiB/S\n'
            text += f'⏱**Tiempo**: {tiempo}\n'
            bots.edit_message_text(message.chat.id,message.id,text)
        except:pass 
        sec = time.localtime().tm_sec


"""==============Progreso de Descargas Directas=============="""
def progresswget(current,total,filename,start,message,bots):
    porcent = int(current * 100 // total)
    act = time.time() - start
    velo = round((round(current/1000000,2)/act),2)
    global sec
    if sec != time.localtime().tm_sec:
        try:
            text = f"⏬**Descargando Para el Servidor**\n\n💾**Nombre**: {filename} \n"
            text += f'{text_progres(current,total)} {current * 100 // total:.1f}%\n\n'
            text += f'🗓**Total**: {round(total/1000000,2)} MiB \n'
            text += f'📥**Descargado**: {round(current/1000000,2)}MiB\n'
            text += f'📥**Velocidad**: {velo} MiB/S\n'
            bots.edit_message_text(message.chat.id,message.id,text)
        except:pass
        sec = time.localtime().tm_sec