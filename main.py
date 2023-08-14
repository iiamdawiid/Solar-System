class Planet():
    """ Holds all the Planet's """
    

    def __init__(self, planet_choice):
        self.planet_choice = planet_choice
    

    def sun(self):
        sun_header = "SUN INFO"
        print(sun_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth")
        sun_input = input("Enter Selection: ")
        
        if sun_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The sun is 1.9891 x 10^30 kilograms, or about 333,000\n"
                  + "times the mass of the Earth!\n")
            
        elif sun_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("Earth's average distance from the Sun is about 93 million\n"
                  + "miles, it would take you 19 years to reach the Sun on a\n"
                  + "plane travelling at 885 km/h (550 mph) or 177 years to \n"
                  + "drive at 96 km/h(60 mph) or 3,536 years to walk there at\n"
                  + "4.8km/h(3 mph).\n")
            
        else:
            print("\n**INVALID INPUT**\n")


    def mercury(self):
        mercury_header = "MERCURY INFO"
        print(mercury_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        mercury_input = input("Enter Selection: ")

        if mercury_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("Mercury is 3.285 x 10^23 kilograms, only about 0.055\n"
                  + "times that of Earth!\n")
            
        elif mercury_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The average distance between Mercury and Earth is 56.97 million\n"
                  + "miles. Mercury is 48 million miles from Earth, and at their\n" 
                  + "furthest, it is 138 million miles from Earth. The distance\n" 
                  + "between Mercury and Earth is constantly changing because they\n" 
                  + "follow elliptical orbits around the sun.\n")
            
        elif mercury_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("Since Mercury is the fastest planet and has the shortest distance\n" 
                  + "to travel around the Sun, it has the shortest year of all the\n" 
                  + "planets in our solar system - 88 days.\n")
            
        else:
            print("\n**INVALID INPUT**\n")


    def venus(self):
        venus_header = "VENUS INFO"
        print(venus_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        venus_input = input("Enter selection: ")

        if venus_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Venus is approximately 4.868×1024 kilograms,\n" 
                  + "or 1.073×1025 pounds. This is around 82 percent of Earth's\n" 
                  + "mass.\n")
        
        elif venus_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The average distance from Venus to Earth is 25.7 million miles\n" 
                  + "or 0.28 AU. The maximum distance between the two planets is 162\n" 
                  + "million miles, while the minimum distance is 23.6 million miles.\n" 
                  + "Venus comes closer to Earth than any other planet, though most of the\n" 
                  + "time, Mercury is closer.\n")
        
        elif venus_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("Venus rotates very slowly on its axis – one day on Venus lasts 243 Earth\n" 
                  + "days. The planet orbits the Sun faster than Earth, however, so one year on\n" 
                  + "Venus takes only about 225 Earth days, making a Venusian day longer than its year!\n")
            
        else:
            print("\n**INVALID INPUT**\n")


    def earth(self):
        earth_header = "EARTH"
        print(earth_header.center(35, '-'))
        print("(I) Mass")
        earth_input = input("Enter selection: ")

        if earth_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Earth is approximately 5.9742 × 1024 kg,\n" 
                  + "or 1.31629 × 1025 lbs. You can also think of Earth's\n" 
                  + "mass as 5.9 sextillion tonnes or 6000 trillion tons.\n"
                  + "Earth's mass makes it the fourth-largest planet by mass\n" 
                  + "in the solar system. It's difficult to precisely measure\n" 
                  + "the mass of a planet due to its size, so this figure has\n" 
                  + "changed over time as we have found better measuring methods.\n")
        
        else:
            print("\n**INVALID INPUT**\n")


    def mars(self):
        mars_header = "MARS"
        print(mars_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        mars_input = input("Enter selection: ")

        if mars_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Mars is 6.41 x 10^23 kilograms or 1.41 x 10^24 pounds. This is\n" 
                  + "roughly 0.11 times the mass of Earth. Mars is the second smallest planet in\n" 
                  + "the Solar System. Mars's smaller mass means that the force of gravity on Mars\n" 
                  + "is much weaker than it is on Earth. Gravity on Mars is 38 percent of Earth's\n" 
                  + "gravity, so a 100-pound person on Earth would weigh 38 pounds on Mars.\n")
            
        elif mars_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The average distance between Earth and Mars is 140 million miles (225 million km).\n"
                  + "The minimum distance from Earth to Mars is about 33.9 million miles (54.6 million\n" 
                  + "kilometers). The maximum distance between Mars and Earth is 250 million miles\n" 
                  + "(401 million km). It would take about seven months and about 300 million miles\n" 
                  + "(480 million kilometers) to travel to Mars by spacecraft.\n")
            
        elif mars_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("A year on Mars lasts 687 Earth days, or 669.6 sols, which is short for 'solar day'.\n" 
                  + "This is roughly 1.88 times the length of a year on Earth. Because Mars is farther\n" 
                  + "from the sun, it takes Mars about twice as long as it does for Earth to make one\n" 
                  + "circle around the sun.\n")
            
        else:
            print("\n**INVALID INPUT**\n")
    

    def jupiter(self):
        jupiter_header = "JUPITER INFO"
        print(jupiter_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        jupiter_input = input("Enter selection: ")

        if jupiter_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("Jupiter's mass is 1.899 x 1027 kg, or 317.8 Earth masses. This is 2.5 times the mass\n" 
                  + "of all the other planets in our Solar System combined. Jupiter is also about 1⁄1000\n" 
                  + "as massive as the sun. Jupiter is made up of mostly hydrogen and helium. Because it's\n" 
                  + "made of gas rather than rock, it's only a fifth as dense as Earth.\n")
            
        elif jupiter_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("Jupiter is currently about 440,560,000 miles from Earth. The distance between Jupiter and\n" 
                  + "Earth is constantly changing because they follow elliptical orbits around the sun. On\n"
                  + "average, Jupiter is 444 million miles from Earth. At their closest points, Jupiter and\n" 
                  + "Earth are 365 million miles apart, and at their farthest points, they are 601 million\n" 
                  + "miles apart. The closest and farthest distances between Jupiter and Earth happen every\n" 
                  + "13 months.\n")
            
        elif jupiter_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("A year on Jupiter is 11.862 Earth years, or 4,332.59 Earth days. This is because it takes\n" 
                  + "Jupiter about 12 Earth years to complete an orbit around the Sun. The long year is due to\n" 
                  + "Jupiter's extreme distance from the sun. A day on Jupiter is just under 10 hours long, which\n" 
                  + "is much shorter than an Earth day.\n")
            
        else:
            print("\n**INVALID INPUT**\n")


    def saturn(self):
        saturn_header = "SATURN INFO"
        print(saturn_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        saturn_input = input("Enter selection: ")

        if saturn_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Saturn is 5.683 × 1026 kilograms, or 1.253 × 1027 pounds. This is about 95 times\n" 
                  + "the mass of Earth. Saturn is the second most massive planet in the Solar System. Saturn's\n" 
                  + "mass is due to its massive size and being made entirely of gas. It has a low mean density\n" 
                  + "of 0.687 g/cm³, making it the only planet in the Solar System that is less dense than water.\n")
            
        elif saturn_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The distance between Saturn and Earth is constantly changing because both planets are moving in\n" 
                  + "elliptical orbits around the sun. The average distance between Saturn and Earth is 792 million\n" 
                  + "miles or 8.52 AUs. When the planets are at their closest, they are about 1.74 billion miles apart,\n" 
                  + "or eight times the distance between Earth and the sun. When they are at their furthest, they are about\n" 
                  + "746 million miles apart.\n")
            
        elif saturn_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("A year on Saturn is 29.4571 Earth years, or 10,759.22 Earth days. This is because Saturn is nearly 10 times\n"
                  + "farther from the sun than Earth. A day on Saturn is about 10.5 hours long. There are 10,475.8 Saturnian days\n" 
                  + "in one Saturnian year. Although the timings are different, Saturn experiences seasons like Earth since the planet\n" 
                  + "is on a tilt.\n")
        
        else:
            print("\n**INVALID INPUT**\n")


    def uranus(self):
        uranus_header = "URANUS INFO"
        print(uranus_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        uranus_input = input("Enter selection: ")

        if uranus_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Uranus is 8.681000e+25 kg, or 14.54 times the mass of Earth. Uranus is the third largest planet in the\n" 
                  + "Solar System and has a diameter of approximately 31,000 miles. Because Uranus is a gas giant planet, you would only\n" 
                  + "weigh about 89 percent of your weight on Earth if you could stand on the surface of Uranus.\n")
            
        elif uranus_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The average distance between Uranus and Earth is 1.7 billion miles, or 18.21 AUs. The closest Uranus gets to Earth is\n" 
                  + "1.6 billion miles, and the farthest it gets is 1.98 billion miles. The distance between Uranus and Earth is constantly\n" 
                  + "changing because they both orbit the sun. It takes light 2 hours, 44 minutes, and 30.7118 seconds to travel from Uranus\n" 
                  + "to Earth.\n")
            
        elif uranus_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("A year on Uranus is 84 Earth years long, or 30,688.5 Earth days. Uranus takes 84 years to complete one orbit around the sun.\n" 
                  + "This means that each of Uranus' four seasons lasts 21 Earth years. Uranus has a nearly circular orbit, so it always remains\n" 
                  + "at roughly the same distance from the sun. Uranus' rotation axis is tilted almost parallel to its orbital plane, so Uranus\n" 
                  + "appears to be rotating on its side.\n")
        
        else:
            print("\n**INVALID INPUT**\n")

    
    def neptune(self):
        neptune_header = "NEPTUNE INFO"
        print(neptune_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year")
        neptune_input = input("Enter selection: ")

        if neptune_input == 'I':
            mass_info = "MASS"
            print(mass_info.center(35, '-'))
            print("The mass of Neptune is 1.024 × 1026 kilograms, or 2.258 × 1026 pounds. This is approximately 17 times the mass of Earth.\n" 
                  + "Neptune is a gas giant and ranks third in terms of mass, ahead of Uranus. It is made up of mostly gas and ice.\n")
            
        elif neptune_input == 'II':
            distance_f_earth = "DISTANCE FROM EARTH"
            print(distance_f_earth.center(35, '-'))
            print("The average distance between Neptune and Earth is 2.703 billion miles or 29.09 AUs.The distance between the two planets\n" 
                  + "is constantly changing as they orbit the sun. When the planets are on the same side of the sun, they are about 2.7\n" 
                  + "billion miles apart. When they are on opposite sides of the sun, the distance is about 2.9 billion miles.\n")
            
        elif neptune_input == 'III':
            length_of_year = "LENGTH OF YEAR"
            print(length_of_year.center(35, '-'))
            print("A year on Neptune is 164.8 Earth years, or 60,182 Earth days. A year is the time it takes a planet to orbit the Sun.\n" 
                  + "Neptune is the eighth planet from the Sun and has an extremely wide orbit and a comparatively slow orbital velocity.\n" 
                  + "As a result, a year on Neptune is very long. One day on Neptune is just over 16 hours long.\n")
            
        else:
            print("\n**INVALID INPUT**\n")



def program_start():
    
    flag_ = True  
    c_str = "Space Program"
    print(c_str.center(35, '-'))
    return flag_

def planet_selection():
    print("(I) Sun\n(II) Mercury\n(III) Venus\n(IV) Earth\n(V) Mars\n(VI) Jupiter\n"
          + "(VII) Saturn\n(VIII) Uranus\n(IX) Neptune\n")
    planet_choice = input("Select a Planet or the Sun or enter Q to Quit: ")
    return planet_choice


# main
flag = program_start()
while flag:
        
        start = input("Enter C to Continue or Q to Quit: ")
        
        if start == 'Q':
            flag = False
        
        elif start == 'C':
            
            # call program to list planets
            p_select = planet_selection()
            planet = Planet(p_select)

            if p_select == 'I':
                planet.sun()

            elif p_select == 'II':
                planet.mercury()

            elif p_select == 'III':
                planet.venus()

            elif p_select == 'IV':
                planet.earth()

            elif p_select == 'V':
                planet.mars()
            
            elif p_select == 'VI':
                planet.jupiter()

            elif p_select == 'VII':
                planet.saturn()

            elif p_select == 'VIII':
                planet.uranus()

            elif p_select == 'IX':
                planet.neptune()

            elif p_select == 'Q':
                flag = False

            else:
                print("\n**INVALID INPUT**\n")

        else:
            end_case = input("\n**INVALID INPUT**\nEnter C to Continue or Q to Quit: ")
            if end_case == 'Q':
                flag = False
