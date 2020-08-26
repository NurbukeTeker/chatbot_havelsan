class Process():
    def __init__(self, name_surname ):
        
        self.member_name_surname = name_surname 
        self.state = -1
        self.errorCount = 0
    
    def process_refresh(self):
        
        self.state = -1
        self.errorCount = 0
     
        
    
       