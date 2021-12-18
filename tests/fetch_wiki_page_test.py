from services.wiki_service import get_wiki_article


def test_correct_wiki_page_returns_200(self):
    wiki_page_response = get_wiki_article('List_of_animal_names')
    assert wiki_page_response.status_code == 200


def test_non_existant_wiki_page_return_404(self):
    wiki_page_response = get_wiki_article('non_existant_wiki_page')
    assert wiki_page_response.status_code == 404