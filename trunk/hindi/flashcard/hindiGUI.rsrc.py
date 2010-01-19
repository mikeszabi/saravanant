{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':"Sara's Hindi Flash Card",
          'size':(660, 300),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'btnLoadFile', 
    'position':(139, 60), 
    'label':'Load File', 
    },

{'type':'Button', 
    'name':'btnNextWord', 
    'position':(282, 198), 
    'label':'&Next Word', 
    },

{'type':'Button', 
    'name':'btnMeaning', 
    'position':(146, 198), 
    'label':'&Show Meaning', 
    },

{'type':'TextField', 
    'name':'txtMeaning', 
    'position':(153, 158), 
    'size':(295, -1), 
    },

{'type':'TextField', 
    'name':'txtWord', 
    'position':(154, 121), 
    'size':(293, -1), 
    },

{'type':'StaticText', 
    'name':'lblMeaning', 
    'position':(66, 157), 
    'backgroundColor':(239, 235, 231), 
    'text':'Meaning', 
    },

{'type':'StaticText', 
    'name':'lblWord', 
    'position':(66, 126), 
    'size':(68, -1), 
    'backgroundColor':(239, 235, 231), 
    'text':'Word', 
    },

{'type':'StaticText', 
    'name':'lblFile', 
    'position':(47, 23), 
    'size':(111, 29), 
    'backgroundColor':(239, 235, 231), 
    'text':'Select File', 
    },

{'type':'Choice', 
    'name':'fileChoice', 
    'position':(139, 23), 
    'size':(148, -1), 
    'items':[], 
    },

{'type':'RadioGroup', 
    'name':'rgDirection', 
    'position':(332, 13), 
    'size':(242, 83), 
    'backgroundColor':(239, 235, 231), 
    'items':['Hindi2English', 'English2Hindi'], 
    'label':'Direction', 
    'layout':'vertical', 
    'max':1, 
    'stringSelection':'Hindi2Endlish', 
    },

] # end components
} # end background
] # end backgrounds
} }
