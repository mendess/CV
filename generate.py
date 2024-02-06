#!/usr/bin/env python3

import os
import subprocess
import sys

class Project:
    def __init__(self,
                 language,
                 title,
                 description,
                 link,
                 linkname='Repository',
                 grade=''):
        self.language = language
        self.title = title
        self.description = ' '.join(description.split())
        self.link = link
        self.linkname = linkname
        self.grade = grade

    def __str__(self):
        return (r'{language} & \ul{{\textbf{{{title}}}}} & \href{{{link}}}{{{linkname}}}\\' + '\n'
                r'& {description} & {grade}\\').format(
                    language=self.language,
                    title=self.title,
                    description=self.description,
                    link=self.link,
                    linkname=self.linkname,
                    grade='Grade {}/20'.format(self.grade) if self.grade else '',
                )


projects = [
    Project(language='C',
            title='Parallel and Distributed Computing (University project)',
            description=
            'Successfully used openMP and MPI to develop a blazingly fast,\
                multiprocess system to calculate product recommendations in C.',
            link='https://github.com/mendess/CPD',
            grade=19),
    Project(
        language='Kotlin \& Rust',
        title='Secure Child Tracking Service (University project)',
        description='Developed a secure and easy to use app that allows parents\
                to track where their child is, taking care to not compromise\
                the sensitive data the app needs to work with.',
        link='https://github.com/mendess/SIRS',
        grade=19
    ),
    Project(
        language='Rust',
        title='Scryfall',
        description='A type safe and complete wrapper around a REST API for\
                fetching and searching for cards from the Magic: The\
                Gathering\\texttrademark{} card game.',
        link='https://crates.io/crates/scryfall',
        linkname='Crates.io',
    ),
    Project(
        language='Markdown',
        title='ResumosMIEI',
        description='A collection of notes written in Portuguese to help students\
                study the base concepts of computer science, lectured at\
                University of Minho.',
        link='https://github.com/mendess/ResumosMIEI',
    ),
    Project(
        language='C++',
        title='Generic Graphics Engine (University project)',
        description='A generic graphics engine, capable of efficiently rendering any kind\
                of scene defined in an XML configuration file',
        link='https://github.com/mendess/CG',
        grade=20
    ),
    Project(
        language='Java',
        title='An auto scalling sudoku solver',
        description='Using AWS\'s API\'s and by instrumenting the code of a sudoku solving program\
                we were able to scale up and down the resources available to the application according\
                to how much computing power it was needing in real time',
        link='https://github.com/mendess/CNV',
        grade=17,
    ),
    Project(
        language='C++ \& Go',
        title='Internet of Sensors and Actuators (University project)',
        description='Assembled an arduino with various sensors and one with various leds and\
                established high throughput, low latency and reliable connection between them\
                over the internet',
        link='https://github.com/mendess/IoT',
        grade='16',
    ),
]

def generate_tex(project_idx):
    with open('./cv_template.tex', 'r') as template, open('./cv_generated.tex', 'w') as generated:
        for line in template:
            if 'PROJECTS' not in line:
                generated.write(line)
            else:
                for p in map(lambda i: projects[i], project_idx):
                    generated.write(str(p))
                    generated.write('\n')

def generate_pdf():
    subprocess.run(['pdflatex', './cv_generated.tex'])
    os.remove('cv_generated.aux')
    os.remove('cv_generated.log')
    os.remove('cv_generated.out')
    os.remove('cv_generated.tex')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        p_to_use = []
        with open(sys.argv[1], 'r') as c:
            for line in c:
                p_to_use.append(int(line.strip()))
    else:
        p_to_use = []
        while len(p_to_use) < 5:
            print('Projects:')
            i = 0
            for p in projects:
                if i in p_to_use: print('\033[2m', end='')
                print(i, p.title, '|', p.language, '\033[0m')
                i += 1
            print(f'{len(p_to_use)} / 5 projects picked')
            new_p = int(input('? '))
            if new_p not in p_to_use:
                p_to_use.append(new_p)
            else:
                print('Already selected')

        reply = input('Save configuration? [Y/n]')
        if reply.lower() != 'n':
            name = input('Config name? ')
            with open(name + '.config', 'w') as c:
                for i in p_to_use:
                    c.write(f'{i}\n')


    generate_tex(p_to_use)
    generate_pdf()
