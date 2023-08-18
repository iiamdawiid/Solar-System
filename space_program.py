# Space Program - Contains information about objects in space such as solar system planets + sun, stars in the universe, blackholes, exoplanets

class Solar_System():
    """ Contains all solar system planets + sun and their info """
    
    def __init__(self, planet_choice):
        self.planet_choice = planet_choice
    
    def sun(self):
        sun_header = "SUN INFO"
        print(sun_header.center(35, '-'))
        print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
        sun_input = input("Enter Selection: ")
        sun_input = sun_input.upper()  
        print("\n")

        while sun_input not in ['I', 'II', 'III', 'IV']: 
                print("\n**INVALID INPUT** Enter I, II, III, or IV...")
                sun_header = "SUN INFO"
                print(sun_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Composition\n(IV) Temperature")
                sun_input = input("Enter Selection: ")
                sun_input = sun_input.upper()
        
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
        mercury_input = mercury_input.upper()
        print("\n")

        while mercury_input not in ['I', 'II', 'III', 'IV', 'V']:
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                mercury_header = "MERCURY INFO"
                print(mercury_header.center(35, '-')) 
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        venus_input = venus_input.upper()
        print("\n")

        while venus_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                venus_header = "VENUS INFO"
                print(venus_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        earth_input = earth_input.upper()
        print("\n")

        while earth_input not in ['I', 'II', 'III']: 
                print("\n**INVALID INPUT** Enter I, II, or III...")
                earth_header = "EARTH"
                print(earth_header.center(35, '-'))
                print("(I) Mass\n(II) Composition\n(III) Temperature")
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
        mars_input = mars_input.upper()
        print("\n")

        while mars_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                mars_header = "MARS"
                print(mars_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        jupiter_input = jupiter_input.upper()
        print("\n")

        while jupiter_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                jupiter_header = "JUPITER INFO"
                print(jupiter_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        saturn_input = saturn_input.upper()
        print("\n")

        while saturn_input not in ['I', 'II', 'III', 'IV', 'V']:
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                saturn_header = "SATURN INFO"
                print(saturn_header.center(35, '-')) 
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        uranus_input = uranus_input.upper()
        print("\n")

        while uranus_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                uranus_header = "URANUS INFO"
                print(uranus_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
        neptune_input = neptune_input.upper()
        print("\n")

        while neptune_input not in ['I', 'II', 'III', 'IV', 'V']: 
                print("\n**INVALID INPUT** Enter I, II, III, IV, or V...")
                neptune_header = "NEPTUNE INFO"
                print(neptune_header.center(35, '-'))
                print("(I) Mass\n(II) Distance from Earth\n(III) Length of Year\n(IV) Composition\n(V) Temperature")
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
            


class Stars():
    """ Holds all the functions for the star menu option """
    
    def __init__(self, star_choice):
        self.star_choice = star_choice

    def what_is_star(self):
        star_def = "WHAT IS A STAR"
        print(star_def.center(35, '-'))
        print("A star is a massive, self-luminous celestial body of gas that shines with radiation from its internal energy sources.\n" 
              + "Stars are made of mostly hydrogen and helium gas and are held together by their own gravity. Stars shine because of\n" 
              + "nuclear fusion, a process that occurs in the core of a star. In this process, hydrogen atoms smash together to form\n" 
              + "helium, releasing huge amounts of energy that heats the gas. This process also produces photons and heat, as well as\n" 
              + "small amounts of heavier elements. Stars are a fundamental component of the universe and collectively form star\n" 
              + "clusters, galaxies, and galaxy clusters. The nearest star to Earth is the Sun. Only a very small percentage of\n" 
              + "the tens of billions of trillions of stars in the observable universe are visible to the naked eye.\n")
        
    def star_composition(self):
        star_comp = "STAR COMPOSITION"
        print(star_comp.center(35, '-'))
        print("Stars are made of very hot gases, mostly hydrogen and helium, the two lightest elements in the universe. Stars\n" 
              + "also contain small amounts of other elements, such as oxygen, nitrogen, and carbon. Most stars in the galaxy\n" 
              + "are chemically similar to the sun, which is about 74% hydrogen, 24 percent helium, and 2 percent other elements.\n" 
              + "The elements heavier than helium are conventionally grouped together under the term metals. Stars are so big that\n" 
              + "they have enormous mass, even though they're made of light gases.\n")
        
    def star_formation(self):
        star_form = "STAR FORMATION"
        print(star_form.center(35, '-'))
        print("Stars form from a large cloud of gas and dust in space that slowly contracts due to gravity. The cloud fragments\n" 
              + "into clumps, which then collapse into stars. The process takes around a million years. The force of gravity\n" 
              + "compresses atoms in the interstellar gas until the fusion reactions begin. The fusion process involves the\n" 
              + "combining of light chemical nuclei to form heavier ones. This process releases energy such as light and\n" 
              + "ultraviolet radiation, which is responsible for the luminosity of stars. Depending on their mass, stars\n" 
              + "can evolve into white dwarfs, neutron stars, or black holes.\n")
        
    def biggest_stars(self):
        big_stars = "BIGGEST STARS IN THE UNIVERSE"
        print(big_stars.center(35, '-'))
        print("(I) VY Canis Majoris\n(II) WOH G64\n(III) V354 Cephei\n(IV) UY Scuti\n(V) KY Cygni")
        big_star_choice = input("Select a choice or enter Q to Quit: ")
        big_star_choice = big_star_choice.upper()
        print("\n")
        return big_star_choice
    
    def canis_majoris(self):
        canis = "VY CANIS MAJORIS"
        print(canis.center(35, '-'))
        print("VY Canis Majoris (VY CMa) is a red supergiant or red hypergiant star located in the constellation Canis Major,\n" 
              + "which means 'great dog' in Latin. VY Canis Majoris is one of the largest known stars, with an estimated radius\n" 
              + "at least 1,420 times that of the Sun. The star is also around 270,000 times brighter than our sun. VY Canis\n" 
              + "Majoris is located approximately 3,820 light-years from Earth. It is estimated to have around 17 solar\n" 
              + "masses. If placed in our Solar System, VY Canis Majoris would extend out to the orbit of Saturn. Hypergiant\n" 
              + "stars like VY Canis Majoris are extremely rare in our galaxy. Most stars in the Milky Way are smaller than the sun.\n")

    def woh(self):
        woh = "WOH G64"
        print(woh.center(35, '-'))
        print("WOH G64 is a red supergiant star located in the Large Magellanic Cloud (LMC). It's one of the largest stars discovered\n" 
              + "so far, and is thought to be the largest star in the LMC. WOH G64 has a number of properties that set it apart from\n" 
              + "other red supergiants in the LMC, including: A thick circumstellar dust torus, An unusually late spectral type, Maser\n" 
              + "activity, Nebular emission lines. WOH G64 was discovered in 1981. It's located in the constellation Dorado, and is\n" 
              + "160,000 light years from Earth.\n")

    def cephei(self):
        cephei = "V354 Cephei"
        print(cephei.center(35, '-'))
        print("V354 Cephei is a red supergiant star located in the constellation Cepheus. It is one of the largest known stars, with\n" 
              + "a diameter between 690 and 1,520 times bigger than the Sun. V354 Cephei is located within the Milky Way, about 8,900\n" 
              + "light-years away from the Sun. It has an estimated radius of 685 solar radii, or 477,000,000 km. V354 Cephei is an\n" 
              + "irregular variable star.\n")

    def scuti(self):
        scuti = "UY SCUTI"
        print(scuti.center(35, '-'))
        print("UY Scuti is a red hypergiant or red supergiant star located in the constellation Scutum. It is considered one of the\n" 
              + "largest known stars by radius. UY Scuti has an estimated radius of 1,708 solar radii, which is around 1,700 times\n" 
              + "larger than the Sun. It has a maximum brightness of magnitude 8.29 and a minimum of magnitude 10.56. UY Scuti is\n" 
              + "also classified as a pulsating variable star, with an approximate pulsation period of 740 days. It is a dust-\n"
              + "enshrouded bright red supergiant. UY Scuti was discovered in 1860. It is approximately 9,500 light-years away.\n"
              + "from earth.\n")

    def cygni(self):
        cygni = "KY CYGNI"
        print(cygni.center(35, '-'))
        print("KY Cygni is a red supergiant star in the Cygnus constellation. It is one of the largest stars known, with a radius\n" 
              + "of about 1,420–1,503 R☉ (6.60–6.99 au). If it were placed at the center of the Solar System, it would extend past\n" 
              + "the orbit of Jupiter (or Saturn). KY Cygni was discovered in 1930. It is not visible from Earth because it emits a\n" 
              + "large amount of light in the infrared spectrum and the blocking effect of interstellar dust on the visible component.\n" 
              + "KY Cygni is losing mass at around 4.9×10−6 M ☉ and has been described as a cool hypergiant. Its surface temperature\n" 
              + "is around 3,500 K. It is approximately 5,000 light-years away from Earth.\n")
        


class Blackholes():
    """ Holds all the options for blackholes """

    def __init__(self, blackhole_choice):
        self.blackhole_choice = blackhole_choice

    def what_is_blackhole(self):
        what_is_blackhole = "WHAT ARE BLACK HOLES?"
        print(what_is_blackhole.center(35, '-'))
        print("A black hole is a region of space where gravity is so strong that nothing, including light, can escape it. The gravity\n" 
              + "is so strong because matter has been squeezed into a tiny space. This can happen when a star is dying. Black holes are\n" 
              + "invisible because no light can get out. However, the material around a black hole is visible. Material falling into a\n" 
              + "black hole forms a disk, similar to a whirlpool in a bathtub drain. Black holes can recycle cosmological debris, stabilize\n" 
              + "the formation of galaxies, define the shape of galaxies, and stratify space around them.\n")
        
    def blackhole_formation(self):
        blackhole_formation = "HOW DO BLACK HOLES FORM"
        print(blackhole_formation.center(35, '-'))
        print("Black holes form when an object reaches a critical density, and its gravity causes it to collapse to an almost infinitely\n" 
              + "small pinpoint. Stellar black holes form when the center of a very massive star collapses in on itself. This collapse also\n" 
              + "causes a supernova, or an exploding star, that blasts part of the star into space. Black holes take up zero space, but do\n" 
              + "have mass. A black hole can have a mass of tens of times the mass of the Sun. It was long thought that black holes are\n" 
              + "impossible to destroy. But we now know that black holes actually evaporate, slowly returning their energy to the Universe.\n")

    def inside_blackhole(self):
        inside_blackhole = "WHAT IS INSIDE A BLACK HOLE"
        print(inside_blackhole.center(35, '-'))
        print("The center of a black hole contains a singularity, which is a point that is infinitely small and dense. The singularity is made\n" 
              + "of matter that is compressed into an infinitely tiny point, breaking down all conceptions of time and space. Singularities are\n" 
              + "mathematically impossible. Black holes also have an event horizon, which is the surface of the black hole where gravity is too\n" 
              + "strong for anything to escape.\n")

    def enter_blackhole(self):
        enter_blackhole = "ENTERING A BLACK HOLE"
        print(enter_blackhole.center(35, '-'))
        print("If you fell into a black hole, you would be torn apart by the extreme gravity. The intense gravity would pull you apart, separating\n" 
              + "your bones, muscles, sinews, and even molecules. This process is called 'spaghettification'. You would be 'spaghettified' by the\n" 
              + "black hole's tidal forces even before you reach the event horizon, the point of no return. The event horizon is the point at which\n" 
              + "the gravitational pull becomes so strong that you can't escape. No material, especially fleshy human bodies, could survive intact.\n" 
              + "Once you pass beyond the event horizon, there's no getting out.\n")

    def nearest_bh_earth(self):
        nearest_bh = "NEAREST BLACK HOLE TO EARTH"
        print(nearest_bh.center(35, '-'))
        print("The nearest known black hole to Earth is Gaia BH1, which is 1,560 light-years away in the direction of the constellation Ophiuchus.\n" 
              + "It was discovered in September 2022 by a team led by Kareem El-Badry. Gaia BH1 is about three times closer to Earth than the\n" 
              + "previous record holder. It is about ten times the size of the Sun and has a Sun-like star orbiting it. Astronomers were able\n" 
              + "to determine the black hole was there by looking at the behavior of a star near the black hole, despite never seeing it directly.\n")

    def biggest_blackholes(self):
        biggest_blackholes = "BIGGEST BLACK HOLES"
        print(biggest_blackholes.center(35, '-'))
        print("(I) Phoenix A\n(II) TON 618\n(III) Holm 15A\n(IV) IC 1101\n(V) S5 0014+81")
        blackhole_choice = input("Select a choice or enter Q to Quit: ")
        blackhole_choice = blackhole_choice.upper()
        print("\n")
        return blackhole_choice
    
    def phoenix_a(self):
        phoenix_a = "PHOENIX A"
        print(phoenix_a.center(35, '-'))
        print("The Phoenix-A Black Hole is the largest and most massive black hole ever discovered. It has a mass of 100 billion solar masses,\n" 
              + "which is 100 billion times more massive than the sun. The Phoenix-A Black Hole is located in the Phoenix Cluster, approximately\n" 
              + "5.8 to 8.57 billion light years away from Earth. The Phoenix Cluster is one of the most intensely studied galaxy clusters in our\n" 
              + "universe. While black holes typically form when massive stars die in supernova explosions, the Phoenix-A Black Hole is probably\n" 
              + "the result of the collision of multiple supermassive black holes that formed shortly after the big bang.\n")

    def ton_618(self):
        ton_618 = "TON 618"
        print(ton_618.center(35, '-'))
        print("TON 618 is a quasar that contains the largest, brightest, and most massive black hole known. It is located in the constellation Canes\n" 
              + "Venatici, 18.2 billion light-years away. The black hole is 66 billion times more massive than the Sun, and 11 solar systems could fit\n" 
              + "inside it. The Lyman-alpha nebula surrounding TON 618 has a diameter of at least 100 kiloparsecs (320,000 light-years), which is twice\n" 
              + "the size of the Milky Way. The light from the quasar is estimated to be 10.8 billion years old. TON 618 is not visible from Earth\n" 
              + "because the quasar outshines the surrounding galaxy.\n")

    def holm_15A(self):
        holm_15A = "HOLM 15A"
        print(holm_15A.center(35, '-'))
        print("The black hole at the center of Holm 15A is a supermassive black hole with a mass of 40 billion solar masses, or 40 billion times the\n" 
              + "mass of the Sun. This makes it one of the largest black holes ever discovered. The black hole is located in the elliptical galaxy\n" 
              + "Holm 15A, which is the dominant galaxy in the Abell 85 galaxy cluster. The black hole is 700 million light years away from Earth.\n" 
              + "To calculate the black hole's mass, astronomers took a snapshot of the stars orbiting the black hole and created a model. The black\n" 
              + "hole is much larger than the Milky Way's central black hole, Sagittarius A*, which has a mass of 4 million solar masses.\n")

    def ic_1101(self):
        ic_1101 = "IC 1101"
        print(ic_1101.center(35, '-'))
        print("The black hole in IC 1101 is a supermassive black hole with an estimated mass of 50 to 70 billion solar masses. This is one of the\n" 
              + "largest black holes ever detected. The black hole is located at the center of IC 1101 and is associated with a bright radio source\n" 
              + "that emits two jets. IC 1101 is a supergiant elliptical galaxy, which means it is devoid of gas and has a very low star formation\n" 
              + "rate. The galaxy is located at 354.0 megaparsecs (1.15 billion light-years) from Earth.\n")

    def s5_0014(self):
        s5_0014 = "S5 0014+81"
        print(s5_0014.center(35, '-'))
        print("S5 0014+81 is a supermassive black hole with a mass of 40 billion solar masses. It is located in the constellation of Cepheus, 12.1\n" 
              + "billion light years from Earth. The black hole was formed 1.6 billion years after the Big Bang. S5 0014+81 has a diameter of 240\n" 
              + "billion kilometers, which is more than 20 times the orbit of Pluto. It is also producing a quasar that is one of the brightest\n" 
              + "known objects in the universe. The quasar has a brightness of 300 trillion suns. S5 0014+81 is estimated to consume 4,000 solar\n" 
              + "masses of matter annually. It is also a strong source of radiation, including gamma, X-ray, and radio waves.\n")
        


class Exoplanets():
    """ Contains info and options for exo planets """

    def __init__(self, exoplanet_choice):
        self.exoplanet_choice = exoplanet_choice

    def what_is_exoplanet(self):
        what_is_exoplanet = "WHAT IS AN EXOPLANET"
        print(what_is_exoplanet.center(35, '-'))
        print("An exoplanet is a planet that is located outside our Solar System. The prefix 'exo' comes from the Greek and means 'outside'.\n" 
              + "Exoplanets are planets that orbit a star other than our sun. They are very hard to see directly with telescopes because they\n" 
              + "are hidden by the bright glare of the stars they orbit. Astronomers have confirmed more than 5,000 exoplanets orbiting distant\n" 
              + "stars. Among the most prevalent is a class of worlds dubbed 'super-Earths' which are worlds ranging from some 30 to 70 percent\n" 
              + "bigger than Earth. Scientists have categorized exoplanets into the following types: Gas giant, Neptunian, super-Earth and terrestrial.\n")
        
    def how_many_exoplanets(self):
        how_many_exoplanets = "HOW MANY EXOPLANETS ARE THERE"
        print(how_many_exoplanets.center(35, '-'))
        print("As of August 11, 2023, there are 5,496 confirmed exoplanets in 4,091 planetary systems. Most of these exoplanets were discovered\n" 
              + "by the Kepler space telescope. Exoplanets are planets outside the Solar System that orbit a star. Scientists discovered the\n" 
              + "first exoplanets in the 1990s. NASA estimates that there are over 100 billion exoplanets in our galaxy. Most of the exoplanets\n" 
              + "discovered so far are in a relatively small region of our galaxy, the Milky Way.\n")
        
    def unique_exoplanets(self):
        unique_exoplanets = "MOST UNIQUE EXOPLANETS"
        print(unique_exoplanets.center(35, '-'))
        print("(I) Kepler-186f\n(II) 55 Cancri e\n(III) Kepler-22b\n(IV) CoRoT-7b\n"
              + "(V) Kepler-452b\n(VI) TrES-2b\n(VII) WASP-12b\n(VIII) Kepler-16b")
        exo_choice = input("Select a choice or enter Q to Quit: ")
        exo_choice = exo_choice.upper()
        print("\n")
        return exo_choice
    
    def kepler_186f(self):
        kepler_186f = "KEPLER-186F"
        print(kepler_186f.center(35, '-'))
        print("Kepler-186f is an Earth-sized planet that was discovered in the habitable zone of a star other than our sun. The planet is located\n" 
              + "in the Cygnus constellation, about 500 light-years from Earth. It was discovered on April 17, 2014 by Elisa Quintana. Kepler-186f\n" 
              + "has a mean radius of 4,631.7 miles and a diameter of 9,263.5 miles. It has an orbital period of 130 days. Kepler-186f is on the\n" 
              + "outer edge of the habitable zone, where it's possible that the planet's water could freeze. However, its larger size could mean\n" 
              + "that it has a thicker atmosphere, which could insulate the planet. \n")

    def cancri(self):
        cancri = "55 CANCRI E"
        print(cancri.center(35, '-'))
        print("55 Cancri e is an exoplanet located in the Milky Way Galaxy that is about twice the size of Earth. It has a surface temperature\n" 
              + "of nearly 4,900 degrees Fahrenheit (2,700 degrees Celsius). 55 Cancri e has a mean radius of 7,422.7 miles and a diameter of\n" 
              + "14,845 miles. It has an orbital period of 18 hours and a gravity of 20.99 m/s². Scientists believe that 55 Cancri e is made\n" 
              + "up of mostly carbon, which has been compressed to form diamond. It's estimated that the planet could contain as much as three\n" 
              + "times the amount of diamond that has ever been mined on Earth. 55 Cancri e was dubbed the 'diamond planet' because scientists\n" 
              + "suggested that it was composed of diamonds and graphite. The exoplanet 55 Cancri e is about 41 light years away from Earth.\n" 
              + "It orbits the star 55 Cancri A, which is a Sun-like star.\n")

    def kepler_22b(self):
        kepler_22b = "KEPLER-22B"
        print(kepler_22b.center(35, '-'))
        print("Kepler-22b is an extrasolar planet that orbits the G-type star Kepler-22. It is located in the constellation Cygnus, about 600\n" 
              + "light-years from Earth. Kepler-22b was discovered by NASA's Kepler Space Telescope. Kepler-22b is a 'super-Earth' with a\n" 
              + "radius of 2.38 Earth radii and an estimated mass of 36 Earth masses. It is thought to be an ocean planet, rather than having\n" 
              + "a rocky, Earth-like composition. It is also thought to be covered in a global ocean. Kepler-22b is the first known planet to\n" 
              + "orbit within the habitable zone of a Sun-like star. It is thought to be a promising spot to search for life. However, at 600\n" 
              + "light-years away, further scrutiny of this world may require more powerful telescopes. Using current technology, it would take\n" 
              + "22 million years to travel 600 light years to visit Kepler-22b.\n")
    
    def corot(self):
        corot = "COROT-7B"
        print(corot.center(35, '-'))
        print("CoRoT-7b is a super Earth exoplanet that orbits a K-type star. It was discovered in February 2009 by ESA's planet-hunting COROT\n" 
              + "spacecraft. CoRoT-7b is the smallest exoplanet to have its diameter measured. It has a mean radius of 6,219.2 miles and a\n" 
              + "diameter of 12,438 miles. It takes 0.9 days to complete one orbit of its star. It races around its orbit at over 200 km per\n" 
              + "second, at a mere 2.5 million km from its parent star. CoRoT-7b is five times heavier than Earth and has approximately the\n" 
              + "same density, so it must be made of rock and metal, like ours. However, it orbits so close to its star that it is likely\n" 
              + "covered with a lava ocean. CoRoT-7b is an exoplanet that orbits the star CoRoT-7 in the constellation Monoceros. It is\n" 
              + "located about 489 light-years from Earth.\n")

    def kepler_452b(self):
        kepler_452b = "KEPLER-452B"
        print(kepler_452b.center(35, '-'))
        print("Kepler-452b is an exoplanet that is 60 percent larger than Earth and orbits a star that is similar to our sun. The planet is located\n" 
              + "in the habitable zone of its star, which is 1,400 light-years away in the constellation Cygnus. Kepler-452b has a year that\n" 
              + "is about 20 days longer than Earth's. Kepler-452b's star is a G2-type star with nearly the same temperature and mass as the\n" 
              + "sun. However, Kepler-452b's star is 1.5 billion years older than the sun and is 20 percent brighter than the sun. Kepler-452b was\n" 
              + "announced in 2015. It was the first near-Earth-size world to be found in the habitable zone of a star that is similar to our sun.\n")

    def tres(self):
        tres = "TRES-2B"
        print(tres.center(35, '-'))
        print("TrES-2b is an extrasolar planet that orbits the star GSC 03549-02811, which is located 750 light years away from the Solar System.\n" 
              + "It was discovered by Francis T. O'Donovan as part of the Trans-Atlantic Exoplanet Survey. The planet is named after the project\n" 
              + "that discovered it. TrES-2b is a giant ball of gas. It has a mean radius of 56,506 miles and a diameter of 113,010 miles. It has\n" 
              + "a gravity of 32.21 m/s². In 2011, TrES-2b was identified as the darkest known exoplanet. It reflects less than 1 percent of the\n" 
              + "light that hits it. This makes it significantly darker than coal and almost as dark as the darkest man-made substance on Earth,\n" 
              + "which was manufactured by NASA. The extrasolar planet TrES-2b is located 750 light years away from Earth in the constellation Draco.\n")

    def wasp(self): 
        wasp = "WASP-12B"
        print(wasp.center(35, '-'))
        print("WASP-12b is an extrasolar planet that orbits the star WASP-12. It is a gas giant that is about twice the size of Jupiter and is\n" 
              + "extremely close to its star, about 2 million miles away. WASP-12b is known as a 'hot Jupiter' because it is very close to its\n" 
              + "star. It is one of the hottest planets known, much hotter than Venus. WASP-12b is orbiting its sun in just 26 hours. The star's\n" 
              + "scorching heat is slowly stripping away and devouring the planet's atmosphere. The gravitational pull of WASP-12 has stretched\n" 
              + "and distorted WASP-12b into an oblong, egg-like shape. The interior of WASP-12b could be dominated by pure-carbon rocks, possibly\n" 
              + "in the form of graphite or diamonds. The atmosphere is found to have a surprising amount of methane. The exoplanet WASP-12b is\n" 
              + "located roughly 1,200 light-years from Earth.\n")

    def kepler_16b(self):
        kepler_16b = "KEPLER-16B"
        print(kepler_16b.center(35, '-'))
        print("Kepler-16b is a gas giant exoplanet that orbits two stars in the Kepler-16 system. The planet is about the size of Saturn and\n" 
              + "has a mass of about a third of Jupiter's. It is more dense than Saturn and has a temperature of 188 K (-85 °C; -121 °F).\n" 
              + "Kepler-16b has no solid surface. Kepler-16b was discovered by NASA's Kepler mission and is located 200 light-years from\n" 
              + "Earth. It was the first confirmed planet in a “circumbinary” orbit, which means it circles two stars instead of one.\n" 
              + "Kepler-16b completes a nearly circular orbit every 228.776 days. Kepler-16b is not thought to harbor life, but its\n" 
              + "discovery demonstrates the diversity of planets in our galaxy.\n")


    
def start_menu():
    print("\nChoose what to learn about...")
    print("(I) Solar System\n(II) Stars in the Universe\n(III) Blackholes in the Universe\n(IV) Exoplanets")
    menu_choice = input("Select a choice or enter Q to Quit: ")
    menu_choice = menu_choice.upper()
    print("\n")
    return menu_choice

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
    planet_choice = planet_choice.upper()
    print("\n")
    return planet_choice

def star_selection():
    stars = "STARS OF THE UNIVERSE"
    print(stars.center(35, '-'))
    print("(I) What is a star?\n(II) What are stars made of?\n(III) How do stars form?\n(IV) Biggest Stars in the Universe")
    star_choice = input("Select an option or enter Q to Quit: ")
    star_choice = star_choice.upper()
    print("\n")
    return star_choice

def blackhole_selection():
    black_holes = "BLACK HOLES"
    print(black_holes.center(35, '-'))
    print("(I) What Is a Black Hole?\n(II) How Do Black Holes Form?\n(III) What Is Inside a Black Hole?\n" 
          + "(IV) What Would Happen if You Entered a Black Hole?\n(V) Nearest Black Hole to Earth\n(VI) Biggest Known Black Holes")
    black_hole_choice = input("Select and option or enter Q to Quit: ")
    black_hole_choice = black_hole_choice.upper()
    print("\n")
    return black_hole_choice

def exoplanet_selection():
    exoplanet = "EXOPLANETS"
    print(exoplanet.center(35, '-'))
    print("(I) What Is An Exoplanet?\n(II) How Many Exoplanets Are There?\n(III) Most Unique Exoplanets")
    exoplanet_choice = input("Select an option or enter Q to Quit: ")
    exoplanet_choice = exoplanet_choice.upper()
    print("\n")
    return exoplanet_choice



# main
flag = program_start()
while flag:
        
        start = input("Enter C to Continue or Q to Quit: ")
        start = start.upper()
        while start != 'C' and start != 'Q':
            start = input("\n**INVALID INPUT**\nEnter C to Continue or Q to Quit: ")
        
        if start == 'Q':
            flag = False
        
        elif start == 'C':
            # call start menu function - displays choices such as solar system, blackholes, stars
            menu_choice = start_menu()
            
            while menu_choice not in ['I', 'II', 'III', 'IV', 'Q']:
                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                menu_choice = start_menu()

            if menu_choice == 'I':
                #solar system
                p_select = planet_selection()
                planet = Solar_System(p_select)
        
                while p_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'Q']:
                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                    p_select = planet_selection()

                if p_select == 'I':
                    planet.sun()
                    
                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.sun()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'II':
                    planet.mercury()
                    
                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.mercury()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'III':
                    planet.venus()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.venus()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'IV':
                    planet.earth()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.earth()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'V':
                    planet.mars()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.mars()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
            
                elif p_select == 'VI':
                    planet.jupiter()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.jupiter()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'VII':
                    planet.saturn()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.saturn()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'VIII':
                    planet.uranus()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.uranus()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'IX':
                    planet.neptune()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            planet.neptune()
                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif p_select == 'Q':
                    flag = False
            
            elif menu_choice == 'II':
                #stars
                s_select = star_selection()
                star = Stars(s_select)

                while s_select not in ['I', 'II', 'III', 'IV', 'Q']:
                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                    s_select = star_selection()
                
                if s_select == 'I':
                    star.what_is_star()

                    # working so far -- check for user input
                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            s_select = star_selection()

                            while s_select not in ['I', 'II', 'III', 'IV', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                s_select = star_selection()

                            if s_select == 'I':
                                star.what_is_star()

                            elif s_select == 'II':
                                star.star_composition()

                            elif s_select == 'III':
                                star.star_formation()

                            elif s_select == 'IV':                      
                                big_star_choice = star.biggest_stars()

                                if big_star_choice == 'I':
                                    star.canis_majoris()

                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                
                elif s_select == 'II':
                    star.star_composition()
                
                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            s_select = star_selection()

                            while s_select not in ['I', 'II', 'III', 'IV', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                s_select = star_selection()

                            if s_select == 'I':
                                star.what_is_star()

                            elif s_select == 'II':
                                star.star_composition()

                            elif s_select == 'III':
                                star.star_formation()

                            elif s_select == 'IV':                      
                                big_star_choice = star.biggest_stars()

                                if big_star_choice == 'I':
                                    star.canis_majoris()

                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                
                elif s_select == 'III':
                    star.star_formation()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            s_select = star_selection()

                            while s_select not in ['I', 'II', 'III', 'IV', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                s_select = star_selection()

                            if s_select == 'I':
                                star.what_is_star()

                            elif s_select == 'II':
                                star.star_composition()

                            elif s_select == 'III':
                                star.star_formation()

                            elif s_select == 'IV':                      
                                big_star_choice = star.biggest_stars()

                                if big_star_choice == 'I':
                                    star.canis_majoris()

                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif s_select == 'IV':                      
                    big_star_choice = star.biggest_stars()
                    
                    if big_star_choice == 'I':
                        star.canis_majoris()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                big_star_choice = star.biggest_stars()
                                if big_star_choice == 'I':
                                    star.canis_majoris()
                    
                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                    
                    elif big_star_choice == 'II':
                        star.woh()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                big_star_choice = star.biggest_stars()
                                if big_star_choice == 'I':
                                    star.canis_majoris()
                    
                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                    
                    elif big_star_choice == 'III':
                        star.cephei()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                big_star_choice = star.biggest_stars()
                                if big_star_choice == 'I':
                                    star.canis_majoris()
                    
                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                    
                    elif big_star_choice == 'IV':
                        star.scuti()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                big_star_choice = star.biggest_stars()
                                if big_star_choice == 'I':
                                    star.canis_majoris()
                    
                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                    
                    elif big_star_choice == 'V':
                        star.cygni()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                big_star_choice = star.biggest_stars()
                                if big_star_choice == 'I':
                                    star.canis_majoris()
                    
                                elif big_star_choice == 'II':
                                    star.woh()
                    
                                elif big_star_choice == 'III':
                                    star.cephei()
                    
                                elif big_star_choice == 'IV':
                                    star.scuti()
                    
                                elif big_star_choice == 'V':
                                    star.cygni()

                                elif big_star_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif big_star_choice == 'Q':
                        flag = False
                        break

                elif s_select == 'Q':
                    flag = False
                    break

            elif menu_choice == 'III':
                #blackholes
                b_select = blackhole_selection()
                blackhole = Blackholes(b_select)

                while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                    b_select = blackhole_selection()

                if b_select == 'I':
                    blackhole.what_is_blackhole()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            b_select = blackhole_selection()

                            while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                b_select = blackhole_selection()

                            if b_select == 'I':
                                blackhole.what_is_blackhole()

                            elif b_select == 'II':
                                blackhole.blackhole_formation()

                            elif b_select == 'III':
                                blackhole.inside_blackhole()

                            elif b_select == 'IV':                      
                                blackhole.enter_blackhole()

                            elif b_select == 'V':
                                blackhole.nearest_bh_earth()

                            elif b_select == 'VI':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    flag = False
                                    break

                            elif b_select == 'Q':
                                flag = False
                                break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif b_select == 'II':
                    blackhole.blackhole_formation()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            b_select = blackhole_selection()

                            while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                b_select = blackhole_selection()

                            if b_select == 'I':
                                blackhole.what_is_blackhole()

                            elif b_select == 'II':
                                blackhole.blackhole_formation()

                            elif b_select == 'III':
                                blackhole.inside_blackhole()

                            elif b_select == 'IV':                      
                                blackhole.enter_blackhole()

                            elif b_select == 'V':
                                blackhole.nearest_bh_earth()

                            elif b_select == 'VI':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    flag = False
                                    break

                            elif b_select == 'Q':
                                flag = False
                                break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif b_select == 'III':
                    blackhole.inside_blackhole()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            b_select = blackhole_selection()

                            while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                b_select = blackhole_selection()

                            if b_select == 'I':
                                blackhole.what_is_blackhole()

                            elif b_select == 'II':
                                blackhole.blackhole_formation()

                            elif b_select == 'III':
                                blackhole.inside_blackhole()

                            elif b_select == 'IV':                      
                                blackhole.enter_blackhole()

                            elif b_select == 'V':
                                blackhole.nearest_bh_earth()

                            elif b_select == 'VI':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    flag = False
                                    break

                            elif b_select == 'Q':
                                flag = False
                                break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif b_select == 'IV':
                    blackhole.enter_blackhole()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            b_select = blackhole_selection()

                            while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                b_select = blackhole_selection()

                            if b_select == 'I':
                                blackhole.what_is_blackhole()

                            elif b_select == 'II':
                                blackhole.blackhole_formation()

                            elif b_select == 'III':
                                blackhole.inside_blackhole()

                            elif b_select == 'IV':                      
                                blackhole.enter_blackhole()

                            elif b_select == 'V':
                                blackhole.nearest_bh_earth()

                            elif b_select == 'VI':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    flag = False
                                    break

                            elif b_select == 'Q':
                                flag = False
                                break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif b_select == 'V':
                    blackhole.nearest_bh_earth()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            b_select = blackhole_selection()

                            while b_select not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                b_select = blackhole_selection()

                            if b_select == 'I':
                                blackhole.what_is_blackhole()

                            elif b_select == 'II':
                                blackhole.blackhole_formation()

                            elif b_select == 'III':
                                blackhole.inside_blackhole()

                            elif b_select == 'IV':                      
                                blackhole.enter_blackhole()

                            elif b_select == 'V':
                                blackhole.nearest_bh_earth()

                            elif b_select == 'VI':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    flag = False
                                    break

                            elif b_select == 'Q':
                                flag = False
                                break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif b_select == 'VI':
                    blackhole_choice = blackhole.biggest_blackholes()

                    while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                        print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                        blackhole_choice = blackhole.biggest_blackholes()

                    if blackhole_choice == 'I':
                        blackhole.phoenix_a()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    # add these two lines to other cases in program
                                    flag = False
                                    break
                                        
                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                            
                    elif blackhole_choice == 'II':
                        blackhole.ton_618()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    # add these two lines to other cases in program
                                    flag = False
                                    break
                                        
                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif blackhole_choice == 'III':
                        blackhole.holm_15A()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    # add these two lines to other cases in program
                                    flag = False
                                    break
                                        
                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif blackhole_choice == 'IV':
                        blackhole.ic_1101()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    # add these two lines to other cases in program
                                    flag = False
                                    break
                                        
                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif blackhole_choice == 'V':
                        blackhole.s5_0014()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                blackhole_choice = blackhole.biggest_blackholes()

                                while blackhole_choice not in ['I', 'II', 'III', 'IV', 'V', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                    blackhole_choice = blackhole.biggest_blackholes()

                                if blackhole_choice == 'I':
                                    blackhole.phoenix_a()

                                elif blackhole_choice == 'II':
                                    blackhole.ton_618()

                                elif blackhole_choice == 'III':
                                    blackhole.holm_15A()

                                elif blackhole_choice == 'IV':
                                    blackhole.ic_1101()

                                elif blackhole_choice == 'V':
                                    blackhole.s5_0014()

                                elif blackhole_choice == 'Q':
                                    # add these two lines to other cases in program
                                    flag = False
                                    break
                                        
                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif blackhole_choice == 'Q':
                        flag = False

                elif b_select == 'Q':
                    flag = False
            
            elif menu_choice == 'IV':
                #exoplanets
                e_select = exoplanet_selection()
                exoplanet = Exoplanets(e_select)

                while e_select not in ['I', 'II', 'III', 'Q']:
                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                    e_select = exoplanet_selection()

                if e_select == 'I':
                    exoplanet.what_is_exoplanet()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            e_select = exoplanet_selection()

                            while e_select not in ['I', 'II', 'III', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                e_select = exoplanet_selection()
                            
                            if e_select == 'I':
                                exoplanet.what_is_exoplanet()

                            elif e_select == 'II':
                                exoplanet.how_many_exoplanets()

                            elif e_select == 'III':
                                exoplanet_choice = exoplanet.unique_exoplanets()
                                
                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif e_select == 'II':
                    exoplanet.how_many_exoplanets()

                    while True:
                        go_again = input("Would you like to choose another option? (Y/N): ")
                        go_again = go_again.upper()  # Convert input to uppercase
                        if go_again == 'Y':
                            e_select = exoplanet_selection()

                            while e_select not in ['I', 'II', 'III', 'Q']:
                                print("\n**INVALID INPUT**\nPlease enter a valid numeral...")
                                e_select = exoplanet_selection()
                            
                            if e_select == 'I':
                                exoplanet.what_is_exoplanet()

                            elif e_select == 'II':
                                exoplanet.how_many_exoplanets()

                            elif e_select == 'III':
                                exoplanet_choice = exoplanet.unique_exoplanets()
                                
                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                        elif go_again == 'N':
                            break
                        else:
                            print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                elif e_select == 'III':
                    exoplanet_choice = exoplanet.unique_exoplanets()

                    while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                        print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                        exoplanet_choice = exoplanet.unique_exoplanets()

                    if exoplanet_choice == 'I':
                        exoplanet.kepler_186f()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'II':
                        exoplanet.cancri()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'III':
                        exoplanet.kepler_22b()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'IV':
                        exoplanet.corot()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'V':
                        exoplanet.kepler_452b()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'VI':
                        exoplanet.tres()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'VII':
                        exoplanet.wasp()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")

                    elif exoplanet_choice == 'VIII':
                        exoplanet.kepler_16b()

                        while True:
                            go_again = input("Would you like to choose another option? (Y/N): ")
                            go_again = go_again.upper()  # Convert input to uppercase
                            if go_again == 'Y':
                                exoplanet_choice = exoplanet.unique_exoplanets()

                                while exoplanet_choice not in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Q']:
                                    print("\n**INVALID INPUT**\nPlease enter a valid numeral...\n")
                                    exoplanet_choice = exoplanet.unique_exoplanets()

                                if exoplanet_choice == 'I':
                                    exoplanet.kepler_186f()

                                elif exoplanet_choice == 'II':
                                    exoplanet.cancri()

                                elif exoplanet_choice == 'III':
                                    exoplanet.kepler_22b()

                                elif exoplanet_choice == 'IV':
                                    exoplanet.corot()

                                elif exoplanet_choice == 'V':
                                    exoplanet.kepler_452b()

                                elif exoplanet_choice == 'VI':
                                    exoplanet.tres()

                                elif exoplanet_choice == 'VII':
                                    exoplanet.wasp()

                                elif exoplanet_choice == 'VIII':
                                    exoplanet.kepler_16b()
                        
                                elif exoplanet_choice == 'Q':
                                    flag = False
                                    break

                            elif go_again == 'N':
                                break
                            else:
                                print("\n**INVALID INPUT**\nPlease enter Y or N...\n")
                        
                    elif exoplanet_choice == 'Q':
                        flag = False
                        break

                elif e_select == 'Q':
                    flag = False

            elif menu_choice == 'Q':
                flag = False

#end
