from random import randint

from _datetime import datetime


class Feed:

    def __init__(self, header, text):
        self.ending = ''
        self.header = header
        self.text = text

    def post(self):
        with open('feed.txt', 'a') as file:
            file.write(self.__get_header() + '\n')
            file.write(self.text + '\n')
            file.write(self.ending + '\n')
            file.write('\n')

    def _set_ending(self, ending):
        self.ending = ending

    def __get_header(self):
        return self.header + ' ' + '-' * (30 - len(self.header))


class News(Feed):

    def __init__(self, text, city):
        super().__init__('News', text)
        self.city = city

    def post(self):
        post_datetime = datetime.now().strftime("%Y-%m-%d %H.%M")
        super()._set_ending(self.city + ', ' + post_datetime)
        super().post()


class PrivateAdd(Feed):

    def __init__(self, text, expiration_date):
        super().__init__('Private Ad', text)
        self.date_format = '%Y-%m-%d'
        self.expiration_date = self.__validate_expiration_date(expiration_date)

    def post(self):
        now = datetime.now()
        if self.expiration_date < now:
            super()._set_ending('news are expired')
        else:
            days_left = (self.expiration_date - now).days
            if days_left == 0:
                days_left = 'news expire today'
            elif days_left == 1:
                days_left = '1 day left'
            else:
                days_left = str(days_left) + ' days left'
            super()._set_ending(f"Actual until: {self.expiration_date.strftime(self.date_format)}, {days_left}")
        super().post()

    def __validate_expiration_date(self, date_to_validate):
        try:
            return datetime.strptime(date_to_validate, self.date_format)
        except ValueError:
            print('Date is not valid')
            return ''  # no re-input for invalid date


class Weather(Feed):

    def __init__(self, text):
        super().__init__('Weather', text)
        self.precipitation_chance = randint(0, 100)

    def post(self):
        super()._set_ending(f"Precipitation chance: {self.precipitation_chance}%")
        super().post()


while (True):
    print('-------------------')
    print('Select feed type to add:')
    print('1 - News')
    print('2 - Private Ad')
    print('3 - Weather')

    user_input = input()
    if user_input not in ('1', '2', '3'):
        print('>>>Input is incorrect<<<')
        continue

    text = input('Enter text: ')
    if user_input == '1':
        city = input('Enter city: ')
        News(text, city).post()
    elif user_input == '2':
        expiration_date = input('Enter expiration date (yyyy-mm-dd): ')
        PrivateAdd(text, expiration_date).post()
    elif user_input == '3':
        Weather(text).post()
