![logo](https://raw.githubusercontent.com/raoanmol/NARDS/main/ams-logo-small.jpg)
# Attendance Management System - Working Prototype
The Attendance Management System (AMS) is an automated software solution to the issue of time-consuming manual attendance recording methods prevalent throughout many introductory STEM courses at Arizona State University (ASU).

Key Features include:
- Integration with ASU's existing Integrated System for ASU Access Control (ISAAC) card access control logging system to determine the timeframes in which a student is present in a specific room (ASU-provided USB-based card swipe scanner used for prototype)
- Integration with Zoom API to retrieve meeting participant data to determine timeframe in which a student was present in an online class meeting (meeting participant CSV file reports used for prototype)
- Integration with Instructure Canvas LMS API to autograde attendance assignments for students each day

This project was originally created for the Devils Invent: Back In Person event at ASU in October 2022, in which it placed 2nd out of 10 other projects. The general concept and elements of its design will be used in the next iteration of the project as it is developed to record attendance for Computer Science and Engineering (CSE) labs in subsequent semesters.

## Getting Started

Welcome to PNARD's Attendance Management System project. To simplify the onboarding process, I've decided not to use any build tools for this project beyond the basic [Project Manager for Java](https://github.com/microsoft/vscode-java-dependency) extension.
Dependencies will be included as part of the content of this repository in the `lib` directory.

## Folder Structure

This VS Code workspace contains two folders, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies

Meanwhile, the compiled output files will be generated in the `bin` folder.

> Be sure to configure this folder structure by updating the related settings in `.vscode/settings.json`

## Dependencies

- [SQLite JDBC Driver](https://github.com/xerial/sqlite-jdbc)
- [CanvasAPI](https://github.com/ucfopen/canvasapi)

## Credits
- Anmol Rao - Systems Design, Programming (Zoom integration)
- Deep Goyal - Systems Design, Additional Programming
- Nishant Dhongadi - Conceptual Design, Documentation
- Pranav Aratikatla - Conceptual Design, Programming (Canvas integration)
- Ryan Woo - Systems Design, Programming (ISAAC integration, Canvas Integration)
- Sahil Sinha - Conceptual Design, Documentation

&copy; 2022, PNARDS. All rights reserved.
