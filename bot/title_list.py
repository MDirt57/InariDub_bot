from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ContextTypes

from database.title_repository import TitleRepository
import inject
from bot import navigation_keyboard

@inject.params(repository=TitleRepository)
async def title_list(update: Update, context: ContextTypes.DEFAULT_TYPE, repository: TitleRepository):
    query = update.inline_query.query

    if query != "t:":
        return

    all_titles = repository.get_all_titles()[:10]

    results = [
        InlineQueryResultArticle(
            id=str(title.id),
            url=title.mal_link,
            description="Немає",
            title=f"{title.name} ({title.series_count})",
            thumbnail_url="https://cdn.myanimelist.net/images/anime/1344/131301.jpg",
            input_message_content=InputTextMessageContent(f"/t {title.id}"),
        ) for title in all_titles
    ]

    await update.inline_query.answer(results)

@inject.params(repository=TitleRepository)
async def title_list(update: Update, context: ContextTypes.DEFAULT_TYPE, repository: TitleRepository):
    query = update.inline_query.query
    all_titles = []

    if query != "d:" and query != "s:":
        return

    if query == "d:":
        all_titles = repository.get_dub_titles()
    if query == "s:":
        all_titles = repository.get_sub_titles()

    results = [
        InlineQueryResultArticle(
            id=str(title.id),
            url=title.mal_link,
            description="Немає",
            title=f"{title.name} ({episode_count})",
            thumbnail_url="https://cdn.myanimelist.net/images/anime/1344/131301.jpg",
            input_message_content=InputTextMessageContent(f"/{query[0]} {title.id}"),
        ) for title, episode_count in all_titles
    ]

    await update.inline_query.answer(results)

