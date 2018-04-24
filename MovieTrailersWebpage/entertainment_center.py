import fresh_tomatoes
import media

american_crime = media.Movie("An American Crime",
                             "Sisters are taken in by a sadistic woman--only one survives",
                             "https://upload.wikimedia.org/wikipedia/en/7/77/American_crimemp.jpg",
                             "https://youtu.be/4zXBML55O08")

bully = media.Movie("Bully",
                    "Victims of a bully get the ultimate revenge",
                    "https://upload.wikimedia.org/wikipedia/en/4/49/Bullyposter.jpg",
                    "https://youtu.be/uKSIMkKIEek")

great_escape = media.Movie("The Great Escape",
                           "WWII prisoners plan escape from German camp",
                           "https://upload.wikimedia.org/wikipedia/en/c/c7/Great_escape.jpg",
                           "https://youtu.be/ykL0MtsaNdc")

hacksaw_ridge = media.Movie("Hacksaw Ridge",
                            "Army medic refuses to kill during WWII",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/Hacksaw_Ridge_poster.png",
                            "https://youtu.be/s2-1hz1juBI")

true_story = media.Movie("True Story",
                         "Murderer Christian Longo steals the identity of a reporter",
                         "https://upload.wikimedia.org/wikipedia/en/9/92/True_Story_poster.jpg",
                         "https://youtu.be/Y_NiP_bqlns")

wind_rises = media.Movie("The Wind Rises",
                         "Animated tale of the Japanese WWII fighter plane designer",
                         "https://upload.wikimedia.org/wikipedia/en/a/a3/Kaze_Tachinu_poster.jpg",
                         "https://youtu.be/2QFBZgAZx7g")

movies = [american_crime, bully, great_escape,
          hacksaw_ridge, true_story, wind_rises]
'''This function call uses lists of movie instances as input to generate
an HTML file to open in a browser.'''
fresh_tomatoes.open_movies_page(movies)
