# API Reporting Microservice

The **API Reporting Microservice** handles reporting for the IT Expense Management (ITAM) and Telecom Expense Management (TEM) SaaS platform. It enables accurate reporting and auditing of complex organizational data, including insights into asset lifecycles, location, associations, and other useful financial metrics.

---

## Key Features

- Direct interacting with Data API sources, for gathering Expenses, Assets, and other insightful data points.
- Flexible support for generating reports in **PDF**, **Excel**, and **Word** and **Jason Value** formats.
- Integration with **Quarto** for modern reporting capabilities.
- Modular design for scalability and maintainability.

---

## Technology Stack

- **Framework**: Python 3.11
- **Reporting Tools**: Quarto for PDF, Excel, and Word generation; ReportLab for detailed PDF layouts. GPT for AI.
- **Database**: SQL Server with SQLAlchemy as the ORM.
- **API Architecture**: FastAPI with automatic Swagger UI generation.
- **Dependency Injection**: SQLAlchemy session integration with FastAPI.
- **Tests**: Pytest and htmlCov, basic testing added thus far.
- **Containerization**: Docker support for running the microservice in Kubernetes (TODO!).
- **CI/CD**: GitLab CI/CD pipelines for automated deployment (TODO!).

---

## Getting Started

### Prerequisites

- Python 3.11
- Docker (if running containerised, can run in localhost too)
- Kubernetes (if running in MiniKube or Azure Kubernetes Service)
- Quarto (Install from [Quarto's website](https://quarto.org))
- GPT API Key

### Setup and Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/GeorgeBPrice/PythonReportingAPI.git
   cd api-report-microservice
   ```

2. Install Python dependencies (this will install globally, run this step in venv otherwise):

   ```bash
   pip install -r requirements.txt
   ```

3. Start Python environment, Run the application:

   ```bash
   source venv/bin/activate  # For Linux/macOS
   \venv\Scripts\activate   # For Windows
   ```

   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the Swagger UI:

   ```bash
   Navigate to http://127.0.0.1:8000/docs
   ```

5. Testing:

   - Run Pytest Tests, in a new Terminal.
   - (only basic tests implemented)

     ```bash
     pytest -v
     ```

   - Run Coverage Tests.

     ```bash
     pytest --cov=app --cov-report html
     ```

   - Open the HTML Coverage Reports.

     ```bash
     xdg-open htmlcov/index.html   # For Linux/macOS
     start htmlcov/index.html   # For Windows
     ```

6. (Optional) Render reports using Quarto:

   - Install Quarto and ensure it is added to your system's PATH.
   - Run a sample report:

     ```bash
     quarto render reports/asset_report.qmd --to pdf
     ```

---

### API Documentation

All endpoints are documented and accessible through Swagger UI, allowing developers to interact and test the APIs seamlessly.

---

## Contributing

Only approved collaborators can submit issues or pull requests, sorry!
