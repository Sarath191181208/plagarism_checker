import asyncio
import ssl
import aiohttp

async def fetch(session, url):
    async with session.get(url, ssl=ssl.SSLContext()) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results


if __name__ == '__main__':

    url_list = ['https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530396000&before=1530436000',
                'https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530436000&before=1530476000']

    loop = asyncio.get_event_loop()
    urls = url_list
    htmls = loop.run_until_complete(fetch_all(urls, loop))
    print(htmls)
