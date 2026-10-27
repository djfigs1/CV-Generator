from recipe.recipe import ResumeRecipe


# Represents subsections in a Me file
class ResumeSubsection:
    def __init__(self, key: str, section_key: str, data: dict[str, any]) -> None:
        self.key = key
        self.section_key = section_key
        self.data = data

    def should_include(self, recipe: ResumeRecipe) -> bool:
        include_subsection = True

        # Check inclusions
        if self.section_key in recipe.include_items:
            items = recipe.include_items[self.section_key]
            if not self.key in items:
                include_subsection = False
        else:
            if self.key.lower() in recipe.exclude_items:
                include_subsection = False
            else:
                for tag in self.get_tags():
                    tag = tag.lower()
                    if tag in recipe.exclude_tags and not tag in recipe.include_tags:
                        include_subsection = False
                        break

        return include_subsection

    def get_title(self) -> str:
        if "Title" in self.data:
            return self.data["Title"]

        # Fall back to the subsection's key
        return self.key

    def get_subtitle(self) -> str | None:
        if "Subtitle" in self.data:
            return self.data["Subtitle"]

        return None

    def get_date_range(self) -> str | None:
        if "Start" in self.data and "End" in self.data:
            start = self.data["Start"]
            end = self.data["End"]
            dateRange = f"{start} - {end}"
            return dateRange
        elif "Date" in self.data:
            return self.data["Date"]

        return None

    def get_description(self) -> list[str] | str | None:
        if "Description" in self.data:
            return self.data["Description"]

        return None

    def get_description_type(self) -> str | None:
        if "DescriptionType" in self.data:
            return self.data["DescriptionType"]

        return None

    def get_tags(self) -> list[str]:
        if "Tags" in self.data:
            return self.data["Tags"]

        return []
