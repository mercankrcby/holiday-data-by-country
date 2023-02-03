# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
from datetime import date
import holidays
import datetime as dt
from workalendar.europe import Germany
from workalendar.europe import Switzerland
from workalendar.europe import Finland
from workalendar.europe import Sweden
from workalendar.europe import Cyprus
from workalendar.europe import Denmark
from workalendar.europe import Spain
from workalendar.europe import France
from workalendar.europe import Estonia
from workalendar.europe import Netherlands
from workalendar.europe import Italy
from workalendar.europe import Norway
from workalendar.europe import Belgium
from workalendar.europe import Lithuania
from workalendar.europe import Malta
from workalendar.europe import Hungary
from workalendar.europe import Romania
from workalendar.europe import Austria
from workalendar.europe import Slovenia
from workalendar.europe import UnitedKingdom
from workalendar.europe import Bulgaria


def weatherData():


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # USING holidays API FOR GETTING HOLIDAYS FOR GERMANY



    dt.date.today().isoweekday() == 1

    'FR', 'CH', 'no_country_name', 'FI', 'SE', 'CY', 'DK', 'ES', 'DE',
    'EE', 'NL', 'IT', 'NO', 'BE', 'LV', 'MT', 'HU', 'RO', 'AT', 'SI',
    'GB', 'BG'
    years = [2023]
    holiday_list = []
    country_code = []
    country_name = []

    df_all_country = pd.DataFrame(columns=['date', 'holiday', 'HolidayNameEng', 'CountryName', 'Country'])

    ##GERMANY
    for holiday in holidays.Germany(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('DE')
        country_name.append('Germany')

    holidays_df = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
    de_calendar = Germany()

    # de_calendar.is_working_day(date(2020, 1, 1))

    holidays_2023_df = pd.DataFrame(de_calendar.holidays(2023),
                                    columns=["date", "holiday"])

    ## monday = holidays_2023_df['date'].dt.day_name()

    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])

    holidays_df['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df['CountryName'] = country_name
    holidays_df['Country'] = country_code

    dw_mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    holidays_df['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'

    print("Holidays Data Frame -germany \n", holidays_df);

    # df_all_country = pandas.concat(holidays_df)
    ##GERMANY

    ##SWITZERLAND

    holiday_list.clear()
    country_code.clear()
    country_name.clear()
    for holiday in holidays.Switzerland(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('CH')
        country_name.append('Switzerland')

    holidays_df_ch = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
    ch_calendar = Switzerland()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])

    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])

    holidays_df_ch['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_ch['CountryName'] = country_name
    holidays_df_ch['Country'] = country_code

    holidays_df_ch['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'

    # print("Switzerland", holidays_2023_df['date'].dt.weekday.map(dw_mapping))
    #
    # if holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Monday':
    #     holidays_df_ch['IsThursday'] = 1
    # else:
    #     holidays_df_ch['IsThursday'] = 0

    df_all_country = pd.concat([holidays_df, holidays_df_ch])
    ##SWITZERLAND

    ##FINLAND

    holiday_list.clear()
    country_code.clear()
    country_name.clear()
    for holiday in holidays.Finland(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('FI')
        country_name.append('Finland')

    holidays_df_fi = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
    ch_calendar = Finland()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])

    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])

    holidays_df_fi['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_fi['CountryName'] = country_name
    holidays_df_fi['Country'] = country_code
    holidays_df_fi['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - finland \n", holidays_df_fi);
    df_all_country = pd.concat([df_all_country, holidays_df_fi])
    ##FINLAND

    ##SWEDEN
    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Sweden(2022).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('SE')
        country_name.append('Sweden')

    if len(holiday_list) > 0:
        holidays_df_se = pd.DataFrame(holiday_list, columns=["date", "holiday"])

        # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
        ch_calendar = Sweden()
        holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                        columns=["date", "holiday"])

        holidays_df_se['HolidayNameEng'] = holidays_2023_df["holiday"]
        holidays_df_se['CountryName'] = country_name
        holidays_df_se['Country'] = country_code
        print("Holidays Data Frame - sweden \n", holidays_df_se);
        df_all_country = pd.concat([df_all_country, holidays_df_se])

        print("Concat version \n", df_all_country)

    ch_calendar = Sweden()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_se = pd.DataFrame(holiday_list, columns=["date", "holiday"])
    date = []
    holiday_name_ing = []
    print("holidays_2023_df", holidays_2023_df)
    for index, holiday in holidays_2023_df.iterrows():
        print("Holiday Detail", holiday['date'])
        # holiday_list.append(holidays_2023_df[holiday])
        date.append(holiday['date'])
        holiday_name_ing.append(holiday['holiday'])
        country_code.append('SE')
        country_name.append('Sweden')

    print("holiday list", holiday_list)

    holidays_df_se['date'] = date
    holidays_df_se['HolidayNameEng'] = holiday_name_ing
    holidays_df_se['CountryName'] = country_name
    holidays_df_se['Country'] = country_code
    holidays_df_se['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - sweden \n", holidays_df_se);
    df_all_country = pd.concat([df_all_country, holidays_df_se])
    print("Holidays 2023 df", holidays_2023_df)
    ##SWEDEN

    ##CYPRUS

    holiday_list.clear()
    country_code.clear()
    country_name.clear()
    for holiday in holidays.Cyprus(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('CY')
        country_name.append('Cyprus')

    holidays_df_cy = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
    ch_calendar = Cyprus()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_cy['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_cy['CountryName'] = country_name
    holidays_df_cy['Country'] = country_code
    holidays_df_cy['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - cyprus \n", holidays_df_cy);
    df_all_country = pd.concat([df_all_country, holidays_df_cy])
    ##CYPRUS

    ##DENMARK

    holiday_list.clear()
    country_code.clear()
    country_name.clear()
    for holiday in holidays.Denmark(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('DK')
        country_name.append('Denmark')

    holidays_df_dk = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR GERMANY
    ch_calendar = Denmark()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])

    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_dk['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_dk['CountryName'] = country_name
    holidays_df_dk['Country'] = country_code
    holidays_df_dk['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - cyprus \n", holidays_df_dk);
    df_all_country = pd.concat([df_all_country, holidays_df_dk])
    ##DENMARK

    ##SPAIN

    holiday_list.clear()
    country_code.clear()
    country_name.clear()
    for holiday in holidays.Spain(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('ES')
        country_name.append('Spain')

    holidays_df_es = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR SPAIN
    ch_calendar = Spain()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_es['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_es['CountryName'] = country_name
    holidays_df_es['Country'] = country_code
    holidays_df_es['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - cyprus \n", holidays_df_es);
    df_all_country = pd.concat([df_all_country, holidays_df_es])
    ##SPAIN

    ##FRANCE

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Spain(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('FR')
        country_name.append('France')

    holidays_df_fr = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR SPAIN
    ch_calendar = France()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_fr['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_fr['CountryName'] = country_name
    holidays_df_fr['Country'] = country_code
    holidays_df_fr['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - france \n", holidays_df_fr);
    df_all_country = pd.concat([df_all_country, holidays_df_fr])
    ##FRANCE

    ##ESTONIA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Estonia(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('EE')
        country_name.append('Estonia')

    holidays_df_ee = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Estonia()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_ee['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_ee['CountryName'] = country_name
    holidays_df_ee['Country'] = country_code
    holidays_df_ee['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - estonia \n", holidays_df_ee)
    df_all_country = pd.concat([df_all_country, holidays_df_ee])
    ##ESTONIA

    ##NETHERLANDS

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Netherlands(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('NL')
        country_name.append('Netherlands')

    holidays_df_nl = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Netherlands()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_nl['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_nl['CountryName'] = country_name
    holidays_df_nl['Country'] = country_code
    holidays_df_nl['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - estonia \n", holidays_df_nl)
    df_all_country = pd.concat([df_all_country, holidays_df_nl])
    ##NETHERLANDS

    ##ITALY

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Italy(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('IT')
        country_name.append('Italy')

    holidays_df_it = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Italy()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_it['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_it['CountryName'] = country_name
    holidays_df_it['Country'] = country_code
    holidays_df_it['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - italy \n", holidays_df_it)
    df_all_country = pd.concat([df_all_country, holidays_df_it])
    ##ITALY

    # ##NORWAY
    #
    # holiday_list.clear()
    # country_code.clear()
    # country_name.clear()
    #
    # for holiday in holidays.Norway(years).items():
    #     print("Holiday Detail", holiday)
    #     holiday_list.append(holiday)
    #     country_code.append('NO')
    #     country_name.append('Norway')
    #
    # holidays_df_no = pd.DataFrame(holiday_list, columns=["date", "holiday"])
    #
    # # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    # ch_calendar = Norway()
    # holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
    #                                 columns=["date", "holiday"])
    #
    # holidays_df_no['HolidayNameEng'] = holidays_2023_df["holiday"]
    # holidays_df_no['CountryName'] = country_name
    # holidays_df_no['Country'] = country_code
    # print("Holidays Data Frame - Norway \n", holidays_df_no)
    # df_all_country = pd.concat([df_all_country, holidays_df_no])
    # ##NORWAY

    ##BELGIUM

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Belgium(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('BE')
        country_name.append('Belgium')

    holidays_df_be = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Belgium()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_be['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_be['CountryName'] = country_name
    holidays_df_be['Country'] = country_code
    holidays_df_be['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - belgium \n", holidays_df_be)
    df_all_country = pd.concat([df_all_country, holidays_df_be])
    ##BELGIUM

    ##LITHUANIA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Lithuania(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('LV')
        country_name.append('Lithuania')

    holidays_df_lv = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Lithuania()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_lv['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_lv['CountryName'] = country_name
    holidays_df_lv['Country'] = country_code
    holidays_df_lv['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Lithuania \n", holidays_df_lv)
    df_all_country = pd.concat([df_all_country, holidays_df_lv])
    ##LITHUANIA

    ##MALTA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Lithuania(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('MT')
        country_name.append('Malta')

    holidays_df_mt = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Malta()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_mt['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_mt['CountryName'] = country_name
    holidays_df_mt['Country'] = country_code
    holidays_df_mt['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Malta \n", holidays_df_mt)
    df_all_country = pd.concat([df_all_country, holidays_df_mt])
    ##MALTA

    ##HUNGARY

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Hungary(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('HU')
        country_name.append('Hungary')

    holidays_df_hu = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Hungary()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_hu['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_hu['CountryName'] = country_name
    holidays_df_hu['Country'] = country_code
    holidays_df_hu['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Malta \n", holidays_df_hu)
    df_all_country = pd.concat([df_all_country, holidays_df_hu])
    ##HUNGARY

    ##ROMANIA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Romania(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('RO')
        country_name.append('Romania')

    holidays_df_ro = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Romania()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_ro['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_ro['CountryName'] = country_name
    holidays_df_ro['Country'] = country_code
    holidays_df_ro['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Malta \n", holidays_df_ro)
    df_all_country = pd.concat([df_all_country, holidays_df_ro])
    ##ROMANIA

    # ##AUSTRIA
    #
    # holiday_list.clear()
    # country_code.clear()
    # country_name.clear()
    #
    # for holiday in holidays.Austria(years).items():
    #     print("Holiday Detail", holiday)
    #     holiday_list.append(holiday)
    #     country_code.append('AT')
    #     country_name.append('Austria')
    #
    # holidays_df_at = pd.DataFrame(holiday_list, columns=["date", "holiday"])
    #
    # # USING workalendar API FOR GETTING HOLIDAYS FOR AUSTRIA
    # ch_calendar = Austria()
    # holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
    #                                 columns=["date", "holiday"])
    #
    # holidays_df_at['HolidayNameEng'] = holidays_2023_df["holiday"]
    # holidays_df_at['CountryName'] = country_name
    # holidays_df_at['Country'] = country_code
    # print("Holidays Data Frame - Austria \n", holidays_df_at)
    # df_all_country = pd.concat([df_all_country, holidays_df_at])
    # ##AUSTRIA

    ##SLOVENIA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Slovenia(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('SI')
        country_name.append('Slovenia')

    holidays_df_si = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Slovenia()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_si['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_si['CountryName'] = country_name
    holidays_df_si['Country'] = country_code
    holidays_df_si['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Slovenia \n", holidays_df_si)
    df_all_country = pd.concat([df_all_country, holidays_df_si])
    ##SLOVENIA

    # ##UNITEDKINGDOM
    #
    # holiday_list.clear()
    # country_code.clear()
    # country_name.clear()
    #
    # for holiday in holidays.UnitedKingdom(years).items():
    #     print("Holiday Detail", holiday)
    #     holiday_list.append(holiday)
    #     country_code.append('GB')
    #     country_name.append('UnitedKingdom')
    #
    # holidays_df_gb = pd.DataFrame(holiday_list, columns=["date", "holiday"])
    #
    # # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    # ch_calendar = UnitedKingdom()
    # holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
    #                                 columns=["date", "holiday"])
    #
    # holidays_df_gb['HolidayNameEng'] = holidays_2023_df["holiday"]
    # holidays_df_gb['CountryName'] = country_name
    # holidays_df_gb['Country'] = country_code
    # print("Holidays Data Frame - United Kingdom \n", holidays_df_gb)
    # df_all_country = pd.concat([df_all_country, holidays_df_gb])
    # ##UNITEDKINGDOM

    ##BULGARIA

    holiday_list.clear()
    country_code.clear()
    country_name.clear()

    for holiday in holidays.Bulgaria(years).items():
        print("Holiday Detail", holiday)
        holiday_list.append(holiday)
        country_code.append('BG')
        country_name.append('Bulgaria')

    holidays_df_bg = pd.DataFrame(holiday_list, columns=["date", "holiday"])

    # USING workalendar API FOR GETTING HOLIDAYS FOR ESTONIA
    ch_calendar = Bulgaria()
    holidays_2023_df = pd.DataFrame(ch_calendar.holidays(2023),
                                    columns=["date", "holiday"])
    holidays_2023_df['date'] = pd.to_datetime(holidays_2023_df['date'])
    holidays_df_bg['HolidayNameEng'] = holidays_2023_df["holiday"]
    holidays_df_bg['CountryName'] = country_name
    holidays_df_bg['Country'] = country_code
    holidays_df_bg['IsThursday'] = holidays_2023_df['date'].dt.weekday.map(dw_mapping) == 'Thursday'
    print("Holidays Data Frame - Bulgaria \n", holidays_df_bg)
    df_all_country = pd.concat([df_all_country, holidays_df_bg])
    ##BULGARIA

    ## WRITE CSV FILE
    header = ["date", "holiday", "HolidayNameEng", "CountryName", "Country", "IsThursday"]
    df_all_country.to_csv('holiday_data.csv', columns=header)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
