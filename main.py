import		os
		from		fastapi	import FastAPI, Request
		from		aiogram	import Bot, Dispatcher
		from		aiogram.types import Update

		from		bot	import bot, dp

		WEBHOOK_URL = os.
getenv("WEBHOOK_URL")
app = FastAPI()
@ app.on_event("startup")
async def on_startup():
await bot.set_webhook(WEBHOOK_URL)
@ app.post("/webhook")
async def telegram_webhook(request: Request):
data = await request.json()
update = Update(**data)
await dp.feed_update(bot, update)
return {"ok":True}
