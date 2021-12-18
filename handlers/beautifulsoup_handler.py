import traceback

from bs4 import BeautifulSoup

from common.constants import TABLE_BODY, TABLE_DATA, TABLE, TABLE_ROW


def split_multiple_collateral_adjactive(coll_adj_str):
    return coll_adj_str.split(", ")


def clean_str(str, removables_arr):
    clean_str = str
    for removable in removables_arr:
        clean_str = str.replace(removable, '')
    return clean_str


def scrape_page_content(page_content, element, element_name_dict):
    name_to_collateral_adjective = []
    try:
        beauti_soup = BeautifulSoup(page_content, 'html5lib')
        wrap_div = beauti_soup.find(element, attrs=element_name_dict)
        table = wrap_div.find(TABLE, attrs={"style":"text-align:left;"})
        table_body = table.find(TABLE_BODY)

        rows = table_body.find_all(TABLE_ROW)
        for row in rows:
            columns = row.find_all(TABLE_DATA)
            if len(columns) < 1:
                continue
            collateral_adjactives = split_multiple_collateral_adjactive(columns[5].text)
            if len(collateral_adjactives) > 1:
                for coll_adj in collateral_adjactives:
                    animal_name = clean_str(columns[6].text, ['\n'])
                    name_to_collateral_adjective.append(f'{animal_name} : {coll_adj}')
            else:
                animal_name = clean_str(columns[6].text, ['\n'])
                name_to_collateral_adjective.append(f'{animal_name} : {columns[5].text}')
    except Exception as ex:
        print(
            f'Failed to scrape web page with exception: {ex}, Traceback: {traceback.format_exc()}')  # [YS] I would use some kind of logger

    return name_to_collateral_adjective


