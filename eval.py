import langsmith
from langchain import chat_models, prompts, smith
from langchain.schema import output_parser


# Define your runnable or chain below.
prompt = prompts.ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful AI assistant."),
    ("human", "{prompt}")
  ]
)
llm = chat_models.ChatLiteLLM(model="ollama/llama2", temperature=0)
chain = prompt | llm | output_parser.StrOutputParser()

# Define the evaluators to apply
eval_config = smith.RunEvalConfig(
    evaluators=[
        "cot_qa",
        smith.RunEvalConfig.LabeledCriteria("conciseness"),
        smith.RunEvalConfig.LabeledCriteria("relevance"),
        smith.RunEvalConfig.LabeledCriteria("coherence")    
    ],
    custom_evaluators=[],
    eval_llm=chat_models.ChatLiteLLM(model="ollama/llama2", temperature=0)
)

client = langsmith.Client()
chain_results = client.run_on_dataset(
    dataset_name="ds-timely-increase-19",
    llm_or_chain_factory=chain,
    evaluation=eval_config,
    project_name="test-this-charm-85",
    concurrency_level=5,
    verbose=True,
)