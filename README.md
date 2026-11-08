#  SmartCut — Digital Poka-Yoke System

### Intelligent CNC Cutting Assistant | Industrial Automation Prototype

**Reducing Human Error Through QR Code Identification and Software Automation**

---

## 1. Project Overview

SmartCut is a low-cost software automation prototype designed to reduce human errors in CNC cutting operations.

The system uses QR Code identification to retrieve job information and automate data input through a software adapter, reducing the need for repetitive manual entry.

The project applies the concept of **Digital Poka-Yoke**, integrating computer vision, user interface design, and desktop automation into an accessible solution for industrial manufacturing environments.

## 2. Problem Statement

Traditional CNC workflows often require operators to manually enter job parameters from production documents.

This process may lead to:

- Incorrect job parameter entry.
- Human errors caused by repetitive tasks.
- Additional setup time.
- Material waste and production delays.

## 3. Proposed Solution

SmartCut introduces a digital workflow:

1. Scan or upload a Job QR Code.
2. Decode the QR Code using OpenCV.
3. Validate the Job Code against stored job data.
4. Retrieve the corresponding job information.
5. Display verified information through a Streamlit interface.
6. Transfer the Job Code using a software automation adapter.

## 4. System Architecture

QR Code / Manual Input  
↓  
OpenCV QR Code Detection  
↓  
Job Code Validation  
↓  
SmartCut Adapter (Streamlit)  
↓  
PyAutoGUI + Pyperclip  
↓  
Notepad Automation Demo

## 5. Key Features

- QR Code scanning using OpenCV.
- Manual Job Code input.
- Job Code validation.
- Automatic job information retrieval.
- Streamlit-based user interface.
- Clipboard integration.
- Keyboard automation using PyAutoGUI.
- Input confirmation and validation feedback.

## 6. Technology Stack

| Technology | Application |
|---|---|
| Python | Core programming language |
| Streamlit | User interface |
| OpenCV | QR Code detection |
| NumPy | Image processing |
| PyAutoGUI | Keyboard automation |
| Pyperclip | Clipboard integration |
| Git & GitHub | Version control |

## 7. Before & After Improvement Concept

**Traditional Process**
- Manual Job Code entry.
- Repetitive operator input.
- Potential human input errors.

**SmartCut Process**
- QR Code identification.
- Automatic job information retrieval.
- Automated data transfer demonstration.

*Actual time savings and error reduction have not yet been experimentally quantified.*

## 8. Project Limitations & Safety

This project is currently an educational software prototype.

- Automation has been tested with Windows Notepad only.
- The prototype is not connected to any CNC machine.
- No real CNC cutting operation has been performed.
- Industrial integration and machine-controller compatibility require further development and validation.

**Safety Notice:** Do not connect the current demonstration software directly to CNC machinery.

## 9. Project Team

**Warakamon Pinwanna**
- Project concept and idea development.
- Frontend development.
- Software testing.

**Jakkarin Eiamsam-ang**
- Software implementation.
- Backend development.
- Programming and automation logic.

## 10. Future Development

- Support additional QR Code job formats.
- Improve job data management.
- Develop industrial controller communication interfaces.
- Conduct controlled performance testing.
- Evaluate cycle time and human error reduction.

## 11. Installation & Usage

Clone the repository:

```bash
git clone https://github.com/Jakkalin44/SmartCut-Digital-Poka-Yoke.git
cd SmartCut-Digital-Poka-Yoke
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

### Project Information

**Project:** SmartCut — Digital Poka-Yoke System  
**Field:** Industrial Engineering & Automation  
**Type:** Educational Software Prototype  
**Repository:** https://github.com/Jakkalin44/SmartCut-Digital-Poka-Yoke

*Developed as an educational project to explore the application of software automation in industrial manufacturing.*