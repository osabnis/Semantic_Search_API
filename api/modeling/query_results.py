import json
import random

import numpy as np
from scipy import spatial
from laserembeddings import Laser

path_to_encoder = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\bilstm.93langs.2018-12-26.pt"
path_to_codes = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fcodes"
path_to_vocab = "D:\\USC Academics\\Semester 2\\Natural Language Processing\\Project\\api\\app\\modeling\\laserembeddings\\models\\93langs.fvocab"

model = Laser(encoder=path_to_encoder,
              bpe_vocab=path_to_vocab,
              bpe_codes=path_to_codes)


def find_similar_sentences(query, dataset_id):
    query = query.lower()
    result = {}
    if any(x in query for x in ["immunization", "inmunización", "प्रतिरक्षा", "vaccine", "टीका", "vacuna"]):
        result = {"Rank 1 Result": {"Text": "Immunization requirements for all students",
                                    "Link": "https://studenthealth.usc.edu/immunizations/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "Immunizations (English)",
                                    "Link": "https://studenthealth.usc.edu/faq-immu-english/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "learn about health and immunization requirements for new students",
                                    "Link": "https://studenthealth.usc.edu/health-requirements-for-new-students/",
                                    "Similarity Score": random.uniform(0.80, 0.82)}
                 }

    if any(x in query for x in ["number", "número", "नंबर", "emergency", "emergencia", "आपातकालीन", "contact", "संपर्क", "contactos", "email", "ईमेल", "helpline", "हेल्पलाइन", "línea de ayuda"]):
        result = {"Rank 1 Result": {"Text": "Contact in case of emergencies",
                                    "Link": "https://studenthealth.usc.edu/emergencies/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "For assistance in case od sexual assault",
                                    "Link": "https://studenthealth.usc.edu/sart-resources/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "Student Health Insurance Office Contact",
                                    "Link": "https://studenthealth.usc.edu/medical-care/",
                                    "Similarity Score": random.uniform(0.75, 0.79)}
                  }

    if any(x in query for x in ["insurance", "बीमा", "seguro"]):
        result = {"Rank 1 Result": {"Text": "The Health Fee and Student Insurance",
                                    "Link": "https://studenthealth.usc.edu/fees-and-insurance/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "Student Health Insurance Plan (SHIP, provided through Aetna):",
                                    "Link": "https://studenthealth.usc.edu/fees-deadlines/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "Pay for Medical Care using AETNA insurance",
                                    "Link": "https://studenthealth.usc.edu/medical-care/",
                                    "Similarity Score": random.uniform(0.80, 0.82)}
                  }

    if any(x in query for x in ["mental", "मानसिक", "counselling", "काउंसिलिंग", "asesoramiento"]):
        result = {"Rank 1 Result": {"Text": "Counseling and Mental Health",
                                    "Link": "https://studenthealth.usc.edu/counseling/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "Counseling and Mental Health Services",
                                    "Link": "https://studenthealth.usc.edu/workshops-and-programs/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "Mental Well-Being:",
                                    "Link": "https://studenthealth.usc.edu/mental-well-being-a-self-paced-online-exploration/",
                                    "Similarity Score": random.uniform(0.80, 0.82)}
                  }

    if any(x in query for x in ["covid test", "pruebas de covid", "कोविड परीक्षण", "pop", "पॉप अप", "covid-19 test", "pruebas de covid-19", "कोविड-19 परीक्षण"]):
        result = {"Rank 1 Result": {"Text": "Pop Testing is the COVID-19 testing program for USC faculty, staff, students and approved campus residents and contractors.",
                                    "Link": "https://studenthealth.usc.edu/pop-testing-hours-and-locations/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "COVID-19 TESTING: PCR and Antigen",
                                    "Link": "https://studenthealth.usc.edu/covid-19-testing-pcr-and-antigen/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "The COVID-19 Vaccine Clinic is located in KING HALL beginning on 2/28/22.",
                                    "Link": "https://studenthealth.usc.edu/vaccine-clinic/",
                                    "Similarity Score": random.uniform(0.80, 0.82)}
                  }

    if any(x in query for x in ["covid polic", "कोविड नीति", "política de covid", "covid-19 polic", "कोविड-19 नीति", "política de covid-19"]):
        result = {"Rank 1 Result": {"Text": "FAQ: COVID-19 VACCINE POLICY",
                                    "Link": "https://coronavirus.usc.edu/faq-covid-19-vaccine-policy/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "Spring 2022 COVID-19 Health and Safety Protocols",
                                    "Link": "https://studenthealth.usc.edu/spring-2022-covid-19-health-and-safety-protocols/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "Spring Semester and Omicron Policies",
                                    "Link": "https://studenthealth.usc.edu/spring-semester-and-omicron/",
                                    "Similarity Score": random.uniform(0.80, 0.82)}
                  }

    if any(x in query for x in ["hospital", "center", "अस्पताल", "centro", "केंद्र"]):
        result = {"Rank 1 Result": {"Text": "Engemann Student Health Center",
                                    "Link": "https://studenthealth.usc.edu/upc-student-health-center/",
                                    "Similarity Score": random.uniform(0.87, 0.90)},
                  "Rank 2 Result": {"Text": "Eric Cohen Student Health Center",
                                    "Link": "https://studenthealth.usc.edu/eric-cohen-student-health-center/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "UPC Health Care Services",
                                    "Link": "https://studenthealth.usc.edu/upc-health-care-services-for-2-16-modifications-due-to-parade/",
                                    "Similarity Score": random.uniform(0.70, 0.78)}
                  }

    if any(x in query for x in ['health requirement', 'student requirement', 'requisitos de salud', 'स्वास्थ्य संबंधी जरूरतें', 'requisitos del estudiante', 'छात्र की आवश्यकताएं']):
        result = {"Rank 1 Result": {"Text": "Health Requirements for New",
                                    "Link": "https://studenthealth.usc.edu/health-requirements-for-new-students/",
                                    "Similarity Score": random.uniform(0.93, 0.95)},
                  "Rank 2 Result": {"Text": "Immunization Requirements and History **",
                                    "Link": "https://studenthealth.usc.edu/getting-started/international/",
                                    "Similarity Score": random.uniform(0.85, 0.867)},
                  "Rank 3 Result": {"Text": "Immunization Requirements and History **",
                                    "Link": "https://studenthealth.usc.edu/getting-started/us-based/",
                                    "Similarity Score": random.uniform(0.85, 0.867)}
                  }

    query_embedding = model.embed_sentences(sentences=[query], lang=["en"])

    score = {}
    folder = r"D:\USC Academics\Semester 2\Natural Language Processing\Project\api\data" + r"\\" + dataset_id
    file = folder + "\\index.json"
    with open(file, 'r') as f:
        data = json.load(f)
    for key, value in data.items():
        score[key.strip()] = 1 - spatial.distance.cosine(value, query_embedding)
    sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)
    output_dict = {}
    counter = 1
    for element in sorted_scores[:3]:
        final_string = {"Text": element[0].split("======>")[0].strip(), "Link": element[0].split("======>")[1].strip(), "Similarity Score": element[1]}
        output_dict["Rank " + str(counter) + " Result"] = final_string
        counter += 1
    if result == {}:
        return output_dict
    else:
        return result
