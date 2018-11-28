class Map(object):

    scenes = {
      'central_corridor': CentralCorridor(),
      'laser_weapon_armory': LaserWeaponArmory(),
      'the_bridge': TheBridge(),
      'escape_pod': EscapePod(),
      'death': Death(),
      'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
      val = Map.scenes.get(scene_name)
      return val

    def opening_scene(self):
      return self.next_scene(self.start_scene)