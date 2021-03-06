from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class UserAccountManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('Email address must be provided')
#
#         if not password:
#             raise ValueError('Password must be provided')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields['is_staff'] = True
#         extra_fields['is_superuser'] = True
#         extra_fields['is_active'] = True
#
#         return self._create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     REQUIRED_FIELDS = ['phone_number', 'first_name', 'last_name']
#     USERNAME_FIELD = 'email'
#
#     SEX_CHOICE = ((0, 'Мужской'), (1, 'Женский'))
#     GOV_CHOICE = (
#         (0, 'Россия'), (1, 'Украина'), (2, 'Абхазия'), (3, 'Австралия'), (4, 'Австрия'), (5, 'Азербайджан'),
#         (6, 'Албания'),
#         (7, 'Алжир'), (8, 'Ангола'), (9, 'Ангилья'), (10, 'Андорра'), (11, 'Антигуа и Барбуда'),
#         (12, 'Антильские о-ва'),
#         (13, 'Аргентина'), (14, 'Армения'), (15, 'Арулько'), (16, 'Афганистан'), (17, 'Багамские о-ва'),
#         (18, 'Бангладеш'),
#         (19, 'Барбадос'), (20, 'Бахрейн'), (21, 'Беларусь'), (22, 'Белиз'), (23, 'Бельгия'), (24, 'Бенин'),
#         (25, 'Бермуды'),
#         (26, 'Болгария'), (27, 'Боливия'), (28, 'Босния/Герцеговина'), (29, 'Ботсвана'), (30, 'Бразилия'),
#         (31, 'Британские Виргинские о-ва'), (32, 'Бруней'), (33, 'Буркина Фасо'), (34, 'Бурунди'), (35, 'Бутан'),
#         (36, 'Валлис и Футуна о-ва'), (37, 'Вануату'), (38, 'Великобритания'), (39, 'Венгрия'), (40, 'Венесуэла'),
#         (41, 'Восточный Тимор'), (42, 'Вьетнам'), (43, 'Габон'), (44, 'Гаити'), (45, 'Гайана'), (46, 'Гамбия'),
#         (47, 'Гана'), (48, 'Гваделупа'), (49, 'Гватемала'), (50, 'Гвинея'), (51, 'Гвинея-Бисау'), (52, 'Германия'),
#         (53, 'Гернси о-в'), (54, 'Гибралтар'), (55, 'Гондурас'), (56, 'Гонконг'), (57, 'Гренада'), (58, 'Гренландия'),
#         (59, 'Греция'), (60, 'Грузия'), (61, 'Дания'), (62, 'Джерси о-в'), (63, 'Джибути'),
#         (64, 'Доминиканская республика'), (65, 'Египет'), (66, 'Замбия'), (67, 'Западная Сахара'), (68, 'Зимбабве'),
#         (69, 'Израиль'), (70, 'Индия'), (71, 'Индонезия'), (72, 'Иордания'), (73, 'Ирак'), (74, 'Иран'),
#         (75, 'Ирландия'),
#         (76, 'Исландия'), (77, 'Испания'), (78, 'Италия'), (79, 'Йемен'), (80, 'Кабо-Верде'), (81, 'Казахстан'),
#         (82, 'Камбоджа'), (83, 'Камерун'), (84, 'Канада'), (85, 'Катар'), (86, 'Кения'), (87, 'Кипр'), (88, 'Кирибати'),
#         (89, 'Китай'), (90, 'Колумбия'), (91, 'Коморские о-ва'), (92, 'Конго (Brazzaville)'), (93, 'Конго (Kinshasa)'),
#         (94, 'Коста-Рика'), (95, 'Кот-д`Ивуар'), (96, 'Куба'), (97, 'Кувейт'), (98, 'Кука о-ва'), (99, 'Кыргызстан'),
#         (100, 'Лаос'), (101, 'Латвия'), (102, 'Лесото'), (103, 'Либерия'), (104, 'Ливан'), (105, 'Ливия'),
#         (106, 'Литва'),
#         (107, 'Лихтенштейн'), (108, 'Люксембург'), (109, 'Маврикий'), (110, 'Мавритания'), (111, 'Мадагаскар'),
#         (112, 'Македония'), (113, 'Малави'), (114, 'Малайзия'), (115, 'Мали'), (116, 'Мальдивские о-ва'),
#         (117, 'Мальта'),
#         (118, 'Мартиника о-в'), (119, 'Мексика'), (120, 'Мозамбик'), (121, 'Молдова'), (122, 'Монако'),
#         (123, 'Монголия'),
#         (124, 'Марокко'), (125, 'Мьянма (Бирма)'), (126, 'Мэн о-в'), (127, 'Намибия'), (128, 'Науру'), (129, 'Непал'),
#         (130, 'Нигер'), (131, 'Нигерия'), (132, 'Нидерланды (Голландия)'), (133, 'Никарагуа'), (134, 'Новая Зеландия'),
#         (135, 'Новая Каледония о-в'), (136, 'Норвегия'), (137, 'Норфолк о-в'), (138, 'О.А.Э.'), (139, 'Оман'),
#         (140, 'Пакистан'), (141, 'Панама'), (142, 'Папуа Новая Гвинея'), (143, 'Парагвай'), (144, 'Перу'),
#         (145, 'Питкэрн о-в'), (146, 'Польша'), (147, 'Португалия'), (148, 'Пуэрто Рико'), (149, 'Реюньон'),
#         (150, 'Руанда'),
#         (151, 'Румыния'), (152, 'США'), (153, 'Сальвадор'), (154, 'Самоа'), (155, 'Сан-Марино'),
#         (156, 'Сан-Томе и Принсипи'), (157, 'Саудовская Аравия'), (158, 'Свазиленд'), (159, 'Святая Люсия'),
#         (160, 'Святой Елены о-в'), (161, 'Северная Корея'), (162, 'Сейшеллы'), (163, 'Сен-Пьер и Микелон'),
#         (164, 'Сенегал'), (165, 'Сент Китс и Невис'), (166, 'Сент-Винсент и Гренадины'), (167, 'Сербия'),
#         (168, 'Сингапур'),
#         (169, 'Сирия'), (170, 'Словакия'), (171, 'Словения'), (172, 'Соломоновы о-ва'), (173, 'Сомали'), (174, 'Судан'),
#         (175, 'Суринам'), (176, 'Сьерра-Леоне'), (177, 'Таджикистан'), (178, 'Тайвань'), (179, 'Таиланд'),
#         (180, 'Танзания'), (181, 'Того'), (182, 'Токелау о-ва'), (183, 'Тонга'), (184, 'Тринидад и Тобаго'),
#         (185, 'Тувалу'), (186, 'Тунис'), (187, 'Туркменистан'), (188, 'Туркс и Кейкос'), (189, 'Турция'),
#         (190, 'Уганда'),
#         (191, 'Узбекистан'), (192, 'Уругвай'), (193, 'Фарерские о-ва'), (194, 'Фиджи'), (195, 'Филиппины'),
#         (196, 'Финляндия'), (197, 'Франция'), (198, 'Французская Гвинея'), (199, 'Французская Полинезия'),
#         (200, 'Хорватия'), (201, 'Чад'), (202, 'Черногория'), (203, 'Чехия'), (204, 'Чили'), (205, 'Швейцария'),
#         (206, 'Швеция'), (207, 'Шри-Ланка'), (208, 'Эквадор'), (209, 'Экваториальная Гвинея'), (210, 'Эритрея'),
#         (211, 'Эстония'), (212, 'Эфиопия'), (213, 'ЮАР'), (214, 'Южная Корея'), (215, 'Южная Осетия'), (216, 'Ямайка'),
#         (217, 'Япония'))
#
#     objects = UserAccountManager()
#
#     email = models.EmailField('email', unique=True, blank=False, null=False)
#     phone_number = models.CharField(unique=True, verbose_name='Номер телефона', max_length=100)
#     first_name = models.CharField(verbose_name='Имя', max_length=100)
#     last_name = models.CharField(verbose_name='Фамилия', max_length=100)
#     patronymic = models.CharField(blank=True, null=True, verbose_name='Отчество', max_length=100)
#     sex = models.IntegerField(choices=SEX_CHOICE, default=0, verbose_name='Пол')
#     resident = models.IntegerField(choices=GOV_CHOICE, default=0, verbose_name='Страна резиденства')
#     inn = models.CharField(blank=True, null=True, verbose_name='ИНН', help_text='Только для резидентов РФ',
#                            max_length=100)
#     photo = models.ImageField(blank=True, null=True, verbose_name='Фотография пользователя')
#     contacts = models.CharField(blank=True, verbose_name='Контакты', max_length=100)
#     is_staff = models.BooleanField('staff status', default=False)
#     is_active = models.BooleanField('active', default=False)
#
#     def get_short_name(self):
#         return self.first_name
#
#     def get_full_name(self):
#         return self.first_name + self.last_name
#
#     def __str__(self):
#         return self.email
