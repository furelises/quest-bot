import layer
from layer import Layer
from user import User

project = {"project": "https://github.com/furelises/quest-bot.git"}

root = Layer(
    id='1',
    title='Начало',
    desc='Вы, просыпаетесь подвале неизвестного здания. Вокруг темнота, лишь '
         'тусклый свет пробивается из маленького окна под потолком. Оглядевшись, вы замечаете две двери перед собой. Одна дверь '
         'выглядит крепкой и надежной, а другая - старой и обветшалой. ВЫ понимаете, что придется выбирать между этими двумя'
         ' дверями, но ни одна из них не обещает легкого пути.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)

l21 = Layer(
    id='21',
    title='дверь1',
    desc='Вы находитесь в таин'
         'ственной комнате. В этой комнате на столе находятся два необычных предмета - головка чеснока и лук со стрелами.'
         'Вы должны сделать выбор: взять с собой чеснок для защиты или лук со с'
         'трелами для возможности охотиться и защищаться на расстоянии.',
    pictures=['chesnock.jpg']
)
l22 = Layer(
    id='22',
    title='дверь2',
    desc='Вы оказываетесь в новой комнате. На столе посреди комнаты лежат три предмета: нож, старая карта и кусок сыра.'
         ' Вам следует выбрать один из этих предметов и взять его с собой.',
    pictures=['karta.jpg']
)
l31 = Layer(
    id='31',
    title='чеснок',
    desc='Перед вами две новые двери, каждая из которых ведет в неизвестность. Выберите, в какую дверь вы пойдете теперь.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l32 = Layer(
    id='32',
    title='лук и стрелы',
    desc='Перед вами две новые двери, каждая из которых ведет в неизвестность. Выберите, в какую дверь вы пойдете теперь.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l33 = Layer(
    id='33',
    title='нож',
    desc='Перед вами две новые двери, каждая из которых ведет в неизвестность. Выберите, в какую дверь вы пойдете теперь.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l34 = Layer(
    id='34',
    title='карта',
    desc='Перед вами две новые двери, каждая из которых ведет в неизвестность. Выберите, в какую дверь вы пойдете теперь.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l35 = Layer(
    id='35',
    title='сыр',
    desc='Перед вами две новые двери, каждая из которых ведет в неизвестность. Выберите, в какую дверь вы пойдете теперь.',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l41 = Layer(
    id='41',
    title='дверь3',
    desc='',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)
l42 = Layer(
    id='42',
    title='дверь4',
    desc='',
    pictures=['door1.jpg', 'door2.jpg', 'door3.jpg', 'door4.jpg']
)

root.add_sub([l21, l22])
l21.add_sub([l31, l32])
l22.add_sub([l33, l34, l35])
l31.add_sub([l41, l42])
l32.add_sub([l41, l42])
l33.add_sub([l41, l42])
l34.add_sub([l41, l42])
l35.add_sub([l41, l42])


def find_layer(id: str) -> Layer:
    return layer.find_layer_from(id, root)


def is_winner(user: User) -> bool:
    return {"31", "41"}.issubset(user.get_path()) or {"34", "42"}.issubset(user.get_path())


def get_current_layer(user: User) -> Layer:
    path = user.get_path()
    if len(path) == 0:
        return root
    layer_id = path[-1]
    return find_layer(layer_id)


def project_to_str() -> str:
    a = ''
    for i in project:
        b = f'{i} : {project[i]}\n'
        a += b
    return a
