class Node:
    def __init__(self,data):
        self.data = data
        self.up = None 
        self.down = None
        self.right = None
        self.left = None
class Pyramid:
    # This  Data Structure help to store data in pyramid like structure                                     
    def __init__(self):
        
        ROOT_node = Node("ROOT")

        self.root = ROOT_node 
        self.left_last = self.root
        self.right_last = self.root
        self.up_last = self.root 
        self.down_last = self.root
    
    def insert_pyramid_layer(self,DownData=None,RightData=None,UpData=None,LeftData=None):
        """
            This Method use to insert data in pyramid layer 
            take four parameter as 
            UpData = Up most node data 
            DownData = Down most node Data
            LeftData = Left most node data
            RightData = Right most node data

        """
        new_UP_Node = Node(UpData)
        new_DOWN_Node = Node(DownData)
        new_LEFT_Node = Node(LeftData)
        new_RIGHT_Node = Node(RightData)
                
        self.left_last.left = new_LEFT_Node     # Insert New NOde Data in Left Most Node
        self.right_last.right = new_RIGHT_Node  # Insert New NOde Data in Right Most Node
        self.up_last.up = new_UP_Node           # Insert New NOde Data in Up Most Node
        self.down_last.down = new_DOWN_Node     # Insert New NOde Data in Down Most Node     

        temp = self.left_last
        self.left_last = self.left_last.left     # Change Left Most Pointer to New Left Most Node
        self.left_last.down = self.down_last.down
        self.left_last.up = self.up_last.up
        self.left_last.right = temp

        temp = self.right_last
        self.right_last = self.right_last.right  # Change Right Most Pointer to New Right Most Node
        self.right_last.down = self.down_last.down
        self.right_last.up = self.up_last.up
        self.right_last.left = temp

        temp = self.up_last
        self.up_last = self.up_last.up           # Change UP Most Pointer to New UP Most Node
        self.up_last.right = self.right_last
        self.up_last.left = self.left_last
        self.up_last.down = temp

        temp = self.down_last
        self.down_last = self.down_last.down     # Change Down Most Pointer to New Down Most Node
        self.down_last.right = self.right_last
        self.down_last.left = self.left_last
        self.down_last.up = temp

    def up_to_down_list(self):
        """
            Return Up to Down Data list 
        """
        if self.root == self.up_last :
                return None
        else:
            lis=[]
            temp = self.up_last
            while temp.down != None:
                lis.append(temp.data)
                temp = temp.down
            lis.append(temp.data)
            return lis

    def left_to_right_list(self):
        """
            Return Left to Right Data list 
        """
        if self.root == self.up_last :
                return None
        else:
            lis=[]
            temp = self.left_last
            while temp.right != None:
                lis.append(temp.data)
                temp = temp.right
            lis.append(temp.data)
            return lis

    def right_to_left_list(self):
        """
            Return Right to List Data list 
        """
        if self.root == self.up_last :
                return None
        else:
        
            lis=[]
            temp = self.right_last
            while temp.left != None:
                lis.append(temp.data)
                temp = temp.left
            lis.append(temp.data)
            return lis

    def down_to_up_list(self):
        """
            Return Down to UP Data list 
        """
        if self.root == self.up_last :
                return None
        else:
            lis=[]
            temp = self.down_last
            while temp.up != None:
                lis.append(temp.data)
                temp = temp.up
            lis.append(temp.data)
            return lis
    
    def graph_view(self):
        """
            Display all pyramid node in top view of pyramid 
        """ 
        if self.root == self.up_last :
                print("Empty Pyramid")
        else:
            st=""
            lis=[]
            temp =self.left_last
            while temp.right != None:
                st += str(temp.data)
                lis.append(temp.data)
                temp = temp.right
            st += str(temp.data)
            # print(len(st))
            lenth = len(st)//2 + len(lis)//2 -2
            
            temp = self.up_last
            while temp.data != "ROOT":
                print(" "*lenth,temp.data)
                print(" "*lenth,"|")
                temp = temp.down
            # print("*"*(pow(lenth,2)),temp.data)
            backup=temp
            temp = self.left_last
            while temp.right != None:
                print(temp.data,end="-")
                temp = temp.right
            print(temp.data)

            temp = backup.down
            while temp.down != None:
                print(" "*lenth,"|")
                print(" "*lenth,temp.data)
                temp = temp.down
            print(" "*lenth,"|")
            print(" "*lenth,temp.data)
    
    def pop_pyramid_layer(self):
        """
            delete pyramid layer from botom of pyramid ( means layer that insert in last that pop from this pyramid)
        """
        
        if self.root == self.up_last :
                return None
        else:
            pop_up = self.up_last.data
            pop_down = self.down_last.data
            pop_left = self.left_last.data
            pop_right = self.right_last.data

            self.up_last = self.up_last.down
            self.up_last.up = None
            
            self.down_last = self.down_last.up
            self.down_last.down = None

            self.right_last = self.right_last.left
            self.right_last.right = None

            self.left_last = self.left_last.right
            self.left_last.left = None
            
            return pop_down,pop_right,pop_up,pop_left

    def dequeue_pyramid(self):
        """
            Delete pyramid layer from TOP ( means pyramid layer that insert first )
        """

        if self.root == self.up_last :
                return None
        else:
            try :
                    
                del_up = self.root.up.data
                del_down = self.root.down.data
                del_left = self.root.left.data
                del_right = self.root.right.data
                
                self.root.up.up.down = self.root
                self.root.up = self.root.up.up
                
                self.root.down.down.up = self.root
                self.root.down = self.root.down.down
                
                self.root.left.left.right=self.root
                self.root.left = self.root.left.left

                self.root.right.right.left = self.root
                self.root.right = self.root.right.right
                
                return del_down,del_right,del_up,del_left
            except:
                return self.pop_pyramid_layer()




if __name__ == "__main__":
    import os
    myPyramid = Pyramid()
    while 1:
            
        print("---Pyramid DataStructure---")
        print("\n |1| Insert Pyramid Layer")
        print("\n |2| View Pyramid Graph")
        print("\n |3| Get Up - Down data list ")
        print("\n |4| Get Down - Up data list ")
        print("\n |5| Get Left - Right data list ")
        print("\n |6| Get Right - Left data list ")
        print("\n |7| POP Pyramid Layer")
        print("\n |8| DeQueue Pyramid Layer")
        ch=input("Enter : ")
        if ch == "1":
            myPyramid.insert_pyramid_layer(input("Enter Down Data :"),input("Enter Right Data :"),input("Enter Top Data :"),input("Enter Left Data :"))
        elif ch == "2":
                myPyramid.graph_view()
        elif ch == "3":
            print(myPyramid.up_to_down_list())
        elif ch == "4":
            print(myPyramid.down_to_up_list())
        elif ch == "5":
            print(myPyramid.left_to_right_list())
        elif ch == "6":
            print(myPyramid.right_to_left_list())
        elif ch == "7":
            print(myPyramid.pop_pyramid_layer())
        elif ch == "8":
            print(myPyramid.dequeue_pyramid())
        else:
            print("Plese Enter Correct number")
        
        input("\n Press any key...")
        os.system("clear")

        
        
            

            

