events = [
    {"name": "Конференция IT Future", "category": "Образование"},
    {"name": "Музыкальный фестиваль", "category": "Музыка"},
    {"name": "Мастер-класс по дизайну", "category": "Образование"},
    {"name": "Спортивный турнир", "category": "Спорт"}
]


def search_events(query):
    results = []

    for event in events:
        if query.lower() in event["name"].lower():
            results.append(event)

    return results


search_query = input("Введите название мероприятия: ")
found_events = search_events(search_query)

if found_events:
    print("Найденные мероприятия:")
    for event in found_events:
        print(event["name"], "-", event["category"])
else:
    print("Мероприятия не найдены.")
