import matplotlib as mpl

d = {'dark_purple': '#7E446C',
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
                                             [(0,    d['dark_purple']),
                                              (0.125, d['purple']),
                                              (0.25, d['pink']),
                                              (0.375, d['coral']),
                                              (0.5, d['gold']),
                                              (0.625, d['yellow']),
                                              (0.75, d['green']),
                                              (0.875, d['blue']),
                                              (1,    d['dark_blue'])], N=126)            
        return cmap
    def dct(self, theme='all'):
        if theme == 'dark':
            d = dark_dict
        elif theme == 'light':
            d = light_dict
        elif theme == 'medium':
            d = medium_dict
        else: 
            pass
        return d
