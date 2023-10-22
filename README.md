# Med-Xplain
# Your tool for post-diagnosis decision making. 

Med-Xplain is a patient-centric tool that leverages Generative AI to produce text-based medical summaries. This tool serves as a post-diagnostic aid with the primary goal of increasing patient awareness about their treatment options and improving clinician-patient conversations. It also acts as an intermediary interface between healthcare providers and patients, addressing the need for enhanced patient involvement in their care while alleviating the burden on clinicians.

**Key Features**

* Patient Information Tool: This application acts as an intermediate interface that bridges the gap between doctors and patients. It empowers patients with valuable information about their medical conditions, treatment options, and ongoing care. This is especially crucial in healthcare environments where patients often feel disconnected from the decision-making process.

* Enhanced Patient Governance: The tool aims to provide patients with more control over their healthcare journey. By making comprehensive medical summaries accessible, it encourages patients to actively participate in their care decisions. This enhanced governance can lead to improved patient outcomes.

* Ongoing Support and Insights into Medical Research: The Medical Summary Generator is designed to provide ongoing support, particularly for chronic illnesses. It can regularly update patients with relevant information and evolving treatment landscapes, helping them better understand their options as well as providing insights into ongoing medical research.



**Data Sources**
1. BMJ PDF Data
We began by collecting a significant amount of medical research data from the BMJ (British Medical Journal) in the form of PDF documents. To leverage this data effectively, we transformed it into embeddings. These embeddings enabled us to capture the semantic and contextual information within the documents.

2. NHS Web Scraped Data
In addition to BMJ PDF data, we conducted web scraping of NHS (National Health Service) web pages to gather real-time healthcare information. The data extracted from these web pages was structured, processed, and incorporated into our knowledge repository.

3. PubMed Papers
PubMed serves as a valuable resource for accessing a wide range of medical research papers. We gathered a selection of relevant papers from PubMed and extracted key information from them. These papers were also converted into embeddings for further analysis.

**Technical Approach**

Med-Xplain employs a multi-faceted strategy that combines data from the BMJ (Biomedical Journal), NHS web scraped data, and PubMed papers to answer queries about therapeutic options and suggest relevant research papers. We used the Pinecone vector database to accommodate the embeddings and integrated HumanLoop functions enhanced with the power of OpenAI's GPT-3.5 Turbo model. 

**Acknowledgments**

**This project was completed for the Oxford Generative AI hackathon 2023. Team members: Julian Wyatt, Sravan Kumar, Ananya Bhalla, Cornelia Weinzierl and Ciprian Florea. We thank the University of Oxford, Hackathon sponsors Humanloop, Co:Helm, Mind Foundry and Quine, as well as the Hackathon organising committee for hosting us.**

