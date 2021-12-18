from common.config import Config
from common.constants import DIV, ELEMENT_ATTR
from handlers.beautifulsoup_handler import scrape_page_content
from services.wiki_service import get_wiki_article


if __name__ == '__main__':

    wiki_page_response = get_wiki_article(Config.WIKI_ANIMAL_NAMES)
    name_to_collateral_adjective = scrape_page_content(wiki_page_response.content, DIV, ELEMENT_ATTR)

    print(*name_to_collateral_adjective, sep="\n")

