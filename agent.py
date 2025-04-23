from langchain.agents import Tool, initialize_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# .env の読み込み（ローカル用）
load_dotenv()

# APIキーの取得
openai_api_key = os.getenv("OPENAI_API_KEY")

# ツールの読み込み
from tools.weather_tool import get_weather
from tools.forex_tool import get_forex
from tools.time_tool import get_current_time

# Toolオブジェクトの定義
tools = [
    Tool(name="WeatherTool", func=get_weather, description="現在の天気を取得します（例：東京の天気は？）"),
    Tool(name="ForexTool", func=get_forex, description="為替レートを取得します（例：ドル円の為替レートは？）"),
    Tool(name="TimeTool", func=get_current_time, description="現在時刻を返します（例：今何時？）")
]

# LLMを初期化（OpenAIを使用）
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=openai_api_key
)
# Agentの初期化（zero-shot agent）
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
