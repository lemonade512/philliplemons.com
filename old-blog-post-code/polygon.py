from itertools import tee, izip
from collections import namedtuple
from pprint import pprint as pp
from math import radians
from vector import Vector
from vector_math import find_intersection_point, find_perp_coord
import sys

# Point is used in place of coordinate so we can use Polygon without needing
# to import the Projection library from coordinate
Point = namedtuple('Point', ['lon', 'lat'])
Edge = namedtuple('Edge', ['c1', 'c2', 'name', 'color'])

_huge = sys.float_info.max

def ccw(coords):
    '''
    returns true if the coordinates are in counter clockwise order

    Gotten from:
        stackoverflow.com/questions/1165647/how-to-determine-if-a-list-of-polygon-points-are-in-clockwise-order/
    '''
    the_sum = 0
    for i in range(len(coords)):
        vec1 = coords[0].vec_to_coord(coords[i])
        vec2 = coords[0].vec_to_coord(coords[(i+1)%len(coords)])
        x1, y1 = vec1._to_rect()
        x2, y2 = vec2._to_rect()
        the_sum += (x2-x1) * (y2+y1)

    if the_sum < 0:
        return True
    else:
        return False

class Polygon:
    '''
    A polygon object
    '''
    colors = ['ivory', 'gold', 'black', 'purple', 'blue', 'dark green', 'khaki', 'olive drab', 'violet red', 'dark blue']
    color_index = 0

    def __init__(self, coords, name=''):
        '''
        coords is a sequence of coordinate objects
        '''
        if len(coords) < 1:
            print "ERROR: a polygon cannot be made with 0 points!"
            raise TypeError
        elif len(coords) == 1:
            print "ERROR: a polygon cannot be made with 1 point. Making a Point object"
            raise NotImplementedError
        elif len(coords) == 2:
            print "ERROR: a polygon cannot be made with 2 points. Making a Line object"
            raise NotImplementedError

        self.coords = coords
        self.name = name
        self.edges = self._calculate_edges()

    def __repr__(self):
        string = "Polygon(coords=("
        string += "\n    "
        string += "\n    ".join(str(c) for c in self.coords) + "\n    ))"
        return string

    def _calculate_edges(self):
        edge_list = list()

        for i in range(len(self.coords)):
            j = (i+1) % len(self.coords)
            c1 = self.coords[i]
            c2 = self.coords[j]
            edge_list.append(Edge(c1, c2, self.name+'E'+str(i), Polygon.colors[Polygon.color_index]))
            Polygon.color_index = (Polygon.color_index + 1) % len(Polygon.colors)

        return edge_list

    def find_tangent_points(self, coord):
        #TODO can be convex hull instead of all coords
        tan_coords = []
        for c in self.coords:
            vec_to_c = coord.vec_to_coord(c)
            test_coord1 = c.coord_of_vec(Vector.Polar(0.001, vec_to_c.heading))
            test_coord2 = c.coord_of_vec(Vector.Polar(-0.001, vec_to_c.heading))
            if self.contains(test_coord1) or self.contains(test_coord2):
                continue
            tan_coords.append(c)
        return tan_coords

    def buffer(self, dist):
            new_coords = []
            if ccw(self.coords):
                is_ccw = True
            else:
                is_ccw = False

            for i in range(len(self.coords)):
                j = (i+1) % len(self.coords)
                k = (i+2) % len(self.coords)

                vec1 = self.coords[i].vec_to_coord(self.coords[j])
                vec2 = self.coords[j].vec_to_coord(self.coords[k])

                if is_ccw:
                    psi = radians(90)
                else:
                    psi = -radians(90)

                perp_vec1 = Vector.Polar(dist, vec1.heading+psi)
                perp_vec2 = Vector.Polar(dist, vec2.heading+psi)

                # push walls out to make two lines
                c1 = self.coords[i].coord_of_vec(perp_vec1)
                c2 = self.coords[j].coord_of_vec(perp_vec1)
                c3 = self.coords[j].coord_of_vec(perp_vec2)
                c4 = self.coords[k].coord_of_vec(perp_vec2)

                # use coordinate of where those lines intersect TODO will need to change this
                x1, y1 = [0, 0]
                x2, y2 = c1.vec_to_coord(c2)._to_rect()
                x3, y3 = c1.vec_to_coord(c3)._to_rect()
                x4, y4 = c1.vec_to_coord(c4)._to_rect()

                px, py = find_intersection_point([x1, y1], [x2,y2], [x3,y3], [x4,y4])

                vec_to_intersection = Vector.XY(px, py)
                new_coord = c1.coord_of_vec(vec_to_intersection)
                colors = ['purple', 'orange', 'black', 'blue']
                #new_coords.append(new_coord)
                new_coords.append(c1)
                new_coords.append(c2)

            new_poly = Polygon(new_coords)
            return new_poly

    def contains(self, coord):
        '''
        Determines if a coordinate is inside this polygon. If the coordinate is on one of the
        edges then the polygon does not contain the coordinate and so this returns False

        For a full explanation see http://rosettacode.org/wiki/Ray-casting_algorithm#Python
        '''
        inside = False
        for edge in self.edges:
            a, b = edge.c1, edge.c2
            # Make sure a is always the south-most point
            if a.lat > b.lat:
                a, b = b, a

            # The horizontal ray does not intersect with the edge
            if (coord.lat > b.lat or coord.lat < a.lat or coord.lon > max(a.lon, b.lon)):
                continue

            # The horizontal ray definitely intersects with the edge
            if coord.lon < min(a.lon, b.lon):
                inside = not inside
                continue

            try:
                m_edge = (b.lat - a.lat) / (b.lon - a.lon)
            except ZeroDivisionError:
                m_edge = _huge

            try:
                m_coord = (coord.lat - a.lat) / (coord.lon - a.lon)
            except ZeroDivisionError:
                m_coord = _huge

            if m_coord >= m_edge:
                inside = not inside
                continue

        return inside

    def project(self, coord):
        '''
        Finds the coord on this polygon that is closest to the given coord
        '''
        best_dist = None
        best_coord = None
        for edge in self.edges:
            perp_coord, distance = find_perp_coord(edge.c1, edge.c2, coord)
            if best_dist == None or distance < best_dist:
                best_dist = distance
                best_coord = perp_coord

        return best_coord

    def find_closest_edge(self, coord):
        best_dist = None
        best_edge = None
        for edge in self.edges:
            perp_coord, distance = find_perp_coord(edge.c1, edge.c2, coord)
            if best_dist == None or distance < best_dist:
                best_dist = distance
                best_edge = edge

        return best_edge

if __name__ == "__main__":
    p = Polygon([Point(0,0),
                 Point(0,1),
                 Point(1,1),
                 Point(1,0)])
    #print p
    pp(p)
    pp(p.coords)
    pp(p.edges)
