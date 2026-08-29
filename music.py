import pygame
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

pygame.mixer.init()

song = "song.mp3"

sound = pygame.mixer.Sound(song)
song_length = sound.get_length()

pygame.mixer.music.load(song)
pygame.mixer.music.play()

lyrics = [
    (0,  "Hlian che ila ka dawn lungruk,"),
    (8,  "Hlian zai mi rel ve maw lungrun;"),
    (16, "Kei leh ka chhungte kan lawm nan,"),
    (24, "Kei riangte hi min hnawl suh aw."),

    (32, "Fak hla siamt'u'n a hrilhfiah zawh loh,"),
    (40, "Ang a nasa in ka duh che;"),
    (48, "Hria la chuan maw ka dawn lungruk hi,"),
    (56, "Uire nu iang min fawp mahna.")
]


def format_time(seconds):

    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    return f"{minutes:02d}:{seconds:02d}"


def progress_bar(current, total, width=40):

    percentage = min(current / total, 1)

    filled = int(width * percentage)
    empty = width - filled

    return (
        Fore.GREEN
        + "█" * filled
        + Fore.WHITE
        + "░" * empty
    )


def get_current_lyric(position):

    current = 0

    for i, (start, lyric) in enumerate(lyrics):

        if position >= start:
            current = i

    return current


# Clear terminal once
os.system("cls")

# Hide cursor
print("\033[?25l", end="")

try:

    while pygame.mixer.music.get_busy():

        position = pygame.mixer.music.get_pos() / 1000

        current_index = get_current_lyric(position)

        # Move cursor to beginning
        print("\033[H", end="")

        # HEADER

        print(
            Fore.YELLOW +
            "╔══════════════════════════════════════════════════╗"
        )

        print(
            Fore.YELLOW +
            "║" +
            Fore.WHITE +
            Style.BRIGHT +
            "              ♫ NOW PLAYING ♫                   " +
            Fore.YELLOW +
            "║"
        )

        print(
            Fore.YELLOW +
            "║" +
            Fore.CYAN +
            "                    ♪ SONG ♪                     " +
            Fore.YELLOW +
            "║"
        )

        print(
            Fore.YELLOW +
            "╚══════════════════════════════════════════════════╝"
        )

        print()

        # PREVIOUS

        if current_index > 0:

            print(
                Fore.BLUE +
                "        " +
                lyrics[current_index - 1][1]
            )

        else:

            print(
                Fore.BLUE +
                "                 ♪ ♪ ♪"
            )

        print()

        # CURRENT

        current = lyrics[current_index][1]

        if current_index < 4:
            colour = Fore.CYAN
        else:
            colour = Fore.MAGENTA

        print(
            colour +
            Style.BRIGHT +
            "        ♫ " +
            current +
            " ♫"
        )

        print()

        # NEXT

        if current_index < len(lyrics) - 1:

            print(
                Fore.BLUE +
                "        " +
                lyrics[current_index + 1][1]
            )

        else:

            print(
                Fore.BLUE +
                "                 ♡ ♡ ♡"
            )

        print()

        print(
            Fore.MAGENTA +
            "        ✦ ───────────────────────── ✦"
        )

        print()

        # PROGRESS BAR

        print(
            "             " +
            progress_bar(
                position,
                song_length
            )
        )

        print()

        # TIME

        print(
            Fore.WHITE +
            "                 " +
            format_time(position) +
            " / " +
            format_time(song_length)
        )

        print()

        print(
            Fore.MAGENTA +
            "             ♪   ♫   ♪   ♫   ♪"
        )

        # Refresh display
        time.sleep(0.1)

finally:

    print("\033[?25h")

    pygame.mixer.music.stop()

    print()
    print(
        Fore.MAGENTA +
        "                 ♡ END ♡"
    )

    pygame.mixer.quit()