import movie
import fresh_tomatoes

toystory = movie.Movie("Toystory", "Andy's favourite toy, Woody, is worried that after Andy receives his birthday gift, a new toy called Buzz Lightyear, his importance may get reduced. He thus hatches a plan to eliminate Buzz.",
                       "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#toystory.show_Trailer()
hidden_figures = movie.Movie("Hidden Figures",
                             "The story of a team of African-American women mathematicians who served a vital role in NASA during the early years of the US space program.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxOTkxODUyN15BMl5BanBnXkFtZTgwNTU3NTM3OTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                             "https://www.youtube.com/watch?v=5wfrDhgUMGI")
beauty_and_beast = movie.Movie("Beauty and the beast",
                               "An adaptation of the Disney fairy tale about a monstrous-looking prince and a young woman who fall in love.",
                               "https://media1.popsugar-assets.com/files/thumbor/T-wBuVA9aQHvREiLT4QjN2bbmzU/fit-in/550x550/filters:format_auto-!!-:strip_icc-!!-/2017/01/20/737/n/1922283/fc9b3ccc58823df25109f2.20676134_edit_img_image_17053399_1484928813/i/Belle-Ear-Beauty-Beast-Poster.jpg",
                               "hhttps://www.youtube.com/watch?v=e3Nl_TCQXuw")
logan = movie.Movie("Logan",
                    "Logan's attempts to hide from the world and his legacy are upended when a young mutant arrives, pursued by dark forces.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                    "https://www.youtube.com/watch?v=Div0iP65aZo")
kong = movie.Movie("Kong: Skull Island ",
                   "A team of scientists explore an uncharted island in the Pacific, venturing into the domain of the mighty Kong, and must fight to escape a primal Eden.",
                   "http://t3.gstatic.com/images?q=tbn:ANd9GcS3OOr06uE3lEZwum5WxKkkdsC37ObLwjKZgSSx-V96yrt6DhKE",
                   "https://www.youtube.com/watch?v=44LdLqgOpjo")
lalaland = movie.Movie("La La Land","A jazz pianist falls for an aspiring actress in Los Angeles.",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcRhFtgdSYQ89vUMjMJal2D8H39qBCkh9ptCEoZEsafOzkeQPTu2",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")
#make a list of movies and input it to fresh_tomatoes to ouput movie weebsite!!
movies_list = [toystory,hidden_figures,beauty_and_beast,logan,kong,lalaland]
fresh_tomatoes.open_movies_page(movies_list)
