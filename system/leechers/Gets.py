import aiohttp, asyncio
import urllib3
# Title
#     sys.stdout.write(f"\x1b]2;Scraper 3.0 by alperen_36 | Total Checked: {total} | TimeOut: {timeoutCount} | Finded: {totfind}\x07")
# Title

async def getSb(key, session):
    async with session.get(f"http://bin.shortbin.eu:8080/documents/{key}", verify_ssl=False, timeout=5) as response:
        response.raise_for_status()
        j = await response.json()
        if j['message']:
            return "Account does not found", response.status_code
        else:
            return j, response.status_code