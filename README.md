# NFL Expected Fantasy Points (xFP) Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Overview
This repository contains the code and analysis pipeline for building an **Expected Fantasy Points (xFP)** model for the NFL. By shifting our focus from actual fantasy points (which are noisy and heavily dependent on touchdown variance) to expected fantasy points based on situational volume (air yards, down and distance, field position, and red-zone usage), this project aims to evaluate player efficiency, opportunity share, and regression candidates.

To maintain structural consistency and avoid era-bias from major rule changes and shifting offensive philosophies, the project focuses on **seasons from 2010 to the present**.

---

## Repository Structure

```text
MATH-331-Proj/
│
├── data/               # (Ignored in Git) Local storage for raw and processed datasets
├── notebooks/          # Exploratory data analysis and model prototyping notebooks
├── src/                # Modular scripts for data cleaning, feature engineering, and modeling
├── .gitignore          # Excludes large data files, environments, and OS/IDE junk
├── LICENSE             # MIT License
└── README.md           # Project documentation
