from typing import Optional
from wildlife_tracker.habitat_manager.habitat import Habitat

class MigrationPath:
    def __init__(self, destination: Habitat, path_id: int, species: str, start_location: Habitat, duration: Optional[int] = None) ->None: 
        self.destination = destination
        self.duration = duration
        self.path_id = path_id
        self.species = species
        self.start_location = start_location

    def get_migration_path_details(self,path_id: int) -> dict:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass
