import svgwrite
import distances
"""dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.line((0, 0), (10, 0), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Test', insert=(0, 20), fill='red'))
dwg.save()"""

class Cell:
    def __init__(self, row, column):
        self.row, self.column = row, column
        self.links = {}

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi = True):
        if cell in self.links:
            del self.links[cell]
        if bidi: cell.unlink(self, False)

    def show_links(self):
        print (self.links)

    def get_links(self):
        return self.links.keys()

    def linked(self, cell):
        if cell in self.links:
            return True
        return False

    def neighbors(self):
        list = []
        if self.north: list.append(self.north)
        if self.south: list.append(self.south)
        if self.west: list.append(self.west)
        if self.east: list.append(self.east)
        return list

    def distances(self):
        distances = distances.Distances()
        frontier = [self]

        while len(frontier) > 0:
            new_frontier = []

            for cell in frontier:
                for link in cell.get_links():
                    if not distances[link]:
                        distances[link] = distances[cell] + 1
                        new_frontier.append(link)

            frontier = new_frontier