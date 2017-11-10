#importing modules
import media
import fresh_tomatoes

#creating instances or objects of Class Movie
iron_man = media.Movie('Iron Man','Genius, billionaire, and playboy Tony Stark fights villain Stane','https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG','https://www.youtube.com/watch?v=8hYlB38asDY')

thor = media.Movie('Thor','Odin strips his son of his godly power and exiles him to Earth as a mortal','https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/Thor_poster.jpg/220px-Thor_poster.jpg','https://www.youtube.com/watch?v=JOddp-nlNvQ')

captain_america = media.Movie('Captain America','Steve Rogers is rejected for World War II military recruitment becomes a super-soldier','https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Captain_America_The_First_Avenger_poster.jpg/220px-Captain_America_The_First_Avenger_poster.jpg','https://www.youtube.com/watch?v=JerVrbLldXw')

avengers = media.Movie('The Avengers','Superheros saves earth from Alien Invasion with the help of an organisation called S.H.I.E.L.D.','https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg','https://www.youtube.com/watch?v=eOrNdBpGMv8')

iron_man_3 = media.Movie('Iron Man 3','When Tony Stark\'s world is torn apart by a formidable terrorist called the Mandarin, he starts an odyssey of rebuilding and retribution.','https://upload.wikimedia.org/wikipedia/en/thumb/d/d5/Iron_Man_3_theatrical_poster.jpg/220px-Iron_Man_3_theatrical_poster.jpg','https://www.youtube.com/watch?v=Ke1Y3P9D0Bc')

guardians_of_the_galaxy = media.Movie('Guardians of the Galaxy','A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.','https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg','https://www.youtube.com/watch?v=d96cjJhvlMA')

avengers_second = media.Movie('Avengers: Age of Ultron','Tony Stark creates the Ultron Program to protect the world but program becomes hostile, The Avengers team up and fight','https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg','https://www.youtube.com/watch?v=tmeOjFno6Do')

captain_america_civil_war = media.Movie('Captain America:Civil War','Political interference in the Avengers\' activities causes a rift between former allies Captain America and Iron Man.','https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg','https://www.youtube.com/watch?v=dKrVegVI0Us')

doctor_strange = media.Movie('Doctor Strange','While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.','https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg','https://www.youtube.com/watch?v=HSzx-zryEgM')

guardians_of_the_galaxy_2 = media.Movie('Guardians of the Galaxy 2','The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill\'s true parentage','https://upload.wikimedia.org/wikipedia/en/thumb/9/95/GotG_Vol2_poster.jpg/220px-GotG_Vol2_poster.jpg','https://www.youtube.com/watch?v=d96cjJhvlMA')

spider_man = media.Movie('Spider-Man: Homecoming','Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man','https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg','https://www.youtube.com/watch?v=8wNgphPi5VM')

thor_second = media.Movie('Thor: Ragnarok','Imprisoned, the almighty Thor finds himself fighting Hulk,Thor must fight for survival and save his civilization from Hela','https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg','https://www.youtube.com/watch?v=ue80QwXMRHg')

#creating List of various objects 
movies_list = [iron_man , thor , captain_america , avengers , iron_man_3 , guardians_of_the_galaxy , avengers_second , captain_america_civil_war , doctor_strange , guardians_of_the_galaxy_2 , spider_man , thor_second]

#calling a function and passing the object list as argument
fresh_tomatoes.open_movies_page(movies_list)
