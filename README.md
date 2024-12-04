# API Reporting Microservice

The **API Reporting Microservice** handles reporting for the IT Expense Management (ITAM) and Telecom Expense Management (TEM) SaaS platform. It enables accurate reporting and auditing of complex organizational data, including insights into asset lifecycles, location, associations, and other useful financial metrics.

---

## Key Features

- CRUD operations and generation of reports for Expenses, Assets, and other insightful data.
- Flexible support for generating reports in **PDF**, **Excel**, and **Word** and **Jason Value** formats.
- Use of AI for improved reporting analysis, and custom "on the fly" reports, leveraging GPT prompt API.
- Comprehensive audit logging for tracking data changes and modifications.
- Integration with **Quarto** for modern reporting capabilities.
- Modular design for scalability and maintainability.

---

## Technology Stack

- **Framework**: Python 3.11
- **Reporting Tools**: Quarto for PDF, Excel, and Word generation; ReportLab for detailed PDF layouts. GPT for AI.
- **Database**: SQL Server with SQLAlchemy as the ORM.
- **API Architecture**: FastAPI with automatic Swagger UI generation.
- **Dependency Injection**: SQLAlchemy session integration with FastAPI.
- **Containerization**: Docker support for running the microservice in Kubernetes.
- **CI/CD**: GitLab CI/CD pipelines for automated deployment.

---

## Getting Started

### Prerequisites

- Python 3.11
- Docker Containers
- Kubernetes (MiniKube or Azure Kubernetes Service)
- GitLab Runner (if testing CI/CD)
- Quarto (Install from [Quarto's website](https://quarto.org))
- GPT API Key

### Setup and Run Locally

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/temtam/backend/microservices/api-reporting-service.git
   cd api-report-management
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start Python environment, Run the application:

   ```bash
   venv\Scripts\activate
   ```

   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the Swagger UI:

   ```bash
   Navigate to http://127.0.0.1:8000/docs
   ```

5. (Optional) Render reports using Quarto:
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

Only approved collaborators can submit issues or pull requests. Ensure all contributions adhere to established coding and documentation standards.
