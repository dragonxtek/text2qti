# text2qti – Create quizzes in QTI format from Markdown-based plain text

text2qti converts
[Markdown](https://daringfireball.net/projects/markdown/)-based plain text
files into quizzes in QTI format, which can be imported by
[Canvas](https://www.instructure.com/canvas/) and other educational software.
It includes basic support for LaTeX math within Markdown, and allows a limited
subset of [siunitx](https://ctan.org/pkg/siunitx) notation for units and for
numbers in scientific notation.



## Examples

text2qti allows quick and efficient quiz creation.  Example plain-text quiz
question that can be converted to QTI and then imported by Canvas:

```
1.  What is 2+3?
a)  6
b)  1
*c) 5
```

A **question** is created by a line that starts with a number followed by a
period and one or more spaces or tabs ("`1. `").  Possible **choices** are
created by lines that start with a letter followed by a closing parenthesis
and one or more spaces or tabs ("`a) `").  Numbers and letters do not have to
be ordered or unique.  The **correct** choice is designated with an asterisk
("`*c) `").  All question and choice text is processed as
[Markdown](https://daringfireball.net/projects/markdown/).

There is also support for a quiz title, a quiz description, and feedback.
Note that unlike all other text, the title and description are treated as
plain text, not Markdown, due to the QTI format.

```
Quiz title: Addition
Quiz description: Checking addition.

1.  What is 2+3?
... General question feedback.
+   Feedback for correct answer.
-   Feedback for incorrect answer.
a)  6
... Feedback for this particular answer.
b)  1
... Feedback for this particular answer.
*c) 5
... Feedback for this particular answer.
```

**Numerical questions** are indicated by an equals sign followed by one or
more spaces or tabs followed by the numerical answer.  Acceptable answers can
be designated as a range of the form `[<min>, <max>]` or as a correct answer
with a specified acceptable margin of error `<ans> +- <margin>`.  When the
latter form is used, `<margin>` can be either a number or a percentage.
`<margin>` can be omitted when the answer is an integer and an exact answer is
required.  In this case, scientific notation is not permitted, but the
underscore can be used as a digit separator; for example, `1000` and `1_000`
are both valid, but `1e3` is not.  An exact answer can be required for
floating-point numbers, but this requires an explicit `+- 0`, since a range is
typically more appropriate for floating-point values.  Numerical questions
have the limitation that the absolute value of the smallest acceptable answer
must be greater than or equal to 0.0001 (1e-4).

```
1.  What is the square root of 2?
=   1.4142 +- 0.0001

2.  What is the cube root of 2?
=   [1.2598, 1.2600]

3.  What is 2+3?
=   5
```


**Essay questions** are indicated by a sequence of three or more underscores.
They do not support feedback.

```
1.  Write an essay.
____
````

Currently there are three major limitations:
  * Images are not yet supported.
  * Only multiple-choice, true/false, numerical, and essay questions are
    supported at present.
  * All titles, descriptions, questions, choices, and feedback are limited to
    a single paragraph each.  If this paragraph is wrapped over multiple
    lines, all lines after the first must be indented to the same level as the
    start of the paragraph text on the initial line (so, indented as much as
    the "`1. `" or "`a) `", etc.).  All tabs are expanded to 4 spaces before
    indentation is compared, following the typical Markdown approach.
    Multiple paragraphs will likely be enabled at some point in the future.
    ```
    1.  A question paragraph that is long enough to wrap onto a second line.
        The second line must be indented to match up with the start of the
        paragraph text on the first line.  Multiple paragraphs are not yet
        supported.
    ```



## Installation

Install **Python 3.6+** if it is not already available on your machine.  See
https://www.python.org/, or use the package manager or app store for your
operating system.  Depending on your use case, you may want to consider a
Python distribution like [Anaconda](https://www.anaconda.com/distribution/)
instead.

Install
[setuptools](https://packaging.python.org/tutorials/installing-packages/)
for Python if it is not already installed.  This can be accomplished by
running
```
python -m pip install setuptools
```
on the command line.  Depending on your system, you may need to use `python3`
instead of `python`.  This will often be the case for Linux and OS X.

Install text2qti by running this on the command line:
```
python -m pip install text2qti
```
Depending on your system, you may need to use `python3` instead of `python`.
This will often be the case for Linux and OS X.

### Installing the development version

If you want to install the development version to use the latest features,
download `text2qti` from [GitHub](https://github.com/gpoore/text2qti), extract
the files, and then run
```
python setup.py install
```
Depending on your system, you may need to use `python3` instead of `python`.
This will often be the case for Linux and OS X.



## Usage

text2qti has been designed to create QTI files for use with
[Canvas](https://www.instructure.com/canvas/).  Some features may not be
supported by other educational software.  You should **always preview**
quizzes or assessments after converting them to QTI and importing them.

Write your quiz or assessment in a plain text file.  You can use a basic
editor like Notepad or gedit, or a code editor like
[VS Code](https://code.visualstudio.com/).  You can even use Microsoft Word,
as long as you save your file as plain text (*.txt).

text2qti is a command-line application.  Open a command line in the same
folder or directory as your quiz file.  Under Windows, you can hold the SHIFT
button down on the keyboard, then right click next to your file, and select
"Open PowerShell window here" or "Open command window here".  You can also
launch "Command Prompt" or "PowerShell" through the Start menu, and then
navigate to your file using `cd`.

Run the `text2qti` application using a command like this:
```
text2qti quiz.txt
```
Replace "quiz.txt" with the name of your file.  This will create a file like
`quiz.zip` (with "quiz" replaced by the name of your file) which is the
converted quiz in QTI format.

Instructions for using the QTI file with Canvas:
  * Go to the course in which you want to use the quiz.
  * Go to Settings, click on "Import Course Content", select "QTI .zip file",
    choose your file, and click "Import".  Typically you should not need to
    select a question bank; that should be managed automatically.
  * While the quiz upload will often be very fast, there is an additional
    processing step that can take up to several minutes.  The status will
    probably appear under "Current Jobs" after upload.
  * Once the quiz import is marked as "Completed", the imported quiz should be
    available under Quizzes.  If the imported quiz does not appear after
    several minutes, there may be an error in your quiz file or a bug in
    `text2qti`.  When Canvas encounters an invalid quiz file, it tends to fail
    silently; instead of reporting an error in the quiz file, it just never
    creates a quiz based on the invalid file.
  * You should **always preview the quiz before use**.  text2qti can detect a
    number of potential issues, but not everything.

Typically, you should start your quizzes with a title, like this:
```
Quiz title: Title here
```
Otherwise, all quizzes will have the default title "Quiz", so it will be
difficult to tell them apart.  Another option is to rename quizzes after
importing them.

When you run `text2qti` for the first time, it will attempt to create a
configuration file called `.text2qti.bespon` in your home or user directory.
It will also ask for an institutional LaTeX rendering URL.  This is only
needed if you plan to use LaTeX math; if not, simply press ENTER to continue.
 * If you use Canvas, log into your account and look in the browser address
   bar.  You will typically see an address that starts with something like
   `institution.instructure.com/` or `canvas.institution.edu/`, with
   `institution` replaced by the name of your school or an abbreviation for
   it.  The LateX rendering URL that you want to use will then be something
   like `https://institution.instructure.com/equation_images/` or
   `https://canvas.institution.edu/equation_images/`, with `institution`
   replaced by the appropriate value for your school.  If the URL is like the
   second form, you may need to replace the `.edu` domain with the appropriate
   value for your institution.
 * If you use other educational software that handles LaTeX in a manner
   compatible with Canvas, consult the documentation for your software.  Or
   perhaps create a simple quiz within the software using its built-in tools,
   then export the quiz to QTI and look through the resulting output to find
   the URL.
 * If you are using educational software that does not handle LaTeX in a
   manner compatible with Canvas, please open an issue requesting support for
   that software, and include as much information as possible about how that
   software processes LaTeX.



## Additional features

### Question groups

A question group contains multiple questions, and only a specified number of
these are randomly selected and used each time a quiz is taken.

```
GROUP
pick: 1
points per question: 1

1.  A question.
*a) true
b)  false

2.  Another question.
*a) true
b)  false

END_GROUP
```

The number of questions from the group that are used is specified with
`pick:`.  If this is omitted, it defaults to `1`.  The points assigned per
question is specified with `points per question:`.  If this is omitted, it
defaults to `1`.  All questions within a group must be worth the same number
of points.


### Executable code blocks

text2qti can execute the code in Markdown-style fenced code blocks.  Code can
be used to generate questions within a quiz.  Everything written to stdout by
the executed code is included in the quiz file; the code block is replaced by
stdout.

``````
```{.python .run}
import textwrap
for x in [2, 3]:
    print(textwrap.dedent(rf"""
        1.  What is ${x}\times 5$?
        *a) ${x*5}$
        b)  ${x+1}$
        """))
```
``````


For code to be executed, there are a few requirements:
* The code block fences (` ``` `) must not be indented; the code block must be
  at the top level of the document, not part of a question, choice, or
  feedback.
* As a security measure, code execution is disabled by default, so executable
  code blocks will trigger an error.  Run `text2qti` with the option
  `--run-code-blocks` to enable code execution, or set `run_code_blocks =
  true` in the text2qti config file in your user or home directory.
* The text immediately after the opening fence must have the form `{.lang
  .run}`.  This is inspired by the code-block attributes in
  [Pandoc Markdown](https://pandoc.org/MANUAL.html).  `lang` must designate an
  executable that can run the code once the code has been saved to a file.  In
  the example above, `python` is extracted from the first line
  (` ```{.python .run}`),  code is saved in a temporary file, and then the
  file is executed via `python <file>`.

Each code block is executed in its own process, so data and variables are not
shared between code blocks.

If an executable code block generates multiple questions that are identical,
or multiple choices for a single question that are identical, this will be
detected by `text2qti` and an error will be reported.  Questions or choices
that may be equivalent, but are not represented by exactly the same text,
cannot be detected (for example, things like `100` versus `1e2`, or `answer`
versus `Answer`).




## Details for writing quiz text

text2qti processes almost all text as
[Markdown](https://daringfireball.net/projects/markdown/), using
[Python-Markdown](https://python-markdown.github.io/).  (The only exception is
the quiz title and quiz description, which are processed as plain text due to
the QTI format.)  For example, `*emphasized*` produces emphasized text, which
typically appears as italics.  Text can be styled using Markdown notation, or
with HTML.  Remember to preview quizzes after conversion to QTI, especially
when using any significant amount of HTML.

All titles, descriptions, questions, choices, and feedback are limited to a
single paragraph each.  If this paragraph is wrapped over multiple lines, all
lines after the first must be indented to the same level as the start of the
paragraph text on the initial line

text2qti supports inline LaTeX math within dollar signs `$`.  There must be a
non-space character immediately after the opening `$` and immediately before
the closing `$`.  For example, `$F = ma$`.  LaTeX math is limited to what is
supported by Canvas or whatever other educational software you are using.  It
is usually a good idea to preview imported quizzes before assigning them,
because text2qti cannot detect LaTeX incompatibilities or limitations.  There
is currently not support for block LaTeX math; only inline math is supported.

When using Canvas with LaTeX math, be aware that in some cases Canvas's
vertical alignment of math leaves much to be desired.  Sometimes this can be
improved by including `\vphantom{fg}` or `\strut` at the beginning of an
equation.  An alternative is simply to use LaTeX for all question or choice
text (via `\text`, etc.).

text2tqi supports a limited subset of LaTeX
[siunitx](https://ctan.org/pkg/siunitx) notation.  You can use notation like
`\num{1.23e5}` to enter numbers in scientific notation.  This would result in
`1.23×10⁵`.  You can use notation like `\si{m/s}` or `\si{N.m}` to enter
units.  These would result in `m/s` and `N·m`.  Unit macros currently are not
supported, with these exceptions: `\degree`, `\celsius`, `\fahrenheit`,
`\ohm`, `\micro`.  Finally, numbers and units can be combined with notation
like `\SI{1.23e5}{m/s}`.  All of these can be used inside or outside LaTeX
math.

Technical note: LaTeX and siunitx support are currently implemented as
preprocessors that are used separately from Python-Markdown.  In rare cases,
this may lead to conflicts with Markdown syntax.  These features may be
reimplemented as Python-Markdown extensions in the future.
