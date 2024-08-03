from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from nes_music import db
from nes_music.models import Video


# engine = create_engine("sqlite:///nes_music.db")
# session = Session(engine)

data = [
    # Company
    Company(
        id=1,
        name="Natsume"
    ),
    Company(
        id=2,
        name="Taito"
    ),
    Company(
        id=3,
        name="Human Entertainment"
    ),
    Company(
        id=4,
        name="HAL Laboratory"
    ),
    Company(
        id=5,
        name="Winky Soft"
    ),
    Company(
        id=6,
        name="SETA"
    ),
    Company(
        id=7,
        name="Sunsoft"
    ),
    Company(
        id=8,
        name="Konami"
    ),
    Company(
        id=9,
        name="Nintendo"
    ),
    Company(
        id=10,
        name="Shouei"
    ),
    Company(
        id=11,
        name="Electro Brain"
    ),
    Company(
        id=12,
        name="First Star Software"
    ),
    Company(
        id=13,
        name="Kemco"
    ),
    Company(
        id=14,
        name="Tecmo"
    ),
    Company(
        id=15,
        name="Capcom"
    ),
    Company(
        id=16,
        name="Software Creations"
    ),
    Company(
        id=17,
        name="American Softworks"
    ),
    Company(
        id=18,
        name="Aicom"
    ),
    Company(
        id=19,
        name="American Sammy"
    ),
    Company(
        id=20,
        name="SNK"
    ),
    Company(
        id=21,
        name="Rare"
    ),
    Company(
        id=22,
        name="Tradewest"
    ),

    #Game
    Game(
        id=1,
        name="Power Blade",
        developer_id=1,
        publisher_id=2,
        year=1991
    ),
    Game(
        id=2,
        name="Kabuki: Quantum Fighter",
        developer_id=3,
        publisher_id=4,
        year=1991
    ),
    Game(
        id=3,
        name="The Adventures of Tom Sawyer",
        developer_id=5,
        publisher_id=6,
        year=1989
    ),
    Game(
        id=4,
        name="Hebereke",
        developer_id=7,
        publisher_id=7,
        year=1991
    ),
    Game(
        id=5,
        name="The Adventures of Bayou Billy",
        developer_id=8,
        publisher_id=8,
        year=1989
    ),
    Game(
        id=6,
        name="Journey to Silius",
        developer_id=7,
        publisher_id=7,
        year=1990
    ),
    Game(
        id=7,
        name="Super Mario Bros. 2",
        developer_id=9,
        publisher_id=9,
        year=1988
    ),
    Game(
        id=8,
        name="Puss 'n Boots: Pero's Great Adventure",
        developer_id=10,
        publisher_id=11,
        year=1990
    ),
    Game(
        id=9,
        name="Spy vs. Spy",
        developer_id=12,
        publisher_id=13,
        year=1988
    ),
    Game(
        id=10,
        name="Ninja Gaiden",
        developer_id=14,
        publisher_id=14,
        year=1989
    ),
    Game(
        id=11,
        name="Little Nemo: The Dream Master",
        developer_id=15,
        publisher_id=15,
        year=1990
    ),
    Game(
        id=12,
        name="Treasure Master",
        developer_id=16,
        publisher_id=17,
        year=1991
    ),
    Game(
        id=13,
        name="Vice: Project Doom",
        developer_id=18,
        publisher_id=19,
        year=1991
    ),
    Game(
        id=14,
        name="Super Mario Bros. 3",
        developer_id=9,
        publisher_id=9,
        year=1990
    ),
    Game(
        id=15,
        name="Gimmick!",
        developer_id=7,
        publisher_id=7,
        year=1992
    ),
    Game(
        id=16,
        name="Crystalis",
        developer_id=20,
        publisher_id=20,
        year=1990
    ),
    Game(
        id=17,
        name="Battletoads",
        developer_id=21,
        publisher_id=22,
        year=1991
    ),
    Game(
        id=18,
        name="Shadow of the Ninja",
        developer_id=1,
        publisher_id=1,
        year=1990
    ),
    Game(
        id=19,
        name="Kirby's Adventure",
        developer_id=4,
        publisher_id=9,
        year=1993
    ),

    # Composer
    Musician(
        id=1,
        name="Kinuyo Yamashita"
    ),
    Musician(
        id=2,
        name="Masaki Hashimoto"
    ),
    Musician(
        id=3,
        name="Takahiro Wakuta"
    ),
    Musician(
        id=4,
        name="Naoki Kodaka"
    ),
    Musician(
        id=5,
        name="Nobuyuki Hara"
    ),
    Musician(
        id=6,
        name="Shinichi Seya"
    ),
    Musician(
        id=7,
        name="Jun Funahashi"
    ),
    Musician(
        id=8,
        name="Kiyohiro Sada"
    ),
    Musician(
        id=9,
        name="Hidenori Maezawa"
    ),
    Musician(
        id=10,
        name="Tsutomu Oguro"
    ),
    Musician(
        id=11,
        name="Atsushi Fujio"
    ),
    Musician(
        id=12,
        name="Naohisa Morota"
    ),
    Musician(
        id=13,
        name="Manabu Sakota"
    ),
    Musician(
        id=14,
        name="Koji Kondo"
    ),
    Musician(
        id=15,
        name="Tomohisa Mitsuyasu"
    ),
    Musician(
        id=16,
        name="Kaori Aoki"
    ),
    Musician(
        id=17,
        name="Nick Scarim"
    ),
    Musician(
        id=18,
        name="Hiroyuki Masuno"
    ),
    Musician(
        id=19,
        name="Keiji Yamagishi"
    ),
    Musician(
        id=20,
        name="Ryuichi Nitta"
    ),
    Musician(
        id=21,
        name="Ichiro Nakagawa"
    ),
    Musician(
        id=22,
        name="Junko Tamiya"
    ),
    Musician(
        id=23,
        name="Tim Follin"
    ),
    Musician(
        id=24,
        name="Kiyoshi Yokoyama"
    ),
    Musician(
        id=25,
        name="Masashi Kageyama"
    ),
    Musician(
        id=26,
        name="Yoko Osaka"
    ),
    Musician(
        id=27,
        name="David Wise"
    ),
    Musician(
        id=28,
        name="Iku Mizutani"
    ),
    Musician(
        id=29,
        name="Kouichi Yamanishi"
    ),
    Musician(
        id=30,
        name="Hirokazu Ando"
    ),
    Musician(
        id=31,
        name="Jun Ishikawa"
    ),

    # Song
    Song(
        id=1,
        name='"Ending" [Soundtrack]',
        game_id=1
    ),
    Song(
        id=2,
        name='“Round 5” [Soundtrack]',
        game_id=2
    ),
    Song(
        id=3,
        name='“Prologue” [Soundtrack]',
        game_id=3
    ),
    Song(
        id=4,
        name='"Hebe in the Parallel Area" [Unused soundtrack, edited]',
        game_id=4
    ),
    Song(
        id=5,
        name='"Annabelle is Kidnapped/Stage 1" [Soundtrack]',
        game_id=5
    ),
    Song(
        id=6,
        name='"Title Screen" [Soundtrack]',
        game_id=6
    ),
    Song(
        id=7,
        name='"Underground/Underground paused" [Soundtrack]',
        game_id=7
    ),
    Song(
        id=8,
        name='"Demon Boss" [Soundtrack, edited]',
        game_id=8
    ),
    Song(
        id=9,
        name='"In-game Theme" [Soundtrack]',
        game_id=9
    ),
    Song(
        id=10,
        name='"Melancholy Destiny" [Soundtrack]',
        game_id=10
    ),
    Song(
        id=11,
        name='"Dream 4: Night Sea" [Soundtrack]',
        game_id=11
    ),
    Song(
        id=12,
        name='"World 1: The Islands" [Soundtrack]',
        game_id=12
    ),
    Song(
        id=13,
        name='"Ending" [Soundtrack, edited]',
        game_id=13
    ),
    Song(
        id=14,
        name='"Sector 2" [Soundtrack]',
        game_id=1
    ),
    Song(
        id=15,
        name='"World 6 Map" [Soundtrack]',
        game_id=14
    ),
    Song(
        id=16,
        name='"Good Morning" [Soundtrack]',
        game_id=15
    ),
    Song(
        id=17,
        name='"Fields" [Soundtrack]',
        game_id=16
    ),
    Song(
        id=18,
        name='"Stage 2" [Soundtrack]',
        game_id=6
    ),
    Song(
        id=19,
        name='"Level 10—Rat Race" [Soundtrack]',
        game_id=17
    ),
    Song(
        id=20,
        name='"Ending" [Soundtrack]',
        game_id=18
    ),
    Song(
        id=21,
        name='“Level 3: Butter Building" [Soundtrack]',
        game_id=19
    ),

    # SongMusician
    SongMusician(
        id=1,
        song_id=1,
        composer_id=1
    ),
    SongMusician(
        id=2,
        song_id=2,
        composer_id=2
    ),
    SongMusician(
        id=3,
        song_id=2,
        composer_id=3
    ),
    SongMusician(
        id=4,
        song_id=3
    ),
    SongMusician(
        id=5,
        song_id=4,
        composer_id=4
    ),
    SongMusician(
        id=6,
        song_id=4,
        composer_id=5
    ),
    SongMusician(
        id=7,
        song_id=4,
        composer_id=6
    ),
    SongMusician(
        id=8,
        song_id=5,
        composer_id=7
    ),
    SongMusician(
        id=9,
        song_id=5,
        composer_id=8
    ),
    SongMusician(
        id=10,
        song_id=5,
        composer_id=9
    ),
    SongMusician(
        id=11,
        song_id=5,
        composer_id=10
    ),
    SongMusician(
        id=12,
        song_id=5,
        arranger_id=11
    ),
    SongMusician(
        id=13,
        song_id=6,
        composer_id=4
    ),
    SongMusician(
        id=14,
        song_id=6,
        composer_id=5
    ),
    SongMusician(
        id=15,
        song_id=6,
        composer_id=6
    ),
    SongMusician(
        id=16,
        song_id=6,
        composer_id=12
    ),
    SongMusician(
        id=17,
        song_id=6,
        composer_id=13
    ),
    SongMusician(
        id=18,
        song_id=7,
        composer_id=14
    ),
    SongMusician(
        id=19,
        song_id=8,
        composer_id=15
    ),
    SongMusician(
        id=20,
        song_id=8,
        composer_id=16
    ),
    SongMusician(
        id=21,
        song_id=9,
        composer_id=17
    ),
    SongMusician(
        id=21,
        song_id=9,
        arranger_id=18
    ),
    SongMusician(
        id=22,
        song_id=10,
        composer_id=19
    ),
    SongMusician(
        id=23,
        song_id=10,
        composer_id=20
    ),
    SongMusician(
        id=24,
        song_id=10,
        composer_id=21
    ),
    SongMusician(
        id=25,
        song_id=11,
        composer_id=22
    ),
    SongMusician(
        id=26,
        song_id=12,
        composer_id=23
    ),
    SongMusician(
        id=27,
        song_id=13,
        composer_id=24
    ),
    SongMusician(
        id=28,
        song_id=14,
        composer_id=1
    ),
    SongMusician(
        id=29,
        song_id=15,
        composer_id=14
    ),
    SongMusician(
        id=30,
        song_id=16,
        composer_id=25
    ),
    SongMusician(
        id=31,
        song_id=16,
        composer_id=12
    ),
    SongMusician(
        id=32,
        song_id=17,
        composer_id=26
    ),
    SongMusician(
        id=33,
        song_id=18,
        composer_id=4
    ),
    SongMusician(
        id=34,
        song_id=18,
        composer_id=5
    ),
    SongMusician(
        id=35,
        song_id=18,
        composer_id=6
    ),
    SongMusician(
        id=36,
        song_id=18,
        composer_id=12
    ),
    SongMusician(
        id=37,
        song_id=18,
        composer_id=13
    ),
    SongMusician(
        id=38,
        song_id=19,
        composer_id=27
    ),
    SongMusician(
        id=39,
        song_id=20,
        composer_id=28
    ),
    SongMusician(
        id=40,
        song_id=20,
        composer_id=29
    ),
    SongMusician(
        id=41,
        song_id=21,
        composer_id=30
    ),
    SongMusician(
        id=42,
        song_id=21,
        composer_id=31
    ),

    # Video
    Video(
        id=1,
        game_id=1,
        song_id=1,
        description="End music for Power Blade on the Nintendo Entertainment System.",
        process_note="I used Game Genie code YANNLTZA, which immediately shows the ending after starting a game.",
        upload_date=datetime(2024, 6, 26, 7, 54, 16),
        link="https://youtu.be/RKpMkeXW97I"
    ),
    Video(
        id=2,
        game_id=2,
        song_id=2,
        description="Music for Round 5 of Kabuki: Quantum Fighter on the Nintendo Entertainment System.",
        process_note="I used Game Genie codes AVUUZPSZ+ESUZGAEY to have invincibility, then played to Round 5.",
        upload_date=datetime(2024, 6, 27, 9, 18, 39),
        link="https://youtu.be/YfCrVB27I40"
    ),
    Video(
        id=3,
        game_id=3,
        song_id=3,
        description="Prologue music for The Adventures of Tom Sawyer on the Nintendo Entertainment System.",
        process_note="Only about 13 of about 28 seconds of the original composition appear in the game.",
        upload_date=datetime(2024, 6, 27, 16, 33, 17),
        link="https://youtu.be/aosXPQeTND8"
    ),
    Video(
        id=4,
        game_id=4,
        song_id=4,
        description="Unused music for Hebereke on the Nintendo Famicon.",
        desc_note="The original NSFe file is 25 seconds long and doesn't loop.",
        process_note="I used cheat code 0505:00 to slowly descend. I played the game to reach the point shown in the video.",
        upload_date=datetime(2024, 6, 27,19, 49, 9),
        link="https://youtu.be/kBG86jKnw24"
    ),
    Video(
        id=5,
        game_id=5,
        song_id=5,
        description="Introductory and Stage 1 music for The Adventures of Bayou Billy on the Nintendo Entertainment System.",
        process_note="Songs combined by me.",
        upload_date=datetime(2024, 6, 29, 10, 40, 28),
        link="https://youtu.be/TM8C-_dHt-w"
    ),
    Video(
        id=6,
        game_id=6,
        song_id=6,
        description="Title screen music for Journey to Silius on the Nintendo Entertainment System.",
        upload_date=datetime(2024, 6, 30, 11, 32, 40),
        link="https://youtu.be/QQrjegx0B8w"
    ),
    Video(
        id=7,
        game_id=7,
        song_id=7,
        description='"Underground" and "Underground" paused music for Super Mario Bros. 2 on the Nintendo Entertainment System.',
        process_note='I personally discovered the glitch when playing the game a few months before I made the video: throwing the potion at the top of the screen, then entering the door, causes the character to appear at the bottom of the screen when exiting the door in the subspace. Also, there was no pause music in the game’s NSFe files, so I deleted the square channels using FamiStudio to create a new NSFe file of “Underground paused”.',
        upload_date=datetime(2024, 6, 30, 15, 6, 41),
        link="https://youtu.be/nO2fhOmDdVk"
    ),
    Video(
        id=8,
        game_id=8,
        song_id=8,
        description="Demon boss battle music for Puss 'n Boots: Pero's Great Adventure on the Nintendo Entertainment System.",
        desc_note="The original composition is a loop roughly 15 seconds long; my edited version loops that hot jam part of the song.",
        process_note="I made a new NSFe file in FamiStudio, where I’d edited the original composition to contain the looping that I wanted it to. I played through the game with no cheats to make it to the Demon boss.",
        upload_date=datetime(2024, 7, 1, 8, 31, 23),
        link="https://youtu.be/FpcauB7hMiA"
    ),
    Video(
        id=9,
        game_id=9,
        song_id=9,
        description="In-game music for Spy vs. Spy on the Nintendo Entertainment System.",
        upload_date=datetime(2024, 7, 2, 16, 48, 23),
        link="https://youtu.be/uiiSrFWOn7U"
    ),
    Video(
        id=10,
        game_id=10,
        song_id=10,
        description="First-stage final boss music for Ninja Gaiden on the Nintendo Entertainment System.",
        process_note="I used invincibility codes 0095:02+0093:80, then played through to first final boss.",
        upload_date=datetime(2024, 7, 6, 11, 44, 26),
        link="https://youtu.be/wX_h5qwyZvE"
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
    Video(
        id=,
        game_id=,
        song_id=,
        description="",
        desc_note="",
        process_note="",
        upload_date=,
        link=""
    ),
]


# session.add_all(data)
# session.commit()
# session.close()
# engine.dispose()