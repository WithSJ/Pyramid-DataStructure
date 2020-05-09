# Pyramid-DataStructure
This  Data Structure help to store data in pyramid like structure     

## Create Pyramid
Create root node for pyramid 

    from pyramid import Pyramid
    mypyramid = Pyramid()

**Note** :- When createing object of pyramid by default "ROOT" is data you can change it

    mypyramid = Pyramid("Start")

## Pointers
> **Root Pointer**
> self.root
> **LEFT LAST Pointer**
> self.left_last
> **RIGHT LAST Pointer**
> self.right_last 
> **UP LAST Pointer**
> self.up_last = self.root 
> **DOWN LAST Pointer**
> self.down_last = self.root

## Function you can use 
**|1| Insert Pyramid Lyer**
    Insert data in pyramid layer this function take 4 arguments and return none
    
    insert_pyramid_layer(self , UpData = None , LeftData = None , DownData = None , RightData = None )

**|2| Graph View**
This Function print graph of pyramid data structure on console and return none

    graph_view(self)

**|3| Horizontal List**
This Function return list ( left to right data list )

    horizontal_list(self)

**|4| Reverse Horizontal List**
This Function return list ( right to left data list )

    horizontal_rev_list(self)

**|5| Vertical List**
This Function return list ( Up to down data list )

    vertical_list(self)

**|6| Reverse Vertical List**
This Function return list ( down to up data list )

    vertical_rev_list(self)

**|7| Root To Up List**
This Function return root to up all data
    
    root_to_up_list(self)

**|8| Root To Left List**
This Function return root to Left all data
    
    root_to_left_list(self)

**|8| Root To Down List**
This Function return root to down all data
    
    root_to_down_list(self)

**|10| Root To Right List**
This Function return root to right all data
    
    root_to_right_list(self)

**|11| Pop Pyramid Layer**
This Function delete pyramid layer that insert in last and return tupple of deleted node data ( up, left, down ,right )
    
    pop_pyramid_layer(self):

**|12| DeQueue Pyramid Layer**
This Functiion delete pyramid layer that insert first and return tupple of deleted node data ( up, left, down ,right )

    dequeue_pyramid(self):

