# 100 Days of Cloud Challenge

Welcome to my **100 Days of Cloud Challenge** repository! 🚀 This challenge is designed to deepen my understanding of Azure cloud technologies and improve my hands-on skills by working on real-world projects every day for 100 days.

---

## 📅 Challenge Overview

| Day | Topic/Activity                           | Tools/Technologies     | Links/Notes         |
|-----|------------------------------------------|-----------------------|---------------------|
| 1   | Exploring Resource Groups in Azure       | Azure                 | [Notes](./Day-1.md) |
| 2   | Virtual Machine Deployment in Azure      | Azure                 | [Notes](./Day-2.md) |
| 3   | Introduction to Azure Database Services  | Azure SQL Database    | [Notes](./Day-3.md) |
| 4   | Azure OCR in AI Services                 | Azure Computer Vision | [Notes](./Day-4.md) |

---

## 🌟 Goals
1. Gain hands-on experience with Azure cloud computing.
2. Explore and implement different Azure services and architectures.
3. Learn to use Azure tools and technologies effectively.
4. Prepare for Azure certifications like AZ-104.

---

## 📖 Progress Tracking
- I will document my daily progress in the **logs** folder.
- Each day's log will include:
  - Activities performed
  - Challenges faced
  - Solutions and learnings.

---

## 🚀 How to Use This Repository
- **Explore Logs**: Navigate to the `logs` folder for daily progress.
- **Follow Along**: Check out project folders for detailed implementations.
- **Collaborate**: Feel free to open issues or pull requests for feedback or improvements.

---

## 🤝 Connect with Me
- [LinkedIn](https://www.linkedin.com/in/jms-luck/)
- [Portfolio](https://your-portfolio.com)

---

## 📜 License
This repository is licensed under the [MIT License](./LICENSE).

---

Let's get cloud-ready with Azure! ☁️

---

## Day 3: Introduction to Azure Database Services

📌 **Topics Covered**
- Introduction to Database Services on Azure
- Creating an Azure SQL Server using the Azure Portal
- Creating an Azure SQL Database
- Adding Tables to the Azure Database

📝 **Notes**
- Azure SQL Database does not use the same version as SQL Server.
- It is a managed cloud database that follows a versionless model, meaning Microsoft handles updates and improvements behind the scenes.
- This allows seamless upgrades, security patches, and performance improvements without manual intervention.
- Some features and syntax may differ between on-premises SQL Server and Azure SQL Database.

🔗 **Resources**
- [Azure SQL Database Documentation](https://learn.microsoft.com/en-us/azure/azure-sql/)

---

## Day 4: Azure OCR in AI Services

📌 **Topics Covered**
- Introduction to Optical Character Recognition (OCR) in Azure AI Services
- Setting up Azure Computer Vision for OCR
- Extracting text from images using OCR
- Recognizing handwritten text in medical prescriptions

📝 **Notes**
- **Azure OCR (Optical Character Recognition)** is a feature of **Azure AI Services** that enables text extraction from images and scanned documents.
- It supports **printed and handwritten text recognition**, making it useful for applications like document digitization, form processing, and medical applications.
- **Azure Computer Vision API** provides **OCR capabilities** to extract structured and unstructured text data.

### 🏥 **Use Case in My Project**
- Used **Azure OCR** to **recognize handwritten text** in **medical prescriptions**.
- The system extracts **doctor's handwritten notes**, **medicine names**, and **dosage instructions** from scanned prescriptions.
- Integrated **Azure Computer Vision API** with **Python** to process the prescription images and extract meaningful data.
- Improved **accuracy by pre-processing images** using **OpenCV** (e.g., noise reduction, thresholding).

🔗 **Resources**
- [Azure OCR Documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/overview-ocr)
- [Azure Computer Vision API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Handwritten Text Recognition with Azure](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/concept-handwriting)
