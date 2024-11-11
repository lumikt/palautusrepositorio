import toml

class Project:
    def __init__(self, name, description, release_license, authors,
     dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.license = release_license
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list_stuff(self, list):
        my_string = ""
       
        for i in list:
            my_string += f"\n-{i}"
        return my_string
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors: {self._list_stuff(self.authors)}"
            f"\n"
            f"\nDependencies: {self._list_stuff(self.dependencies)}"
            f"\n"            
            f"\nDevelopment dependencies: {self._list_stuff(self.dev_dependencies)}"
        )
