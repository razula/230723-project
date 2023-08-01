import pickle

def load_file(filename="task.pickle"):
    try:
        with open (filename , "rb") as f:
            loaded_list=pickle.load(f)
            return loaded_list
    except:
        with open (filename , "wb") as f:
            pickle.dump([],f)
            return []

category_list=["home","work","sport","bank","friends"]
owner_list=["Raz","Tal","Mikey","Walter","Jessie"]
def load_list(filename="category.pickle",list_name=category_list):
    try:
        with open (filename , "rb") as f:
            loaded_list=pickle.load(f)
            return loaded_list
    except:
        with open (filename , "wb") as f:
            pickle.dump(list_name,f)
            return list_name



def save_file(list_to_save,filename="task.pickle"):
    with open (filename , "wb") as f:
        pickle.dump (list_to_save,f)

