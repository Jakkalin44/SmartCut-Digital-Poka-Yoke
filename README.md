# SmartCut – Digital Poka-Yoke System

### Intelligent CNC Cutting Assistant

SmartCut is a low-cost software adapter designed to reduce human error in CNC cutting operations through QR Code identification and automated job data input.

## Project Overview

Traditional CNC workflows often require operators to manually enter job parameters, which can lead to incorrect inputs, wasted materials, and production delays.

SmartCut aims to improve this process through digital job identification and software automation.

## Key Features

- QR Code scanning using OpenCV
- Job Code validation
- Automatic job information retrieval
- Streamlit-based user interface
- Windows Clipboard integration
- PyAutoGUI keyboard automation
- Modular software architecture

## System Workflow

QR Code
   ↓
OpenCV QR Scanner
   ↓
Job Code Validation
   ↓
SmartCut Adapter
   ↓
Clipboard Integration
   ↓
PyAutoGUI Automation
   ↓
Notepad Demo

## Technology Stack

- Python
- Streamlit
- OpenCV
- NumPy
- PyAutoGUI
- Pyperclip

## Current Development Status

- [x] Job Code validation
- [x] QR Code image scanning
- [x] Streamlit interface
- [x] Clipboard integration
- [x] Notepad automation demo
- [ ] Advanced QR scanning workflow
- [ ] Industrial controller integration research

## Safety Notice

This project is currently an educational prototype.

The automation module is designed and tested for Notepad demonstration only.

It is NOT connected to any CNC machine or industrial controller.

Further safety validation and engineering development
would be required before any industrial deployment.

## Project Purpose

Developed as an Industrial Engineering and Automation
portfolio project to explore digital error prevention,
process improvement, and low-cost industrial software integration.
