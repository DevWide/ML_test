# ML API Automation Testing Suite

## 🚀 Project Overview

This project is a Proof of Concept (PoC) demonstrating an automated testing suite for a web application serving predictions from a pre-trained Machine Learning (ML) model. 

The application leverages the **Hugging Face** model `distilbert-base-uncased-finetuned-sst-2-english` for sentiment analysis, which is lightweight, efficient, and specialized in classifying text as **POSITIVE** or **NEGATIVE** based on sentiment. The web application is built using **Flask**.


The testing suite includes:
- Unit tests and benchmarks using **pytest**.
- End-to-End (E2E) tests using **Cypress**.
- Continuous Integration (CI) pipeline with **GitHub Actions** for automated test execution on every commit.

---

## 📋 Features
- REST API with endpoints:
  - `/predict`: Accepts text input and returns sentiment predictions.
  - `/health`: Simple health check endpoint.
- **Benchmarking**:
  - Ensures performance and response times meet acceptable thresholds.
  - Validates model inference quality using a pre-defined dataset.
- Automated testing:
  - Functional, performance, and E2E tests to validate API functionality and robustness.
- CI/CD pipeline:
  - Automatically runs tests on every push or pull request.

---

## 📊 Details of the ML Model

### **Model Used**
- **Name:** `distilbert-base-uncased-finetuned-sst-2-english`
- **Source:** [Hugging Face Transformers](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- **Type:** Pre-trained Transformer model
- **Task:** Sentiment Analysis

### **Why this model?**
This model was chosen for its:
1. **Accuracy:** High performance in sentiment classification tasks.
2. **Efficiency:** Based on DistilBERT, which is optimized for inference speed and memory usage.
3. **Pre-training on SST-2:** Fine-tuned on the Stanford Sentiment Treebank dataset, making it highly reliable for text classification into "POSITIVE" or "NEGATIVE".
4. **Ease of integration:** Easily integrated using the Hugging Face Transformers library.

### **How it works**
The model accepts a string of text as input and returns:
- **Label:** Either `POSITIVE` or `NEGATIVE`.
- **Score:** A confidence score for the prediction.

Example response:
```json
{
    "label": "POSITIVE",
    "score": 0.999847412109375
}
```

## ⚙️ Setup Instructions

### Prerequisites
1. Python 3.9+ installed on your system.
2. Node.js (v14+ recommended) and npm installed for Cypress.
3. (Optional) Docker, if you wish to containerize the application.

### Steps to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ml-api-automation-suite.git
   cd ml-api-automation-suite


2. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```

3. Install the required Python dependencies:
```
pip install -r requirements.txt
```

4. Start the Flask server:
```
python app.py
```

The server will run at ``http://127.0.0.1:5000``.

## 🧪 Running the Tests
### Unit and Benchmark Tests
To run the unit benchmark tests:
```
pytest app/tests
```

### Cypress E2E Tests
1. Install Cypress dependencies:
```
npm install
```

2. Open the Cypress Test Runner:
```
npx cypress open
```

Run the ``api_tests.cy.js`` script in the Cypress interface.

Alternatively, to run tests headlessly:
```
npx cypress run 
```

## 🔄 CI/CD Pipeline

The CI/CD pipeline is implemented using GitHub Actions. It runs the following steps automatically on each push or pull request:

* Setup: Installs Python and Node.js dependencies.
* Unit Testing: Runs pytest for unit and benchmark tests.
* E2E Testing: Executes Cypress tests headlessly in a GitHub-hosted environment.

You can view the pipeline configuration in the .github/workflows/ci.yml file.

## 📊 Benchmarking

Performance and inference quality benchmarks are integrated into the pytest tests:

- **Performance:** Ensures the ML model responds within acceptable latency (e.g., 500ms).
- **Inference Quality:** Validates predictions against a predefined dataset. For example:
  - Input: `"I love this!"` → Prediction: `POSITIVE`
  - Input: `"This is terrible!"` → Prediction: `NEGATIVE`
  - Input: `"It's okay, I guess."` → Prediction: `POSITIVE`

## 🛠 Future Improvements

- Add Docker support for containerized deployments.
- Integrate visualization tools (e.g., Grafana) for monitoring benchmarking results.
- Expand test coverage with additional edge cases.
- Explore fine-tuning the sentiment analysis model on domain-specific data.


## 👤 Author

Developed by Rafael da Silva Barbosa.

## 📝 License

This project is licensed under the MIT License.

