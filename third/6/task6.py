import os
import csv

def read_book_collection(data_path: str) -> dict:
    """
    递归读取 data_path 下的图书馆书籍收藏，返回嵌套字典结构。
    """
    def helper(path):
        result = {}
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                # 递归处理子文件夹
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

def count_books_by_category(data: dict, book_cat: str) -> int:
    """
    递归统计指定类别的书籍数量。
    """
    count = 0
    for key, value in data.items():
        if key == book_cat:
            count += len(value)
        elif isinstance(value, dict):
            count += count_books_by_category(value, book_cat)
    return count

def find_books_by_author(data: dict, author: str, path='') -> list:
    """
    递归查找指定作者的所有书籍，并添加 category 字段。
    """
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

def search_by_keywords(data: dict, keywords: list, similarity_threshold: float, path='') -> list:
    """
    递归查找与关键词相似度大于阈值的书籍，返回带 category 和 score 字段的列表。
    """
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
    # 排序：先按相似度降序，再按年份降序
    results.sort(key=lambda x: (-x['score'], -x['year']))
    return results