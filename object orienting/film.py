

class movie:

    id:int

    title:str

    rating:int

    director:str
    
    genre:str

    def set_movie(self,id,title,rating,director,run_time,genre):

        self.title=title

        self.id=id

        self.rating=rating
        
        self.director=director

        self.genre=genre


    def display(self):

        print(self.id,self.title,self.genre)

film_instance1=movie()

film_instance1.set_movie(100,"arm",4.5,"jithin lal",120,"action")

film_instance1.display()

