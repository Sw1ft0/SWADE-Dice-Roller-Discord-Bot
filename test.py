import main
import tokenizer

test_commands_list: list[str] = [
    "5d2+d8+2dice6+d4",
    "5d2+d8 +2dice6 + d4",
    "d4++d8",
    "d6+d4",
    "d2 + dice6",
    "dice2",
    "d4",
    ""
    "2dice+12+d6+1dice4 + 3d8",
    ]

for command in test_commands_list:
    print(main.roll_dice(command))

# for command in test_commands_list:
#     for token in tokenizer.tokenize(command):
#         print(token)

print()
for command in test_commands_list:
    print(tokenizer.roll_with_tokenizer(command))
