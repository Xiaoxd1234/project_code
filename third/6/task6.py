import os
import csv
import re


def read_book_collection(data_path: str) -> dict:
    import os
    import csv
    def helper(path):
        result = {}
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                result[entry.lower()] = helper(full_path)
            elif entry.endswith('.csv'):
                category = entry[:-4].lower()
                books = []
                with open(full_path, encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        book = {
                            'book_id': row.get('book_id', ''),
                            'type': row.get('type', 'physical'),
                            'copies': int(row.get('copies', 1)),
                            'title': row.get('title', ''),
                            'author': [a.strip() for a in row.get('author', '').split('&')],
                            'year': int(row.get('year', 0)),
                            'keywords': [k.strip() for k in row.get('keywords', '').split(':')]
                        }
                        books.append(book)
                result[category] = books
        return result
    return helper(data_path)

def count_books_by_category(data: dict, book_cat:str) -> int:
    count = 0
    for key, value in data.items():
        if key == book_cat:
            count += len(value)
        elif isinstance(value, dict):
            count += count_books_by_category(value, book_cat)
    return count

def find_books_by_author(data:dict, author:str, path='') -> list:
    results = []
    for key, value in data.items():
        current_path = f"{path}/{key}"
        if isinstance(value, list):
            for book in value:
                if author in book.get('author', []):
                    book_with_cat = book.copy()
                    book_with_cat['category'] = current_path
                    results.append(book_with_cat)
        elif isinstance(value, dict):
            results.extend(find_books_by_author(value, author, current_path))
    return results

def search_by_keywords(data:dict, keywords: list, similarity_threshold, path='') -> list:
    def jaccard(a, b):
        set_a = set([w.lower() for w in a])
        set_b = set([w.lower() for w in b])
        intersection = set_a & set_b
        union = set_a | set_b
        return len(intersection) / len(union) if union else 0

    results = []
    for key, value in data.items():
        current_path = f"{path}/{key}"
        if isinstance(value, list):
            for book in value:
                title_words = book.get('title', '').lower().replace(':', ' ').replace('&', ' ').split()
                score = jaccard(keywords, title_words)
                if score >= similarity_threshold:
                    book_with_score = book.copy()
                    book_with_score['category'] = current_path
                    book_with_score['score'] = score
                    results.append(book_with_score)
        elif isinstance(value, dict):
            results.extend(search_by_keywords(value, keywords, similarity_threshold, current_path))
    results.sort(key=lambda x: (-x['score'], -x['year']))
    return results


# WARNING!!! *DO NOT* REMOVE THIS LINE
# THIS ENSURES THAT THE CODE BELLOW ONLY RUNS WHEN YOU HIT THE GREEN `Run` BUTTON, AND NOT THE BLUE `Test` BUTTON
if __name__ == "__main__":
    # 测试数据路径
    data_path = "./data"
    # 1. 读取书籍层级结构
    books_dict = read_book_collection(data_path)
    print("=== 书籍层级结构 ===")
    print(books_dict)

    # 2. 统计某类别书籍数量
    category = "machinelearning"
    count = count_books_by_category(books_dict, category)
    print(f"\n=== '{category}' 类别书籍数量: {count} ===")

    # 3. 查找某作者的所有书籍
    author = "Eric Matthes"
    author_books = find_books_by_author(books_dict, author)
    print(f"\n=== 作者 '{author}' 的所有书籍 ===")
    for book in author_books:
        print(book)

    # 4. 按关键词相似度搜索书籍
    keywords = ["python", "programming"]
    threshold = 0.25
    search_results = search_by_keywords(books_dict, keywords, threshold)
    print(f"\n=== 按关键词 {keywords} 相似度搜索结果 (阈值 {threshold}) ===")
    for book in search_results:
        print(book)


