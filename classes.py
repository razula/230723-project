

class Task():
    def __init__(self,id=0,name="",start_date="",finish_date="",owner="",description="",category="",finished="no"):
        self.id=id
        self.name=name
        self.start_date=start_date
        self.finish_date=finish_date
        self.owner=owner
        self.description=description
        self.category=category
        self.finished=finished
    def __repr__(self):
        return f"Task-ID:{self.id}\tTask:{self.name}\tStart Date:{self.start_date}\tFinish Date:{self.finish_date}\tCategory:{self.category}\tFinished:{self.finished}\tDescription:{self.description}"
    

