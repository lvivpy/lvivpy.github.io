"""
Usage: statistic.py <API_KEY> <path to file with IDS>
"""
import sys
import asyncio
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def _get_member(session: aiohttp.ClientSession, api_key, mid):
    r = await session.get(f'https://api.meetup.com/2/member/{mid}'
                          f'?key={api_key}'
                          f'&sign=true'
                          f'&format=json')
    try:
        return await r.json()
    except Exception as e:
        logger.exception(f'Failed to fetch member info {mid}')


async def main(api_key, members_filename):

    with open(members_filename) as members_fd:
        member_ids = members_fd.readlines()

    async with aiohttp.ClientSession() as session:
        for mid in member_ids:
            member_obj = await _get_member(session, api_key, mid.strip())
            print(member_obj.get('city'),
                  member_obj.get('gender'),
                  member_obj.get('hometown'))


if __name__ == '__main__':
    _, api_key, members_filename = sys.argv

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(api_key, members_filename))
    loop.close()
