from src.states.blogstate import BlogState


class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Create the title of the blog
        """
        topic=state["topic"]
        if topic is not None:
            prompt = f"""
                    You are an expert blog content writter. Use markdown formatting. Generate a blog title 
                    for the {topic}. This title should be creative.
                    """
            system_message = prompt.format(topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog": {"title": response.content}}

    def content_creation(self, state: BlogState):
        """
        Create the content of the blog
        """
        topic=state["topic"]
        if topic is not None:
            prompt = f"""
                      You are an expert blog content writter. Use markdown formatting. 
                      Generate a blog content for the {topic}. This title should be creative.
                      """
            system_message = prompt.format(topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state['blog']['title'], "content": response.content}}