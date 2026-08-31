class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        seen_points = {(0,0)}

        for direction in path:
            match direction:
                case "N":
                    y += 1
                    if (x, y) in seen_points:
                        return True
                    seen_points.add((x, y))
                case "S":
                    y -= 1
                    if (x, y) in seen_points:
                        return True
                    seen_points.add((x, y))
                case "E":
                    x -= 1
                    if (x, y) in seen_points:
                        return True
                    seen_points.add((x, y))
                case "W":
                    x += 1
                    if (x, y) in seen_points:
                        return True
                    seen_points.add((x, y))
        
        return False
                

        