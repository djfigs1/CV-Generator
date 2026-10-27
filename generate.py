import os

from pylatex import Document, Command, Section, Subsection

from builder.me import MeFile
from builder.subsection import ResumeSubsection
from latex.dated_subsection import DatedSubsection
from latex.description import create_bullets, create_description
from recipe.recipe import ResumeRecipe

# Directory containing cv.cls
CLASS_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_pdf(me: MeFile, path: str, recipe: ResumeRecipe, tex_path: None | str = None):
    doc = create_document(me, recipe)

    # pdflatex runs from the output directory, so add the class directory to the TeX search path.
    # The trailing separator keeps the default search paths.
    old_texinputs = os.environ.get("TEXINPUTS")
    os.environ["TEXINPUTS"] = CLASS_DIR + os.pathsep + (old_texinputs or "")
    try:
        doc.generate_pdf(path, compiler="pdflatex")
    finally:
        if old_texinputs is None:
            del os.environ["TEXINPUTS"]
        else:
            os.environ["TEXINPUTS"] = old_texinputs

    if tex_path is not None:
        doc.generate_tex(tex_path)


def create_subsection(doc: Document, subsection: ResumeSubsection):
    title = subsection.get_title()
    subsection_title = title if title is not None else ""
    section_header = Subsection(subsection_title)

    # Check for date range
    date_range = subsection.get_date_range()
    if subsection.get_date_range() is not None:
        section_header = DatedSubsection(title, date_range, subsection.get_subtitle())

    with doc.create(section_header):
        desc = subsection.get_description()
        create_description(doc, desc)


def create_document(me: MeFile, recipe: ResumeRecipe, margin: str = "0.3in") -> Document:
    doc = Document(documentclass="cv", geometry_options={"margin": margin})

    # Add name/contact information
    doc.append(Command("name", me.get_name()))
    contact_info = []
    for key, val in me.get_contact_info().items():
        if not key.lower() in recipe.exclude_contact:
            contact_info.append(val)
    contact = " | ".join(contact_info)
    doc.append(Command("centerline", contact))

    for sectionKey, section in me.get_sections().items():
        title = section.get_title()
        section_title = title if title is not None else ""
        with doc.create(Section(section_title)):
            desc = section.get_description()
            create_description(doc, desc)

            # Check for subsections
            subsections = section.get_subsections()
            if subsections is not None:
                for subsection in subsections.values():
                    # Check to see if the section should be included
                    if subsection.should_include(recipe):
                        create_subsection(doc, subsection)

    return doc
