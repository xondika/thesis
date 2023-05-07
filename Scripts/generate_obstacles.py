import random, math

def dist( p1, p2 ):
    res = 0.0
    for i in range( 3 ):
        res += ( p1[ i ] - p2[ i ] ) ** 2
    return math.sqrt( res )

def to_json( cubes, current = 101 ):
    modules = ""
    joints = ""
    for cube in cubes:
        modules += "{ \"id\": " + str( current ) + ", \"type\": \"cube\" },"
        joints += "{ \"point\": " + str( cube ) \
         + ",\"joint\": { \"type\":\"rigid\", \"sourceToDestination\":\"identity\", \"positions\": [] }," \
         + "\"to\": { \"id\" : " + str( current ) + ", \"component\": 0 }" "},"
        current += 1

    return ( modules, joints )

def generate_walls( x1, x2, y1, y2, z1, z2 ):
    if( x1 > x2 ):
        x1, x2 = x2, x1
    if( y1 > y2 ):
        y1, y2 = y2, y1
    if( z1 > z2 ):
        z1, z2 = z2, z1

    cubes = []
    for x in range( x1, x2 + 1 ):
        for y in range( y1, y2 + 1 ):
            for z in range( z1, z2 + 1 ):
                cubes.append( [ x, y, z ] )

    return cubes

def generate_clusters( x1, x2, y1, y2, z1, z2, amount = 20 ):
    if( x1 > x2 ):
        x1, x2 = x2, x1
    if( y1 > y2 ):
        y1, y2 = y2, y1
    if( z1 > z2 ):
        z1, z2 = z2, z1

    cubes = []
    while len( cubes ) < amount:
        x = random.randint( x1 * 10, x2 * 10 ) / 10
        y = random.randint( y1 * 10, y2 * 10 ) / 10
        z = random.randint( z1 * 10, z2 * 10 ) / 10

        collides = False
        for cube in cubes:
            if dist( cube, [x, y, z] ) < 2.0:
                collides = True

        if not collides:
            cubes.append( [ x, y, z ] )

    return cubes
