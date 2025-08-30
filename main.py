import requests

BASE_URL = "https://catfact.ninja/facts"


def main():
    # 1. Получаем первую страницу
    response = requests.get(BASE_URL)
    response.raise_for_status()
    data = response.json()

    # 2. Узнаем общее количество фактов
    total = data.get("total")
    per_page = data.get("per_page")

    print(f"Всего фактов: {total}, на странице: {per_page}")

    # 3. Вычисляем номер последней страницы
    last_page = (total + per_page - 1) // per_page
    print(f"Номер последней страницы: {last_page}")

    # 4. Делаем запрос на последнюю страницу
    response_last = requests.get(BASE_URL, params={"page": last_page})
    response_last.raise_for_status()
    last_data = response_last.json()

    facts = [item["fact"] for item in last_data.get("data", [])]

    # 5. Находим самый короткий факт
    shortest_fact = min(facts, key=len)

    print("\nСамый короткий факт с последней страницы:")
    print(shortest_fact)


if __name__ == "__main__":
    main()
