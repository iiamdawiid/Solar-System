#Solar System Program - Lists all planets in solar system + the sun and displays info after receiving user input -- more stuff being added

class Solar_System():
    """ Contains all solar system planets + sun and their info """
    

    def __init__(self, planet_choice):
        self.planet_choice = planet_choice
    

    def sun(self):
        sun_header = "SUN INFO"
        print(sun_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
        sun_input = input("Enter Selection: ")

        while sun_input not in ['I', 'II', 'III', 'IV']: 
                print("\n**INVALID INPUT** Enter I, II, III, or IV...")
                sun_header = "SUN INFO"
                print(sun_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
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
        
        elif sun_input == 'III':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("The Sun is mostly made up of hydrogen and helium.By mass,\n" 
                  + "the Sun is 92.1% hydrogen and 7.9 percent helium. The remaining\n" 
                  + "0.1 percent of the Sun's mass is made up of metals and other\n" 
                  + "elements.These elements include carbon, nitrogen, oxygen,\n" 
                  + "neon, iron, silicon, magnesium, and sulfur.\n")
            
        elif sun_input == 'IV':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The Sun is a huge, glowing sphere of hot gas. The Sun's\n" 
                  + "surface temperature is about 10,340 degrees Fahrenheit\n" 
                  + "(5,726 degrees Celsius).\n")


    def mercury(self):
        mercury_header = "MERCURY INFO"
        print(mercury_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        mercury_input = input("Enter Selection: ")

        while mercury_input not in ['I', 'II', 'III', 'IV', 'V']:
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                mercury_header = "MERCURY INFO"
                print(mercury_header.center(35, '-')) 
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
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
            
        elif mercury_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Mercury is made up of iron and silica rocks. The planet's composition\n" 
                  + "is estimated to be 70% metals and 30 percent silicate material.Mercury's core\n" 
                  + "is made up of iron-nickel and takes up nearly three-quarters of the\n" 
                  + "planet's diameter. Iron makes up about 70 percent of Mercury's total weight,\n" 
                  + "making it the most iron-rich planet in the Solar System. Mercury's\n" 
                  + "density is the second highest in the Solar System, only slightly less\n" 
                  + "than Earth's density. The planet's exosphere is made up mostly of oxygen,\n" 
                  + "sodium, hydrogen, helium, and potassium.\n")
            
        elif mercury_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The surface temperature of Mercury ranges from 100 to 700 K (−173 to 427 °C;\n" 
                  + "−280 to 800 °F) at the most extreme places. During the day, temperatures on\n" 
                  + "the surface can reach 800 degrees Fahrenheit (430 degrees Celsius). Because\n" 
                  + "the planet has no atmosphere to retain that heat, nighttime temperatures on\n" 
                  + "the surface can drop to minus 290 degrees Fahrenheit (minus 180 degrees Celsius).\n" 
                  + "The mean temperature of Mercury is 333 °F. The average temperature of Mercury's\n" 
                  + "surface is about 354 °F.\n")
            
        


    def venus(self):
        venus_header = "VENUS INFO"
        print(venus_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        venus_input = input("Enter selection: ")

        while venus_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                venus_header = "VENUS INFO"
                print(venus_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                venus_input = input("Enter Selection: ")

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
            
        elif venus_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Venus is a rocky planet with a composition similar to Earth. It has an iron core,\n" 
                  + "a rocky mantle, and a crust of silicate minerals. Its atmosphere is mostly carbon\n" 
                  + "dioxide (96%) and nitrogen (3%), with small amounts of other gases. The atmosphere\n" 
                  + "also contains trace amounts of sulfur dioxide, water vapor, argon, and helium. The\n" 
                  + "sulfur dioxide and sulfuric acid in the atmosphere create a blanket of clouds that\n" 
                  + "shrouds the planet from view.\n")
            
        elif venus_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The surface temperature of Venus is about 900 degrees Fahrenheit (475 degrees Celsius),\n" 
                  + "which is hot enough to melt lead. The average temperature of Venus' surface is about\n" 
                  + "847 °F (from 820 to 900 °F). Venus is the hottest planet in our solar system, even\n" 
                  + "though Mercury is closer to the Sun. The planet's thick atmosphere is primarily made\n" 
                  + "of carbon dioxide and has a pressure 92 times higher than Earth's atmosphere. The\n" 
                  + "atmosphere traps heat, which is why the surface temperature is very hot and does not\n" 
                  + "change much during the seasons. It's believed that Venus may have been a temperate\n" 
                  + "planet hosting liquid water for 2 to 3 billion years before a massive resurfacing\n" 
                  + "event about 700 million years ago triggered a runaway greenhouse effect, which\n" 
                  + "caused the planet's atmosphere to become incredibly dense and hot.\n")
            
        


    def earth(self):
        earth_header = "EARTH"
        print(earth_header.center(35, '-'))
        print("(I) Mass\n(II) Composition\n(III) Temperature")
        earth_input = input("Enter selection: ")

        while earth_input not in ['I', 'II', 'III']: 
                print("\n**INVALID INPUT** Enter I, II, or III...")
                earth_header = "EARTH"
                print(earth_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                earth_input = input("Enter Selection: ")

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
        
        elif earth_input == 'II':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("The mantle is hot and represents about 68 percent of Earth's mass.\n" 
                  + "The core is mostly iron metal. The flow of the liquid outer core\n" 
                  + "generates the Earth's magnetic field. The crust makes up less than\n" 
                  + "1 percent of Earth by mass. There are two types of crust: oceanic and\n" 
                  + "continental. Oceanic crust is denser and thinner and mainly composed of\n" 
                  + "basalt.\n")
            
        elif earth_input == 'III':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The average temperature of the Earth's surface is about 59°F (15°C).\n" 
                  + "This includes both terrestrial and marine environments.\n")
        
        


    def mars(self):
        mars_header = "MARS"
        print(mars_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        mars_input = input("Enter selection: ")

        while mars_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                mars_header = "MARS"
                print(mars_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                mars_input = input("Enter Selection: ")

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
            
        elif mars_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Mars is a rocky planet made of iron, nickel, and sulfur. The planet's core is\n" 
                  + "surrounded by a rocky mantle that's between 770 and 1,170 miles thick. Above\n" 
                  + "the mantle is a crust made of iron, magnesium, aluminum, calcium, and potassium.\n" 
                  + "The crust is between 6 and 30 miles deep. The most abundant elements in the Martian\n" 
                  + "crust are silicon, oxygen, iron, magnesium, aluminum, calcium, and potassium. The\n" 
                  + "oxidation of iron dust gives the surface its reddish hue. Mars' atmosphere is made\n" 
                  + "up of 95 percent carbon dioxide, 3% nitrogen gas, and 1.6 percent argon. The atmospheric\n" 
                  + "pressure at the surface is 6.35 mbar, which is over 100 times less Earth's. Humans\n" 
                  + "therefore cannot breathe Martian air. The dust that covers the surface of Mars is fine\n" 
                  + "like talcum powder. Beneath the layer of dust, the Martian crust consists mostly of\n" 
                  + "volcanic basalt rock. The soil of Mars also holds nutrients such as sodium, potassium,\n" 
                  + "chloride, and magnesium.\n")
            
        elif mars_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The average temperature on Mars is about minus 80 degrees F (minus 60 degrees Celsius).\n" 
                  + "The temperature on Mars can range from as high as 70 degrees Fahrenheit (20 degrees Celsius)\n" 
                  + "to as low as about -225 degrees Fahrenheit (-153 degrees Celsius). Mars's atmosphere is about\n" 
                  + "100 times thinner than Earth's, so it can't retain heat energy. Because of this, heat from the\n" 
                  + "Sun easily escapes the planet. The atmosphere on Mars is also mostly carbon dioxide. In the summer,\n" 
                  + "daytime temperatures on Mars can peak at about 290 K (62 °F, 17 °C). At night, temperatures can\n" 
                  + "rapidly fall to as low as minus 100 degrees Fahrenheit. Temperatures at the poles on Mars are even\n" 
                  + "colder.\n")
            

    

    def jupiter(self):
        jupiter_header = "JUPITER INFO"
        print(jupiter_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        jupiter_input = input("Enter selection: ")

        while jupiter_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                jupiter_header = "JUPITER INFO"
                print(jupiter_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                jupiter_input = input("Enter Selection: ")

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
            
        elif jupiter_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Jupiter is composed of mostly hydrogen and helium, similar to the Sun. The gas giant is 90%\n" 
                  + "hydrogen and 10% helium, with traces of methane, water, ammonia, and rock dust. The hydrogen\n" 
                  + "is a gas in the outer layers of Jupiter, but as you go deeper, the intense atmospheric pressure\n" 
                  + "turns the gas into a dense fluid. This gives Jupiter the largest ocean in the solar system, made\n" 
                  + "of hydrogen instead of water. Jupiter may also have a solid inner core about the size of Earth.\n")
            
        elif jupiter_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("Jupiter is composed of mostly hydrogen and helium, similar to the Sun. The gas giant is 90% hydrogen\n" 
                  + "and 10 percent helium, with traces of methane, water, ammonia, and rock dust. The hydrogen is a gas\n" 
                  + "in the outer layers of Jupiter, but as you go deeper, the intense atmospheric pressure turns the gas\n" 
                  + "into a dense fluid. This gives Jupiter the largest ocean in the solar system, made of hydrogen instead\n" 
                  + "of water. Jupiter may also have a solid inner core about the size of Earth.\n")
            
        


    def saturn(self):
        saturn_header = "SATURN INFO"
        print(saturn_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        saturn_input = input("Enter selection: ")

        while saturn_input not in ['I', 'II', 'III', 'IV', 'V']:
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                saturn_header = "SATURN INFO"
                print(saturn_header.center(35, '-')) 
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                saturn_input = input("Enter Selection: ")

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
            
        elif saturn_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Saturn is a giant gas planet made up of 94% hydrogen, 6 percent helium, and small amounts of methane and ammonia.\n" 
                  + "It also contains traces of ices containing ammonia, methane, and water. Scientists believe that Saturn may have\n" 
                  + "a molten, rocky core about the size of Earth deep within it. This core is thought to be made up of iron and nickel\n" 
                  + "and surrounded by several layers of hydrogen and helium in different phases. The intense pressure and heat within\n" 
                  + "Saturn are so great that these gases are compressed into liquids and metals. Saturn's atmosphere is similar to\n" 
                  + "Jupiter's, but is much less interesting to look at from a distance.\n")
            
        elif saturn_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("Saturn's average temperature is -288 degrees Fahrenheit (-178 degrees Celsius). The planet's temperature varies\n" 
                  + "horizontally, with some small differences as you travel from the equator to the poles. The top layer of Saturn's\n" 
                  + "atmosphere has a temperature range of -173 degrees Celsius (-280 degrees Fahrenheit) to -113 degrees Celsius\n" 
                  + "(-170 degrees Fahrenheit). Saturn's environment is not conducive to life as we know it. The temperatures,\n" 
                  + "pressures, and materials on the planet are likely too extreme and volatile for organisms to adapt to.\n")
        
        


    def uranus(self):
        uranus_header = "URANUS INFO"
        print(uranus_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        uranus_input = input("Enter selection: ")

        while uranus_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                uranus_header = "URANUS INFO"
                print(uranus_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                uranus_input = input("Enter Selection: ")

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
            
        elif uranus_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Uranus is an ice giant, a type of planet that is mostly made up of water, ammonia, and methane in solid form. Uranus has three\n" 
                  + "layers: Iron-nickel core: A small core in the center - Icy mantle: A middle layer - Hydrogen, helium, and methane atmosphere:\n" 
                  + "An outer gaseous layer Uranus' atmosphere is made up of 82.5% hydrogen, 15.2 percent helium, and 2.3% methane. The planet's\n" 
                  + "mass is made up of more than 80 percent hot dense fluids of water, methane, and ammonia. Near the core, the planet heats up\n" 
                  + "to 9,000 degrees Fahrenheit (4,982 degrees Celsius).\n")
            
        elif uranus_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The mean temperature of Uranus is -320 °F (-195 °C). The average temperature of Uranus' surface is about -353 °F. The average\n" 
                  + "temperature within Uranus' clouds is -315 °F. Uranus is the coldest planet in the solar system. The planet's temperature\n" 
                  + "doesn't change much because it is so far away from the Sun. The reason Uranus is so cold is partly due to its distance\n" 
                  + "from the Sun, but also because billions of years ago, something big crashed into Uranus, causing a large amount of energy\n" 
                  + "and heat to escape from its core.\n")
        
        

    
    def neptune(self):
        neptune_header = "NEPTUNE INFO"
        print(neptune_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
        neptune_input = input("Enter selection: ")

        while neptune_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                neptune_header = "NEPTUNE INFO"
                print(neptune_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                neptune_input = input("Enter Selection: ")

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
            
        elif neptune_input == 'IV':
            composition = "COMPOSITION"
            print(composition.center(35, '-'))
            print("Neptune is made up of a thick soup of water, ammonia, and methane over a solid center about the size of Earth. The\n" 
                  + "planet's atmosphere is made of hydrogen, helium, and methane. The surface of Neptune is composed of about 80%\n" 
                  + "hydrogen and 19 percent helium, with a trace amount of methane. Neptune is one of two ice giants in the outer solar\n" 
                  + "system (the other is Uranus). It is the densest of the giant planets. The methane in Neptune's atmosphere gives it\n" 
                  + "its striking blue hue.\n")
            
        elif neptune_input == 'V':
            temperature = "TEMPERATURE"
            print(temperature.center(35, '-'))
            print("The average temperature on Neptune is about -392°F (-200°C). This is much colder than Earth's average temperature\n" 
                  + "of 15°C. Neptune is the farthest known planet in our solar system, located about 30 times farther away from the\n" 
                  + "sun than Earth. Only about one thousandth of the sunlight received by Earth reaches Neptune. Neptune lacks a solid\n" 
                  + "surface and is instead surrounded by cold clouds. Temperatures within these clouds vary from -240°F to -330°F. At\n" 
                  + "its core, Neptune reaches temperatures of up to 12,632°F (7,000°C), which is comparable to the surface of the Sun.\n" 
                  + "The huge temperature differences between Neptune's center and its surface create huge wind storms, which can reach\n" 
                  + "as high as 2,100 km/hour.\n")
            
        



def program_start():
    
    flag_ = True  
    c_str = "Space Program"
    print(c_str.center(35, '-'))
    return flag_

def planet_selection():
    solar_system = "SOLAR SYSTEM"
    print(solar_system.center(35, '-'))
    print("(I) Sun\n(II) Mercury\n(III) Venus\n(IV) Earth\n(V) Mars\n(VI) Jupiter\n"
          + "(VII) Saturn\n(VIII) Uranus\n(IX) Neptune\n")
    planet_choice = input("Select a Planet or the Sun or enter Q to Quit: ")
    return planet_choice


# main
flag = program_start()
while flag:
        
        start = input("Enter C to Continue or Q to Quit: ")
        while start != 'C' and start != 'Q':
            start = input("\n**INVALID INPUT**\nEnter C to Continue or Q to Quit: ")
        
        if start == 'Q':
            flag = False
        
        elif start == 'C':
            
            # call program to list planets
            p_select = planet_selection()
            planet = Solar_System(p_select)
        
            while p_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'Q']:
                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                p_select = planet_selection()

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
            end_case = input("\n**INVALID INPUT**\nEnter C to Continue or Q to Quit: ")
            if end_case == 'Q':
                flag = False
