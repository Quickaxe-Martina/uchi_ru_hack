import django


django.setup()

from accounts.models import CustomUser
from core.db_models.faculty_db_model import Faculty
from core.db_models.question_db_model import Question
from core.db_models.subject_db_model import Subject
from core.db_models.topic_db_model import Topic
from core.db_models.answer_db_model import Answer

# How to run:
# python manage.py shell
# exec(open('deploy_script.py').read())


if not CustomUser.objects.filter(username='admin').exists():
    CustomUser.objects.create_superuser(
        username='admin',
        password='H6r3Lh\D#-~PcMQ6',
    )

if CustomUser.objects.filter(username='test_user1').exists():
    user1 = CustomUser.objects.get(username='test_user1')
else:
    user1 = CustomUser.objects.create_user(
        username='test_user1',
        password='test_user1@qwer',
    )

if CustomUser.objects.filter(username='test_user2').exists():
    user2 = CustomUser.objects.get(username='test_user2')
else:
    user2 = CustomUser.objects.create_user(
        username='test_user2',
        password='test_user2@qwer',
    )

FACULTY = [
    {
        'name': 'faculty1'
    },
    {
        'name': 'faculty2'
    },
    {
        'name': 'faculty3'
    },
    {
        'name': 'faculty4'
    },
]

for f in FACULTY:
    if not Faculty.objects.filter(name=f['name']).exists():
        Faculty.objects.create(name=f['name'])


QUESTION_DATA = {
    'География': {
        'Горы и равнины России': {
            'Чем обусловлен разнообразный рельеф России?': [
                'Большой территорией страны',
                'Российская Федерация протянулась на огромные расстояния с севера на юг и особенно с запада на '
                'восток. Благодаря внушительной площади рельеф страны отличается большим разнообразием. Реки, '
                'равнины и горы России составляют уникальную природную систему, которая отражает всю самобытность '
                'евразийского материка. '
            ],
            'Какова особенность всех равнин?': [
                'Равнина - значительные по площади участки поверхности суши, дна морей и океанов, для которых '
                'характерны: незначительный уклон местности (до 5°) и небольшое колебание высот (до 200 м); которое '
                'если и достигает сотен метров, то эти изменения имеют место на большом протяжении. Что ведёт к тому, '
                'что высоты соседних точек мало отличаются друг от друга.',

            ],
            'Каким цветом выделяют низменности на физической карте?': [
                'Зеленый цвет',
                'Если не ошибаюсь, то зеленый'
            ],
            'Как называется самая крупная равнина в России?': [
                'Восточно-Европейская (Русская) равнина — самая большая равнина на территории России.',

            ],
            'Какие горы в РФ являются самыми древними?': [
                'Уральские. Не только самые древние, но и одни из самых красивых на Земле.',
                'Уральские'
            ],
            'В какой горной системе встречаются действующие вулканы?': [
                'Большего всего вулканов в России на Камчатке. Согласно данным ЮНЕСКО, всего в стране их около '
                '30 действующих и 300 потухших. Последними называют вулканы, которые давно не проявляли активности.',

            ],
            'Как называется равнинная поверхность, лежащая высоко над уровнем моря?': [
                'Плоскогорье – местность с равнинной или холмистой поверхностью, лежащая высоко над уровнем моря. '
                'Холмистая – поверхность земли с холмами. '
            ],
            'В каких горах добывают самоцветы и драгоценные камни?': [
                'Самоцветная полоса прошла по восточному склону Уральских гор. Она объединяет сотни месторождений '
                'самоцветных камней. Здесь встречаются рубины, сапфиры, бериллы, аметисты, топазы, турмалины, '
                'рубеллиты, аквамарины, морионы, переливт и многие другие ценные камни. Некоторые камни самоцветной '
                'полосы Урала считаются лучшими в мире. '
            ],
            'Как называется самая высокая гора на территории России?': [
                'Эверест'
            ],
            'Какие горы разделяют Россию на две части: европейскую и азиатскую?': [
                'Уральские горы',
                '«Каменный пояс Земли Русской». Урал'
            ]
        },
        'Слои атмосферы': {
            'В какой сфере содержится весь водяной пар?': [
                'Практически весь водяной пар атмосферы содержится в 1) стратосфере 2) тропосфере 3) ее верхние слоях.',
                'Стратосфера'
            ],
            'Назовите самый плотный слой атмосферы': [
                'Тропосфера — самый нижний и наиболее плотный слой атмосферы. Тропосфера наиболее пригодна для жизни. '
                'Здесь обитает большинство живых организмов Земли, включая людей. Атмосфера вращается вместе с '
                'планетой, поэтому она так же сплюснута у полюсов '
            ],
            'До какой высоты простирается стратосфера?': [
                'СТРАТОСФЕ́РА (от лат. stratum – настил, слой и сфера), слой атмосферы, лежащий между тропосферой и '
                'мезосферой на высотах от 7–16 км до 50–55 км над уровнем моря',
            ],
            'Какой газ поглощает ультрафиолетовые лучи?': [
                'Поглощение в УФ-излучении лучше всего описать как отсечки с низкой длиной волны, а не как узкие '
                'полосы. Озон (O3) начинает поглощать ультрафиолетовое излучение с длиной волны менее 300 нм. '
            ],
            'Что принято считать нижней границей атмосферы?': [
                'Земля',
                'Земная поверхность'
            ]
        }
    },
    'Английский язык': {
        'Спряжение глаголов в английском языке': {
            'В каком времени к смысловым английским глаголам добавляют окончание s/es?': [
                'Окончание –s / –es / –ies в английском языке. Во–первых, простое настоящее время, всем известное как '
                'Present Simple. Оно используется, когда мы рассказываем о каких–то фактах или же обычных действиях. '
                'Формируем настоящее время, используя базовую форму инфинитива (без частички to). '
            ],
            'В каком времени глагол to be не употребляется в качестве смыслового?': [
                'Объясню, как обычно объясняю своим ученикам. Глагол to be употребляется в качестве сказуемого в '
                'английском языке в предложениях, в которых при переводе на русский язык он не звучит. Например,'
                '"Я - русский" - "I am Russian" или " Погода хорошая сегодня" - " The weather is nice today" или " Мы '
                'из Москвы" - " We are from Moscow". Во всех остальных случаях глагол to be является вспомогательным, '
                'а сказуемыми являются другие смысловые глаголы. '
            ],
            'Вспомогательным глаголом к какому времени является did?': [
                'Did – форма прошедшего времени oт «do». Если «do» смысловой, он понимается как «делать». '
                'Если вспомогательный – никак не переводится. I DID (смысловой) my homework – Я СДЕЛАЛ домашнюю работу '
            ],
            'Что выражают модальные глаголы в английском языке?': [
                'Модальные глаголы (modal verbs) — это особая группа глаголов. Они обозначают возможность, '
                'вероятность, необходимость или способность совершить какое-то действие. Есть модальные глаголы, '
                'используя которые, вы можете рассказать об умениях человека (can/could), запретить или приказать '
                'кому-либо что-то делать (must), дать совет (should) и т. д. '
            ],
            'Какому модальному глаголу требуется вспомогательный do/does?': [
                'Do как вспомогательный глагол нужен, чтобы задать вопрос или сформулировать отрицание в Present '
                'Simple. Если речь идет о he/she/it (3 лицо единственного числа), используется does. '
            ],
            'Какой эквивалент глагола can?': [
                'Эквивалент модального глагола can. Эквивалентом модального глагола can является '
                'конструкция to be able to, которая переводится на русский язык «мочь, уметь, быть способным» и '
                'идеально подходит модальному глаголу can, выражающему умственную и физическую способность человека. '
                'Пример: He will be able to help you tomorrow — Он сможет помочь тебе завтра '
            ]
        }
    },
    'Алгебра': {
        'Виды уравнений': {
            'Как решаются квадратные уравнения?': [
                'Через дискриминант'
            ],
            'Для решения каких уравнений применяют теорему Виета?': [
                'Обычно теорема Виета используется для решения приведённых квадратных уравнений, т. е. если '
                'коэффициент (a = 1). '
            ],
            'Для каких уравнений используют ОДЗ?': [
                'Область допустимых значений и область определения имеет один и тот же смысл. Только второй из '
                'них используется для выражений, а первый – для уравнений или неравенств. При помощи ОДЗ выражение '
                'или неравенство имеет смысл. '
            ],
            'Может ли у квадратного уравнения не быть корней?': [
                'Нет'
            ],
        }
    },
    'Математика': {
        'Деление двузначного числа на однозначное': {
            'Назовите операцию обратную делению?': [
                'Сложение'
            ],
            'Что получается при делении любого числа на 1?': [
                'Тоже число'
            ],
            'Если ноль поделить на любое число, то получится?': [
                'Ноль'
            ],
            'Можно ли делить на ноль?': [
                'Можно'
            ],

        }
    },
    'Биология': {
        'Появление человека': {
            'К какому семейству относятся люди?': [
                'Люди (лат. Homo) — род семейства гоминидов отряда приматов. Включает вид человек разумный (Homo '
                'sapiens) и близкие ему вымершие виды. Предками Homo, вероятно, являются австралопитеки. Люди (род). '
                'Научная классификация промежуточные ранги Домен: Эукариоты Царство: Животные Тип: Хордовые Класс: '
                'Млекопитающие Отряд: Приматы Семейство: Гоминиды Род: Люди. '
            ],
            'Кто является предком всех человекообразных обезьян?': [
                'Дриопитеки - род вымерших человекообразных обезьян, которые жили 9-12 млн. лет назад. Вероятнее '
                'всего, к дриопитекам относится общий предок человека, гориллы и шимпанзе. '
            ],
            'Где жили дриопитеки?': [
                'В Восточной Африке',
                'В Восточной Африке и Евразии'
            ],
            'Кто является предком неандертальца?': [
                'Предками неандертальцев были европейские Homo heidelbergensis. Принадлежали они к тому же виду, '
                'но проживали в Африке. Поэтому можно сказать, что неандертальцы — это как бы наши двоюродные братья '
                '(но никак не предшественники, вопреки распространенному заблуждению). '
            ],
            'Когда появились прямоходящие предки человека?': [
                'Человек прямоходящий или Эректус (Homo erectus), появился около 2 миллионов лет назад. Последние '
                'представители этого рода жили 27 тысяч лет назад в Индонезии, их относят к виду питекантропов. Этот '
                'вид предков человека раньше назывался архантропы, он непосредственный древнейший предок современных '
                'людей. '
            ],
            'Как выглядели австралопитеки?': [
                'Как обезьяна',
                'Являются предками рода Люди. С человеком австралопитеков сближает слабое развитие челюстей, '
                'отсутствие крупных выступающих клыков, хватательная кисть с развитым большим пальцем, опорная стопа '
                'и строение таза, приспособленное для прямохождения. Головной мозг относительно крупный (530 см³) '
            ],
            'Когда впервые стали использовать примитивные орудия?': [
                'Начало использования каменных инструментов началось около 2,5-3 млн лет назад в Африке. '
                'Высокоразвитый австралопитек, который начал использовать каменные орудия, получил название “Человек '
                'умелый”. '
            ],

        },
        'Царства живой природы': {
            'Как называется империя внеклеточных организмов?': [
                'Империя неклеточные организмы (Noncellulata). Царство вирусы (Virae). Вирусная частица (вирион) '
                'состоит из нуклеиновой кислоты (ДНК или РНК), окруженной белковой оболочкой – капсидом, состоящим из '
                'капсомеров. '
            ],
            'Сколько царств у живой природы?': [
                'В живой природе чаще всего выделяют четыре царства – Бактерии, Грибы, Растения и Животные. Живые '
                'организмы имеют ряд черт, отличающих их от объектов неживой природы: живые организмы состоят из '
                'клеток (от одной до множества), сходны по химическому составу, требуют поступления веществ и энергии '
                'извне. '
            ],
            'Где находятся молекулы ДНК у бактерий?': [
                'В клетках эукариот (животных, растений и грибов) ДНК находится в ядре клетки в составе хромосом, '
                'а также в некоторых клеточных органеллах (митохондриях и пластидах). В клетках прокариотических '
                'организмов (бактерий и архей) кольцевая или линейная молекула ДНК, так называемый нуклеоид, '
                'прикреплена изнутри к клеточной мембране. '
            ],
            'Какие органеллы не относятся к растительной клетке?': [
                "Хитиновая клеточная стенка (признак Грибов), центриоль (Признак Животной клетки) - органоиды не "
                "представленные в растительной клетке. "
            ]
        }
    },
    'Информатика': {
        'История развития ЭВМ': {
            'Какие из компьютеров являются самыми высокопроизводительными?': [
                'Самый мощный ПК обладает легковесной многоядерной ОС IHK/McKernel, состоящей из ядра Linux и '
                'облегченного ядра McKernel. Первая составляющая операционной системы необходима для всех '
                'POSIX-совместимых сервисов, а другая — для выполнения высокопроизводительной симуляции. '
            ],
            'Кто предложил идею создания электронно-вычислительной машины ENIAC?': [
                'ENIAC (название расшифровывается как «Электронный числовой интегратор и вычислитель») первоначально '
                'разрабатывался учеными из Пенсильванского университета (США) Джоном Преспером Эккертом и Джоном '
                'Уильямом Мокли в военных целях — а именно, для расчетов таблиц стрельбы, которые до того выполнялись '
                'вручную на арифмометрах. '
            ],
            'На какой элементной базе собран вычислительный центр ENIAC?': [
                'У ENIAC было несколько электромеханических частей, в частности, релейный регистр, служивший буфером '
                'между электронными аккумуляторами и перфораторными машинами от IBM, использовавшимися для ввода и '
                'вывода. Эта архитектура очень напоминала «Колосс» '
            ],
            'Какой из моделей ЭВМ полностью выполнен на транзисторной полупроводниковой базе?': [
                'Apple II'
            ],

        }
    },
    'История': {
        'Биография Мономаха': {
            'В каком году появился на свет Владимир Мономах?': [
                'Владимир (в крещении – Василий) Всеволодович родился в 1053 году. Прозвище Мономах он получил '
                'благодаря матери, которая, как считают историки, была дочерью византийского императора Константина '
                'IX Мономаха. '
            ],
            'Каким князем был Владимир Мономах уже в юношеские годы?': [
                'Владимир Всеволодович Мономах — древнерусский государственный деятель, князь ростовский (1066—1073 '
                'г.), смоленский (1073—1078 г.), черниговский (1078—1094г.), переяславский (1094—1113 г.), '
                'а впоследствии — киевский (1113—1125 г.). Его по праву называют одной из наиболее ярких фигур ранней '
                'отечественной истории. '
            ],
            'Кому Владимир Мономах уступил киевский престол после смерти отца?': [
                'В 1093 г., после смерти отца, он, чтобы не вступать в конфликт со своим двоюродным братом '
                'Святополком Изяславичем, уступил ему киевский престол. Затем Владимир Мономах активно помогал '
                'великому князю в борьбе против половцев. '
            ],
            'С кем успешно воевал Владимир Мономах?': [
                'В 1077 г. Владимир воевал с Полоцком. На поле брани Владимир Мономах одерживал одну победу за '
                'другой. С 13 до 25 лет он совершил 20 военных походов («великих путей», по выражению '
                'самого Владимира Мономаха; всего на его жизнь придется 83 «великих пути»). '
            ],
        },
        'Биография Князя Игоря': {
            'Кем был отец Игоря Святославича?': [
                'Уже в семилетнем возрасте мальчик принял участие в походе князя Изяслава за киевский престол. В '
                '18-летнем возрасте, в 1169 году, он выступил вместе с 11 князьями под руководством Андрея '
                'Боголюбского на столицу. '
            ],
            'В каком возрасте Игорь принял участие в походе князя Изяслава за киевский престол?': [
                'Уже в семилетнем возрасте мальчик принял участие в походе князя Изяслава за киевский престол. В '
                '18-летнем возрасте, в 1169 году, он выступил вместе с 11 князьями под руководством Андрея '
                'Боголюбского на столицу. '
            ],
            'В каком году Игорь Святославич пришёл к власти?': [
                '1180'
            ],

        },
        'Октябрьская революция': {
            'Кто открыл заседания II Cъезда советов?': [
                'Съезд провел два заседания: Первое заседание съезда с 22:45 25 октября до 6:00 26 октября: Съезд '
                'открыл меньшевик Ф. Дан 25 октября (7 ноября) в 22:45, в разгар начавшегося в Петрограде '
                'вооружённого восстания; в нём приняли участие многие делегаты, прибывшие с мест. '
            ],
            'Кто возглавлял последнее Временное правительство?': [
                'В последний состав Временного правительства вошли 4 кадета, 2 эсера, 3 меньшевика, 1 трудовик, '
                '1 «независимый» и 2 военных специалиста '
            ],
            'Кто арестовывал Временное правительство?': [
                'Министры Временного правительства были арестованы представителем Петроградского '
                'военно-революционного комитета В. А. Антоновым-Овсеенко в 2 часа 10 минут 26 октября 1917 года. '
            ]
        }
    },
    'Русский язык': {
        'Пунктуационный разбор': {
            'С каким языковым разбором часто путают пунктуационный разбор?': [
                'Нельзя  путать пунктуационный и синтаксический разборы, так как они преследуют разные цели: '
                'синтаксический – проанализировать предложение, пунктуационный – проанализировать знаки препинания. '
            ],
            'Что является объектом пунктуационного разбора?': [
                'Выполнить пунктуационный разбор - это значит объяснить пунктограмму (графически + анализ)'
            ],
            'Какой пункт плана пунктуационного разбора является первым?': [
                'Назвать и объяснить пунктограмму в конце предложения (точка, вопросительный знак, восклицательный '
                'знак, многоточие, сочетание знаков) '
            ]
        }
    }
}

for s in QUESTION_DATA:
    print(s)
    if Subject.objects.filter(name=s).exists():
        sub = Subject.objects.get(name=s)
    else:
        sub = Subject.objects.create(name=s)

    for t in QUESTION_DATA[s]:
        print(t)
        if Topic.objects.filter(name=t).exists():
            top = Topic.objects.get(name=t)
        else:
            top = Topic.objects.create(name=t, subject=sub)
        for q in QUESTION_DATA[s][t]:
            if Question.objects.filter(text=q).exists():
                ques = Question.objects.get(text=q)
            else:
                ques = Question.objects.create(
                    author_id=1,
                    topic=top,
                    text=q,
                    status='closed'
                )
            for i in range(len(QUESTION_DATA[s][t][q])):
                a = QUESTION_DATA[s][t][q][i]
                if not Answer.objects.filter(text=a).exists():
                    Answer.objects.create(
                        author=user1 if i == 0 else user2,
                        text=a,
                        question=ques
                    )
