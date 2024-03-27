# /d4 : return number from 1 to 4.
# /d6 : return number from 1 to 6.
# /d8 : return number from 1 to 8.
# /d10 : return number from 1 to 10.
# /d12 : return number from 1 to 12.
import random
import discord
import os
import sys
import re


def roll_dice(command: str) -> str:
    dice: str
    quantity: int
    result_line: str = f'Result of rolling {command} is '
    dices_list: list[str] = command.split('+')
    dice_pair = re.compile(r"^([1-9]?)(d|dice)([1-9]+)$")
    for i, dice in enumerate(dices_list):
        dice_matched: re.Match[str] | None = dice_pair.match(dice)
        if not dice_matched:
            return "Error. Invalid command"
        quantity = int(dice_matched.group(1)) if dice_matched.group(1) else 1
        for j in range(quantity):
            result_line += f'{solve(int(dice_matched.group(3)))}'
            if j != quantity-1 or i != len(dices_list)-1:
                result_line += f' + '
    return result_line


def solve(num: int) -> str:
    roll_result: int = random.randint(1, int(num))
    dice_result: int = roll_result
    while roll_result == int(num):
        roll_result = random.randint(1, int(num))
        dice_result += roll_result
    return str(dice_result)


if __name__ == '__main__':
    bot = discord.Client(intents=discord.Intents(message_content=True, messages=True))

    @bot.event
    async def on_message(message):
        if message.content.startswith('//'):
            await message.channel.send(roll_dice(message.content[2:]))
    token = os.getenv('TOKEN')
    if not token:
        print('There is no token specified')
        sys.exit(1)
    bot.run(token)
