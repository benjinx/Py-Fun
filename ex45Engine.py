import ex45Scenes

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Map(object):

    scenes = {
        'central_corridor' : ex45Scenes.CentralCorridor(),
        'laser_weapon_armory' : ex45Scenes.LaserWeaponArmory(),
        'the_bridge' : ex45Scenes.TheBridge(),
        'escape_pod' : ex45Scenes.EscapePod(),
        'death' : ex45Scenes.Death(),
        'finished' : ex45Scenes.Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

