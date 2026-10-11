# Get Ceratin resume details from a txt file 
# validate those details via pydantic model
# Match those details with a certain job description
# Return a structured analysis report 

# version-1:- simply pass the necessary resume details and job details in json format
# then we'll parse and compare them via the llm api 
from pydantic import Field, BaseModel
from langchain_core.output_parsers import StrOutputParser
import json
from click import parser
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

# All these classes Will be used to validate the output
class OutputSchema(BaseModel):
    Matching_Skills:list[str] = Field(description='This list will include all the skills that are a match b/w the skills mentioned in the resume and those required by the job description')
    Missing_Skills:list[str] = Field(description='This list will include all the skills that are not a match b/w the skills mentioned in the resume and those required by the job description')
    Strengths:list[str] = Field(description='This list will include the strong points of the candidate with respect to the job description')
    Improvements:list[str] = Field(description='This list will include all the improvements that the candidate needs to make in the resume to make it a match for the job description')
    Match_Score:float = Field(description='This variable will show the match b/w the candidate and the job description (on a scale of 1 to 10)')

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature='1.0')
structured_model = model.with_structured_output(OutputSchema)

with open('resume.json', 'r') as file:
    resume_details = json.load(file)

with open('job_description.json', 'r') as file:
    job_details = json.load(file)


template = ChatPromptTemplate.from_messages([
    (
        "system",
        "Act as an expert resume reviewer and match {resume_details} with"
        " {job_details} and return a structured analysis report",
    ),
    (
        "human",
        (
            "Give the deep analysis and a similarity score b/w the two at the"
            " end , also suggest the improvements required in the resume and"
            " also suggest the roles you think are relevant to this candidate"
        ),
    ),
])


chain = template | structured_model

response = chain.invoke({
    'resume_details':resume_details,
    'job_details':job_details
})


print('Resume Analysis Report:')

print('Matching SKills:')
for skills in response.Matching_Skills:
    print(f'- {skills}')

print('\nMissing Skills:')
for skills in response.Missing_Skills:
    print(f'- {skills}')

print('\nStrengths:')
for strengths in response.Strengths:
    print(f'- {strengths}')

print('\nImprovements:')
for improvements in response.Improvements:
    print(f'- {improvements}')

print('\nMatch Score:')
print(f'{response.Match_Score}')