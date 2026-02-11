from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import Groqllm
from src.states.blogstate import BlogState
from src.nodes.blog_node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_blog(self):
        """
        Build a graph for title creation based on topic
        """
        blog_obj=BlogNode(self.llm)

        #Define Nodes
        self.graph.add_node("title_creation", blog_obj.title_creation)
        self.graph.add_node("content_creation", blog_obj.content_creation)
        #Define Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", END)
        return self.graph

    def setup_graph(self, usecase):
        if usecase == "blog_creation":
            self.build_blog()

        return self.graph.compile()

