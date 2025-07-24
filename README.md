# Hybrid Log Classification System

## Project Description

The **Hybrid Log Classification System** is designed to automatically classify log messages using a combination of **rule-based**, **machine learning**, and **large language model (LLM)** approaches. This multi-layered framework ensures robust and efficient handling of log entries, regardless of their complexity or the amount of labeled data available. It's ideal for log analysis and monitoring in software development, IT operations, and security.

---

## Table of Contents

- [Project Description](#project-description)  
- [Key Features](#key-features)  
- [Folder Structure](#folder-structure)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Run Classification Locally](#run-classification-locally)  
  - [Start the API Server](#start-the-api-server)  
  - [Classification Workflow](#classification-workflow)  
  - [Example](#example)  
---

## Key Features

### 🔀 Hybrid Classification Pipeline  
Integrates three complementary techniques for optimal accuracy and efficiency:

- **Regex-Based Classification**  
  Rapidly classifies logs with simple and predictable patterns using regular expressions.

- **Sentence Transformer + Logistic Regression**  
  Handles more complex patterns using embeddings from Sentence Transformers and a Logistic Regression classifier, ideal when training data is available.

- **LLM Classification**  
  Falls back to powerful Large Language Models (LLMs) for ambiguous or rare patterns, especially useful with limited labeled data.

### ⚙️ Flexible & Scalable  
Easily accommodates new log types and adapts to different datasets or logging formats.

### 🧱 Modular Codebase  
Well-structured code for adding new rules, machine learning models, or integrating with other systems.

---

## Folder Structure

| Folder/File          | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| `training/`          | Training code for ML models; regex classification scripts.         |
| `models/`            | Pre-trained models and embeddings.                                 |
| `resources/`         | Sample log files, configs, outputs, etc.                           |
| `server.py`          | FastAPI server for serving classification as an API.               |
| `classify.py`        | Main script for running classification locally.                    |
| `processor_bert.py`  | Utilities for working with Sentence Transformers.                  |
| `processor_llm.py`   | LLM inference utilities.                                            |
| `processor_regex.py` | Regex matching utilities.                                           |
| `requirements.txt`   | Python dependency list.                                             |
| `.gitignore`         | Standard Git ignore rules.                                          |
| `README.md`          | Project documentation (this file).                                 |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ChakradharReddy3237/hybrid_log_classification_system.git
cd hybrid_log_classification_system
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download or Train Models

- Pre-trained models may be available in the `models/` directory.  
- To train your own models, use the scripts inside the `training/` folder.

---

## Usage

### Run Classification Locally

```bash
python classify.py --input input_log_file.txt --output results.txt
```

### Start the API Server

```bash
uvicorn server:app --reload
```

Once the server is running, use Postman, `curl`, or your own app to send log messages for classification.

---

### Classification Workflow

1. The log message is first checked against regex rules.
2. If no match is found, the ML model (Sentence Transformer + Logistic Regression) attempts classification.
3. If data is insufficient or prediction confidence is low, the log is passed to an LLM for final classification.

---

### Example

Suppose you have logs from a web application and want to detect critical vs non-critical errors:

- Obvious error strings (e.g., `Connection timeout`, `404 Not Found`) are tagged via **regex**.
- Logs with subtle clues (e.g., `"User authentication failed due to expired token"`) are classified using the **ML model**.
- Ambiguous or rare logs (e.g., `"Node response inconsistent with schema"`) are handled using an **LLM** that can infer context better.

