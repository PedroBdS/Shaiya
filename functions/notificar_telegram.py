import asyncio
from telegram import Bot

bot = Bot(token='7507348213:AAHSYUXN1RppFnMGFxVaclmQDyT4o7UvLx8')
CHAT_ID = '7234952237'

async def enviar_mensagem_telegram(texto):
    await bot.send_message(chat_id=CHAT_ID, text=texto)

def notificar_via_telegram(texto):
    # Obtém o loop de eventos atual ou cria um novo se não houver
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Se o loop já estiver rodando, cria uma tarefa assíncrona
            asyncio.ensure_future(enviar_mensagem_telegram(texto))
        else:
            # Se não houver loop rodando, roda até a conclusão
            loop.run_until_complete(enviar_mensagem_telegram(texto))
    except RuntimeError:
        # Se não houver um loop ativo, cria um novo e define como padrão
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(enviar_mensagem_telegram(texto))


if __name__ == '__main__':
    notificar_via_telegram('teste')
