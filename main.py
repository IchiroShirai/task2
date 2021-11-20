from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

MYNAVI_URL = "https://tenshoku.mynavi.jp/"


def main():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(MYNAVI_URL)
    sleep(3)
    try:
        # ポップアップを閉じる
        driver.execute_script('document.querySelector(".karte-close").click()')
        sleep(1)
        driver.execute_script('document.querySelector(".karte-close").click()')
    except Exception:
        pass

    # テキストボックスの要素
    element = driver.find_element_by_css_selector(".topSearch__text")
    element.send_keys("プログラミング")
    # ボタンの要素
    btn_element = driver.find_element_by_css_selector(
        ".topSearch__button.js__searchRecruitTop"
    )
    btn_element.click()
    sleep(3)
    elements = driver.find_elements_by_css_selector(".cassetteRecruit")
    for el in elements:
        title_el = el.find_element_by_css_selector(
            ".cassetteRecruit__copy.boxAdjust > a"
        )
        print(f'会社名：{el.find_element_by_css_selector("h3").text}')
        print(f"タイトル：{title_el.text}")
        print(f'URL:{title_el.get_attribute("href")}')
        table_heads = el.find_elements_by_css_selector(".tableCondition__head")
        table_bodies = el.find_elements_by_css_selector(".tableCondition__body")
        for table_head, table_body in zip(table_heads, table_bodies):
            if "仕事内容" == table_head.text:
                print(f"仕事内容：{table_body.text}")
            elif "給与" == table_head.text:
                print(f"給与：{table_body.text}")
        print("----------------------------------------------")


if __name__ == "__main__":
    main()