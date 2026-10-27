\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cv}[DJs CV Class]
\LoadClass{article}
\RequirePackage{titlesec}
\RequirePackage{etoolbox}
\RequirePackage{enumitem}

% Define spacing in-between bullet points
\setitemize{itemsep=0pt}

% Set title spacing
\titlespacing*{\section}
{0pt}{16pt}{3pt}
\titlespacing*{\subsection}
{0pt}{1pt}{3pt}

\setlength{\parskip}{0.0em} % Adjusts the space between paragraphs

\titleformat{\section}         % Customise the \section command
  {\scshape\raggedright\bfseries} % Make the \section headers large (\Large),
                               % small capitals (\scshape) and left aligned (\raggedright)
  {}{0em}                      % Can be used to give a prefix to all sections, like 'Section ...'
  {}                           % Can be used to insert code before the heading
  [\titlerule]                 % Inserts a horizontal line after the heading

\titleformat{\subsection}
  {\bfseries\raggedright}
  {}{0em}
  {}

\newcommand{\datedsection}[2]{%
  \section[#1]{#1 \hfill #2}%
}
\newcommand{\datedsubsection}[3]{%
  \subsection[#1]{\bfseries#1\normalfont \hfill #2 \ifstrempty{#3}{}{\\ \small#3}}%
}

\newcommand{\name}[1]{%
  \centerline{\Huge{#1}}
}