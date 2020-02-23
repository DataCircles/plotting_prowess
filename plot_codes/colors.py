import matplotlib as mpl

full_dict = {'dark_purple': '#7E446C',
             'dark_pink' : '#912267',
             'dark_coral' : '#BD4D55',
             'dark_gold' : '#DE8127',
             'dark_yellow' : '#F0BC10',
             'dark_green' : '#2B8A54',
             'dark_blue' : '#185675',
             'light_purple' : '#C06F98',
             'light_pink' : '#DC6986',
             'light_coral' : '#F2AB9B',
             'light_gold' : '#F2C56C',
             'light_yellow' : '#FFEB82',
             'light_green' : '#92BA72',
             'light_blue' : '#5AADA4',
             'pink' : '#C6407D',
             'coral' : '#E85F69',
             'gold' : '#E3A711',
             'yellow' : '#F9DB67',
             'green' : '#66A35F',
             'blue' : '#5AADA4',
             'purple': '#915B8D'}

dark_dict = {'dark_purple': '#7E446C',
             'dark_pink' : '#912267',
             'dark_coral' : '#BD4D55',
             'dark_gold' : '#DE8127',
             'dark_yellow' : '#F0BC10',
             'dark_green' : '#2B8A54',
             'dark_blue' : '#185675'}
light_dict = {'light_purple' : '#C06F98',
              'light_pink' : '#DC6986',
              'light_coral' : '#F2AB9B',
              'light_gold' : '#F2C56C',
              'light_yellow' : '#FFEB82',
              'light_green' : '#92BA72',
              'light_blue' : '#5AADA4'}
medium_dict = {'pink' : '#C6407D',
               'coral' : '#E85F69',
               'gold' : '#E3A711',
               'yellow' : '#F9DB67',
               'green' : '#66A35F',
               'blue' : '#5AADA4',
               'purple': '#915B8D'}

class Color_Coded:
    def color_map(self, group='all'):
        if group == 'all':
            cmap = mpl.colors.LinearSegmentedColormap.from_list('custom', 
                                             [(0,     full_dict['dark_purple']),
                                              (0.125, full_dict['purple']),
                                              (0.25,  full_dict['pink']),
                                              (0.375, full_dict['coral']),
                                              (0.5,   full_dict['gold']),
                                              (0.625, full_dict['yellow']),
                                              (0.75,  full_dict['green']),
                                              (0.875, full_dict['blue']),
                                              (1,     full_dict['dark_blue'])], N=126)            
        return cmap
    def dct(self, theme='all'):
        if theme == 'dark':
            d = dark_dict
        elif theme == 'light':
            d = light_dict
        elif theme == 'medium':
            d = medium_dict
        else: 
            d = full_dict
        return d
