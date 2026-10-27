# CV
An automatic resume builder for me!

## Setup
This project uses [uv](https://docs.astral.sh/uv/). A LaTeX distribution providing `pdflatex` must also be installed.

```bash
uv sync
```

## me.yaml format
The `me.yaml` file contains all of your information and experiences that can be put in your resume. The file is structured as follows:

```yaml
# The Me section defines your name and all of your contact info.
# The only required key in Me is your name with the Name key. You can decide
# everything else you want to include with a custom key and its string value. 
Me:
  Name: "Your Name Here" # REQUIRED!
  MyPhoneNumber: 123-456-7890
  MyGitHub: https://github.com/djfigs1
  # etc...

# The Sections object defines all of your resume sections. Each section can have
# a top-level description and accompanying subsections. 
# For all sections and subsections, the key of the section/subsection is used as
# the title unless specified otherwise.
Sections:
  Education: 
    # The description is the content within the section / subsection.
    # Here, the description is a simple paragraph at the start of the section
    Description: Trust builder, I have a lot of educational experiences! 

  Likes & Hobbies:
    # Here, the description is a list of items (as indicated by the '-' before 
    # each item) This will be represented as a series of bullets on the
    # generated resume.
    Description:
      - I like computers.
      - I like foxes.
      - I like virtual reality.

  Work Experience:
    Description: This is everything that I have ever worked for!
    
    # You can define subsections within a section by including a "Subsections"
    # key. Here, every item within the Subsections object represents a
    # different subsection.
    Subsections:

      # This will create a subsection with the key "Example"
      Example:
        # This defines a custom title for the Example subsection.
        Title: Example Company

        # You can also define a subtitle to define your position; it appears
        # below the title.
        Subtitle: Super Awesome Employee

        # You can specify a date range for a subsection using the "Start"
        # and "End" keys.
        Start: January 1970
        End: March 2038

        Description:
          - Worked very hard doing very hard things.
          - Worked in a large team of very many people.
```

You can generate this example resume using the command:
```
uv run sastre.py -m demo.yaml -o demo.pdf
```

## sastre.py

You can view a list of arguments using the command:
```
uv run sastre.py --help
```