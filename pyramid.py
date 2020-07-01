class Node:
    def __init__(self,data):
        self.data = data
        self.up = None 
        self.down = None
        self.right = None
        self.left = None
class Pyramid:
    """ This  Data Structure help to store data in 
        pyramid like structure
    """
    def __init__(self,rootdata="ROOT"):
        self.rootdata = rootdata
        ROOT_node = Node(rootdata)
        self.root = ROOT_node 
        self.left_last = self.root
        self.right_last = self.root
        self.up_last = self.root 
        self.down_last = self.root
    
    def insert_pyramid_layer(
        self,UpData=None,
        LeftData=None,
        DownData=None,
        RightData=None
        ):
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
                
        self.left_last.left = new_LEFT_Node     
        # Insert New NOde Data in Left Most Node
        
        self.right_last.right = new_RIGHT_Node  
        # Insert New NOde Data in Right Most Node
        
        self.up_last.up = new_UP_Node           
        # Insert New NOde Data in Up Most Node
        
        self.down_last.down = new_DOWN_Node     
        # Insert New NOde Data in Down Most Node     

        temp = self.left_last
        
        self.left_last = self.left_last.left     
        # Change Left Most Pointer to New Left Most Node
        
        self.left_last.down = self.down_last.down
        self.left_last.up = self.up_last.up
        self.left_last.right = temp

        temp = self.right_last
        
        self.right_last = self.right_last.right  
        # Change Right Most Pointer to New Right Most Node
        
        self.right_last.down = self.down_last.down
        self.right_last.up = self.up_last.up
        self.right_last.left = temp

        temp = self.up_last
        
        self.up_last = self.up_last.up           
        # Change UP Most Pointer to New UP Most Node
        
        self.up_last.right = self.right_last
        self.up_last.left = self.left_last
        self.up_last.down = temp

        temp = self.down_last
        
        self.down_last = self.down_last.down     
        # Change Down Most Pointer to New Down Most Node
        
        self.down_last.right = self.right_last
        self.down_last.left = self.left_last
        self.down_last.up = temp

    def vertical_list(self):
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

    def horizontal_list(self):
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

    def horizontal_rev_list(self):
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

    def vertical_rev_list(self):
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
            while temp.data != self.rootdata:
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
            delete pyramid layer from botom of pyramid 
            ( means layer that insert in last that pop 
            from this pyramid)
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
            
            return pop_up,pop_left,pop_down,pop_right

    def dequeue_pyramid(self):
        """
            Delete pyramid layer from TOP 
            ( means pyramid layer that insert first )
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
                
                return del_up,del_left,del_down,del_right
            except:
                return self.pop_pyramid_layer()
        
    def root_to_right_list(self):
        """
            Return root to right end data list of pyramid
        """
        lis=[]
        temp = self.root
        while temp.right != None:
            lis.append(temp.data)
            temp = temp.right
        lis.append(temp.data)
        return lis
    
    def root_to_left_list(self):
        """
            Return root to  left end data list of pyramid
        """
        lis=[]
        temp = self.root
        while temp.left != None:
            lis.append(temp.data)
            temp = temp.left
        lis.append(temp.data)
        return lis

    def root_to_up_list(self):
        """
            Return root to up end data list of pyramid
        """
        lis=[]
        temp = self.root
        while temp.up != None:
            lis.append(temp.data)
            temp = temp.up
        lis.append(temp.data)
        return lis

    def root_to_down_list(self):
        """
            Return root to down end data list of pyramid
        """
        lis=[]
        temp = self.root
        while temp.down != None:
            lis.append(temp.data)
            temp = temp.down
        lis.append(temp.data)
        return lis