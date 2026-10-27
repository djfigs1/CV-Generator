import argparse
import os
import sys

from builder.me import read_me_file
from generate import generate_pdf
from recipe.recipe import ResumeRecipe


def main():
    # Create and configure argparser
    parser = argparse.ArgumentParser(description="A utility that creates my resume.")
    subparsers = parser.add_subparsers(dest="command", title="commands")

    generate_parser = subparsers.add_parser("generate", help="generate a resume PDF from a resume YAML file",
                                            description="Generate a resume PDF from a resume YAML file.")
    generate_parser.add_argument("me_file", metavar="RESUME_FILE", help="path to resume YAML file")
    generate_parser.add_argument("-iT", "--include-tags", help="include tags in resume", dest="include_tags")
    generate_parser.add_argument("-i", "--include-items", action="store", type=str, help="include items in resume",
                                 dest="include_items")
    generate_parser.add_argument("-eI", "--exclude-items", action="store", type=str, default="",
                                 help="exclude items from resume", dest="exclude_items")
    generate_parser.add_argument("-eT", "--exclude-tags", action="store", type=str, default="",
                                 help="exclude tags from resume", dest="exclude_tags")
    generate_parser.add_argument("-eC", "--exclude-contact", action="store", type=str, default="",
                                 help="exclude contact info from resume", dest="exclude_contact")
    generate_parser.add_argument("-r", "--recipe-file", help="create resume from recipe file")
    generate_parser.add_argument("-t", "--output-tex", action="store", dest="tex_path", default=None,
                                 help="outputs a .tex file")
    generate_parser.add_argument("-o", "--output-file", default="./resume", action="store", dest="pdf_path",
                                 help="outputs a .pdf file (default: ./resume.pdf)")
    generate_parser.add_argument("-f", "--fill-page", action="store_true", dest="fill_page",
                                 help="stretch spacing so a one-page resume fills the page")

    # Parse arguments
    args = parser.parse_args()

    # Show help when no command is given
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    # Parse path information
    me_path = args.me_file
    if not os.path.isfile(me_path):
        generate_parser.error(f"resume file not found: {me_path}")
    pdf_path = args.pdf_path
    # Remove unnecessary .pdf extension
    if pdf_path.endswith(".pdf"):
        pdf_path = pdf_path[:-4]

    # Create recipe
    recipe = ResumeRecipe()

    # Extract include items
    # format SectionKey:A,B,C;OtherSectionKey:D,E,F;...
    if args.include_items is not None and len(args.include_items) > 0:
        include_sections = args.include_items.split(";")
        for section in include_sections:
            section_key, items = section.split(":")
            items = items.split(",")
            recipe.include_items[section_key] = items

    recipe.exclude_items = args.exclude_items.lower().split(",")
    recipe.exclude_tags = args.exclude_tags.lower().split(",")
    recipe.exclude_contact = args.exclude_contact.lower().split(",")
    tex_path = args.tex_path
    if tex_path is not None and tex_path.endswith(".tex"):
        tex_path = tex_path[:-4]

    me_file = read_me_file(path=me_path)
    generate_pdf(me_file, pdf_path, recipe, tex_path, fill_page=args.fill_page)


if __name__ == "__main__":
    main()
