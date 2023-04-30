def get_production_version(version_list):    
    production_versions = []
    for version in version_list:
        # Split version string into version and branch parts
        version_parts = version.split("-")
        # Check if the version has a branch part
        if len(version_parts) == 1:
            production_versions.append(version)
        else:
            # If the version has a branch part, check if the branch is empty (i.e. "dev")
            if version_parts[-1].isdigit():
                production_versions.append(version_parts[0])
    
    # Return the latest version string from the production versions
    return max(production_versions)

versions = ["2.5.0-dev.1", "2.4.2-5354", "2.4.2-test.675", "2.4.1-integration.1"]
production_version = get_production_version(versions)
print(production_version) # Output: "2.4.2-5354"
