import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import Message, FSInputFile
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

# from botBd import resultlvl

API_TOKEN: str = os.environ['API_TOKEN']

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    kb = [
        [types.KeyboardButton(text='Уровни закулисья')],
        [types.KeyboardButton(text='Предметы закулисья')],
        [types.KeyboardButton(text='Группы закулисья')],
        [types.KeyboardButton(text='Сущности закулисья')]
    ]
    keyboardStart = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer('Привет, я твой корманный помощник, по закулисью\n О чём бы вы хотели узнать?',
                         reply_markup=keyboardStart)


@dp.message(Text("Уровни закулисья"))
async def levelBackrooms(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Уровень 0 "Хаб"')],
        [types.KeyboardButton(text='Уровень 1 "Обитаемая зона"')],
        [types.KeyboardButton(text='Уровень 2 "Водопровод мечты"')],
        [types.KeyboardButton(text='Уровень 3 "Электрическая станция"')],
        [types.KeyboardButton(text='Уровень 4 "Заброшенные офисы"')],
        [types.KeyboardButton(text='Уровень 5 "Ужасающий отель"')],
        [types.KeyboardButton(text='Уровень 6 "Тёмная сторона"')],
        [types.KeyboardButton(text='Уровень 7 "Талассофобия"')],
        [types.KeyboardButton(text='Уровень 8 "Система пещер"')],
    ]
    keyboardLvl = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Вы перешли во вкладку с Уровнями закулисья", reply_markup=keyboardLvl)


@dp.message(Text("Предметы закулисья"))
async def itemBackrooms(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Миндальная вода')],
        [types.KeyboardButton(text='Уровневые ключи')],
        [types.KeyboardButton(text='Банки с воспоминаниями')],
        [types.KeyboardButton(text='Сок Памяти')],
        [types.KeyboardButton(text='Скарабей')],
        [types.KeyboardButton(text='Огнесоль')],
        [types.KeyboardButton(text='Царский Паёк')],
        [types.KeyboardButton(text='Жидкая тишина')],
        [types.KeyboardButton(text='Жидкая боль')],
    ]
    keyboardItem = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Вы перешли во вкладку с предметами закулисья", reply_markup=keyboardItem)


@dp.message(Text("Сущности закулисья"))
async def monstersBackrooms(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Бактерия')],
        [types.KeyboardButton(text='Улыбающиеся')],
        [types.KeyboardButton(text='Смертомоль')],
        [types.KeyboardButton(text='Многорук')],
        [types.KeyboardButton(text='Серость')],
        [types.KeyboardButton(text='Кожекрады')],
        [types.KeyboardButton(text='Убогие')],
        [types.KeyboardButton(text='Окна')],
        [types.KeyboardButton(text='Гончие')],
    ]
    keyboardMonster = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Вы перешли во вкладку с сущностями закулисья", reply_markup=keyboardMonster)


@dp.message(Text("Группы закулисья"))
async def teamBackrooms(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Backrooms Remodeling Co')],
        [types.KeyboardButton(text='Backrooms Robotics')],
        [types.KeyboardButton(text='Тёмные Рыцари')],
        [types.KeyboardButton(text='Н.Т.О.З')],
        [types.KeyboardButton(text='Капитанский Экипаж')],
        [types.KeyboardButton(text='Глаза Аргоса')],
        [types.KeyboardButton(text='Последователи Джерри')],
        [types.KeyboardButton(text='Б.И.Г')],
        [types.KeyboardButton(text='Девы в Масках')],
    ]
    keyboardTeam = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer("Вы перешли во вкладку с группами закулисья", reply_markup=keyboardTeam)


@dp.message(Text('Уровень 0 "Хаб"'))
async def lvl0(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Назад')],
    ]

    photo = FSInputFile('photo/level0.jpg')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await bot.send_photo(chat_id=message.chat.id, photo=photo,
                         caption='[Безопасен]\n[Стабилен]\n[Минимальное количество сущностей]\nУровень 0 — обучающий уровень, нелинейное пространство, напоминающее подсобные помещения торговых точек. Как и в своём первом варианте, все комнаты уровня 0 выглядят однообразно и обладают общими чертами, такими как желтые обои, влажные ковры и беспорядочно расположенные люминесцентные лампы. Несмотря на это, на уровне вы не встретите две одинаковые комнаты. Установленные лампы хаотично мигают и издают постоянное гудение. Этот звук намного громче и навязчивее шума обычных люминесцентных ламп, исследование светильников с целью обнаружения источника этого звука не дало результатов. Жидкость, которой пропитаны ковры, не опознана. Это не вода, и пить её небезопасно.',
                         reply_markup=keyboard)


@dp.message(Text('Уровень 1 "Обитаемая зона"'))
async def lvl1(message: Message):
    kb = [
        [types.KeyboardButton(text='На главную')],
        [types.KeyboardButton(text='Назад')],
    ]

    photo1 = FSInputFile('photo/level1.jpg')
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await bot.send_photo(chat_id=message.chat.id, photo=photo1,
                         caption='[Безопасен]\n[Стабилен]\n[Минимальное количество сущностей]\nУровень 1 — огромный просторный склад с бетонными полами и стенами, торчащей арматурой и низко висящим туманом, источник которого не обнаружен. Туман часто образует конденсат, создавая лужи на полу в различных местах. В отличие от Уровня 0, на данном уровне содержится постоянный запас воды и электричества, что делает его пригодным для жизни при условии соблюдения мер предосторожности. Также пространство уровня является более разнообразным, включая в себя лестницы, Лифты, отдельные комнаты и коридоры.Ящики с припасами появляются и исчезают случайным образом. В них часто содержатся жизненно необходимые предметы (еда, Миндальная вода, батареи, тенты, оружие, одежда и медикаменты), но также они могут содержать и бесполезные вещи (автомобильные детали, коробки цветных карандашей, использованные шприцы, частично сожженную бумагу, живых мышей, мышей в кататоническом состоянии, которым были введены неизвестные вещества, шнурки, мелочь, пучки человеческих волос).',
                         reply_markup=keyboard1)


@dp.message(Text('На главную'))
async def main(message: Message):
    kb = [
        [types.KeyboardButton(text='Уровни закулисья')],
        [types.KeyboardButton(text='Предметы закулисья')],
        [types.KeyboardButton(text='Группы закулисья')],
        [types.KeyboardButton(text='Сущности закулисья')]
    ]
    keyboardMain = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    await message.answer('Вы перешли на главную страницу', reply_markup=keyboardMain)


if __name__ == '__main__':
    dp.run_polling(bot)
