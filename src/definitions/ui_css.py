BASE = """#error_lbl {
            background-color: rgba(27,29,35,255);
            color: "red";
        }
        QWidget {
            background-color: rgba(27,29,35,255);
            color: "white";
        }
        QLabel {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        QRadioButton {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        QScrollArea{
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        QCheckBox {
            background-color: rgba(44,49,62,255);
        }
        QLineEdit {
           background-color: rgba(80,90,120,255);
        }
        QComboBox {
            background-color: rgba(80,90,120,255);
        }
        QDateEdit {
            background-color: rgba(80,90,120,255);
        }"""

WIG_4 = """ 
    #verticalLayoutWidget_4 {
            background-color: rgba(44,49,62,255);
            color: "white";
    }"""

WIG_6 = """
        #verticalLayoutWidget_6 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }"""
WIG_7 = """"""

START_WINDOW_SHOW_SAVED_TREES_CSS = BASE + WIG_4 + WIG_6 + \
    """
        #show_saved_trees {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
       
        #label{
             background-color: rgba(27,29,35,255);
        }
              
    """

START_WINDOW_PREPARE_BACKGROUND_CSS = BASE + WIG_4 + """
                           #add_person {
                               background-color: rgba(44,49,62,255);
                               color: "white";
                               border: 2px solid white;
                               border-color: rgba(44,49,62,255);
                           }
                           #label{
                            background-color: rgba(27,29,35,255)
                            }

                               """

START_WINDOW_FIND_PERSON_CSS = BASE + WIG_4 + WIG_6 + """
                            #find_person {
                                background-color: rgba(44,49,62,255);
                                color: "white";
                                border: 2px solid white;
                                border-color: rgba(44,49,62,255);
                            }
                            #label{
                             background-color: rgba(27,29,35,255)
                             }

                                """

START_WINDOW_EDIT_PERSON_CLICKED = BASE + WIG_4 + WIG_6 + """
                                    #edit_person {
                                        background-color: rgba(44,49,62,255);
                                        color: "white";
                                        border: 2px solid white;
                                        border-color: rgba(44,49,62,255);
                                    }
                                    #verticalLayoutWidget_7 {
                                        background-color: rgba(44,49,62,255);
                                            color: "white";
                                    }
                                    #label{
                                     background-color: rgba(27,29,35,255)
                                     }

                                        """
START_WINDOW_ADD_TREE_CSS = BASE + WIG_6 + \
    """
        #add_tree {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }color: "white";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_ADD_CITY_CSS = BASE + WIG_6 + \
    """
        #add_city {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_ADD_DEATH_REASON_CSS = BASE + WIG_6 + \
    """
        #add_death_reason {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_ADD_ILLNESS_CSS = BASE + WIG_6 + \
    """
        #add_illness {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_ADD_PROFESSION_CSS = BASE + WIG_6 + \
    """
        #add_profession {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
    """

START_WINDOW_FIND_RELATION_CSS = BASE + WIG_6 + \
    """
        #find_relation {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
        horizontalLayoutWidget{
            background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_FIND_SIMILARITIES_CSS = BASE + WIG_6 + \
    """
        #find_similarities {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
        horizontalLayoutWidget{
            background-color: rgba(27,29,35,255)
        }
    """
START_WINDOW_ANALISE_TREE_CSS = BASE + WIG_6 + \
    """
        #analise_tree {
            background-color: rgba(44,49,62,255);
            color: "white";
            border: 2px solid white;
            border-color: rgba(44,49,62,255);
        }
        #info_lbl {
            background-color: rgba(44,49,62,255);
            color: "red";
        }
        #verticalLayoutWidget_7 {
            background-color: rgba(44,49,62,255);
            color: "white";
        }
        #label{
             background-color: rgba(27,29,35,255)
        }
        horizontalLayoutWidget{
            background-color: rgba(27,29,35,255)
        }
    """
