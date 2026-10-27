from typing import List

from builder.subsection import ResumeSubsection


# Represents a section within the Me file
class ResumeSection:
    def __init__(self, key: str, data) -> None:
        self.key = key
        self.data = data

    def get_title(self) -> str:
        if "Title" in self.data:
            return self.data["Title"]

        # Fall back to the section's key
        return self.key

    def get_description(self) -> str | list[str] | None:
        if "Description" in self.data:
            return self.data["Description"]

        return None

    def get_description_type(self) -> str | None:
        if "DescriptionType" in self.data:
            return self.data["DescriptionType"]

        return None

    def get_subsections(self) -> dict[str, ResumeSubsection] | None:
        sections = None
        if "Subsections" in self.data:
            sections = {}
            for key, section in self.data["Subsections"].items():
                sections[key] = ResumeSubsection(key, self.key, section)

        return sections
