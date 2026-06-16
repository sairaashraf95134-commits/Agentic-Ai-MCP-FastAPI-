import os

from serpapi import GoogleSearch

from dotenv import load_dotenv

load_dotenv()


def internet_search(query: str):
    """
    Search the internet 
    """

    api_key = os.getenv("SERPAPI_API_KEY")


    try:

        search = GoogleSearch(
            {
                "q": query,
                "api_key": api_key,
                "num": 5,
                "hl": "en"
            }
        )

        results = search.get_dict()

        organic_results = results.get(
            "organic_results",
            []
        )

        if not organic_results:
            return "No results found"

        formatted_results = []

        for index, result in enumerate(
                organic_results[:5],
                start=1
        ):

            title = result.get(
                "title",
                "No title"
            )

            link = result.get(
                "link",
                ""
            )

            snippet = result.get(
                "snippet",
                "No description"
            )

            formatted_results.append(
                f"{index}. {title}\n"
                f"Link: {link}\n"
                f"{snippet}\n"
            )

        return "\n".join(
            formatted_results
        )

    except Exception as e:

        return f"Search failed: {str(e)}"