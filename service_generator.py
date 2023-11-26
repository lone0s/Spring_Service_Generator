import sys
import os

def generate_service_class(entity_name, path, package_name):
    service_class = f"""package {package_name}.services;

import {package_name}.entities.{entity_name};
import {package_name}.repositories.{entity_name}Repository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class {entity_name}Service {{

    @Autowired
    private {entity_name}Repository {entity_name.lower()}Repository;

    public List<{entity_name}> getAll{entity_name}s() {{
        return {entity_name.lower()}Repository.findAll();
    }}

    public Optional<{entity_name}> get{entity_name}ById(Integer id) {{
        return {entity_name.lower()}Repository.findById(id);
    }}

    public {entity_name} save{entity_name}({entity_name} {entity_name.lower()}) {{
        return {entity_name.lower()}Repository.save({entity_name.lower()});
    }}

    public void delete{entity_name}(Integer id) {{
        {entity_name.lower()}Repository.deleteById(id);
    }}
}}
"""

    file_path = os.path.join(path, f"{entity_name}Service.java")
    with open(file_path, "w") as file:
        file.write(service_class)
    
    print(f"Service class generated at: {file_path}")


if __name__ == "__main__":

    entities = []

    path = r""

    package_name = ""

    for entity_name in entities: 
        generate_service_class(entity_name, path, package_name)