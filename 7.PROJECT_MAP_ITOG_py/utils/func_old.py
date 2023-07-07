import json
import random
categ = input(
    'Введите категорию объекта который хотите проанализировать, можно выбрать одну из 3 - cheap, midle, expensive.\nЕсли нажать ENTER то будет проведен усредненный анализ без категории:')
if not categ:
    categ = None
metroObj = [
       {'coords': [55.751432, 37.716621], 'name': 'Авиамоторная', 'area': 'Лефортово', 'densyty': 10387 },
       {'coords': [55.706634, 37.657008], 'name': 'Автозаводская', 'area': 'Даниловский', 'densyty': 7414},
       {'coords': [55.687660, 37.573339], 'name': 'Академическая', 'area': 'Академический', 'densyty': 18736},
       {'coords': [55.752075, 37.609308], 'name': 'Александровский сад', 'area': 'Академический', 'densyty': 18736},
       {'coords': [55.807800, 37.638737], 'name': 'Алексеевская', 'area': 'Алексеевский', 'densyty': 15197},
       {'coords': [55.633490, 37.765678], 'name': 'Алма-Атинская', 'area': 'Братеево', 'densyty': 14393},
       {'coords': [55.898376, 37.587344], 'name': 'Алтуфьево', 'area': 'Бибирево', 'densyty': 24814},
       {'coords': [55.583657, 37.596812], 'name': 'Аннино', 'area': 'Чертаново Южное', 'densyty': 15999},
       {'coords': [55.752516, 37.604116], 'name': 'Арбатская', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.752131, 37.601519], 'name': 'Арбатская', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.800261, 37.532870], 'name': 'Аэропорт', 'area': 'Аэропорт', 'densyty': 17313},
       {'coords': [55.869794, 37.664581], 'name': 'Бабушкинская', 'area': 'Бабушкинский', 'densyty': 17415},
       {'coords': [55.743801, 37.497863], 'name': 'Багратионовская', 'area': 'Филёвский Парк', 'densyty': 9640},
       {'coords': [55.760818, 37.581280], 'name': 'Баррикадная', 'area': 'Филёвский Парк', 'densyty': 9640},
       {'coords': [55.772406, 37.679035], 'name': 'Бауманская', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.773505, 37.545518], 'name': 'Беговая', 'area': 'Хорошевский', 'densyty': 7199},
       {'coords': [55.777170, 37.586194], 'name': 'Белорусская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.777439, 37.582107], 'name': 'Белорусская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.642357, 37.526115], 'name': 'Беляево', 'area': 'Коньково', 'densyty': 21756},
       {'coords': [55.883868, 37.603011], 'name': 'Бибирево', 'area': 'Бибирево', 'densyty': 24814},
       {'coords': [55.752501, 37.611482], 'name': 'Библиотека имени Ленина', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.601188, 37.555328], 'name': 'Битцевский парк', 'area': 'Ясенево', 'densyty': 7010},
       {'coords': [55.633587, 37.743831], 'name': 'Борисово', 'area': 'Братеево', 'densyty': 14393},
       {'coords': [55.750454, 37.609254], 'name': 'Боровицкая', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.844597, 37.637811], 'name': 'Ботанический сад', 'area': 'Ростокино', 'densyty': 11132},
       {'coords': [55.659460, 37.750514], 'name': 'Братиславская', 'area': 'Марьино', 'densyty': 21319},
       {'coords': [55.545207, 37.542329], 'name': 'Бульвар адмирала Ушакова', 'area': 'Южное Бутово', 'densyty': 8143},
       {'coords': [55.569667, 37.577346], 'name': 'Бульвар Дмитрия Донского', 'area': 'Северное Бутово', 'densyty': 10467},
       {'coords': [55.814264, 37.735117], 'name': 'Бульвар Рокоссовского', 'area': 'Богородское', 'densyty': 10558},
       {'coords': [55.537964, 37.515919], 'name': 'Бунинская аллея', 'area': 'Южное Бутово', 'densyty': 8143},
       {'coords': [55.653294, 37.619522], 'name': 'Варшавская', 'area': 'Нагорный', 'densyty': 15064},
       {'coords': [55.821401, 37.641090], 'name': 'ВДНХ', 'area': 'Останкинский', 'densyty': 5068},
       {'coords': [55.847922, 37.590282], 'name': 'Владыкино', 'area': 'Отрадное', 'densyty': 18190},
       {'coords': [55.840209, 37.486616], 'name': 'Водный стадион', 'area': 'Головинский', 'densyty': 11551},
       {'coords': [55.818923, 37.497791], 'name': 'Войковская', 'area': 'Головинский', 'densyty': 11551},
       {'coords': [55.724900, 37.687102], 'name': 'Волгоградский проспект', 'area': 'Южнопортовый', 'densyty': 16419},
       {'coords': [55.690446, 37.754314], 'name': 'Волжская', 'area': 'Люблино', 'densyty': 9876},
       {'coords': [55.835508, 37.382034], 'name': 'Волоколамская', 'area': 'Митино', 'densyty': 15223},
       {'coords': [55.710438, 37.559317], 'name': 'Воробьёвы горы', 'area': 'Гагаринский', 'densyty': 14651},
       {'coords': [55.749547, 37.543021], 'name': 'Выставочная', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.715682, 37.817969], 'name': 'Выхино', 'area': 'Выхино-Жулебино', 'densyty': 15016},
       {'coords': [55.748843, 37.542671], 'name': 'Деловой центр', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.789704, 37.558212], 'name': 'Динамо', 'area': 'Аэропорт', 'densyty': 17313},
       {'coords': [55.807881, 37.580831], 'name': 'Дмитровская', 'area': 'Бутырский', 'densyty': 14090},
       {'coords': [55.729012, 37.622711], 'name': 'Добрынинская', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.610697, 37.717905], 'name': 'Домодедовская', 'area': 'Орехово-Борисово Южное', 'densyty': 21284},
       {'coords': [55.781484, 37.614716], 'name': 'Достоевская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.718070, 37.676259], 'name': 'Дубровка', 'area': 'Южнопортовый', 'densyty': 16419},
       {'coords': [55.684539, 37.855123], 'name': 'Жулебино', 'area': 'Выхино-Жулебино', 'densyty': 15016},
       {'coords': [55.612329, 37.745205], 'name': 'Зябликово', 'area': 'Зябликово', 'densyty': 30387},
       {'coords': [55.787746, 37.781380], 'name': 'Измайловская', 'area': 'Северное Измайлово', 'densyty': 20849},
       {'coords': [55.656682, 37.540075], 'name': 'Калужская', 'area': 'Обручевский', 'densyty': 14012},
       {'coords': [55.636107, 37.656218], 'name': 'Кантемировская', 'area': 'Царицыно', 'densyty': 15298},
       {'coords': [55.653177, 37.598232], 'name': 'Каховская', 'area': 'Зюзино', 'densyty': 23224},
       {'coords': [55.655432, 37.649256], 'name': 'Каширская', 'area': 'Москворечье-Сабурово', 'densyty': 8657},
       {'coords': [55.655432, 37.649256], 'name': 'Каширская', 'area': 'Москворечье-Сабурово', 'densyty': 8657},
       {'coords': [55.744596, 37.567545], 'name': 'Киевская', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.744075, 37.566449], 'name': 'Киевская', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.743117, 37.564132], 'name': 'Киевская', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.756498, 37.631326], 'name': 'Китай-город', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.754360, 37.633877], 'name': 'Китай-город', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.706320, 37.685710], 'name': 'Кожуховская', 'area': 'Южнопортовый', 'densyty': 16419},
       {'coords': [55.677423, 37.663719], 'name': 'Коломенская', 'area': 'Нагатино-Садовники', 'densyty': 10139},
       {'coords': [55.775672, 37.654772], 'name': 'Комсомольская', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.774072, 37.654565], 'name': 'Комсомольская', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.633658, 37.520024], 'name': 'Коньково', 'area': 'Тёплый Стан', 'densyty': 17906},
       {'coords': [55.613717, 37.746355], 'name': 'Красногвардейская', 'area': 'Зябликово', 'densyty': 30387},
       {'coords': [55.760211, 37.577211], 'name': 'Краснопресненская', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.779849, 37.666072], 'name': 'Красносельская', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.768795, 37.648888], 'name': 'Красные ворота', 'area': 'Басманный', 'densyty': 13160},
       {'coords': [55.732464, 37.664788], 'name': 'Крестьянская застава', 'area': 'Таганский', 'densyty': 15099},
       {'coords': [55.745068, 37.603487], 'name': 'Кропоткинская', 'area': 'Хамовники', 'densyty': 10790},
       {'coords': [55.756842, 37.408139], 'name': 'Крылатское', 'area': 'Крылатское', 'densyty': 6860},
       {'coords': [55.761598, 37.623780], 'name': 'Кузнецкий мост', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.705417, 37.765902], 'name': 'Кузьминки', 'area': 'Тверской', 'densyty': 17875},
       {'coords': [55.730877, 37.446874], 'name': 'Кунцевская', 'area': 'Тверской', 'densyty': 9144},
       {'coords': [55.730634, 37.445123], 'name': 'Кунцевская', 'area': 'Тверской', 'densyty': 9144},
       {'coords': [55.758463, 37.660287], 'name': 'Курская', 'area': 'Басманный', 'densyty': 13160},
       {'coords': [55.758640, 37.659155], 'name': 'Курская', 'area': 'Басманный', 'densyty': 13160},
       {'coords': [55.740178, 37.534236], 'name': 'Кутузовская', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.707689, 37.586239], 'name': 'Ленинский проспект', 'area': 'Гагаринский', 'densyty': 14651},
       {'coords': [55.701765, 37.852275], 'name': 'Лермонтовский проспект', 'area': 'Выхино-Жулебино', 'densyty': 15016},
       {'coords': [55.581968, 37.577310], 'name': 'Лесопарковая', 'area': 'Чертаново Южное', 'densyty': 15999},
       {'coords': [55.759162, 37.627346], 'name': 'Лубянка', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.676265, 37.762003], 'name': 'Люблино', 'area': 'Люблино', 'densyty': 9876},
       {'coords': [55.740993, 37.656802], 'name': 'Марксистская', 'area': 'Таганский', 'densyty': 15099},
       {'coords': [55.793723, 37.616180], 'name': 'Марьина роща', 'area': 'Марьина роща', 'densyty': 14395},
       {'coords': [55.649368, 37.744118], 'name': 'Марьино', 'area': 'Марьино', 'densyty': 21319},
       {'coords': [55.769808, 37.596192], 'name': 'Маяковская', 'area': 'Тверской', 'densyty': 9144},
       {'coords': [55.887473, 37.661527], 'name': 'Медведково', 'area': 'Северное Медведково', 'densyty': 22518},
       {'coords': [55.748640, 37.533041], 'name': 'Международная', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.781788, 37.598735], 'name': 'Менделеевская', 'area': 'Тверской', 'densyty': 9144},
       {'coords': [55.846098, 37.361220], 'name': 'Митино', 'area': 'Митино', 'densyty': 15223},
       {'coords': [55.741004, 37.416386], 'name': 'Молодёжная', 'area': 'Кунцева', 'densyty': 9144},
       {'coords': [55.823990, 37.384747], 'name': 'Мякинино', 'area': 'Кунцева', 'densyty': 9144},
       {'coords': [55.683676, 37.623061], 'name': 'Нагатинская', 'area': 'Нагорный', 'densyty': 15064},
       {'coords': [55.672854, 37.610745], 'name': 'Нагорная', 'area': 'Нагорный', 'densyty': 15064},
       {'coords': [55.662379, 37.605274], 'name': 'Нахимовский проспект', 'area': 'Зюзино', 'densyty': 23224},
       {'coords': [55.751675, 37.817295], 'name': 'Новогиреево', 'area': 'Новогиреево', 'densyty': 22108},
       {'coords': [55.745113, 37.864052], 'name': 'Новокосино', 'area': 'ННовокосино', 'densyty': 29902},
       {'coords': [55.742276, 37.629125], 'name': 'Новокузнецкая', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.779565, 37.601421], 'name': 'Новослободская', 'area': 'Тверской', 'densyty': 9144},
       {'coords': [55.601833, 37.553442], 'name': 'Новоясеневская', 'area': 'Ясенево', 'densyty': 7070},
       {'coords': [55.670077, 37.554493], 'name': 'Новые Черёмушки', 'area': 'Черемушки', 'densyty': 19845},
       {'coords': [55.731257, 37.612766], 'name': 'Октябрьская', 'area': 'Якиманка', 'densyty': 5748},
       {'coords': [55.729255, 37.610979], 'name': 'Октябрьская', 'area': 'Якиманка', 'densyty': 5748},
       {'coords': [55.793581, 37.493317], 'name': 'Октябрьское поле', 'area': 'Щукино', 'densyty': 14340},
       {'coords': [55.612690, 37.695214], 'name': 'Орехово', 'area': 'Орехово-Борисово Северное', 'densyty': 17200},
       {'coords': [55.863384, 37.604843], 'name': 'Отрадное', 'area': 'Отрадное', 'densyty': 18190},
       {'coords': [55.756523, 37.615327], 'name': 'Охотный ряд', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.731536, 37.636329], 'name': 'Павелецкая', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.729787, 37.638961], 'name': 'Павелецкая', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.736077, 37.595061], 'name': 'Парк культуры', 'area': 'Хамовники', 'densyty': 10790},
       {'coords': [55.735150, 37.592905], 'name': 'Парк культуры', 'area': 'Хамовники', 'densyty': 10790},
       {'coords': [55.736164, 37.516925], 'name': 'Парк Победы', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.736478, 37.514401], 'name': 'Парк Победы', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.788424, 37.749265], 'name': 'Партизанская', 'area': 'Измайлово', 'densyty': 7004},
       {'coords': [55.794376, 37.799364], 'name': 'Первомайская', 'area': 'Измайлово', 'densyty': 7004},
       {'coords': [55.751320, 37.786887], 'name': 'Перово', 'area': 'Новогиреево', 'densyty': 22108},
       {'coords': [55.836524, 37.575558], 'name': 'Петровско-Разумовская', 'area': 'Тимирязевский', 'densyty': 8019},
       {'coords': [55.692972, 37.728398], 'name': 'Печатники', 'area': 'Печатники', 'densyty': 4832},
       {'coords': [55.735986, 37.467078], 'name': 'Пионерская', 'area': 'Фили-Давыдково', 'densyty': 16510},
       {'coords': [55.860529, 37.436382], 'name': 'Планерная', 'area': 'Северное Тушино', 'densyty': 17581},
       {'coords': [55.747024, 37.680589], 'name': 'Площадь Ильича', 'area': 'Таганский', 'densyty': 15099},
       {'coords': [55.756741, 37.622360], 'name': 'Площадь Революции', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.777201, 37.517895], 'name': 'Полежаевская', 'area': 'Хорошёвский', 'densyty': 7199},
       {'coords': [55.736807, 37.618471], 'name': 'Полянка', 'area': 'Якиманка', 'densyty': 5748},
       {'coords': [55.611577, 37.603972], 'name': 'Пражская', 'area': 'Чертаново Центральное', 'densyty': 17898},
       {'coords': [55.796167, 37.715022], 'name': 'Преображенская площадь', 'area': 'Преображенское', 'densyty': 16046},
       {'coords': [55.731546, 37.666917], 'name': 'Пролетарская', 'area': 'Южнопортовый', 'densyty': 16419},
       {'coords': [55.676910, 37.505831], 'name': 'Проспект Вернадского', 'area': 'Проспект Вернадского', 'densyty': 13677},
       {'coords': [55.781757, 37.633482], 'name': 'Проспект Мира', 'area': 'Мещанский', 'densyty': 13213},
       {'coords': [55.779631, 37.633464], 'name': 'Проспект Мира', 'area': 'Мещанский', 'densyty': 13213},
       {'coords': [55.677671, 37.562595], 'name': 'Профсоюзная', 'area': 'Черёмушки', 'densyty': 19845},
       {'coords': [55.765747, 37.603900], 'name': 'Пушкинская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.855644, 37.354025], 'name': 'Пятницкое шоссе', 'area': 'Митино', 'densyty': 15223},
       {'coords': [55.854891, 37.476231], 'name': 'Речной вокзал', 'area': 'Левобережный', 'densyty': 6744},
       {'coords': [55.792513, 37.636123], 'name': 'Рижская', 'area': 'Мещанский', 'densyty': 13213},
       {'coords': [55.746228, 37.681254], 'name': 'Римская', 'area': 'Мещанский', 'densyty': 13213},
       {'coords': [55.717366, 37.793606], 'name': 'Рязанский проспект', 'area': 'Рязанский', 'densyty': 16574},
       {'coords': [55.793313, 37.588296], 'name': 'Савёловская', 'area': 'Савёловский', 'densyty': 21920},
       {'coords': [55.855558, 37.653379], 'name': 'Свиблово', 'area': 'Свиблово', 'densyty': 14061},
       {'coords': [55.651552, 37.598384], 'name': 'Севастопольская', 'area': 'Зюзино', 'densyty': 23224},
       {'coords': [55.783195, 37.719423], 'name': 'Семёновская', 'area': 'Соколиная Гора', 'densyty': 11618},
       {'coords': [55.726680, 37.625199], 'name': 'Серпуховская', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.729828, 37.472171], 'name': 'Славянский бульвар', 'area': 'Фили-Давыдково', 'densyty': 16510},
       {'coords': [55.749060, 37.581658], 'name': 'Смоленская', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.747642, 37.583841], 'name': 'Смоленская', 'area': 'Арбат', 'densyty': 16838},
       {'coords': [55.805042, 37.514787], 'name': 'Сокол', 'area': 'Аэропорт', 'densyty': 17313},
       {'coords': [55.789198, 37.679700], 'name': 'Сокольники', 'area': 'Сокольники', 'densyty': 5950},
       {'coords': [55.817234, 37.434801], 'name': 'Спартак', 'area': 'Покровское-Стрешнево', 'densyty': 4519},
       {'coords': [55.722761, 37.562227], 'name': 'Спортивная', 'area': 'Хамовники', 'densyty': 10790},
       {'coords': [55.766299, 37.636374], 'name': 'Сретенский бульвар', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.803691, 37.403118], 'name': 'Строгино', 'area': 'Строгино', 'densyty': 9500},
       {'coords': [55.738784, 37.548375], 'name': 'Студенческая', 'area': 'Дорогомилово', 'densyty': 9417},
       {'coords': [55.772315, 37.632332], 'name': 'Сухаревская', 'area': 'Мещанский', 'densyty': 13213},
       {'coords': [55.850510, 37.439787], 'name': 'Сходненская', 'area': 'Южное Тушино', 'densyty': 13725},
       {'coords': [55.742433, 37.653146], 'name': 'Таганская', 'area': 'Таганский', 'densyty': 15099},
       {'coords': [55.739199, 37.653613], 'name': 'Таганская', 'area': 'Таганский', 'densyty': 15099},
       {'coords': [55.764455, 37.605939], 'name': 'Тверская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.758808, 37.617680], 'name': 'Театральная', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.709211, 37.732117], 'name': 'Текстильщики', 'area': 'Текстильщики', 'densyty': 17705},
       {'coords': [55.618730, 37.505912], 'name': 'Тёплый Стан', 'area': 'Ясенево', 'densyty': 7010},
       {'coords': [55.818660, 37.574498], 'name': 'Тимирязевская', 'area': 'Тимирязевский', 'densyty': 8019},
       {'coords': [55.741125, 37.626142], 'name': 'Третьяковская', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.740319, 37.625981], 'name': 'Третьяковская', 'area': 'Замосковречье', 'densyty': 13573},
       {'coords': [55.767939, 37.621902], 'name': 'Трубная', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.708841, 37.622612], 'name': 'Тульская', 'area': 'Даниловский', 'densyty': 7414},
       {'coords': [55.765276, 37.636742], 'name': 'Тургеневская', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.827080, 37.437604], 'name': 'Тушинская', 'area': 'Покровское-Стрешнево', 'densyty': 4519},
       {'coords': [55.764273, 37.561419], 'name': 'Улица 1905 года', 'area': 'Пресненский', 'densyty': 10894},
       {'coords': [55.595883, 37.600675], 'name': 'Улица академика Янгеля', 'area': 'Чертаново Южное', 'densyty': 15999},
       {'coords': [55.541825, 37.531226], 'name': 'Улица Горчакова', 'area': 'Южное Бутово', 'densyty': 8143},
       {'coords': [55.548034, 37.554618], 'name': 'Улица Скобелевская', 'area': 'Южное Бутово', 'densyty': 8143},
       {'coords': [55.568838, 37.576708], 'name': 'Улица Старокачаловская', 'area': 'Северное Бутово', 'densyty': 10467},
       {'coords': [55.692440, 37.534532], 'name': 'Университет', 'area': 'Раменки', 'densyty': 7504},
       {'coords': [55.739519, 37.483328], 'name': 'Филёвский парк', 'area': 'Филёвский парк', 'densyty': 9640},
       {'coords': [55.745970, 37.514949], 'name': 'Фили', 'area': 'Филёвский парк', 'densyty': 9640},
       {'coords': [55.727232, 37.580328], 'name': 'Фрунзенская', 'area': 'Хамовники', 'densyty': 10790},
       {'coords': [55.620982, 37.669612], 'name': 'Царицыно', 'area': 'Царицыно', 'densyty': 15298},
       {'coords': [55.771616, 37.620986], 'name': 'Цветной бульвар', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.802988, 37.744819], 'name': 'Черкизовская', 'area': 'Преображенское', 'densyty': 16046},
       {'coords': [55.640538, 37.606065], 'name': 'Чертановская', 'area': 'Чертаново Северное', 'densyty': 21205},
       {'coords': [55.765843, 37.608167], 'name': 'Чеховская', 'area': 'Тверской', 'densyty': 10660},
       {'coords': [55.764794, 37.638683], 'name': 'Чистые пруды', 'area': 'Красносельский', 'densyty': 9785},
       {'coords': [55.755930, 37.659263], 'name': 'Чкаловская', 'area': 'Басманный', 'densyty': 13160},
       {'coords': [55.718821, 37.607799], 'name': 'Шаболовская', 'area': 'Донской', 'densyty': 9045},
       {'coords': [55.620982, 37.743723], 'name': 'Шипиловская', 'area': 'Зябликово', 'densyty': 30387},
       {'coords': [55.758255, 37.751583], 'name': 'Шоссе Энтузиастов', 'area': 'Соколиная Гора', 'densyty': 11618},
       {'coords': [55.810228, 37.798556], 'name': 'Щёлковская', 'area': 'Северное Измайлово', 'densyty': 20849},
       {'coords': [55.808827, 37.463772], 'name': 'Щукинская', 'area': 'Щукино', 'densyty': 14340},
       {'coords': [55.782066, 37.705284], 'name': 'Электрозаводская', 'area': 'Басманный', 'densyty': 13160},
       {'coords': [55.663146, 37.482852], 'name': 'Юго-Западная', 'area': 'Тропарёво-Никулино', 'densyty': 10956},
       {'coords': [55.622436, 37.609047], 'name': 'Южная', 'area': 'Чертаново Северное', 'densyty': 21205},
       {'coords': [55.606182, 37.533400], 'name': 'Ясенево', 'area': 'Ясенево', 'densyty': 7010}
]

from geopy.distance import geodesic
from itertools import count, takewhile
import random
from statistics import mean
from pprint import pprint
import pandas as pd
import json
import requests
from lxml import html
from pprint import pprint
import random
from statistics import mean
import time
from tqdm import tqdm
# origin = (30.172705, 31.526725)  # (latitude, longitude) don't confuse
revenue_list = random.sample(range(3000, 500000), 2000)

with open("files/ostanovk.json", "r") as read_file:
    data_ost = json.load(read_file)

list_coor = []
vaq_coor = {}
list_ostanovok = []
# print(data)
for i in data_ost:
    list_coor = [float(i["Latitude_WGS84"]), float(i["Longitude_WGS84"])]
    vaq_coor = {'ostanov_name': i['StationName'], 'coords' : list_coor}
    list_ostanovok.append(vaq_coor)

def get_tretty_num(revenue_list):
    new_list = []
    for i in revenue_list:
        i = '{0:,}'.format(i).replace(',', ' ')
        i = f'{i} тыс. руб. в год'
        new_list.append(i)
    return new_list
revenue_list = get_tretty_num(revenue_list)
def get_status(i):
    # if any(item in it for it in collections):
    coll_exp = ['Челюстно-лицевая хирургия', 'Услуги косметолога', 'SPA']
    coll_cheap = ['Больницы', 'Взрослые поликлиники', 'Детские поликлиники']
    if any(ext in i['Подрубрика'] for ext in coll_exp):
        category = 'expensive'
    elif any(ext in i['Подрубрика'] for ext in coll_cheap):
        category = 'cheap'
    else:
        category = 'midle'
    return category

def prep_data(data):
    coords = {}
    new_data = []
    for i in tqdm(data):
        # del i['icq']
        # del i['odnoklassniki']
        # del i['instagram']
        # del i['youtube']
        # del i['Регион']
        # del i['Город']
        # del i['Район']
        # del i['Индекс']
        del i['ID']
        # del i['Телефон']
        # del i['Мобильный телефон']
        # del i['Email']
        # del i['Email с сайта']
        # del i['Сайт']
        # del i['Рубрика']
        # del i['Подрубрика']
        # del i['Способы оплаты']
        # del i['vkontakte']
        # del i['twitter']
        # del i['facebook']
        # del i['skype']
        a = i['latitude']
        b = i['longitude']
        coords['coord'] = [a,b]

        i['coordinates'] = coords['coord']
        i['date_start_statistic'] = '09.02.2020'
        i['status'] = 'old'
        i['category'] = get_status(i)
        i['revenue'] = random.choice(revenue_list)
        # coords.clear()
        # del i['latitude']
        # del i['longitude']
        new_data.append(i)
        time.sleep(0.000000000000001)
    return new_data

""" Вспомогательные функции"""
def plusobj(a, b):
    return a + b

def plusing(a, b):
    ll = {}
    for i in a:
        l = list(map(lambda x: plusobj(x, i), b))
        ll[i] = sorted(l)[0]
    return ll

""" Функция генерация массива дробных координат"""
def frange(start, stop, step):
       return takewhile(lambda x: x< stop, count(start, step))
# print(list(frange(0.5, 50, 0.005)))
""" функция получения новых координат точек по широте """
def get_new_coordinates_lat(a,b, step):
       latitude_list = list(frange(a, b, step))
       return latitude_list
def get_new_coordinates_long(a,b, step):
       longitude_list = list(frange(a, b, step))
       return longitude_list

# """Функция по получению массива координат в рамках координат"""
def get_new_spisok_coordinat(get_new_coordinates_lat, get_new_coordinates_long):
       list = []
       for i in get_new_coordinates_lat:
              for j in get_new_coordinates_long:
                     list.append((i,j))
       return list

""" Функция по нахождению расстояния между новой точкой и метро"""
# # origin = (30.172705, 31.526725)  # (latitude, longitude) don't confuse
def distance_new_point_metro(a, b):
    a = tuple(a)
    b = tuple(b)
    return geodesic(a, b).meters

# """ Функция по нахождению расстоянию между двумя точками """
def distance_point_metro(a, b):
    a = tuple(a)
    b = tuple(b)
    return geodesic(a, b).meters

def distance_point_point(a, b):
    a = tuple(a)
    b = tuple(b)
    return geodesic(a, b).meters
# # print(distance_point_point([30.172705, 31.526725], [30.288281, 31.732326]))

def get_all_coord(list):
    l = []
    for i in list:
        l.append(i['coordinates'])
    return l
# """Добавление в json словарь данных по ближайшему конкуренту"""
def get_closer_conquer(list_all):
    new_list_all = []
    for i in tqdm(list_all):
        lll = get_all_coord(list_all.copy())
        multiple = i['coordinates']
        l = sorted(list(map(lambda x: distance_point_point(x, multiple), lll)))[1]
        i['dist_to_closest_conquer'] = l
        new_list_all.append(i)
        time.sleep(0.00000000000000000000001)
        # break # Убрать загрушку на ночь чтобы все прогрузилось """
    return new_list_all


""" Две функции по сокращению времени расчетов"""
def lambda_high_h(multiple, data_house):
    massive_list = []
    for i in data_house:
        massive_list.append(i.get('coords'))
    res = list(map(lambda x: distance_point_metro(multiple, x), massive_list))
    return res
def lambda_high_new(multiple, massive):
    massive_list = []
    for i in massive:
        massive_list.append(i['coordinates'])
    res = list(map(lambda x: distance_point_metro(multiple, x), massive_list))
    return res
def lambda_high_ost(multiple, massive):
    massive_list = []
    for i in massive:
        massive_list.append(i['coords'])
    res = list(map(lambda x: distance_point_metro(multiple, x), massive_list))
    return res
""" вверху 2 функции по сокращению времени расчетов"""

def get_closer_metro_info(list_all):
    vaq2 = {}
    vaq_zag= {}
    nn_list_all = []
    for i in tqdm(list_all):
           multiple = i['coordinates']
           res = lambda_high(multiple, metroObj)
           re_sort = sorted(res)
           res_info = re_sort[0]
           res_ind = res.index(res_info)
           res_ost = lambda_high_ost(multiple, list_ostanovok)
           res_sort = sorted(res_ost)
           res_info_ost = res_sort[0]
           res_ost_ind = res_ost.index(res_info_ost)
           i['dist_to_closer_metro'] = res_info
           i['metro_name'] = metroObj[res_ind]['name']
           i['close_metro_coords'] = metroObj[res_ind]['coords']
           i['closer_metro_area'] = metroObj[res_ind]['area']
           i['closer_metro_area_densyty'] = metroObj[res_ind]['densyty']
           i['dist_to_closer_ostanovk'] = res_info_ost
           i['ostanovka_transp'] = list_ostanovok[res_ost_ind]['ostanov_name']
           i['ostanovka_coord'] = list_ostanovok[res_ost_ind]['coords']
           time.sleep(0.000000001)
                  # break  # Убрать загрушку на ночь чтобы все прогрузилось """
           nn_list_all.append(i)
           time.sleep(0.00000000000000000000001)
    return nn_list_all

""" Функция нахождение ближайшего метро для новой точки"""
def get_closer_metro_info_p(list_all):
    vaq2 = {}
    # vaq_zag= {}
    nn_list_all = []
    for i in tqdm(list_all):
           multiple = i
           res = lambda_high(multiple, metroObj)
           re_sort = sorted(res)
           res_info = re_sort[0]
           res_ind = res.index(res_info)
           res_ost = lambda_high_ost(multiple, list_ostanovok)
           res_sort = sorted(res_ost)
           res_info_ost = res_sort[0]
           res_ost_ind = res_ost.index(res_info_ost)
           vaq2 = {'coordinates': multiple, 'dist_to_closer_metro': res_info, 'metro_name': metroObj[res_ind]['name'],
                   'close_metro_coords': metroObj[res_ind]['coords'], 'closer_metro_area': metroObj[res_ind]['area'], \
                   'closer_metro_area_densyty': metroObj[res_ind]['densyty'], 'dist_to_closer_ostanovk': res_info_ost,
                   'ostanovka_transp': list_ostanovok[res_ost_ind]['ostanov_name'], \
                   'ostanovka_coord': list_ostanovok[res_ost_ind]['coords']}
           nn_list_all.append(vaq2)
           time.sleep(0.00000000000000000000001)
    return nn_list_all


def get_square(list_all):
    new_list = []
    for i in tqdm(list_all):
        rad = i['dist_to_closest_conquer']
        square = 3.14*rad*rad
        chisl = i['closer_metro_area_densyty']*square/1000000
        i['square'] = square
        i['chisl'] = chisl
        new_list.append(i)
        time.sleep(0.0000000000000000000000001)
        # break  # Убрать загрушку на ночь чтобы все прогрузилось """
    return new_list

# """ Функция получения среднего значения расстояния до ближайшего конкурента, метро, и плотности населения в радиусе"""
def get_midle_list_info(list_all, categ=None):
    dist_to_closest_conquer = []
    dist_to_closer_metro = []
    chisl = []
    if categ is not None:
        for i in tqdm(list_all):
            if i['category'] == categ:
               dist_to_closest_conquer.append(i['dist_to_closest_conquer'])
               dist_to_closer_metro.append(i['dist_to_closer_metro'])
               chisl.append(i['chisl'])
               time.sleep(0.00000000000000000000001)
            else:
               dist_to_closest_conquer.append(i['dist_to_closest_conquer'])
               dist_to_closer_metro.append(i['dist_to_closer_metro'])
               chisl.append(i['chisl'])
               time.sleep(0.00000000000000000000001)
    else:
        for i in tqdm(list_all):
            dist_to_closest_conquer.append(i['dist_to_closest_conquer'])
            dist_to_closer_metro.append(i['dist_to_closer_metro'])
            chisl.append(i['chisl'])
            time.sleep(0.00000000000000000000001)
    dist_to_closest_conquer_mean = mean(dist_to_closest_conquer)
    dist_to_closer_metro_mean = mean(dist_to_closer_metro)
    chisl_mean = mean(chisl)
    return dist_to_closest_conquer_mean, dist_to_closer_metro_mean, chisl_mean

# """ Функция получения массива из новых координат и информации по ним"""
def get_dots_all_info(new_coords_list, list_all):
    vaq2 = {}
    nn_list_all = []
    status = 'new'
    # category = category
    for i in tqdm(new_coords_list):
        multiple = i['coordinates']
        time.sleep(0.00000000000000000000001)
        res = lambda_high_new(multiple, list_all)
        sort_res = sorted(res)[0]
        res_ind = res.index(sort_res)
        res_info = sort_res
        population_before_conq = res_info * res_info * 3.14 * list_all[res_ind][
            'closer_metro_area_densyty'] / 1000000
        dist_to_closest_conquer_mean, dist_to_closer_metro_mean, chisl_mean = get_midle_list_info(list_all, categ)
        dist_to_conquer_aprise = 'good' if res_info > dist_to_closest_conquer_mean*1.2 else 'bad'
        dist_to_closer_metro_aprise = 'good' if i['dist_to_closer_metro']/1.2 < dist_to_closer_metro_mean else 'bad'
        chisl_apprise = 'good' if population_before_conq > chisl_mean*1.2 else 'bad'
        dist_to_close_ost_apr = 'good' if i['dist_to_closer_ostanovk'] <= float(600) else 'bad'
        # новое
        i['dist_to_closest_conquer'] = res_info
        i['dist_to_close_ost_apr'] = dist_to_close_ost_apr
        i['dist_to_conquer_aprise']= dist_to_conquer_aprise
        i['dist_to_closer_metro_aprise'] = dist_to_closer_metro_aprise
        i['chisl_before_conquer_apprise'] = chisl_apprise
        i['status'] = status
        i['date_start_statistic'] = '09.02.2021'
        i['latitude'] = multiple[0]
        i['longitude'] = multiple[1]
        i['chisl'] = population_before_conq
        i['category'] = categ
        print(new_coords_list.index(i))
        print((len(new_coords_list) - new_coords_list.index(i)) / len(new_coords_list) * 100)
        nn_list_all.append(i)
    return nn_list_all
# #

# #
""" Функция получения итогового списка координат по условиям"""
def get_itog_dots_list_with_options(list):
    itog_dots = []
    itog_dots_point = []
    for i in list:
        if i.get("chisl_before_conquer_apprise") == 'good' and i.get('dist_to_conquer_aprise') == 'good' and i.get('dist_to_closer_metro_aprise')\
            and i.get('dist_to_close_ost_apr') == 'good':
            itog_dots.append(i)
            # itog_dots_point.append(i['coordinates'])
            print(len(list))
            print((len(list)-list.index(i))/len(list)*100)
        elif i.get('status')=='old':
            itog_dots.append(i)
        else:
            continue
        # time.sleep(0.0000000000000000000000000001)
    return itog_dots

""" объединение 2 списков первоначального и новых координат"""
def get_one_list_from_twoe(list_all, itog_list_coords):
    for i in tqdm(itog_list_coords):
        list_all.append(i)
        time.sleep(0.00000000000000000000000000001)
    return list_all

#


def get_dots_all_info_one_point(input_coord_list, list_all):
    vaq2 = {}
    nn_list_all = []
    status = 'new'
    # for i in tqdm(input_coord_list):
    multiple = input_coord_list
    time.sleep(0.00000000000000000000001)


    res = lambda_high_new(multiple, list_all)
    res_ind = res.index(sorted(res)[0])
    res_info = sorted(res)[0]
    dist_metro = distance_point_metro(multiple, list_all[res_ind]['close_metro_coords'])
    # dist_metro = distance_new_point_metro(multiple, list_all[res_ind]['metro_info']['close_metro_coords'])
    population_before_conq = res_info * res_info * 3.14 * list_all[res_ind][
        'closer_metro_area_densyty'] / 1000000

    dist_to_closest_conquer_mean, dist_to_closer_metro_mean, chisl_mean = get_midle_list_info(list_all, categ)
    dist_to_conquer_aprise = 'good' if res_info > dist_to_closest_conquer_mean else 'bad'
    dist_to_closer_metro_aprise = 'good' if dist_metro < dist_to_closer_metro_mean else 'bad'
    chisl_apprise = 'good' if population_before_conq > chisl_mean else 'bad'
    ### Добавил ID


    vaq2 = {
    'Email': '',
    'Email с сайта': '',
    'category': categ,
    'chisl': chisl_apprise,
    'close_metro_coords': list_all[res_ind]['close_metro_coords'],
    'closer_metro_area': list_all[res_ind]['closer_metro_area'],
    'closer_metro_area_densyty': list_all[res_ind]['closer_metro_area_densyty'],
    'coordinates': multiple,
    'date_start_statistic': '09.02.2021',
    'dist_to_closer_metro': dist_metro, 'population_before_conq': population_before_conq,
    'dist_to_closest_conquer': res_info,
    'facebook': '',
    'icq': '',
    'instagram': '',
    'latitude': multiple[0],
    'longitude': multiple[1],
    'metro_name': list_all[res_ind]['metro_name'],
    'odnoklassniki': '',
    'revenue': '',
    'skype': '',
    'square': '',
    'status': 'new',
    'twitter': '',
    'vkontakte': '',
    'youtube': '',
    'Адрес': '',
    'Город': 'Москва',
    'Индекс': '',
    'Мобильный телефон': '',
    'Название': '',
    'Подрубрика': '',
    'Район': '',
    'Регион': '',
    'Рубрика': '',
    'Сайт': '',
    'Способы оплаты': '',
    'Телефон': '',
    'dist_to_conquer_aprise' : dist_to_conquer_aprise,
    'chisl_apprise': chisl_apprise,
    'dist_to_closer_metro_aprise': dist_to_closer_metro_aprise
    }

    list_all.append(vaq2)
    return list_all
def get_distances_less_then_need(res, dist, data_house):
    dist_list= []
    dist_sum = []
    dist_vaq = {}
    for i in res:
        if i<dist:
            ind = res.index(i)
            people = data_house[ind]['Зарегистрировано жителей']
            # people = str(people).replace(' ', '')
            dist_vaq = {'dist': i, 'colich_pupl': people}
            dist_list.append(dist_vaq)
            dist_sum.append(float(people))
        else:
            continue
    return dist_list, float(sum([float(i) for i in dist_sum]))

def get_info_oldp_house(data_house, data_point, dist, dist_two_km):
    for i in tqdm(data_point):
           multiple = i.get('coordinates')
           res = lambda_high_h(multiple, data_house)
           # i['информация по домам в радиусе до конкурента'] = get_distances_less_then_need(res,dist,data_house)[0]
           i['количество жителей в радиусе до конкурента методом домов'] = get_distances_less_then_need(res,dist,data_house)[1]
           i['количество жителей в радиусе 2 км методом домов'] =  get_distances_less_then_need(res,dist_two_km,data_house)[1]
           time.sleep(0.00000000000000000000001)

    return data_point

def get_conquer_qantity(data_point, dist_two_km):
    count = 0
    lll = get_all_coord(data_point)
    for i in data_point:
        multiple = i.get('coordinates')
        # lll = get_all_coord(data_point)
        l = list(map(lambda x: distance_point_point(x, multiple), lll))
        for j in l:
            if j < dist_two_km:
                count +=1
            else:
                continue
        numbers = count
        i['население на 1 конкурента в радиусе 2 км методом по домам'] = i.get('количество жителей в радиусе 2 км методом домов')/numbers if numbers >=1 else i.get('количество жителей в радиусе 2 км методом домов')
        i['количество конкурентов в радиусе 2 км'] = count
        """ расчет метрик от плотности населения """
        i['население на 1 конкурента в радиусе 2 км методом плотности'] = (i['chisl']*3.14*2000*2000/1000000)/numbers if numbers >=1 else (i['chisl']*3.14*2000*2000/1000000)

        count = 0
    return data_point











































# l=[]
# v = {}
# m = []
# a = [1,7,2,17,8]
# b = [8,9,8,4]
# def multi(a,b):
#     return a+b
# # for i in range(len(a)):
# #     for j in range(len(b)):
# #         res = multi(a[i], b[j])
# #         res = list(map(lambda x: multi(a[i],x), b))
# #
# #         l.append(res)
# #         v[a[i]] = l
# #     m.append(v)
# # print(m)
#
# for i in a:
#     for j in b:
#         res = multi(i, j)
#         res = sorted(list(map(lambda x: multi(i,x), b)))[0]
#         v[i] = res
# m.append(v)
# print(m)