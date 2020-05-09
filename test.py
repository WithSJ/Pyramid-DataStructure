"""Test file check all Pyramid module funcation """
from pyramid import Pyramid

if __name__ == "__main__":
    import os
    myPyramid = Pyramid()
    while 1:
            
        print("""---Pyramid DataStructure---
                \n |1| Insert Pyramid Layer
                \n |2| View Pyramid Graph
                \n |3| Vertical List 
                \n |4| Reverse Vertical List 
                \n |5| Horizontal List 
                \n |6| Reverse Horizontal List 
                \n |7| POP Pyramid Layer
                \n |8| DeQueue Pyramid Layer
                \n |9| Root to Right List
                \n |10| Root to Left List
                \n |11| Root to Up List
                \n |12| Root to Down List
            """)
        
        ch=input("Enter : ")
        if ch == "1":
            myPyramid.insert_pyramid_layer(input("Enter Down Data :"),input("Enter Right Data :"),input("Enter Top Data :"),input("Enter Left Data :"))
        elif ch == "2":
                myPyramid.graph_view()
        elif ch == "3":
            print(myPyramid.vertical_list())
        elif ch == "4":
            print(myPyramid.vertical_rev_list())
        elif ch == "5":
            print(myPyramid.horizontal_list())
        elif ch == "6":
            print(myPyramid.horizontal_rev_list())
        elif ch == "7":
            print(myPyramid.pop_pyramid_layer())
        elif ch == "8":
            print(myPyramid.dequeue_pyramid())
        elif ch == "9":
            print(myPyramid.root_to_right_list())
        elif ch == "10":
            print(myPyramid.root_to_left_list())
        elif ch == "11":
            print(myPyramid.root_to_up_list())
        elif ch == "12":
            print(myPyramid.root_to_down_list())
        
        else:
            print("Plese Enter Correct number")
        
        input("\n Press any key...")
        os.system("clear")