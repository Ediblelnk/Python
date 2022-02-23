x = 0
while x == 0:

    #start with new line and print welcome message
    print('\n')
    WelcomeMessage = ('Welcome to the Area and Volume Calculator.\n'
        'Would you like to calculate area or volume?\n')
    
    #set request to input
    request = input(WelcomeMessage)

    #request case for volume
    if request.startswith("v"):

        #request for specific 3-d shape
        request = input('What shape would you like to calculate the volume of?\n'
              'Options are cube, prism, cylinder, pyramid, cone, or sphere\n')

        #request case for cube
        if request.startswith("cu"):
            try:
                sidelength = float(input('Sidelength? '))
                unit = input('Units? ')
                volume = sidelength**3
                print('The Volume is', volume,'cubic', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for prism
        elif request.startswith("pr"):
            baseshape = input('Base shape? Options are square, rectangle, parallelogram, \n'
                              'trapeziod, triangle, or regular n-gon:\n')

            #request case for square prism
            if baseshape.startswith('s'):
                try:
                    length = float(input('Square Length? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = (length**2)*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for rectangle prism
            elif baseshape.startswith('rec'):
                try:
                    length = float(input('Rectangle Length? '))
                    height = float(input('Rectangle Height? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = length*height*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for parallelogram prism
            elif baseshape.startswith('pa'):
                try:
                    length = float(input('Parallelogram Length? '))
                    height = float(input('Parallelogram Height? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = length*height*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for a trapezoid prism
            elif baseshape.startswith('tra'):
                try:
                    longbase = float(input('Trapezoid Longer base length? '))
                    shortbase = float(input('Trapezoid Shorter base length? '))
                    height = float(input('Trapezoid Height? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = 0.5*(longbase + shortbase)*height*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for a triangle prism
            elif baseshape.startswith('tri'):
                try:
                    length = float(input('Triangle Length? '))
                    height = float(input('Triangle Height? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = 0.5*length*height*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for a regular n-gon
            elif baseshape.startswith('reg'):
                try:
                    sidenumber = int(input('Number of Sides on n-gon? '))
                    length = float(input('Length of each side on n-gon? '))
                    apothem = float(input('Apothem Length? '))
                    prismheight = float(input('Prism Height? '))
                    unit = input('Units? ')
                    volume = 0.5*sidenumber*length*apothem*prismheight
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')
            else:
                print('\nAn Error Occured due to an unknown request')

        #request case for a cylinder
        elif request.startswith('cy'):
            try:
                radius = float(input('Radius? '))
                height = float(input('Cylinder Height? '))
                unit = input('Units? ')
                approximatevolume = 3.14*radius**2*height
                exactvolume = radius**2*height
                print('The Volume is', exactvolume, 'pi', 'cubic', unit, 'or roughly', approximatevolume, 'cubic', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for pyramid
        elif request.startswith('py'):
            baseshape = input('Base shape? Options are square, rectangle, parallelogram, \n'
                              'trapeziod, triangle, or regular n-gon\n')

            #request case for square pyramid
            if baseshape.startswith('squ'):
                try:
                    length = float(input('Square Length? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = (length**2)*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for rectangular pyramid
            elif baseshape.startswith('rec'):
                try:
                    length = float(input('Rectangle Length? '))
                    height = float(input('Rectangle Height? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = length*height*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for rectangular pyramid
            elif baseshape.startswith('par'):
                try:
                    length = float(input('Parallelogram Length? '))
                    height = float(input('Parallelogram Height? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = length*height*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for trapezoid pyramid
            elif baseshape.startswith('tra'):
                try:
                    longbase = float(input('Trapezoid Longer base length? '))
                    shortbase = float(input('Trapezoid Shorter base length? '))
                    height = float(input('Trapezoid Height? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = 0.5*(longbase + shortbase)*height*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for triangular pyramid
            elif baseshape.startswith('tri'):
                try:
                    length = float(input('Triangle Length? '))
                    height = float(input('Triangle Height? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = 0.5*length*height*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')

            #request case for regular n-gon
            elif baseshape.startswith('reg'):
                try:
                    sidenumber = int(input('Number of Sides on n-gon? '))
                    length = float(input('Length of each side on n-gon? '))
                    apothem = float(input('Apothem Length? '))
                    pyramidheight = float(input('Pyramid Height? '))
                    unit = input('Units? ')
                    volume = 0.5*sidenumber*length*apothem*pyramidheight/3
                    print('The Volume is', volume,'cubic', unit)
                except:
                    print('\nAn Error Occured due to a non-number input')
            else:
                print('\nAn Error Occured due to an unknown request')

        #request case for cone
        elif request.startswith('co'):
            try:
                radius = float(input('Radius? '))
                height = float(input('Cone Height? '))
                unit = input('Units? ')
                approximatevolume = 3.14*radius**2*height/3
                exactvolume = radius**2*height/3
                print('The Volume is', exactvolume, 'pi', 'cubic', unit, 'or roughly', approximatevolume, 'cubic', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for sphere
        elif request.startswith('sp'):
            try:
                radius = float(input('Radius? '))
                unit = input('Units? ')
                approximatevolume = 3.14*radius**3*4/3
                exactvolume = radius**3*4/3
                print('The Volume is', exactvolume, 'pi', 'cubic', unit, 'or roughly', approximatevolume, 'cubic', unit)
            except:
                print('\nAn Error Occured due to a non-number input')
        else:
            print('\nAn Error Occured due to an unknown request')

    #request case for area
    elif request.startswith("a"):
        request = input('What shape would you like to calculate the area of?\n'
              'Options are square, rectangle, parallelogram, trapezoid, \n'
              'triangle, regular n-gon, or circle\n')

        #request case for square
        if request.startswith('squ'):
            try:
                length = float(input('Square Length? '))
                unit = input('Units? ')
                area = length**2
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for rectangle
        elif request.startswith('rec'):
            try:
                length = float(input('Rectangle Length? '))
                width = float(input('Rectangle Width? '))
                unit = input('Units? ')
                area = length*width
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for parallelogram
        elif request.startswith('par'):
            try:
                length = float(input('Parallelogram Length? '))
                height = float(input('Parallelogram Height? '))
                unit = input('Units? ')
                area = length*height
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for trapezoid
        elif request.startswith('tra'):
            try:
                longbase = float(input('Longer base length? '))
                shortbase = float(input('Shorter base length? '))
                height = float(input('Trapezoid Height? '))
                unit = input('Units? ')
                area = 0.5*(longbase + shortbase)*height
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for triangle
        elif request.startswith('tri'):
            try:
                length = float(input('Triangle Length? '))
                height = float(input('Triangle Height? '))
                unit = input('Units? ')
                area = 0.5*length*height
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for regular n-gon
        elif request.startswith('reg'):
            try:
                sidenumber = int(input('Number of Sides? '))
                length = float(input('Length of each side? '))
                apothem = float(input('Apothem Length? '))
                unit = input('Units? ')
                area = 0.5*sidenumber*length*apothem
                print('The Area is', area, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')

        #request case for circle
        elif request.startswith('cir'):
            try:
                radius = float(input('Radius? '))
                unit = input('Units? ')
                approximatearea = 3.14*radius**2
                exactarea = radius**2
                print('The Area is', exactarea, 'pi', 'square', unit, 'or roughly', approximatearea, 'square', unit)
            except:
                print('\nAn Error Occured due to a non-number input')
        else:
            print('\nAn Error Occured due to an unknown request')
    else:
        print('\nAn Error Occured due to an unknown request') 

