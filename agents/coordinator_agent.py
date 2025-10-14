from openai import Agent
from agents.system_data_agent import system_data_agent
from agents.anomaly_agent import anomaly_agent
from agents.report_agent import report_agent

coordinator_agent = Agent(
    name="CoordinatorAgent",
    instructions="Coordinate the system data collection, anomaly detection, and report generation.",
    tools=[system_data_agent, anomaly_agent, report_agent]
)
