#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# PBhamidipati, 2022-Dec-04, Updated title to CD_Inventory.py
# PBhamidipati, 2022-Dec-04, Updated code to reflect the given pseudocode in 
#    order to address Assignment 08 - implementing objects & classes
#------------------------------------------#

from typing import List

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    
    methods:

    """
    # TODone Add Code to the CD class
    #---Fields---#
    
    #---Constructor---#
    def __init__(self, trackId = 0, trackTitle = '<None chosen>', trackArtist = '<Not applicable>'):
        #--Attributes--#
        self.__cd_id = trackId
        self.__cd_title = trackTitle
        self.__cd_artist = trackArtist
        
    #---Properties---#
    @property
    def cd_id(self):
      return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, intID):
        if not str(intID).isnumeric():
            raise Exception('An integer value is required for the CD ID field!')
        else:
            self.__cd_id = intID
    
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    
    @cd_title.setter
    def cd_title(self, strTitle):
        self.__cd_title = str(strTitle)
    
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    
    @cd_artist.setter
    def cd_artist(self, strArtist):
        self.__cd_artist = str(strArtist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:
        
    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        
        load_inventory(file_name): -> (a list of CD objects)
           
    """
    # TODone Add code to process data from a file
    def Load_inventory(file_name) -> List[CD]:
        """ Loads the current CD inventory from file to a list
            
            Args:
                file_name (str): name of the text file that contains the CD inventory that's to be loaded
    
            Returns: 
                list: list of CD objects
        """

        lstTemp = []
        try:                
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                cdTemp = CD()
                cdTemp.cd_id = int(data[0])
                cdTemp.cd_title = data[1]
                cdTemp.cd_artist = data[2]
                lstTemp.append(cdTemp)
        except ValueError as e:
            print(e.__doc__)
            print('Bad Data found! The CD ID in the file cannot be converted to an integer.')
        except FileNotFoundError as e:
            print(e.__doc__)
            print('File not found! Creating a new file.')
            objFile = open(file_name, 'wb')
        except IOError as e:
            print(e.__doc__)
            print('Unhandled error while reading file!')
            raise(e)
        finally:
            objFile.close()
        
        return lstTemp
        
    # TODone Add code to process data to a file
    def save_inventory(file_name, lst_Inventory) -> None:
        """ Writes the current CD inventory from list to the file
            
            Args:
                file_name (str): name of the text file that contains the CD inventory that's to be loaded
                lst_Inventory (list): list of CD objects / inventory details
    
            Returns: 
                None
        """
        try:        
            objFile = open(file_name, 'w')
            for cd in lst_Inventory:
                lstValues = [str(cd.cd_id), cd.cd_title, cd.cd_artist]
                objFile.write(','.join(lstValues) + '\n')
        except IOError as e:
            print(e.__doc__)
            print('Unhandled error while reading file!')
            raise(e)
        finally:
            objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling Input / Output"""
    
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
        
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODone add code to display the current data on screen
    def show_inventory(listInventory):
        """Displays current inventory 


        Args:
            listInventory (list of CD class objects): 2D data structure 
                (list of CD objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in listInventory:
            dictValues = {'ID': cd.cd_id, 'Title': cd.cd_title, 'Artist': cd.cd_artist}
            print('{}\t{} (by:{})'.format(*dictValues.values()))
        print('======================================')
    
    # TODone add code to get CD data from user
    @staticmethod
    def ask_input_addCD():
        """Gets user input for the CD's details that are to be added to the inventory

        Args:
            None.

        Returns:
            None.

        """
        try:
            strID = input('Enter ID: ').strip()
            intID = int(strID)
            strTitle = input('What is the CD\'s title? ').strip()
            strArtist = input('What is the Artist\'s name? ').strip()
            
            cd = CD()
            cd.cd_id = intID
            cd.cd_title = strTitle
            cd.cd_artist = strArtist
            
            lstOfCDObjects.append(cd)
            
            IO.show_inventory(lstOfCDObjects)
            
        except ValueError as e:
            print('The CD ID entered cannot be converted to an integer!')
            print(e)
                
           
    @staticmethod
    def save_data_list():
        """Displays the latest inventory from the in-memory list and confirms that the list is to be saved 
            to the file. If confirmed, the list is written to the file, otherwuse it informs that the list
            was NOT saved and asks the user to go back to the menu list
        
        Args:
            None.

        Returns:
            None.

        """
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # save data
            # TODone move processing code into function 
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
    
    @staticmethod
    def load_from_file():
        """Ascertains from the user if the CD inventory is to be loaded from the file or the in-memory list variable,
            displaying suitable warning messages as to what would happen for each of their choices, and proceeds to
            load or cancel loading as may be the user's choice
        
        Args:
            None.

        Returns:
            list: current list of CD objects loaded from file

        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise, reload will be canceled. ')
        lstTemp = []
        if strYesNo.lower() == 'yes':
            print('\nRe-loading...\n')
            lstTemp = FileIO.Load_inventory(strFileName)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.\n')
        
        return lstTemp

# -- Main Body of Script -- #
# TODone Add Code to the main body

# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.Load_inventory(strFileName)

# Display menu to user
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # Process menu selection
    # process exit first
    if strChoice == 'x':
        break
    
    # show user current inventory (display)
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user add data to the inventory (add)
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        IO.ask_input_addCD()
        continue  # start loop back at top.
    
    # let user save inventory to file (save)
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save 
        IO.save_data_list()
        continue  # start loop back at top.
    
    # let user load inventory from file (load)
    elif strChoice == 'l':
        lstOfCDObjects = IO.load_from_file() # call method to load data from file to in-memory list
        continue  # start loop back at top.
        
    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')

